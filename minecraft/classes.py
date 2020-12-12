"""
The MIT License (MIT)

Copyright (c) 2020 Daniel Nash

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import functools
from typing import Callable

from .errors import NotConnectedError
from . import MinecraftClient


def needs_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if not args[0].is_connected():
            raise NotConnectedError
        return func(*args, **kwargs)

    return wrapper

class Server(MinecraftClient):
    def __init__(self, ip, port, password, connect_on_send=False):
        super(Server, self).__init__(ip, port, password)
        self._connected = False
        self._connect_on_send = connect_on_send

    def is_connected(self): return self._connected

    async def __aenter__(self):
        self._connected = True
        return await super(Server, self).__aenter__()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._connected = False
        await super(Server, self).__aexit__(exc_type, exc_val, exc_tb)

    async def connect(self):
        self._connected = True
        await self.__aenter__()

    async def close(self):
        await self.__aexit__(None, None, None)

    async def send(self, cmd):
        if not self._connected:
            if self._connect_on_send:
                await self.connect()
            else:
                raise NotConnectedError
        return await super(Server, self).send(cmd)

    @needs_connection
    async def online(self):
        return (await self.send("list")).split(":")[1].replace(" ", "").split(",")

