import asyncio
from aiohttp import ClientSession

from ..message.builder import ChatBubble


def _msg_package(session, target, chain):
    return {
        "sessionKey": session,
        "target": target,
        "messageChain": chain,
    }


class HTTPRoBot:
    def __init__(self, server_url, robot_qq, verify_key, session=None) -> None:
        self.robot_qq = robot_qq
        self.server_url = server_url
        self.verify_key = verify_key
        self.session_key = session

    async def __aenter__(self) -> "BotRequest":
        return BotRequest(self.server_url, self.robot_qq, self.verify_key)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return


class BotRequest:
    robot_qq: int
    session_key: str
    verify_key: str
    server_url: str
    http_client: ClientSession

    def __init__(self, robot_qq, server_url, verify_key, session=None) -> None:
        self.robot_qq = robot_qq
        self.server_url = server_url
        self.verify_key = verify_key
        self.session_key = session
        self.http_client = None

    async def __aenter__(self):
        if not self.http_client:
            self.http_client = ClientSession(self.server_url)
        if not self.session_key:
            self._bind(self._session())
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.release()
        await self.http_client.close()
        self.http_client = None

    @property
    async def request(self):
        if not self.http_client:
            self.http_client = ClientSession(self.server_url)
        return self.http_client

    async def _session(self):
        async with self.request.post(
            "/verify", json={"verifyKey": self.verify_key}
        ) as r:
            resp = await r.json()
            if resp["code"] == 0:
                return True
            else:
                raise Exception(resp["msg"])

    async def _bind(self, session):
        async with self.request.post(
            "/bind", json={"sessionKey": session, "qq": self.robot_qq}
        ) as r:
            resp = await r.json()
            if resp["code"] == 0:
                self.session_key = session
                return True
            else:
                raise Exception(resp["msg"])

    async def release(self):
        async with self.request.post(
            "/release", json={"sessionKey": self.session_key, "qq": self.robot_qq}
        ) as r:
            resp = await r.json()
            if resp["code"] == 0:
                self.session_key = None
                return True
            else:
                raise Exception(resp["msg"])

    async def _send_json(self, url, data):
        async with self.request.post(url, json=data) as r:
            resp = await r.json()
            if resp["code"] == 0:
                return resp["messageId"]
            else:
                raise Exception(resp["msg"])

    async def send_msg(self, url, target, message):
        if isinstance(message, dict):
            data = _msg_package(self.session_key, target, [message])
            await self._send_json(url, data)
        elif isinstance(message, ChatBubble):
            data = _msg_package(self.session_key, target, [message])
            await self._send_json(url, data)
        elif isinstance(message, list):
            tasks = [
                asyncio.create_task(
                    self._send_json(
                        url,
                        _msg_package(self.session_key, target, msg),
                    )
                )
                for msg in message
            ]
            await asyncio.gather(*tasks)
        else:
            raise Exception()

    async def send_group(self, target, message):
        return await self.send_msg("/sendGroupMessage", target, message)

    async def send_friend(self, target, message):
        return await self.send_msg("/sendFriendMessage", target, message)

    async def countMessage(self):
        async with self.request.get(
            f"/countMessage", params={"sessionKey": self.session_key}
        ) as r:
            resp = await r.json()
            if resp["code"] == 0:
                return resp["data"]
            else:
                raise Exception(resp["msg"])

    async def fetchMessage(self, count: int = 10):
        async with self.request.get(
            f"/fetchMessage", params={"sessionKey": self.session_key, "count": count}
        ) as r:
            resp = await r.json()

            if resp["code"] == 0:
                return resp["data"]
            else:
                raise Exception(resp["msg"])

    async def peekMessage(self, count: int = 10):
        async with self.request.get(
            f"/peekMessage", params={"sessionKey": self.session_key, "count": count}
        ) as r:
            resp = await r.json()
            if resp["code"] == 0:
                return resp["data"]
            else:
                raise Exception(resp["msg"])
