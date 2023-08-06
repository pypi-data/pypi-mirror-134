import asyncio
import json
import os
import socket
import time
from random import SystemRandom
from typing import Any, Dict, Optional

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class RabbitAir:

    _ts_diff: Optional[float] = None

    def __init__(
        self, host: str, token: Optional[str], port: int = 9009, tcp: bool = False
    ) -> None:
        self._host = host
        self._token = bytes.fromhex(token) if token else None
        self._port = port
        self._tcp = tcp
        self._sock = socket.socket(type=socket.SOCK_DGRAM)
        self._sock.setblocking(False)
        self._id = SystemRandom().randrange(0x1000000)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._sock.close()

    @staticmethod
    def _clock() -> float:
        return time.clock_gettime(time.CLOCK_BOOTTIME)

    def _next_id(self) -> int:
        value = self._id
        self._id += 1
        return value

    def _get_ts(self) -> Optional[int]:
        return round(self._clock() + self._ts_diff) if self._ts_diff else None

    def _decrypt(self, msg: bytes) -> bytes:
        iv = msg[-16:]
        msg = msg[:-16]
        cipher = Cipher(algorithms.AES(self._token), modes.CBC(iv), default_backend())
        decryptor = cipher.decryptor()
        msg = decryptor.update(msg) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(msg) + unpadder.finalize()

    def _encrypt(self, msg: bytes) -> bytes:
        padder = padding.PKCS7(128).padder()
        msg = padder.update(msg) + padder.finalize()
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self._token), modes.CBC(iv), default_backend())
        encryptor = cipher.encryptor()
        return encryptor.update(msg) + encryptor.finalize() + iv

    async def _exchange(self, request_id: int, data: bytes) -> Dict[str, Any]:
        loop = asyncio.get_running_loop()
        await loop.sock_sendall(self._sock, data)
        while True:
            data = await loop.sock_recv(self._sock, 2048)
            if self._token:
                data = self._decrypt(data)
            try:
                response = json.loads(data)
                if response["id"] == request_id:
                    return response
            except (json.JSONDecodeError, KeyError):
                # Ignore any garbage or unexpected responses
                pass

    async def _retry(
        self, request_id: int, data: bytes, count: int = 3, timeout: float = 1.5
    ) -> Dict[str, Any]:
        for i in range(count):
            try:
                return await asyncio.wait_for(self._exchange(request_id, data), timeout)
            except asyncio.TimeoutError as e:
                error = e
        raise error

    async def _command(self, request: Dict[str, Any]) -> Dict[str, Any]:
        data = json.dumps(request, separators=(",", ":")).encode()
        if self._token:
            data = self._encrypt(data)
        return await self._retry(request["id"], data)

    async def command(self, request: Dict[str, Any]) -> Dict[str, Any]:
        if self._token:
            if not self._ts_diff:
                ts_request = {"id": self._next_id(), "cmd": 9}
                response = await self._command(ts_request)
                ts = response["data"]["ts"]
                self._ts_diff = ts - self._clock()
                request["ts"] = ts
            else:
                request["ts"] = self._get_ts()
        request["id"] = self._next_id()
        return await self._command(request)

    async def start(self) -> None:
        loop = asyncio.get_running_loop()
        await loop.sock_connect(self._sock, (self._host, self._port))
