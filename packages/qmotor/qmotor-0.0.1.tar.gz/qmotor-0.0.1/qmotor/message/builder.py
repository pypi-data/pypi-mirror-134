from ..message.common import MsgCellType


def text(text):
    return {"type": MsgCellType.Plain, "text": text}


def image(*args, image_id=None, url=None, path=None, base64=None):
    if image_id:
        return {"type": MsgCellType.Image, "imageId": image_id}
    elif url:
        return {"type": MsgCellType.Image, "url": url}
    elif path:
        return {"type": MsgCellType.Image, "path": path}
    elif base64:
        return {"type": MsgCellType.Image, "base64": base64}
    else:
        raise Exception("Must KWArags!")


def at(target: int):
    return {"type": MsgCellType.At, "target": target}


def at_all():
    return {"type": MsgCellType.AtAll}


def _f(*args, face_id=None, name=None):
    if face_id is not None:
        return {"type": MsgCellType.Face, "faceId": face_id}
    elif name:
        return {"type": MsgCellType.Face, "name": name}
    else:
        raise Exception()


class face:
    def __new__(self, *args, face_id=None, name=None) -> dict:
        return _f(*args, face_id=face_id, name=name)

    JING_YA = _f(face_id=0)

    PIE_ZUI = _f(face_id=1)

    SE = _f(face_id=2)

    DE_YI = _f(face_id=4)

    LIU_LEI = _f(face_id=5)

    HAI_XIU = _f(face_id=6)

    BI_ZUI = _f(face_id=8)

    SHUI = _f(face_id=9)

    DA_KU = _f(face_id=10)

    GAN_GA = _f(face_id=11)

    FA_NU = _f(face_id=12)

    TIAO_PI = _f(face_id=13)

    ZI_YA = _f(face_id=14)

    WEI_XIAO = _f(face_id=15)

    NAN_GUO = _f(face_id=16)

    KU = _f(face_id=17)

    ZHUA_KUANG = _f(face_id=18)

    TU = _f(face_id=19)

    TOU_XIAO = _f(face_id=20)

    KE_AI = _f(face_id=21)

    BAI_YAN = _f(face_id=22)

    AO_MAN = _f(face_id=23)

    JI_E = _f(face_id=24)

    KUN = _f(face_id=25)

    JING_KONG = _f(face_id=26)

    LIU_HAN = _f(face_id=27)

    HAN_XIAO = _f(face_id=28)

    YOU_XIAN = _f(face_id=29)

    FEN_DOU = _f(face_id=30)

    ZHOU_MA = _f(face_id=31)

    YI_WEN = _f(face_id=32)

    XU = _f(face_id=33)

    YUN = _f(face_id=34)

    ZHE_MO = _f(face_id=35)

    SHUAI = _f(face_id=36)

    KU_LOU = _f(face_id=37)

    QIAO_DA = _f(face_id=38)

    ZAI_JIAN = _f(face_id=39)

    FA_DOU = _f(face_id=41)

    AI_QING = _f(face_id=42)

    TIAO_TIAO = _f(face_id=43)

    ZHU_TOU = _f(face_id=46)

    YONG_BAO = _f(face_id=49)

    DAN_GAO = _f(face_id=53)

    SHAN_DIAN = _f(face_id=54)

    ZHA_DAN = _f(face_id=55)

    DAO = _f(face_id=56)

    ZU_QIU = _f(face_id=57)

    BIAN_BIAN = _f(face_id=59)

    KA_FEI = _f(face_id=60)

    FAN = _f(face_id=61)

    MEI_GUI = _f(face_id=63)

    DIAO_XIE = _f(face_id=64)

    AI_XIN = _f(face_id=66)

    XIN_SUI = _f(face_id=67)

    LI_WU = _f(face_id=69)

    TAI_YANG = _f(face_id=74)

    YUE_LIANG = _f(face_id=75)

    ZAN = _f(face_id=76)

    CAI = _f(face_id=77)

    WO_SHOU = _f(face_id=78)

    SHENG_LI = _f(face_id=79)

    FEI_WEN = _f(face_id=85)

    OU_HUO = _f(face_id=86)

    XI_GUA = _f(face_id=89)

    LENG_HAN = _f(face_id=96)

    CA_HAN = _f(face_id=97)

    KOU_BI = _f(face_id=98)

    GU_ZHANG = _f(face_id=99)

    QIU_DA_LE = _f(face_id=100)

    HUAI_XIAO = _f(face_id=101)

    ZUO_HENG_HENG = _f(face_id=102)

    YOU_HENG_HENG = _f(face_id=103)

    HA_QIAN = _f(face_id=104)

    BI_SHI = _f(face_id=105)

    WEI_QU = _f(face_id=106)

    KUAI_KU_LE = _f(face_id=107)

    YING_XIAN = _f(face_id=108)

    QIN_QIN = _f(face_id=109)

    XIA = _f(face_id=110)

    KE_LIAN = _f(face_id=111)

    CAI_DAO = _f(face_id=112)

    PI_JIU = _f(face_id=113)

    LAN_QIU = _f(face_id=114)

    PING_PONG = _f(face_id=115)

    SHI_AI = _f(face_id=116)

    PIAO_CHONG = _f(face_id=117)

    BAO_QUAN = _f(face_id=118)

    GOU_YING = _f(face_id=119)

    QUAN_TOU = _f(face_id=120)

    CHA_JIN = _f(face_id=121)

    AI_NI = _f(face_id=122)

    NO = _f(face_id=123)

    OK = _f(face_id=124)

    ZHUAN_QUAN = _f(face_id=125)

    KE_TOU = _f(face_id=126)

    HUI_TOU = _f(face_id=127)

    TIAO_SHENG = _f(face_id=128)

    HUI_SHOU = _f(face_id=129)

    JI_DONG = _f(face_id=130)

    JIE_WU = _f(face_id=131)

    XIAN_WEN = _f(face_id=132)

    ZUO_TAI_JI = _f(face_id=133)

    YOU_TAI_JI = _f(face_id=134)

    SHUANG_XI = _f(face_id=136)

    BIAN_PAO = _f(face_id=137)

    DENG_LONG = _f(face_id=138)

    K_GE = _f(face_id=140)

    HE_CAI = _f(face_id=144)

    QI_DAO = _f(face_id=145)

    BAO_JIN = _f(face_id=146)

    BANG_BANG_TANG = _f(face_id=147)

    FEI_JI = _f(face_id=151)

    CHAO_PIAO = _f(face_id=158)

    YAO = _f(face_id=168)

    SHOU_QIANG = _f(face_id=169)

    CHA = _f(face_id=171)

    ZHA_YAN_JING = _f(face_id=172)

    LEI_BEN = _f(face_id=148)

    WU_NAI = _f(face_id=174)

    MAI_MENG = _f(face_id=176)

    XIAO_JIU_JIE = _f(face_id=177)

    PEN_XIE = _f(face_id=178)

    DOGE = _f(face_id=179)

    JING_XI = _f(face_id=180)

    SAO_RAO = _f(face_id=181)

    XIAO_KU = _f(face_id=182)

    WO_ZUI_MEI = _f(face_id=183)

    HE_XIE = _f(face_id=184)

    YANG_TUO = _f(face_id=185)

    DAN = _f(face_id=188)

    JU_HUA = _f(face_id=190)

    HONG_BAO = _f(face_id=192)

    DA_XIAO = _f(face_id=193)

    BU_KAI_XIN = _f(face_id=194)

    LENG_MO = _f(face_id=197)

    E = _f(face_id=198)

    HAO_BANG = _f(face_id=199)

    BAI_TUO = _f(face_id=200)

    DIAN_ZAN = _f(face_id=201)

    WU_LIAO = _f(face_id=202)

    TUO_LIAN = _f(face_id=203)

    CHI = _f(face_id=204)

    SONG_HUA = _f(face_id=205)

    HAI_PA = _f(face_id=206)

    XIAO_YANG_ER = _f(face_id=208)

    BIAO_LEI = _f(face_id=210)

    WO_BU_KAN = _f(face_id=211)

    TUO_SAI = _f(face_id=212)

    BO_BO = _f(face_id=214)

    HU_LIAN = _f(face_id=215)

    PAI_TOU = _f(face_id=216)

    CHE_YI_CHE = _f(face_id=217)

    TIAN_YI_TIAN = _f(face_id=218)

    CENG_YI_CENG = _f(face_id=219)

    ZHUAI_ZHA_TIAN = _f(face_id=220)

    DING_GUA_GUA = _f(face_id=221)

    BAO_BAO = _f(face_id=222)

    BAO_JI = _f(face_id=223)

    KAI_QIANG = _f(face_id=224)

    LIAO_YI_LIAO = _f(face_id=225)

    PAI_ZHUO = _f(face_id=226)

    GONG_XI = _f(face_id=228)

    GAN_BEI = _f(face_id=229)

    CHAO_FENG = _f(face_id=230)

    HENG = _f(face_id=231)

    FO_XI = _f(face_id=232)

    QIA_YI_QIA = _f(face_id=233)

    JING_DAI = _f(face_id=234)

    CHAN_DOU = _f(face_id=235)

    KEN_TOU = _f(face_id=236)

    YUAN_LIANG = _f(face_id=239)

    PEN_LIAN = _f(face_id=240)

    SHENG_RI_KUAI_LE = _f(face_id=241)

    TOU_ZHUANG_JI = _f(face_id=242)

    SHUAI_TOU = _f(face_id=243)

    RENG_GOU = _f(face_id=244)

    JIA_YOU_BI_SHENG = _f(face_id=245)

    JIA_YOU_BAO_BAO = _f(face_id=246)

    KOU_ZHAO_HU_TI = _f(face_id=247)

    BAN_ZHUAN_ZHONG = _f(face_id=260)

    MANG_DAO_FEI_QI = _f(face_id=261)

    NAO_KUO_TENG = _f(face_id=262)

    CANG_SANG = _f(face_id=263)

    WU_LIAN = _f(face_id=264)

    LA_YAN_JING = _f(face_id=265)

    O_YO = _f(face_id=266)

    TOU_TU = _f(face_id=267)

    WEN_HAO_LIAN = _f(face_id=268)

    AN_ZHONG_GUAN_CHA = _f(face_id=269)

    EMM = _f(face_id=270)

    CHI_GUA = _f(face_id=271)

    HE_HE_DA = _f(face_id=272)

    WO_SUAN_LE = _f(face_id=273)

    TAI_NAN_LE = _f(face_id=274)

    LA_JIAO_JIANG = _f(face_id=276)

    WANG_WANG = _f(face_id=277)

    HAN = _f(face_id=278)

    DA_LIAN = _f(face_id=279)

    JI_ZHANG = _f(face_id=280)

    WU_YAN_XIAO = _f(face_id=281)

    JING_LI = _f(face_id=282)

    KUANG_XIAO = _f(face_id=283)

    MIAN_WU_BIAO_QING = _f(face_id=284)

    MO_YU = _f(face_id=285)

    MO_GUI_XIAO = _f(face_id=286)

    O = _f(face_id=287)

    QING = _f(face_id=288)

    ZHENG_YAN = _f(face_id=289)

    QIAO_KAI_XIN = _f(face_id=290)

    ZHEN_JING = _f(face_id=291)

    RANG_WO_KANG_KANG = _f(face_id=292)

    MO_JIN_LI = _f(face_id=293)

    QI_DAI = _f(face_id=294)

    NA_DAO_HONG_BAO = _f(face_id=295)

    ZHEN_HAO = _f(face_id=296)

    BAI_XIE = _f(face_id=297)

    YUAN_BAO = _f(face_id=298)

    NIU_A = _f(face_id=299)

    PANG_SAN_JIN = _f(face_id=300)

    HAO_SHAN = _f(face_id=301)

    ZUO_BAI_NIAN = _f(face_id=302)

    YOU_BAI_NIAN = _f(face_id=303)

    HONG_BAO_BAO = _f(face_id=304)

    YOU_QIN_QIN = _f(face_id=305)

    NIU_QI_CHONG_TIAN = _f(face_id=306)

    YOU_BAI_NIAN = _f(face_id=303)

    MIAO_MIAO = _f(face_id=307)

    QIU_HONG_BAO = _f(face_id=308)

    XIE_HONG_BAO = _f(face_id=309)

    XIN_NIAN_YAN_HUA = _f(face_id=310)

    YOU_BAI_NIAN = _f(face_id=303)

    DA_CALL = _f(face_id=311)

    BIAN_XING = _f(face_id=312)

    KE_DAO_LE = _f(face_id=313)

    ZI_XI_FEN_XI = _f(face_id=314)

    JIA_YOU = _f(face_id=315)

    WO_MEI_SHI = _f(face_id=316)

    CAI_GOU = _f(face_id=317)

    CHONG_BAI = _f(face_id=318)

    BI_XIN = _f(face_id=319)

    QING_ZHU = _f(face_id=320)

    LAO_SE_PI = _f(face_id=321)

    JU_JUE = _f(face_id=322)

    XIAN_QI = _f(face_id=323)

    CHI_TANG = _f(face_id=324)


def flash_image(*args, image_id=None, url=None, path=None, base64=None):
    if image_id:
        return {"type": MsgCellType.FlashImage, "imageId": image_id}
    elif url:
        return {"type": MsgCellType.FlashImage, "url": url}
    elif path:
        return {"type": MsgCellType.FlashImage, "path": path}
    elif base64:
        return {"type": MsgCellType.FlashImage, "base64": base64}
    else:
        raise Exception("Must KWArags!")


def voice(*args, voice_id=None, url=None, path=None, base64=None):
    if voice_id:
        return {"type": MsgCellType.Voice, "voiceId": voice_id}
    elif url:
        return {"type": MsgCellType.Voice, "url": url}
    elif path:
        return {"type": MsgCellType.Voice, "path": path}
    elif base64:
        return {"type": MsgCellType.Voice, "base64": base64}
    else:
        raise Exception("Must KWArags!")


def xml(xml):
    return {"type": MsgCellType.Xml, "xml": xml}


def json(json):
    return {"type": MsgCellType.Json, "json": json}


def app(app):
    return {"type": MsgCellType.App, "app": app}


def poke(name):
    # name 的可选值
    # "Poke": 戳一戳
    # "ShowLove": 比心
    # "Like": 点赞
    # "Heartbroken": 心碎
    # "SixSixSix": 666
    # "FangDaZhao": 放大招
    return {"type": MsgCellType.Poke, "name": name}


def dice(value):
    return {"type": MsgCellType.Dice, "value": value}


def music_share(music):
    return {
        "type": MsgCellType.MusicShare,
        "kind": music["kind"],
        "title": music["title"],
        "summary": music["summary"],
        "jumpUrl": music["jumpUrl"],
        "pictureUrl": music["pictureUrl"],
        "musicUrl": music["musicUrl"],
        "brief": music["brief"],
    }


def forward(node_list):
    assert isinstance(node_list, list)
    return {"type": MsgCellType.Forward, "nodeList": node_list}


def file(file):
    return {
        "type": MsgCellType.File,
        "id": file["id"],
        "name": file["name"],
        "size": file["size"],
    }


class ChatBubble(list):
    def __init__(self, *args):
        super(ChatBubble, self).__init__(args)


class MsgChainBuilder:
    __slot__ = ("chain",)

    def __init__(self) -> None:
        self.chain = []

    def msg(self, text):
        self.chain.append({"type": MsgCellType.Plain, "text": text})
        return self

    def image(self, *args, image_id=None, url=None, path=None, base64=None):
        if image_id:
            self.chain.append({"type": MsgCellType.Image, "imageId": image_id})
        elif url:
            self.chain.append({"type": MsgCellType.Image, "url": url})
        elif path:
            self.chain.append({"type": MsgCellType.Image, "path": path})
        elif base64:
            self.chain.append({"type": MsgCellType.Image, "base64": base64})
        else:
            raise Exception("Must KWArags!")
        return self

    def at(self, target: int):
        self.chain.append({"type": MsgCellType.At, "target": target})
        return self

    def at_all(self):
        self.chain.append({"type": MsgCellType.AtAll})
        return self

    def face(self, *args, face_id=None, name=None):
        assert face_id is not None and name is not None
        if face_id:
            self.chain.append({"type": MsgCellType.Face, "faceId": face_id})
        elif name:
            self.chain.append({"type": MsgCellType.Face, "name": name})
        else:
            raise Exception()
        return self

    def flash_image(self, *args, image_id=None, url=None, path=None, base64=None):
        if image_id:
            self.chain.append({"type": MsgCellType.FlashImage, "imageId": image_id})
        elif url:
            self.chain.append({"type": MsgCellType.FlashImage, "url": url})
        elif path:
            self.chain.append({"type": MsgCellType.FlashImage, "path": path})
        elif base64:
            self.chain.append({"type": MsgCellType.FlashImage, "base64": base64})
        else:
            raise Exception("Must KWArags!")
        return self

    def voice(self, *args, voice_id=None, url=None, path=None, base64=None):
        if voice_id:
            self.chain.append({"type": MsgCellType.Voice, "voiceId": voice_id})
        elif url:
            self.chain.append({"type": MsgCellType.Voice, "url": url})
        elif path:
            self.chain.append({"type": MsgCellType.Voice, "path": path})
        elif base64:
            self.chain.append({"type": MsgCellType.Voice, "base64": base64})
        else:
            raise Exception("Must KWArags!")
        return self

    def xml(self, xml):
        self.chain.append({"type": MsgCellType.Xml, "xml": xml})
        return self

    def json(self, json):
        self.chain.append({"type": MsgCellType.Json, "json": json})
        return self

    def app(self, app):
        self.chain.append({"type": MsgCellType.App, "app": app})
        return self

    def poke(self, name):
        # name 的可选值
        # "Poke": 戳一戳
        # "ShowLove": 比心
        # "Like": 点赞
        # "Heartbroken": 心碎
        # "SixSixSix": 666
        # "FangDaZhao": 放大招
        self.chain.append({"type": MsgCellType.Poke, "name": name})
        return self

    def dice(self, value):
        self.chain.append({"type": MsgCellType.Dice, "value": value})
        return self

    def music_share(self, music):
        self.chain.append(
            {
                "type": MsgCellType.MusicShare,
                "kind": music["kind"],
                "title": music["title"],
                "summary": music["summary"],
                "jumpUrl": music["jumpUrl"],
                "pictureUrl": music["pictureUrl"],
                "musicUrl": music["musicUrl"],
                "brief": music["brief"],
            }
        )
        return self

    def forward(self, node_list):
        assert isinstance(node_list, list)
        self.chain.append({"type": MsgCellType.Forward, "nodeList": node_list})
        return self

    def file(self, file):
        self.chain.append(
            {
                "type": MsgCellType.File,
                "id": file["id"],
                "name": file["name"],
                "size": file["size"],
            }
        )
        return self

    def build(self):
        return self.chain


class SendMsgBuilder:
    def __init__(self, command=None, receiver=None):
        self.queue = []
        self.command = command
        self.receiver = receiver

    def friend(self, qq):
        self.command = "sendFriendMessage"
        self.receiver = qq
        return self

    def group(self, qq):
        self.command = "sendGroupMessage"
        self.receiver = qq
        return self

    def bubble(self, bubble):
        self.queue.append(bubble)
        return self

    def msg(self, text):
        self.queue.append([{"type": MsgCellType.Plain, "text": text}])
        return self

    def image(self, *args, image_id=None, url=None, path=None, base64=None):
        if image_id:
            self.queue.append(
                ChatBubble({"type": MsgCellType.Image, "imageId": image_id})
            )
        elif url:
            self.queue.append([{"type": MsgCellType.Image, "url": url}])
        elif path:
            self.queue.append([{"type": MsgCellType.Image, "path": path}])
        elif base64:
            self.queue.append([{"type": MsgCellType.Image, "base64": base64}])
        else:
            raise Exception("Must KWArags!")
        return self

    def at(self, target: int):
        self.queue.append([{"type": MsgCellType.At, "target": target}])
        return self

    def at_all(self):
        self.chain.append([{"type": MsgCellType.AtAll}])
        return self

    def face(self, *args, face_id=None, name=None):
        assert face_id is not None and name is not None
        if face_id:
            self.queue.append([{"type": MsgCellType.Face, "faceId": face_id}])
        elif name:
            self.queue.append([{"type": MsgCellType.Face, "name": name}])
        else:
            raise Exception()
        return self

    def flash_image(self, *args, image_id=None, url=None, path=None, base64=None):
        if image_id:
            self.queue.append([{"type": MsgCellType.FlashImage, "imageId": image_id}])
        elif url:
            self.queue.append([{"type": MsgCellType.FlashImage, "url": url}])
        elif path:
            self.queue.append([{"type": MsgCellType.FlashImage, "path": path}])
        elif base64:
            self.queue.append([{"type": MsgCellType.FlashImage, "base64": base64}])
        else:
            raise Exception("Must KWArags!")
        return self

    def voice(self, *args, voice_id=None, url=None, path=None, base64=None):
        if voice_id:
            self.queue.append([{"type": MsgCellType.Voice, "voiceId": voice_id}])
        elif url:
            self.queue.append([{"type": MsgCellType.Voice, "url": url}])
        elif path:
            self.queue.append([{"type": MsgCellType.Voice, "path": path}])
        elif base64:
            self.queue.append([{"type": MsgCellType.Voice, "base64": base64}])
        else:
            raise Exception("Must KWArags!")
        return self

    def xml(self, xml):
        self.chain.append([{"type": MsgCellType.Xml, "xml": xml}])
        return self

    def json(self, json):
        self.queue.append([{"type": MsgCellType.Json, "json": json}])
        return self

    def app(self, app):
        self.queue.append([{"type": MsgCellType.App, "app": app}])
        return self

    def poke(self, name):
        # name 的可选值
        # "Poke": 戳一戳
        # "ShowLove": 比心
        # "Like": 点赞
        # "Heartbroken": 心碎
        # "SixSixSix": 666
        # "FangDaZhao": 放大招
        self.queue.append([{"type": MsgCellType.Poke, "name": name}])
        return self

    def dice(self, value):
        self.queue.append([{"type": MsgCellType.Dice, "value": value}])
        return self

    def music_share(self, music):
        self.queue.append(
            [
                {
                    "type": MsgCellType.MusicShare,
                    "kind": music["kind"],
                    "title": music["title"],
                    "summary": music["summary"],
                    "jumpUrl": music["jumpUrl"],
                    "pictureUrl": music["pictureUrl"],
                    "musicUrl": music["musicUrl"],
                    "brief": music["brief"],
                }
            ]
        )
        return self

    def forward(self, node_list):
        assert isinstance(node_list, list)
        self.queue.append([{"type": MsgCellType.Forward, "nodeList": node_list}])
        return self

    def file(self, file):
        self.queue.append(
            [
                {
                    "type": MsgCellType.File,
                    "id": file["id"],
                    "name": file["name"],
                    "size": file["size"],
                }
            ]
        )
        return self

    def build(self):
        return [
            {
                "syncId": "-1",
                "command": self.command,
                "subCommand": None,
                "content": {
                    "sessionKey": None,
                    "target": self.receiver,
                    "messageChain": msg,
                },
            }
            for msg in self.queue
        ]
