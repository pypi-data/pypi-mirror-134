from abc import ABC, abstractmethod
from typing import List
from .common import (
    AtCell,
    BasicMessage,
    GroupMessage,
    FriendMessage,
    MsgCellType,
    MessageType,
    PlainCell,
)
from ..utils import is_str_blank, str_contains


class MsgMatcher(ABC):
    def msg_chain_from_ctx(self, ctx):
        return BasicMessage(ctx.msg).messageChain()

    def get_cell_type(self, msg_cell):
        return msg_cell.get("type", None)

    @abstractmethod
    def match(self, ctx) -> bool:
        pass


class GroupMsg(MsgMatcher):
    def match(self, ctx) -> bool:
        return BasicMessage(ctx.msg).type() == MessageType.GroupMessage


class FriendMsg(MsgMatcher):
    def match(self, ctx) -> bool:
        return BasicMessage(ctx.msg).type() == MessageType.FriendMessage


class TempMsg(MsgMatcher):
    def match(self, ctx) -> bool:
        return BasicMessage(ctx.msg).type() == MessageType.TempMessage


class AtMsg(GroupMsg):
    def match(self, ctx) -> bool:
        if not super().match(ctx):
            return False
        msg_chain = self.msg_chain_from_ctx(ctx)
        return self.get_cell_type(msg_chain[1]) == MsgCellType.At


class AtMeMsg(AtMsg):
    me_qq: int

    def __init__(self, me_qq) -> None:
        super(AtMeMsg, self).__init__()
        self.me_qq = me_qq

    def match(self, ctx) -> bool:
        if not super().match(ctx):
            return False
        msg_chain = GroupMessage(ctx.msg).messageChain()
        at = AtCell(msg_chain[1])
        return self.me_qq == at.target()


class JustAtMeMsg(AtMeMsg):
    def __init__(self, me_qq) -> None:
        super(JustAtMeMsg, self).__init__(me_qq)

    def match(self, ctx) -> bool:
        if not super().match(ctx):
            return False
        msg_chain = self.msg_chain_from_ctx(ctx)
        plain = PlainCell(msg_chain[2])
        return is_str_blank(plain.text())


class AtMeCmdMsg(AtMeMsg):
    cmd_list: List[str]

    def __init__(self, me_qq, cmd) -> None:
        super(AtMeCmdMsg, self).__init__(me_qq)
        self.cmd_list = cmd

    def match(self, ctx) -> bool:
        if not super().match(ctx):
            return False
        msg_chain = self.msg_chain_from_ctx(ctx)
        return str_contains(PlainCell(msg_chain[2]).text(), self.cmd_list)


class SpecificFriendMsg(FriendMsg):
    friend_qq: int

    def __init__(self, friend_qq) -> None:
        super(SpecificFriendMsg, self).__init__()
        self.friend_qq = friend_qq

    def match(self, ctx) -> bool:
        if not super().match(ctx):
            return False
        return self.friend_qq == FriendMessage(ctx.msg).friend_qq()


class SpecificGroupMsg(GroupMsg):
    group_qq: int

    def __init__(self, group_qq) -> None:
        super(SpecificGroupMsg, self).__init__()
        self.group_qq = group_qq

    def match(self, ctx) -> bool:
        if not super().match(ctx):
            return False
        return self.group_qq == GroupMessage(ctx.msg).group_qq()


if __name__ == "__main__":
    msg_matcher = JustAtMeMsg(123)

    class Ctx:
        def __init__(self, msg) -> None:
            self.msg = msg

    msg = {
        "type": "GroupMessage",
        "sender": {"id": 123, "nickname": "", "remark": ""},
        "messageChain": [
            {"type": "Source", "id": 123456, "time": 123456},
            {"type": "At", "target": 1234, "display": "@Mirai"},
            {"type": "Plain", "text": " "},
        ],
    }

    print(msg_matcher.match(Ctx(msg)))
