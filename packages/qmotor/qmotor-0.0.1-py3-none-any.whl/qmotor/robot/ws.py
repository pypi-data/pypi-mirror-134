import asyncio
from typing import Dict
from aiohttp import ClientWebSocketResponse, WSMessage, ClientSession
from aiohttp.client import _WSRequestContextManager

from ..framework import QBot
from ..message.builder import ChatBubble


def _msg_package(target, msg, command, session):
    return {
        "syncId": "-1",
        "command": command,
        "subCommand": None,
        "content": {
            "sessionKey": session,
            "target": target,
            "messageChain": msg,
        },
    }


class WebSocketConn:
    ws: ClientWebSocketResponse
    session: str

    def __init__(self, ws, session) -> None:
        self.ws = ws
        self.session = session

    async def send(self, data):
        if isinstance(data, str):
            return await self.ws.send_str(data)
        elif isinstance(data, dict):
            return await self.ws.send_json(data)

    async def receive(self) -> WSMessage:
        return await self.ws.receive()

    async def send_msg(self, queue):
        for msg in queue:
            assert isinstance(msg, list)
            msg["content"]["sessionKey"] = self.session
            await self.send(msg)

    async def send_group(self, target, message):
        tasks = []
        if isinstance(message, dict):
            data = _msg_package(target, [message], "sendFriendMessage", self.session)
            tasks.append(asyncio.create_task(self.send(data)))
        elif isinstance(message, ChatBubble):
            data = _msg_package(target, message, "sendFriendMessage", self.session)
            tasks.append(asyncio.create_task(self.send(data)))
        elif isinstance(message, list):
            for msg in message:
                if isinstance(msg, dict):
                    data = _msg_package(target, [msg], "sendGroupMessage", self.session)
                elif isinstance(msg, list):
                    data = _msg_package(target, msg, "sendGroupMessage", self.session)
                else:
                    raise Exception("Not Support Msg Type")
                tasks.append(asyncio.create_task(self.send(data)))
        else:
            raise Exception()

        await asyncio.gather(*tasks)

    async def send_friend(self, target, message):
        tasks = []
        if isinstance(message, dict):
            data = _msg_package(target, [message], "sendFriendMessage", self.session)
            tasks.append(asyncio.create_task(self.send(data)))
        elif isinstance(message, ChatBubble):
            data = _msg_package(target, message, "sendFriendMessage", self.session)
            tasks.append(asyncio.create_task(self.send(data)))
        elif isinstance(message, list):
            for msg in message:
                if isinstance(msg, dict):
                    data = _msg_package(
                        target, [msg], "sendFriendMessage", self.session
                    )
                elif isinstance(msg, list):
                    data = _msg_package(target, msg, "sendFriendMessage", self.session)
                else:
                    raise Exception("Not Support Msg Type")
                tasks.append(asyncio.create_task(self.send(data)))
        else:
            raise Exception()
        await asyncio.gather(*tasks)


class WSCtx(object):
    app: QBot
    robot_qq: int
    session: str
    ws: WebSocketConn
    msg: Dict

    def __init__(self, app, robot_qq, ws, session, msg) -> None:
        super().__init__()
        self.app = app
        self.robot_qq = robot_qq
        self.ws = ws
        self.session = session
        self.msg = msg


class WSRoBot:
    robot_qq: int
    ws_url: str
    verify_key: str
    channel: str
    ws_ctx: _WSRequestContextManager

    def __init__(self, ws_url, robot_qq, verify_key, channel="all") -> None:
        self.robot_qq = robot_qq
        self.ws_url = ws_url
        self.verify_key = verify_key
        self.channel = channel
        self.ws_ctx = None

    async def __aenter__(self):
        if not self.ws_ctx:
            self.ws_ctx = ClientSession().ws_connect(
                f"{self.ws_url}/{self.channel}",
                params={"qq": self.robot_qq, "verifyKey": self.verify_key},
            )
        return await self.ws_ctx.__aenter__()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.ws_ctx.__aexit__(exc_type, exc_val, exc_tb)
