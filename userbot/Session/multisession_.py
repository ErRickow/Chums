# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

from telethon import functions, utils
from pyrogram import idle
from .._database._var import Var, Database
from logging import getLogger
from .._database import pdB
from .client import *

from .pyroclient import *
import sys
LOGS = getLogger(__name__)
import os

from pyrogram import __version__ as pyrover
PRIVATE = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID"))


cmdhr = os.environ.get("COMMAND_HAND_LER") or "."

MSG_ON = """
꧁༺ Chums Userbot ༻꧂\n\n
User - @{} 
Pyrogram Version - `{}' `[HAVE ENABLED]` 
Type `{}alive` to Check Bot 
Total Clients - {}
"""


THON_ON = """
꧁༺ Panda Userbot ༻꧂\n\n
User - @{} 
Version - `{}' `[HAVE ENABLED]` 
Type `{}alive` to Check Bot 
Total Clients - {}
"""


def Telethon():
    failed = 0
    if pdB.get_key("SESSION") or Var.STRING_SESSION and Database.BOT_TOKEN:
        try:
            ChumsBot.connect()
            tgbot.start(bot_token=Database.BOT_TOKEN)
            config = ChumsBot(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot.session.server_address:
                    if ChumsBot.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot.session.save()
                    break
            tgbot.me = tgbot.get_me()
            ChumsBot.me = ChumsBot.get_me()
            ChumsBot.uid = tgbot.uid = utils.get_peer_id(ChumsBot.me)      
            if pdB.get_key("BOT_USERNAME"):
                pdB.set_key("BOT_USERNAME", tgbot.me.username)
            if pdB.get_key("OWNER_ID") or [] or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot.uid)
           
        except Exception as e:
            LOGS.error(f"STRING_SESSION1 - {e}")
            sys.exit()
            
    if pdB.get_key("SESSION2") or Var.STRING_SESSION2 and Database.BOT_TOKEN:
        try:
            ChumsBot2.connect()
            config = ChumsBot2(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot2.session.server_address:
                    if ChumsBot2.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot2.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot2.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot2.session.save()
                    break
            tgbot.get_me()
            ChumsBot2.me = ChumsBot2.get_me()
            ChumsBot2.uid = tgbot.uid = utils.get_peer_id(ChumsBot2.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot2.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot2.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION2 - {e}")
            sys.exit()

    if pdB.get_key("SESSION3") or Var.STRING_SESSION3 and Database.BOT_TOKEN:
        try:
            ChumsBot3.connect()
            config = ChumsBot3(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot3.session.server_address:
                    if ChumsBot3.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot3.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot3.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot3.session.save()
                    break
            tgbot.get_me()
            ChumsBot3.me = ChumsBot3.get_me()
            ChumsBot3.uid = tgbot.uid = utils.get_peer_id(ChumsBot3.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot3.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot3.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION3 - {e}")
            sys.exit()

    if pdB.get_key("SESSION4") or Var.STRING_SESSION4 and Database.BOT_TOKEN:
        try:
            ChumsBot4.connect()
            config = ChumsBot4(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot4.session.server_address:
                    if ChumsBot4.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot4.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot4.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot4.session.save()
                    break
            tgbot.get_me()
            ChumsBot4.me = ChumsBot4.get_me()
            ChumsBot4.uid = tgbot.uid = utils.get_peer_id(ChumsBot4.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot4.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot4.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION4 - {e}")
            sys.exit()

    if pdB.get_key("SESSION5") or Var.STRING_SESSION5 and Database.BOT_TOKEN:
        try:
            ChumsBot5.connect()
            config = ChumsBot5(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot5.session.server_address:
                    if ChumsBot5.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot5.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot5.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot5.session.save()
                    break
            tgbot.get_me()
            ChumsBot5.me = ChumsBot5.get_me()
            ChumsBot5.uid = tgbot.uid = utils.get_peer_id(ChumsBot5.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot5.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot5.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION5 - {e}")
            sys.exit()

    if pdB.get_key("SESSION6") or Var.STRING_SESSION6 and Database.BOT_TOKEN:
        try:
            ChumsBot6.connect()
            config = ChumsBot6(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot6.session.server_address:
                    if ChumsBot6.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot6.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot6.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot6.session.save()
                    break
            tgbot.get_me()
            ChumsBot6.me = ChumsBot6.get_me()
            ChumsBot6.uid = tgbot.uid = utils.get_peer_id(ChumsBot6.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot6.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot6.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION6 - {e}")
            sys.exit()

    if pdB.get_key("SESSION7") or Var.STRING_SESSION7 and Database.BOT_TOKEN:
        try:
            ChumsBot7.connect()
            config = ChumsBot7(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot7.session.server_address:
                    if ChumsBot7.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot7.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot7.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot7.session.save()
                    break
            tgbot.get_me()
            ChumsBot7.me = ChumsBot7.get_me()
            ChumsBot7.uid = tgbot.uid = utils.get_peer_id(ChumsBot7.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot7.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot7.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION7 - {e}")
            sys.exit()

    if pdB.get_key("SESSION8") or Var.STRING_SESSION8 and Database.BOT_TOKEN:
        try:
            ChumsBot8.connect()
            config = ChumsBot8(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot8.session.server_address:
                    if ChumsBot8.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot8.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot8.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot8.session.save()
                    break
            tgbot.get_me()
            ChumsBot8.me = ChumsBot8.get_me()
            ChumsBot8.uid = tgbot.uid = utils.get_peer_id(ChumsBot8.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot8.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot8.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION8 - {e}")
            sys.exit()

    if pdB.get_key("SESSION9") or Var.STRING_SESSION9 and Database.BOT_TOKEN:
        try:
            ChumsBot9.connect()
            config = ChumsBot9(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot9.session.server_address:
                    if ChumsBot9.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot9.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot9.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot9.session.save()
                    break
            tgbot.get_me()
            ChumsBot9.me = ChumsBot9.get_me()
            ChumsBot9.uid = tgbot.uid = utils.get_peer_id(ChumsBot9.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot9.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot9.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION9 - {e}")
            sys.exit()

    if pdB.get_key("SESSION10") or Var.STRING_SESSION10 and Database.BOT_TOKEN:
        try:
            ChumsBot10.connect()
            config = ChumsBot10(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot10.session.server_address:
                    if ChumsBot10.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot10.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot10.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot10.session.save()
                    break
            tgbot.get_me()
            ChumsBot10.me = ChumsBot10.get_me()
            ChumsBot10.uid = tgbot.uid = utils.get_peer_id(ChumsBot10.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot10.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot10.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION10 - {e}")
            sys.exit()

    if pdB.get_key("SESSION11") or Var.STRING_SESSION11 and Database.BOT_TOKEN:
        try:
            ChumsBot11.connect()
            config = ChumsBot11(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot11.session.server_address:
                    if ChumsBot11.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot11.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot11.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot11.session.save()
                    break
            tgbot.get_me()
            ChumsBot11.me = ChumsBot11.get_me()
            ChumsBot11.uid = tgbot.uid = utils.get_peer_id(ChumsBot11.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot11.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot11.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION11 - {e}")
            sys.exit()

    if pdB.get_key("SESSION12") or Var.STRING_SESSION12 and Database.BOT_TOKEN:
        try:
            ChumsBot12.connect()
            config = ChumsBot12(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot12.session.server_address:
                    if ChumsBot12.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot12.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot12.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot12.session.save()
                    break
            tgbot.get_me()
            ChumsBot12.me = ChumsBot12.get_me()
            ChumsBot12.uid = tgbot.uid = utils.get_peer_id(ChumsBot12.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot12.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot12.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION12 - {e}")
            sys.exit()

    if pdB.get_key("SESSION13") or Var.STRING_SESSION13 and Database.BOT_TOKEN:
        try:
            ChumsBot13.connect()
            config = ChumsBot13(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot13.session.server_address:
                    if ChumsBot13.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot13.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot13.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot13.session.save()
                    break
            tgbot.get_me()
            ChumsBot13.me = ChumsBot13.get_me()
            ChumsBot13.uid = tgbot.uid = utils.get_peer_id(ChumsBot13.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot13.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot13.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION13 - {e}")
            sys.exit()

    if pdB.get_key("SESSION14") or Var.STRING_SESSION14 and Database.BOT_TOKEN:
        try:
            ChumsBot14.connect()
            config = ChumsBot14(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot14.session.server_address:
                    if ChumsBot14.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot14.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot14.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot14.session.save()
                    break
            tgbot.get_me()
            ChumsBot14.me = ChumsBot14.get_me()
            ChumsBot14.uid = tgbot.uid = utils.get_peer_id(ChumsBot14.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot14.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot14.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION14 - {e}")
            sys.exit()

    if pdB.get_key("SESSION15") or Var.STRING_SESSION15 and Database.BOT_TOKEN:
        try:
            ChumsBot15.connect()
            config = ChumsBot15(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot15.session.server_address:
                    if ChumsBot15.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot15.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot15.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot15.session.save()
                    break
            tgbot.get_me()
            ChumsBot15.me = ChumsBot15.get_me()
            ChumsBot15.uid = tgbot.uid = utils.get_peer_id(ChumsBot15.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot15.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot15.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION15 - {e}")
            sys.exit()

    if pdB.get_key("SESSION16") or Var.STRING_SESSION16 and Database.BOT_TOKEN:
        try:
            ChumsBot16.connect()
            config = ChumsBot16(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot16.session.server_address:
                    if ChumsBot16.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot16.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot16.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot16.session.save()
                    break
            tgbot.get_me()
            ChumsBot16.me = ChumsBot16.get_me()
            ChumsBot16.uid = tgbot.uid = utils.get_peer_id(ChumsBot16.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot16.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot16.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION16 - {e}")
            sys.exit()

    if pdB.get_key("SESSION17") or Var.STRING_SESSION17 and Database.BOT_TOKEN:
        try:
            ChumsBot17.connect()
            config = ChumsBot17(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot17.session.server_address:
                    if ChumsBot17.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot17.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot17.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot17.session.save()
                    break
            tgbot.get_me()
            ChumsBot17.me = ChumsBot17.get_me()
            ChumsBot17.uid = tgbot.uid = utils.get_peer_id(ChumsBot17.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot17.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot17.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION17 - {e}")
            sys.exit()

    if pdB.get_key("SESSION18") or Var.STRING_SESSION18 and Database.BOT_TOKEN:
        try:
            ChumsBot18.connect()
            config = ChumsBot18(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot18.session.server_address:
                    if ChumsBot18.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot18.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot18.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot18.session.save()
                    break
            tgbot.get_me()
            ChumsBot18.me = ChumsBot18.get_me()
            ChumsBot18.uid = tgbot.uid = utils.get_peer_id(ChumsBot18.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot18.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot18.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION18 - {e}")
            sys.exit()

    if pdB.get_key("SESSION19") or Var.STRING_SESSION19 and Database.BOT_TOKEN:
        try:
            ChumsBot19.connect()
            config = ChumsBot19(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot19.session.server_address:
                    if ChumsBot19.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot19.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot19.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot19.session.save()
                    break
            tgbot.get_me()
            ChumsBot19.me = ChumsBot19.get_me()
            ChumsBot19.uid = tgbot.uid = utils.get_peer_id(ChumsBot19.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot19.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot19.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION2 - {e}")
            sys.exit()

    if pdB.get_key("SESSION20") or Var.STRING_SESSION20 and Database.BOT_TOKEN:
        try:
            ChumsBot20.connect()
            config = ChumsBot20(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot20.session.server_address:
                    if ChumsBot20.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot20.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot20.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot20.session.save()
                    break
            tgbot.get_me()
            ChumsBot20.me = ChumsBot20.get_me()
            ChumsBot20.uid = tgbot.uid = utils.get_peer_id(ChumsBot20.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot20.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot20.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION20 - {e}")
            sys.exit()

    if pdB.get_key("SESSION21") or Var.STRING_SESSION21 and Database.BOT_TOKEN:
        try:
            ChumsBot21.connect()
            config = ChumsBot21(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot21.session.server_address:
                    if ChumsBot21.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot21.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot21.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot21.session.save()
                    break
            tgbot.get_me()
            ChumsBot21.me = ChumsBot21.get_me()
            ChumsBot21.uid = tgbot.uid = utils.get_peer_id(ChumsBot21.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot21.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot21.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION21 - {e}")
            sys.exit()

    if pdB.get_key("SESSION22") or Var.STRING_SESSION22 and Database.BOT_TOKEN:
        try:
            ChumsBot22.connect()
            config = ChumsBot22(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot22.session.server_address:
                    if ChumsBot22.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot22.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot22.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot22.session.save()
                    break
            tgbot.get_me()
            ChumsBot22.me = ChumsBot22.get_me()
            ChumsBot22.uid = tgbot.uid = utils.get_peer_id(ChumsBot22.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot22.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot22.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION22 - {e}")
            sys.exit()

    if pdB.get_key("SESSION23") or Var.STRING_SESSION23 and Database.BOT_TOKEN:
        try:
            ChumsBot23.connect()
            config = ChumsBot23(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot23.session.server_address:
                    if ChumsBot23.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot23.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot23.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot23.session.save()
                    break
            tgbot.get_me()
            ChumsBot23.me = ChumsBot23.get_me()
            ChumsBot23.uid = tgbot.uid = utils.get_peer_id(ChumsBot23.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot23.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot23.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION23 - {e}")
            sys.exit()

    if pdB.get_key("SESSION24") or Var.STRING_SESSION24 and Database.BOT_TOKEN:
        try:
            ChumsBot24.connect()
            config = ChumsBot24(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot24.session.server_address:
                    if ChumsBot24.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot24.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot24.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot24.session.save()
                    break
            tgbot.get_me()
            ChumsBot24.me = ChumsBot24.get_me()
            ChumsBot24.uid = tgbot.uid = utils.get_peer_id(ChumsBot24.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot24.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot24.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION24 - {e}")
            sys.exit()

    if pdB.get_key("SESSION25") or Var.STRING_SESSION25 and Database.BOT_TOKEN:
        try:
            ChumsBot25.connect()
            config = ChumsBot25(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot25.session.server_address:
                    if ChumsBot25.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot25.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot25.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot25.session.save()
                    break
            tgbot.get_me()
            ChumsBot25.me = ChumsBot25.get_me()
            ChumsBot25.uid = tgbot.uid = utils.get_peer_id(ChumsBot25.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot25.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot25.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION25 - {e}")
            sys.exit()

    if pdB.get_key("SESSION26") or Var.STRING_SESSION26 and Database.BOT_TOKEN:
        try:
            ChumsBot26.connect()
            config = ChumsBot26(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot26.session.server_address:
                    if ChumsBot26.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot26.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot26.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot26.session.save()
                    break
            tgbot.get_me()
            ChumsBot26.me = ChumsBot26.get_me()
            ChumsBot26.uid = tgbot.uid = utils.get_peer_id(ChumsBot26.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot26.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot26.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION26 - {e}")
            sys.exit()

    if pdB.get_key("SESSION27") or Var.STRING_SESSION27 and Database.BOT_TOKEN:
        try:
            ChumsBot27.connect()
            config = ChumsBot27(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot27.session.server_address:
                    if ChumsBot27.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot27.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot27.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot27.session.save()
                    break
            tgbot.get_me()
            ChumsBot27.me = ChumsBot27.get_me()
            ChumsBot27.uid = tgbot.uid = utils.get_peer_id(ChumsBot27.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot27.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot27.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION27 - {e}")
            sys.exit()

    if pdB.get_key("SESSION28") or Var.STRING_SESSION28 and Database.BOT_TOKEN:
        try:
            ChumsBot28.connect()
            config = ChumsBot28(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot28.session.server_address:
                    if ChumsBot28.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot28.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot28.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot28.session.save()
                    break
            tgbot.get_me()
            ChumsBot28.me = ChumsBot28.get_me()
            ChumsBot28.uid = tgbot.uid = utils.get_peer_id(ChumsBot28.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot28.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot28.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION28 - {e}")
            sys.exit()

    if pdB.get_key("SESSION29") or Var.STRING_SESSION29 and Database.BOT_TOKEN:
        try:
            ChumsBot29.connect()
            config = ChumsBot29(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot29.session.server_address:
                    if ChumsBot29.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot29.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot29.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot29.session.save()
                    break
            tgbot.get_me()
            ChumsBot29.me = ChumsBot29.get_me()
            ChumsBot29.uid = tgbot.uid = utils.get_peer_id(ChumsBot29.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot29.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot29.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION29 - {e}")
            sys.exit()

    if pdB.get_key("SESSION30") or Var.STRING_SESSION30 and Database.BOT_TOKEN:
        try:
            ChumsBot30.connect()
            config = ChumsBot30(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot2.session.server_address:
                    if ChumsBot30.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot30.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot30.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot30.session.save()
                    break
            tgbot.get_me()
            ChumsBot30.me = ChumsBot30.get_me()
            ChumsBot30.uid = tgbot.uid = utils.get_peer_id(ChumsBot30.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot30.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot30.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION30 - {e}")
            sys.exit()

    if pdB.get_key("SESSION31") or Var.STRING_SESSION31 and Database.BOT_TOKEN:
        try:
            ChumsBot31.connect()
            config = ChumsBot31(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot31.session.server_address:
                    if ChumsBot31.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot31.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot31.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot31.session.save()
                    break
            tgbot.get_me()
            ChumsBot31.me = ChumsBot31.get_me()
            ChumsBot31.uid = tgbot.uid = utils.get_peer_id(ChumsBot31.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot31.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot31.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION31 - {e}")
            sys.exit()

    if pdB.get_key("SESSION32") or Var.STRING_SESSION32 and Database.BOT_TOKEN:
        try:
            ChumsBot32.connect()
            config = ChumsBot32(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot32.session.server_address:
                    if ChumsBot32.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot32.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot32.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot32.session.save()
                    break
            tgbot.get_me()
            ChumsBot32.me = ChumsBot32.get_me()
            ChumsBot32.uid = tgbot.uid = utils.get_peer_id(ChumsBot32.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot32.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot32.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION32 - {e}")
            sys.exit()

    if pdB.get_key("SESSION33") or Var.STRING_SESSION33 and Database.BOT_TOKEN:
        try:
            ChumsBot33.connect()
            config = ChumsBot33(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot33.session.server_address:
                    if ChumsBot33.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot33.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot33.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot33.session.save()
                    break
            tgbot.get_me()
            ChumsBot33.me = ChumsBot33.get_me()
            PandaBo33.uid = tgbot.uid = utils.get_peer_id(ChumsBot33.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot33.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot33.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION33 - {e}")
            sys.exit()

    if pdB.get_key("SESSION34") or Var.STRING_SESSION34 and Database.BOT_TOKEN:
        try:
            ChumsBot34.connect()
            config = ChumsBot34(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot34.session.server_address:
                    if ChumsBot34.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot34.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot34.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot34.session.save()
                    break
            tgbot.get_me()
            ChumsBot34.me = ChumsBot34.get_me()
            ChumsBot34.uid = tgbot.uid = utils.get_peer_id(ChumsBot34.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot34.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot34.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION34 - {e}")
            sys.exit()

    if pdB.get_key("SESSION35") or Var.STRING_SESSION35 and Database.BOT_TOKEN:
        try:
            ChumsBot35.connect()
            config = ChumsBot35(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot35.session.server_address:
                    if ChumsBot35.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot35.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot35.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot35.session.save()
                    break
            tgbot.get_me()
            ChumsBot35.me = ChumsBot35.get_me()
            ChumsBot35.uid = tgbot.uid = utils.get_peer_id(ChumsBot35.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot35.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot35.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION35 - {e}")
            sys.exit()

    if pdB.get_key("SESSION36") or Var.STRING_SESSION36 and Database.BOT_TOKEN:
        try:
            ChumsBot36.connect()
            config = ChumsBot36(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot36.session.server_address:
                    if ChumsBot36.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot36.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot36.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot36.session.save()
                    break
            tgbot.get_me()
            ChumsBot36.me = ChumsBot36.get_me()
            PandaBo36.uid = tgbot.uid = utils.get_peer_id(ChumsBot36.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot36.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot36.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION36 - {e}")
            sys.exit()
     
    if pdB.get_key("SESSION37") or Var.STRING_SESSION37 and Database.BOT_TOKEN:
        try:
            ChumsBot37.connect()
            config = ChumsBot37(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot37.session.server_address:
                    if ChumsBot37.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot37.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot37.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot37.session.save()
                    break
            tgbot.get_me()
            ChumsBot37.me = ChumsBot37.get_me()
            ChumsBot37.uid = tgbot.uid = utils.get_peer_id(ChumsBot37.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot37.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot37.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION37 - {e}")
            sys.exit()

    if pdB.get_key("SESSION38") or Var.STRING_SESSION38 and Database.BOT_TOKEN:
        try:
            ChumsBot38.connect()
            config = ChumsBot38(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot38.session.server_address:
                    if ChumsBot38.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot38.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot38.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot38.session.save()
                    break
            tgbot.get_me()
            ChumsBot38.me = ChumsBot38.get_me()
            ChumsBot38.uid = tgbot.uid = utils.get_peer_id(ChumsBot38.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot38.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot38.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION38 - {e}")
            sys.exit()

    if pdB.get_key("SESSION39") or Var.STRING_SESSION39 and Database.BOT_TOKEN:
        try:
            ChumsBot39.connect()
            config = ChumsBot39(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot39.session.server_address:
                    if ChumsBot39.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot39.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot39.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot39.session.save()
                    break
            tgbot.get_me()
            ChumsBot39.me = ChumsBot39.get_me()
            ChumsBot39.uid = tgbot.uid = utils.get_peer_id(ChumsBot39.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot39.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot39.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION39 - {e}")
            sys.exit()

    if pdB.get_key("SESSION40") or Var.STRING_SESSION40 and Database.BOT_TOKEN:
        try:
            ChumsBot40.connect()
            config = ChumsBot40(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot40.session.server_address:
                    if ChumsBot40.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot40.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot40.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot40.session.save()
                    break
            tgbot.get_me()
            ChumsBot40.me = ChumsBot40.get_me()
            PandaBo40.uid = tgbot.uid = utils.get_peer_id(ChumsBot40.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot40.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot40.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION40 - {e}")
            sys.exit()
     
    if pdB.get_key("SESSION41") or Var.STRING_SESSION41 and Database.BOT_TOKEN:
        try:
            ChumsBot41.connect()
            config = ChumsBot41(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot41.session.server_address:
                    if ChumsBot41.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot41.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot41.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot41.session.save()
                    break
            tgbot.get_me()
            ChumsBot41.me = ChumsBot41.get_me()
            ChumsBot41.uid = tgbot.uid = utils.get_peer_id(ChumsBot41.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot41.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot41.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION41 - {e}")
            sys.exit()

    if pdB.get_key("SESSION42") or Var.STRING_SESSION42 and Database.BOT_TOKEN:
        try:
            ChumsBot42.connect()
            config = ChumsBot42(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot42.session.server_address:
                    if ChumsBot42.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot42.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot42.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot42.session.save()
                    break
            tgbot.get_me()
            ChumsBot42.me = ChumsBot42.get_me()
            ChumsBot42.uid = tgbot.uid = utils.get_peer_id(ChumsBot42.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot42.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot42.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION42 - {e}")
            sys.exit()

    if pdB.get_key("SESSION43") or Var.STRING_SESSION43 and Database.BOT_TOKEN:
        try:
            ChumsBot43.connect()
            config = ChumsBot43(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot43.session.server_address:
                    if ChumsBot43.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot43.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot43.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot43.session.save()
                    break
            tgbot.get_me()
            ChumsBot43.me = ChumsBot43.get_me()
            ChumsBot43.uid = tgbot.uid = utils.get_peer_id(ChumsBot43.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot43.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot43.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION43 - {e}")
            sys.exit()

    if pdB.get_key("SESSION44") or Var.STRING_SESSION44 and Database.BOT_TOKEN:
        try:
            ChumsBot44.connect()
            config = ChumsBot44(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot44.session.server_address:
                    if ChumsBot44.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot44.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot44.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot44.session.save()
                    break
            tgbot.get_me()
            ChumsBot44.me = ChumsBot44.get_me()
            ChumsBot44.uid = tgbot.uid = utils.get_peer_id(ChumsBot44.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot44.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot44.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION44 - {e}")
            sys.exit()
     
    if pdB.get_key("SESSION45") or Var.STRING_SESSION45 and Database.BOT_TOKEN:
        try:
            ChumsBot45.connect()
            config = ChumsBot45(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot45.session.server_address:
                    if ChumsBot45.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot45.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot45.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot45.session.save()
                    break
            tgbot.get_me()
            ChumsBot45.me = ChumsBot45.get_me()
            ChumsBot45.uid = tgbot.uid = utils.get_peer_id(ChumsBot45.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot45.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot45.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION45 - {e}")
            sys.exit()

    if pdB.get_key("SESSION46") or Var.STRING_SESSION46 and Database.BOT_TOKEN:
        try:
            ChumsBot46.connect()
            config = ChumsBot46(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot46.session.server_address:
                    if ChumsBot46.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot46.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot46.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot46.session.save()
                    break
            tgbot.get_me()
            ChumsBot46.me = ChumsBot46.get_me()
            ChumsBot46.uid = tgbot.uid = utils.get_peer_id(ChumsBot46.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot46.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot46.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION46 - {e}")
            sys.exit()

    if pdB.get_key("SESSION47") or Var.STRING_SESSION47 and Database.BOT_TOKEN:
        try:
            ChumsBot47.connect()
            config = ChumsBot47(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot47.session.server_address:
                    if ChumsBot47.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot47.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot47.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot47.session.save()
                    break
            tgbot.get_me()
            ChumsBot47.me = ChumsBot47.get_me()
            ChumsBot47.uid = tgbot.uid = utils.get_peer_id(ChumsBot47.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot47.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot47.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION47 - {e}")
            sys.exit()

    if pdB.get_key("SESSION33") or Var.STRING_SESSION33 and Database.BOT_TOKEN:
        try:
            ChumsBot48.connect()
            config = ChumsBot48(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot48.session.server_address:
                    if ChumsBot48.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot48.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot48.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot48.session.save()
                    break
            tgbot.get_me()
            ChumsBot48.me = ChumsBot48.get_me()
            ChumsBot48.uid = tgbot.uid = utils.get_peer_id(ChumsBot48.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot48.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot48.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION48 - {e}")
            sys.exit()
     
    if pdB.get_key("SESSION49") or Var.STRING_SESSION49 and Database.BOT_TOKEN:
        try:
            ChumsBot49.connect()
            config = ChumsBot49(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot49.session.server_address:
                    if ChumsBot49.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot49.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot49.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot49.session.save()
                    break
            tgbot.get_me()
            ChumsBot49.me = ChumsBot49.get_me()
            ChumsBot49.uid = tgbot.uid = utils.get_peer_id(ChumsBot49.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot49.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot49.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION49 - {e}")
            sys.exit()

    if pdB.get_key("SESSION50") or Var.STRING_SESSION50 and Database.BOT_TOKEN:
        try:
            ChumsBot50.connect()
            config = ChumsBot50(functions.help.GetConfigRequest())
            for option in config.dc_options:
                if option.ip_address == ChumsBot50.session.server_address:
                    if ChumsBot50.session.dc_id != option.id:
                        LOGS.warning(
                            f"Fixed DC ID in session from {ChumsBot50.session.dc_id}"
                            f" to {option.id}"
                    )
                    ChumsBot50.session.set_dc(option.id, option.ip_address, option.port)
                    ChumsBot50.session.save()
                    break
            tgbot.get_me()
            ChumsBot50.me = ChumsBot50.get_me()
            ChumsBot50.uid = tgbot.uid = utils.get_peer_id(ChumsBot50.me)
            if pdB.get_key("OWNER_ID") or Var.OWNER_ID == 0:
                Var.OWNER_ID = utils.get_peer_id(ChumsBot50.me)
                pdB.set_key("OWNER_ID", Var.OWNER_ID)
            else:
                pdB.set_key("OWNER_ID", ChumsBot50.uid)
        except Exception as e:
            LOGS.error(f"STRING_SESSION50 - {e}")
            sys.exit()

    if not pdB.get_key("SESSION") or Var.STRING_SESSION and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION2") or Var.STRING_SESSION2 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION3") or Var.STRING_SESSION3 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION4") or Var.STRING_SESSION4 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION5") or Var.STRING_SESSION5 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION6") or Var.STRING_SESSION6 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION7") or Var.STRING_SESSION7 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION8") or Var.STRING_SESSION8 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION9") or Var.STRING_SESSION9 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION10") or Var.STRING_SESSION10 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION11") or Var.STRING_SESSION11 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION12") or Var.STRING_SESSION12 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION13") or Var.STRING_SESSION13 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION14") or Var.STRING_SESSION14 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION15") or Var.STRING_SESSION15 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION16") or Var.STRING_SESSION16 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION17") or Var.STRING_SESSION17 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION18") or Var.STRING_SESSION18 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION19") or Var.STRING_SESSION19 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION20") or Var.STRING_SESSION20 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION21") or Var.STRING_SESSION21 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION22") or Var.STRING_SESSION22 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION23") or Var.STRING_SESSION23 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION24") or Var.STRING_SESSION24 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION25") or Var.STRING_SESSION25 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION26") or Var.STRING_SESSION26 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION27") or Var.STRING_SESSION27 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION28") or Var.STRING_SESSION28 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION29") or Var.STRING_SESSION29 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION30") or Var.STRING_SESSION30 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION31") or Var.STRING_SESSION31 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION32") or Var.STRING_SESSION32 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION33") or Var.STRING_SESSION33 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION34") or Var.STRING_SESSION34 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION35") or Var.STRING_SESSION35 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION36") or Var.STRING_SESSION36 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION37") or Var.STRING_SESSION37 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION38") or Var.STRING_SESSION38 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION39") or Var.STRING_SESSION39 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION40") or Var.STRING_SESSION41 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION42") or Var.STRING_SESSION42 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION43") or Var.STRING_SESSION43 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION44") or Var.STRING_SESSION44 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION45") or Var.STRING_SESSION45 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION46") or Var.STRING_SESSION46 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION47") or Var.STRING_SESSION47 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION48") or Var.STRING_SESSION48 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION49") or Var.STRING_SESSION49 and Database.BOT_TOKEN:
        failed += 1
    if not pdB.get_key("SESSION50") or Var.STRING_SESSION50 and Database.BOT_TOKEN:
        failed += 1
    return failed

def Pyrogram():
    if pdB.get_key("PyroSESSION") or Database.PyroSESSION and Database.BOT_TOKEN:
        if app.bot:
            print("Activating assistant.\n")
            app.bot.start()
            print("Assistant activated.\n")
            asistant = app.import_module("userbot/modules/pyrogram/asistant/", exclude=app.NoLoad())
            print(f"\n\n{asistant} modules Loaded Sucesfull\n\n")
        else:
            print("Assistant start unsuccessful, please check that you have given the bot token.\n")
            print("skipping assistant start !")
        
    if app:
        print("Activating assistant.\n")
        app.start()
        print("Assistant activated.\n")
    else:
        print("Assistant start unsuccessful, please check that you have given the bot token.\n")
        print("skipping assistant start !")
    print("Modules: Installing.\n\n")
    modules = app.import_module("userbot/modules/pyrogram/", exclude=app.NoLoad())
    print(f"\n\n{modules} modules Loaded Sucesfull\n\n")
    print(f"⚙️ Chums Userbot {pyrover} Telah Aktif")
    idle()
    
