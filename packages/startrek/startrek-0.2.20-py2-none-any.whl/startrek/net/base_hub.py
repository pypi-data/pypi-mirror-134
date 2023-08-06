# -*- coding: utf-8 -*-
#
#   Star Trek: Interstellar Transport
#
#                                Written in 2021 by Moky <albert.moky@gmail.com>
#
# ==============================================================================
# MIT License
#
# Copyright (c) 2021 Albert Moky
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================

import socket
import traceback
import weakref
from abc import ABC, abstractmethod
from typing import Optional, Set

from ..types import AddressPairMap

from .hub import Hub
from .channel import Channel
from .connection import Connection
from .delegate import ConnectionDelegate


class BaseHub(Hub, ABC):

    """
        Maximum Segment Size
        ~~~~~~~~~~~~~~~~~~~~
        Buffer size for receiving package

        MTU        : 1500 bytes (excludes 14 bytes ethernet header & 4 bytes FCS)
        IP header  :   20 bytes
        TCP header :   20 bytes
        UDP header :    8 bytes
    """
    MSS = 1472  # 1500 - 20 - 8

    def __init__(self, delegate: ConnectionDelegate):
        super().__init__()
        self.__delegate = weakref.ref(delegate)
        self.__connection_pool: AddressPairMap[Connection] = AddressPairMap()

    @property
    def delegate(self) -> ConnectionDelegate:
        return self.__delegate()

    @abstractmethod  # protected
    def _all_channels(self) -> Set[Channel]:
        """
        Get all channels

        :return: copy of channels
        """
        raise NotImplemented

    @abstractmethod  # protected
    def _create_connection(self, channel: Channel, remote: tuple, local: Optional[tuple]) -> Optional[Connection]:
        """
        Create connection with channel channel & addresses

        :param channel: channel channel
        :param remote:  remote address
        :param local:   local address
        :return: None on channel not exists
        """
        raise NotImplemented

    def _all_connections(self) -> Set[Connection]:
        return self.__connection_pool.values

    # Override
    def connect(self, remote: tuple, local: Optional[tuple] = None) -> Optional[Connection]:
        conn = self.__connection_pool.get(remote=remote, local=local)
        if conn is not None:
            # check local address
            if local is None:
                return conn
            address = conn.local_address
            if address is None or address == local:
                return conn
            # local address not matched? ignore this connection
        # try to open channel with direction (remote, local)
        channel = self.open_channel(remote=remote, local=local)
        if channel is None or not channel.opened:
            return None
        # create with channel
        conn = self._create_connection(channel=channel, remote=remote, local=local)
        if conn is not None:
            # NOTICE: local address in the connection may be set to None
            local = conn.local_address
            remote = conn.remote_address
            self.__connection_pool.put(remote=remote, local=local, value=conn)
            return conn

    # Override
    def disconnect(self, remote: tuple = None, local: Optional[tuple] = None,
                   connection: Connection = None) -> Optional[Connection]:
        conn = self.__remove_connection(remote=remote, local=local, connection=connection)
        if conn is not None:
            conn.close()
        if connection is not None and connection is not conn:
            connection.close()
        # if conn is None:
        #     return connection
        # else:
        #     return conn
        return connection if conn is None else conn

    def __remove_connection(self, remote: tuple = None, local: Optional[tuple] = None,
                            connection: Connection = None) -> Optional[Connection]:
        if connection is None:
            assert remote is not None, 'remote address should not be empty'
            connection = self.__connection_pool.get(remote=remote, local=local)
            if connection is None:
                # connection not exists
                return None
        # check local address
        if local is not None:
            address = connection.local_address
            if address is not None and address != local:
                # local address not matched
                return None
        remote = connection.remote_address
        local = connection.local_address
        return self.__connection_pool.remove(remote=remote, local=local, value=connection)

    def _drive_channel(self, channel: Channel) -> bool:
        local = channel.local_address
        # try to receive
        try:
            data, remote = channel.receive(max_len=self.MSS)
        except socket.error as error:
            # print('[NET] failed to receive data: %s' % error)
            remote = channel.remote_address
            # socket error, remove the channel
            self.close_channel(channel=channel)
            # callback
            delegate = self.delegate
            if delegate is not None:
                delegate.connection_error(error=error, data=None, source=remote, destination=local, connection=None)
            return False
        if remote is None:
            # received nothing
            return False
        # get connection for processing received data
        conn = self.connect(remote=remote, local=local)
        if conn is not None:
            conn.received(data=data, remote=remote, local=local)
        return True

    def _drive_channels(self, channels: Set[Channel]) -> int:
        count = 0
        for sock in channels:
            try:
                if sock.alive and self._drive_channel(channel=sock):
                    count += 1  # received data from this socket channel
            except Exception as error:
                print('[NET] drive channel error: %s, %s' % (error, sock))
                traceback.print_exc()
        return count

    # noinspection PyMethodMayBeStatic
    def _drive_connections(self, connections: Set[Connection]):
        for conn in connections:
            try:
                conn.tick()  # drive connection to go on
            except Exception as error:
                print('[NET] drive connection error: %s, %s' % (error, conn))
                traceback.print_exc()
            # NOTICE: let the delegate to decide whether close an error connection
            #         or just remove it.

    def _cleanup_channels(self, channels: Set[Channel]):
        closed_channels = set()
        # 1. check closed channels
        for sock in channels:
            if not sock.alive:
                closed_channels.add(sock)
        # 2. remove closed channels
        for sock in closed_channels:
            self.close_channel(channel=sock)
        return closed_channels

    def _cleanup_connections(self, connections: Set[Connection]):
        # NOTICE: multi connections may share same channel (UDP Hub)
        closed_connections = set()
        # 1. check closed connections
        for conn in connections:
            if not conn.alive:
                closed_connections.add(conn)
        # 2. remove closed connections
        for conn in closed_connections:
            remote = conn.remote_address
            local = conn.local_address
            self.disconnect(remote=remote, local=local, connection=conn)
        return closed_connections

    # Override
    def process(self) -> bool:
        try:
            # 1. drive all channels to receive data
            channels = self._all_channels()
            count = self._drive_channels(channels=channels)
            self._cleanup_channels(channels=channels)
            # 2. drive all connections to move on
            connections = self._all_connections()
            self._drive_connections(connections=connections)
            self._cleanup_connections(connections=connections)
            return count > 0
        except Exception as error:
            print('[NET] hub process error: %s' % error)
            traceback.print_exc()
