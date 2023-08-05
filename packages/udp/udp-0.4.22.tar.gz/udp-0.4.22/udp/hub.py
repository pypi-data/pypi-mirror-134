# -*- coding: utf-8 -*-
#
#   UDP: User Datagram Protocol
#
#                                Written in 2020 by Moky <albert.moky@gmail.com>
#
# ==============================================================================
# MIT License
#
# Copyright (c) 2020 Albert Moky
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
from abc import ABC
from typing import Optional, Dict, Set

from startrek import Channel
from startrek import Connection, ConnectionDelegate
from startrek import BaseConnection, ActiveConnection
from startrek import BaseHub

from .channel import PackageChannel


class PackageHub(BaseHub, ABC):
    """ Base Package Hub """

    def __init__(self, delegate: ConnectionDelegate):
        super().__init__(delegate=delegate)
        # local => channel
        self.__channels: Dict[tuple, Channel] = {}  # local -> Channel

    def bind(self, address: tuple = None, host: str = None, port: int = 0):
        if address is None:
            address = (host, port)
        channel = self.__channels.get(address)
        if channel is None:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            sock.setblocking(True)
            sock.bind(address)
            sock.setblocking(False)
            channel = PackageChannel(sock=sock, remote=None, local=address)
            self.__channels[address] = channel

    def put_channel(self, channel: Channel):
        local = channel.local_address
        self.__channels[local] = channel

    # Override
    def _all_channels(self) -> Set[Channel]:
        return set(self.__channels.values())

    # Override
    def open_channel(self, remote: Optional[tuple], local: Optional[tuple]) -> Optional[Channel]:
        if local is None:
            # get any channel
            keys = set(self.__channels.keys())
            for address in keys:
                channel = self.__channels.get(address)
                if channel is not None:
                    return channel
            # channel not found
        else:
            return self.__channels.get(local)

    # Override
    def close_channel(self, channel: Channel):
        if channel is None or not channel.connected:
            # DON'T close bound socket channel
            return False
        else:
            self.__remove_channel(channel=channel)
        try:
            if channel.opened:
                channel.close()
            return True
        except socket.error:
            return False

    def __remove_channel(self, channel: Channel):
        local = channel.local_address
        if self.__channels.pop(local, None) == channel:
            # removed by key
            return True
        # remove by value
        keys = set(self.__channels.keys())
        for address in keys:
            if self.__channels.get(address) == channel:
                self.__channels.pop(address, None)
                return True


class ServerHub(PackageHub):
    """ Package Server Hub """

    # Override
    def _create_connection(self, sock: Channel, remote: tuple, local: Optional[tuple]) -> Optional[Connection]:
        gate = self.delegate
        conn = BaseConnection(remote=remote, local=None, channel=sock, delegate=gate, hub=self)
        conn.start()  # start FSM
        return conn


class ClientHub(PackageHub):
    """ Package Client Hub """

    # Override
    def _create_connection(self, sock: Channel, remote: tuple, local: Optional[tuple]) -> Optional[Connection]:
        gate = self.delegate
        conn = ActiveConnection(remote=remote, local=None, channel=sock, delegate=gate, hub=self)
        conn.start()  # start FSM
        return conn
