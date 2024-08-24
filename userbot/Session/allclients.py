# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from logging import getLogger
from .._database._var import Var, Database
from .client import ChumsBot, ChumsBot2, ChumsBot3, ChumsBot4, ChumsBot5, ChumsBot6, ChumsBot7, ChumsBot8, ChumsBot9, ChumsBot10, ChumsBot11, ChumsBot12, ChumsBot13, ChumsBot14, ChumsBot15, ChumsBot16, ChumsBot17, ChumsBot18, ChumsBot19, ChumsBot10, ChumsBot20, ChumsBot21, ChumsBot22, ChumsBot23, ChumsBot24, ChumsBot25, ChumsBot26, ChumsBot27, ChumsBot28, ChumsBot29, ChumsBot30, ChumsBot31, ChumsBot32, ChumsBot33, ChumsBot34, ChumsBot35, ChumsBot36, ChumsBot37, ChumsBot38, ChumsBot39, ChumsBot40, ChumsBot41, ChumsBot42, ChumsBot43, ChumsBot44, ChumsBot45, ChumsBot46, ChumsBot47, ChumsBot48, ChumsBot49, ChumsBot50
from .._database import pdB
LOGS = getLogger(__name__)

try:
    if not pdB.get_key("SESSION") or Var.STRING_SESSION and Database.BOT_TOKEN:
        ChumsBot = ChumsBot
    if not pdB.get_key("SESSION2") or Var.STRING_SESSION2 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot2
    if not pdB.get_key("SESSION3") or Var.STRING_SESSION3 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot3
    if not pdB.get_key("SESSION4") or Var.STRING_SESSION4 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot4
    if not pdB.get_key("SESSION5") or Var.STRING_SESSION5 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot5
    if not pdB.get_key("SESSION6") or Var.STRING_SESSION6 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot6
    if not pdB.get_key("SESSION7") or Var.STRING_SESSION7 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot7
    if not pdB.get_key("SESSION8") or Var.STRING_SESSION8 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot8
    if not pdB.get_key("SESSION9") or Var.STRING_SESSION9 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot9
    if not pdB.get_key("SESSION10") or Var.STRING_SESSION10 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot10
    if not pdB.get_key("SESSION11") or Var.STRING_SESSION11 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot11
    if not pdB.get_key("SESSION12") or Var.STRING_SESSION12 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot12
    if not pdB.get_key("SESSION13") or Var.STRING_SESSION13 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot13
    if not pdB.get_key("SESSION14") or Var.STRING_SESSION14 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot14
    if not pdB.get_key("SESSION15") or Var.STRING_SESSION15 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot15
    if not pdB.get_key("SESSION16") or Var.STRING_SESSION16 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot16
    if not pdB.get_key("SESSION17") or Var.STRING_SESSION17 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot17
    if not pdB.get_key("SESSION18") or Var.STRING_SESSION18 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot18
    if not pdB.get_key("SESSION19") or Var.STRING_SESSION19 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot19
    if not pdB.get_key("SESSION20") or Var.STRING_SESSION20 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot20
    if not pdB.get_key("SESSION21") or Var.STRING_SESSION21 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot21
    if not pdB.get_key("SESSION22") or Var.STRING_SESSION22 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot22
    if not pdB.get_key("SESSION23") or Var.STRING_SESSION23 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot25
    if not pdB.get_key("SESSION24") or Var.STRING_SESSION24 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot24
    if not pdB.get_key("SESSION25") or Var.STRING_SESSION25 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot25
    if not pdB.get_key("SESSION26") or Var.STRING_SESSION26 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot26
    if not pdB.get_key("SESSION27") or Var.STRING_SESSION27 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot27
    if not pdB.get_key("SESSION28") or Var.STRING_SESSION28 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot28
    if not pdB.get_key("SESSION29") or Var.STRING_SESSION29 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot29
    if not pdB.get_key("SESSION30") or Var.STRING_SESSION30 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot30
    if not pdB.get_key("SESSION31") or Var.STRING_SESSION31 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot31
    if not pdB.get_key("SESSION32") or Var.STRING_SESSION32 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot32
    if not pdB.get_key("SESSION33") or Var.STRING_SESSION33 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot33
    if not pdB.get_key("SESSION34") or Var.STRING_SESSION34 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot34
    if not pdB.get_key("SESSION35") or Var.STRING_SESSION35 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot35
    if not pdB.get_key("SESSION36") or Var.STRING_SESSION36 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot36
    if not pdB.get_key("SESSION37") or Var.STRING_SESSION37 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot37
    if not pdB.get_key("SESSION38") or Var.STRING_SESSION38 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot38
    if not pdB.get_key("SESSION39") or Var.STRING_SESSION39 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot39
    if not pdB.get_key("SESSION40") or Var.STRING_SESSION41 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot40
    if not pdB.get_key("SESSION42") or Var.STRING_SESSION42 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot42
    if not pdB.get_key("SESSION43") or Var.STRING_SESSION43 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot43
    if not pdB.get_key("SESSION44") or Var.STRING_SESSION44 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot44
    if not pdB.get_key("SESSION45") or Var.STRING_SESSION45 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot45
    if not pdB.get_key("SESSION46") or Var.STRING_SESSION46 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot46
    if not pdB.get_key("SESSION47") or Var.STRING_SESSION47 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot47
    if not pdB.get_key("SESSION48") or Var.STRING_SESSION48 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot48
    if not pdB.get_key("SESSION49") or Var.STRING_SESSION49 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot49
    if not pdB.get_key("SESSION50") or Var.STRING_SESSION50 and Database.BOT_TOKEN:
        ChumsBot = ChumsBot50
except Exception as e:
    LOGS.error(f"ChumsBot - {e}")
