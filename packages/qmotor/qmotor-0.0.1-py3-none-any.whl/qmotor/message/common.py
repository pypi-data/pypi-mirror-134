import enum
from abc import ABC
from typing import Dict, List


class MessageType(str, enum.Enum):
    GroupMessage = "GroupMessage"
    FriendMessage = "FriendMessage"
    TempMessage = "TempMessage"  # 群临时消息
    StrangerMessage = "StrangerMessage"  # 陌生人消息
    OtherClientMessage = "OtherClientMessage"


class EventType(str, enum.Enum):
    BotOnlineEvent = "BotOnlineEvent"
    BotOfflineEventActive = "BotOfflineEventActive"  # Bot主动离线
    BotOfflineEventForce = "BotOfflineEventForce"  # Bot被挤下线
    BotOfflineEventDropped = "BotOfflineEventDropped"  # Bot被服务器断开或因网络问题而掉线
    BotReloginEvent = "BotReloginEvent"  # Bot主动重新登录
    FriendInputStatusChangedEvent = "FriendInputStatusChangedEvent"  # 好友输入状态改变
    FriendNickChangedEvent = "FriendNickChangedEvent"  # 好友昵称改变
    BotGroupPermissionChangeEvent = (
        "BotGroupPermissionChangeEvent"  # Bot在群里的权限被改变. 操作人一定是群主
    )
    BotMuteEvent = "BotMuteEvent"  # Bot被言
    BotUnmuteEvent = "BotUnmuteEvent"  # Bot被取消禁言
    BotJoinGroupEvent = "BotJoinGroupEvent"  # Bot加入了一个新群
    BotLeaveEventActive = "BotLeaveEventActive"  # Bot主动退出一个群
    BotLeaveEventKick = "BotLeaveEventKick"  # Bot被踢出一个群
    GroupRecallEvent = "GroupRecallEvent"  # 群消息撤回
    FriendRecallEvent = "FriendRecallEvent"  # 好友消息撤回
    NudgeEvent = "NudgeEvent"  # 戳一戳事件
    GroupNameChangeEvent = "GroupNameChangeEvent"  # 某个群名改变
    GroupEntranceAnnouncementChangeEvent = (
        "GroupEntranceAnnouncementChangeEvent"  # 某群入群公告改变
    )
    GroupMuteAllEvent = "GroupMuteAllEvent"  # 全员禁言
    GroupAllowAnonymousChatEvent = "GroupAllowAnonymousChatEvent"  # 匿名聊天
    GroupAllowConfessTalkEvent = "GroupAllowConfessTalkEvent"  # 坦白说
    GroupAllowMemberInviteEvent = "GroupAllowMemberInviteEvent"  # 允许群员邀请好友加群
    MemberJoinEvent = "MemberJoinEvent"  # 新人入群的事件
    MemberLeaveEventKick = "MemberLeaveEventKick"  # 成员被踢出群（该成员不是Bot）
    MemberLeaveEventQuit = "MemberLeaveEventQuit"  # 成员主动离群（该成员不是Bot）
    MemberCardChangeEvent = "MemberCardChangeEvent"  # 群名片改动
    MemberSpecialTitleChangeEvent = "MemberSpecialTitleChangeEvent"  # 群头衔改动（只有群主有操作限权）
    MemberPermissionChangeEvent = "MemberPermissionChangeEvent"  # 成员权限改变的事件（该成员不是Bot）
    MemberMuteEvent = "MemberMuteEvent"  #  群成员被禁言事件（该成员不是Bot）
    MemberUnmuteEvent = "MemberUnmuteEvent"  # 群成员被取消禁言事件（该成员不是Bot)
    MemberHonorChangeEvent = "MemberHonorChangeEvent"  # 群员称号改变
    NewFriendRequestEvent = "NewFriendRequestEvent"  # 添加好友申请
    MemberJoinRequestEvent = "MemberJoinRequestEvent"  # 用户入群申请（Bot需要有管理员权限）
    BotInvitedJoinGroupRequestEvent = "BotInvitedJoinGroupRequestEvent"  # Bot被邀请入群申请
    OtherClientOnlineEvent = "OtherClientOnlineEvent"  # 其他客户端上线
    OtherClientOfflineEvent = "OtherClientOfflineEvent"  # 其他客户端下线
    CommandExecutedEvent = "CommandExecutedEvent"  # 命令被执行


class MsgCellType(str, enum.Enum):
    Source = "Source"
    Image = "Image"
    Quote = "Quote"
    FlashImage = "FlashImage"
    At = "At"  # at群
    Face = "Face"  # qq表情
    AtAll = "AtAll"  # 群at all
    Voice = "Voice"
    MusicShare = "MusicShare"
    Plain = "Plain"
    Poke = "Poke"
    Json = "Json"
    Xml = "Xml"
    App = "App"
    Dice = "Dice"
    Forward = "Forward"
    File = "File"
    MiraiCode = "MiraiCode"


class DictWrapper(ABC):
    body: Dict
    __slot__ = ("body",)

    def __init__(self, body):
        self.body = body

    def get(self, *args):
        return self.body.get(*args)

    def __getitem__(self, key):
        return self.body[key]

    def __setitem__(self, key, value):
        self.body[key] = value


class BasicMessage(DictWrapper):
    def __init__(self, body):
        super(BasicMessage, self).__init__(body)

    def sender(self) -> Dict:
        return self.body.get("sender", {})

    def messageChain(self) -> List[Dict]:
        return self.body.get("messageChain", [])

    def type(self) -> str:
        return self.body.get("type", None)

    def source(self) -> Dict:
        return self.messageChain()[0]


class FriendMessage(BasicMessage):
    def __init__(self, body):
        super(FriendMessage, self).__init__(body)

    def friend_qq(self) -> int:
        return self.sender().get("id", None)

    def friend_name(self) -> str:
        return self.sender().get("nickname", None)

    def friend_remark(self) -> str:
        return self.sender().get("remark", None)


class GroupMessage(BasicMessage):
    def __init__(self, body):
        super(GroupMessage, self).__init__(body)

    def group(self) -> Dict:
        return self.sender().get("group", {})

    def group_qq(self) -> int:
        return self.group().get("id", None)

    def sender_qq(self) -> str:
        return self.sender().get("id", None)

    def sender_name(self) -> str:
        return self.sender().get("memberName", None)

    def sender_permission(self) -> str:
        return self.sender().get("permission", None)

    def sender_special_title(self) -> str:
        return self.sender().get("specialTitle", None)


class GroupTempMessage(GroupMessage):
    def __init__(self, body):
        super(GroupTempMessage, self).__init__(body)


class StrangerMessage(FriendMessage):
    def __init__(self, body):
        super(StrangerMessage, self).__init__(body)


class OtherClientMessage(BasicMessage):
    def __init__(self, body):
        super(OtherClientMessage, self).__init__(body)

    def platform(self) -> str:
        return self.sender().get("platform", None)

    def sender_id(self) -> int:
        return self.sender().get("id", None)


class BasicCell(DictWrapper):
    def __init__(self, body):
        super().__init__(body)

    def type(self) -> str:
        return self.body.get("type", None)


class SourceCell(BasicCell):
    def __init__(self, body):
        super().__init__(body)

    def id(self):
        return self.body.get("id", None)

    def time(self):
        return self.body.get("time", None)


class AtCell(BasicCell):
    def __init__(self, body):
        super(AtCell, self).__init__(body)

    def target(self) -> int:
        return self.body.get("target", None)

    def display(self) -> str:
        return self.body.get("display", None)


class AtAllCell(BasicCell):
    def __init__(self, body):
        super(AtAllCell, self).__init__(body)


class PlainCell(BasicCell):
    def __init__(self, body):
        super(PlainCell, self).__init__(body)

    def text(self) -> str:
        return self.body.get("text", None)


class FaceCell(BasicCell):
    def __init__(self, body):
        super(FaceCell, self).__init__(body)

    def face_id(self):
        return self.body.get("faceId", None)

    def name(self):
        return self.body.get("name", None)


class ImageCell(BasicCell):
    def __init__(self, body):
        super(ImageCell, self).__init__(body)

    def image_id(self):
        return self.body.get("imageId", None)

    def url(self):
        return self.body.get("url", None)

    def path(self):
        return self.body.get("path", None)

    def base64(self):
        return self.body.get("base64", None)


class FlashImageCell(ImageCell):
    def __init__(self, body):
        super(FlashImageCell, self).__init__(body)


class VoiceCell(BasicCell):
    def __init__(self, body):
        super(VoiceCell, self).__init__(body)

    def voice_id(self):
        return self.body.get("voiceId", None)

    def url(self):
        return self.body.get("url", None)

    def path(self):
        return self.body.get("path", None)

    def base64(self):
        return self.body.get("base64", None)

    def length(self):
        return self.body.get("length", None)


class XmlCell(BasicCell):
    def __init__(self, body):
        super(XmlCell, self).__init__(body)

    def xml(self):
        return self.body.get("xml", None)


class JsonCell(BasicCell):
    def __init__(self, body):
        super(JsonCell, self).__init__(body)

    def json(self) -> str:
        return self.body.get("json"), None


class AppCell(BasicCell):
    def __init__(self, body):
        super(AppCell, self).__init__(body)

    def content(self):
        return self.body.get("content", None)


class PokeCell(BasicCell):
    def __init__(self, body):
        super(PokeCell, self).__init__(body)

    def name(self):
        return self.body.get("name", None)


class DiceCell(BasicCell):
    def __init__(self, body):
        super(DiceCell, self).__init__(body)

    def value(self):
        return self.body.get("value", None)


class MusicShareCell(BasicCell):
    def __init__(self, body):
        super(MusicShareCell, self).__init__(body)

    def kind(self) -> str:
        return self.body.get("kind", None)

    def title(self) -> str:
        return self.body.get("title", None)

    def summary(self):
        return self.body.get("summary", None)

    def jump_url(self):
        return self.body.get("jumpUrl", None)

    def picture_url(self):
        return self.body.get("pictureUrl", None)

    def music_url(self):
        return self.body.get("musicUrl", None)

    def brief(self):
        return self.body.get("brief", None)


class ForwardCell(BasicCell):
    def __init__(self, body):
        super(ForwardCell, self).__init__(body)

    def node_list(self) -> List[Dict]:
        return self.body.get("nodeList", None)


class FileCell(BasicCell):
    def __init__(self, body):
        super(FileCell, self).__init__(body)

    def id(self):
        return self.body.get("id", None)

    def name(self):
        return self.body.get("name", None)

    def size(self):
        return self.body.get("size", None)


class MiraiCodeCell(BasicCell):
    def __init__(self, body):
        super(MiraiCodeCell, self).__init__(body)

    def code(self):
        return self.body.get("code", None)
