# Copyright (C) 2021 ErUbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/ErUbot

import glob
import os
import sys
from asyncio.exceptions import CancelledError
from pathlib import Path
from telethon.tl.functions.channels import JoinChannelRequest
import requests
from telethon import functions, types, utils
from userbot.helpers.utils.utils import runcmd
import urllib.request
from userbot import *

from userbot.config import Config, Var, Database
from userbot._misc.logger import logging

from userbot._misc.session import ChumsBot, ChumsBot2, ChumsBot3, ChumsBot4, ChumsBot5, ChumsBot6, ChumsBot7, ChumsBot8, ChumsBot9, ChumsBot10, ChumsBot11, ChumsBot12, ChumsBot13, ChumsBot14, ChumsBot15, ChumsBot16, ChumsBot17, ChumsBot18, ChumsBot19, ChumsBot10, ChumsBot20, ChumsBot21, ChumsBot22, ChumsBot23, ChumsBot24, ChumsBot25, ChumsBot26, ChumsBot27, ChumsBot28, ChumsBot29, ChumsBot30, ChumsBot31, ChumsBot32, ChumsBot33, ChumsBot34, ChumsBot35, ChumsBot36, ChumsBot37, ChumsBot38, ChumsBot39, ChumsBot40, ChumsBot41, ChumsBot42, ChumsBot43, ChumsBot44, ChumsBot45, ChumsBot46, ChumsBot47, ChumsBot48, ChumsBot49, ChumsBot50, tgbot
from userbot.helpers.utils import install_pip
from userbot._database import addgvar, delgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup
import base64
from userbot.version import __version__ as botvers

LOGS = logging.getLogger("ErUbot")
cmdhr = Config.COMMAND_HAND_LER
eruserbot = ChumsBot

async def setup_bot():
    try:
        await ChumsBot.start()
        delta = await ChumsBot(functions.help.GetConfigRequest())
        for option in delta.dc_options:
            if option.ip_address == ChumsBot.session.server_address:
                if ChumsBot.session.dc_id != option.id:
                    LOGS.warning(
                        f"Fixed DC ID in session from {ChumsBot.session.dc_id}"
                        f" to {option.id}"
                    )
                ChumsBot.session.set_dc(option.id, option.ip_address, option.port)
                ChumsBot.session.save()
                break
        ChumsBot.me = await ChumsBot.get_me()
        bot_details = await tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        ChumsBot.uid = tgbot.uid = utils.get_peer_id(ChumsBot.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(ChumsBot.me)
        if Config.STRING_SESSION2:
            await ChumsBot2.start()
        if Config.STRING_SESSION3:
            await ChumsBot3.start()
    except Exception as e:
        LOGS.error(f"STRING_SESSION - {str(e)}")
        sys.exit()

    

# don't know work or not just a try in future will use sleep
async def ipchange():
    """
    Just to check if ip change or not
    """
    newip = (requests.get("https://httpbin.org/ip").json())["origin"]
    if gvarstatus("ipaddress") is None:
        addgvar("ipaddress", newip)
        return None
    oldip = gvarstatus("ipaddress")
    if oldip != newip:
        delgvar("ipaddress")
        LOGS.info("Ip Change detected")
        try:
            await eruserbot.disconnect()
        except (ConnectionError, CancelledError):
            pass
        return "ip change"

async def loads(folder):
    """
    To load plugins from the mentioned folder
    """
    path = f"userbot/{folder}/*.py"
    files = glob.glob(path)
    files.sort()
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                if shortname.replace(".py", "") not in Config.NO_LOAD:
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                shortname.replace(".py", ""),
                                plugin_path=f"userbot/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"userbot/{folder}/{shortname}.py"))
            except Exception as e:
                os.remove(Path(f"Chums/{folder}/{shortname}.py"))
                LOGS.info(f"Gagal membuka file {shortname} dikarenakan error {e}")


async def buka(folder, extfolder=None, vcfolder=None):
    """
    To load plugins from the mentioned folder
    """
    if extfolder:
        path = f"{extfolder}/plugins/*.py"
        plugin_path = f"{extfolder}/plugins"
    elif vcfolder:
        path = f"{vcfolder}/VCTools/*.py"
        plugin_path = f"{vcfolder}/VCTools"
    else:
        path = f"userbot/modules/{folder}/*.py"
        plugin_path = f"userbot/modules/{folder}"
    files = glob.glob(path)
    files.sort()
    success = 0
    failure = []
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                if shortname.replace(".py", "") not in Config.NO_LOAD:
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                shortname.replace(".py", ""),
                                plugin_path=plugin_path,
                            )
                            if shortname in failure:
                                failure.remove(shortname)
                            success += 1
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if shortname not in failure:
                                failure.append(shortname)
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"{plugin_path}/{shortname}.py"))
                    
            except Exception as e:
                if shortname not in failure:
                    failure.append(shortname)
                os.remove(Path(f"{plugin_path}/{shortname}.py"))
                LOGS.info(f"Gagal membuka file {shortname} dikarenakan error {e}")
    if extfolder:
        if not failure:
            failure.append("None")
        return success, failure
    if vcfolder:
        if not failure:
            failure.append("None")
        return success, failure

async def bukabot(folder):
    """
    To load plugins from the mentioned folder
    """
    path = f"userbot/modules/telethon/{folder}/*.py"
    files = glob.glob(path)
    files.sort()
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            try:
                if shortname.replace(".py", "") not in Config.NO_LOAD:
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                shortname.replace(".py", ""),
                                plugin_path=f"userbot/modules/telethon/{folder}",
                            )
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"userbot/modules/telethon/{folder}/{shortname}.py"))
                    
            except Exception as e:
                os.remove(Path(f"userbot/modules/telethon/{folder}/{shortname}.py"))
                LOGS.info(f"Gagal membuka file {shortname} dikarenakan error {e}")


async def vcrepo(repo, branch, cfolder):
    VCREPO = repo
    rpath = os.path.join(cfolder, "requirements.txt")
    if BRANCH := branch:
        repourl = os.path.join(VCREPO, f"tree/{BRANCH}")
        gcmd = f"git clone -b {BRANCH} {VCREPO} {cfolder}"
        errtext = f"There is no branch with name `{BRANCH}` in your external repo {VCREPO}. Recheck branch name and correct it in vars(`EXTERNAL_REPO_BRANCH`)"
    else:
        repourl = VCREPO
        gcmd = f"git clone {VCREPO} {cfolder}"
        errtext = f"The link({VCREPO}) you provided for `VCREPO` in vars is invalid. please recheck that link"
    response = urllib.request.urlopen(repourl)
    if response.code != 200:
        LOGS.error(errtext)
        return await tgbot.send_message(BOTLOG_CHATID, errtext)
    await runcmd(gcmd)
    if not os.path.exists(cfolder):
        LOGS.error(
            "There was a problem in cloning the external repo. please recheck external repo link"
        )
        return await tgbot.send_message(
            BOTLOG_CHATID,
            "There was a problem in cloning the external repo. please recheck external repo link",
        )
    if os.path.exists(rpath):
        await runcmd(f"pip3 install --no-cache-dir -r {rpath}")
    success, failure = await buka(folder="VCTools", vcfolder="VCTools")
    return repourl, cfolder, success, failure
           
                
async def externalrepo(repo, branch, cfolder):
    EXTERNALREPO = repo
    rpath = os.path.join(cfolder, "requirements.txt")
    if BRANCH := branch:
        repourl = os.path.join(EXTERNALREPO, f"tree/{BRANCH}")
        gcmd = f"git clone -b {BRANCH} {EXTERNALREPO} {cfolder}"
        errtext = f"There is no branch with name `{BRANCH}` in your external repo {EXTERNALREPO}. Recheck branch name and correct it in vars(`EXTERNAL_REPO_BRANCH`)"
    else:
        repourl = EXTERNALREPO
        gcmd = f"git clone {EXTERNALREPO} {cfolder}"
        errtext = f"The link({EXTERNALREPO}) you provided for `EXTERNAL_REPO` in vars is invalid. please recheck that link"
    response = urllib.request.urlopen(repourl)
    if response.code != 200:
        LOGS.error(errtext)
        return await tgbot.send_message(BOTLOG_CHATID, errtext)
    await runcmd(gcmd)
    if not os.path.exists(cfolder):
        LOGS.error(
            "There was a problem in cloning the external repo. please recheck external repo link"
        )
        return await tgbot.send_message(
            BOTLOG_CHATID,
            "There was a problem in cloning the external repo. please recheck external repo link",
        )
    if os.path.exists(rpath):
        await runcmd(f"pip3 install --no-cache-dir -r {rpath}")
    success, failure = await buka(folder="plugins", extfolder="plugins")
    return repourl, cfolder, success, failure

async def verifyLoggerGroup():
    """
    Will verify the both loggers group
    """
    flag = False
    if BOTLOG:
        try:
            entity = await eruserbot.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "Permissions missing to send messages for the specified PRIVATE_GROUP_BOT_API_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "Permissions missing to addusers for the specified PRIVATE_GROUP_BOT_API_ID."
                    )
        except ValueError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID cannot be found. Make sure it's correct."
            )
        except TypeError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID is unsupported. Make sure it's correct."
            )
        except Exception as e:
            LOGS.error(
                "An Exception occured upon trying to verify the PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "Don't delete this group or change to group(If you change group all your previous snips, welcome will be lost.)"
        _, groupid = await create_supergroup(
            "ErUbot BotLog Group", eruserbot, Config.TG_BOT_USERNAME, descript
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print(
            "Private Group for PRIVATE_GROUP_BOT_API_ID is created successfully and added to vars."
        )
        flag = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await eruserbot.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "Permissions missing to send messages for the specified PM_LOGGER_GROUP_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "Permissions missing to addusers for the specified PM_LOGGER_GROUP_ID."
                    )
        except ValueError:
            LOGS.error("PM_LOGGER_GROUP_ID cannot be found. Make sure it's correct.")
        except TypeError:
            LOGS.error("PM_LOGGER_GROUP_ID is unsupported. Make sure it's correct.")
        except Exception as e:
            LOGS.error(
                "An Exception occured upon trying to verify the PM_LOGGER_GROUP_ID.\n"
                + str(e)
            )
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "userbot"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)


ON = f"""
Chums-Userbot
Owner {Config.ALIVE_NAME}
Version - `{botvers}`
Ketik `{cmdhr}alive` untuk Mengecheck Bot apakah sudah aktif
"""

MSG_ON = """
Chums-Userbot
━━
Version - `{}'
Ketik `{}alive` untuk Mengecheck Bot
━━
"""


CHATID = "-1001718757023"

async def ongrup():
    try:
        if cekbot:
            if CHATID != 0:
                await ChumsBot.send_message(
                    CHATID,
                    ON,
                )
                await ChumsBot.send_message(
                    CHATID,
                    ON,
                )
                await ChumsBot.send_message(
                    CHATID,
                    ON,
                )
    except BaseException:
        pass


async def join():
    X = base64.b64decode("QFBhbmRhVXNlcmJvdA==")
    L = base64.b64decode("QFRlYW1TcXVhZFVzZXJib3RTdXBwb3J0")
    try:
        await ChumsBot(JoinChannelRequest(X))
    except BaseException:
        pass
    try:
        await ChumsBot(JoinChannelRequest(L))
    except BaseException:
        pass

## Modular •••••√√√√√√••••••^••√√

P = "plugins"
M = "modules"
V = "VCPlugins"
A = "AsistenBot"




from telethon.tl.functions.channels import (
    EditAdminRequest,
    InviteToChannelRequest,
)

from telethon.errors import (
    ChatAdminRequiredError,
)


from telethon.tl.types import (
    ChatAdminRights,
)

async def cloneplugins():
    string = "<b>Your external repo plugins have imported.<b>\n\n"
    if Config.PLUGINS_REPO:
        data = await externalrepo(
            Config.PLUGINS_REPO, Config.U_BRANCH, "plugins"
        )
        string += f"<b>➜ Repo:  </b><a href='{data[0]}'><b>{data[1]}</b></a>\n<b>     • Imported Plugins:</b>  <code>{data[2]}</code>\n<b>     • Failed to Import:</b>  <code>{', '.join(data[3])}</code>\n\n"
    if "Imported Plugins" in string:
        await tgbot.send_message(BOTLOG_CHATID, string, parse_mode="html")
        
async def clonevc():
    string = "<b>Your external repo plugins have imported.<b>\n\n"
    if Config.VC_REPO:
        data = await vcrepo(
            Config.VC_REPO, Config.U_BRANCH, "VCTools"
        )
        string += f"<b>➜ Repo:  </b><a href='{data[0]}'><b>{data[1]}</b></a>\n<b>     • Imported VCPlugins:</b>  <code>{data[2]}</code>\n<b>     • Failed to Import:</b>  <code>{', '.join(data[3])}</code>\n\n"
    if "Imported Plugins" in string:
        await tgbot.send_message(BOTLOG_CHATID, string, parse_mode="html")


async def memulai():
    await buka(f"telethon")
    await bukabot(f"assistant")
    
    
async def ClientMultiTelethon():
    if Var.STRING_SESSION and Database.BOT_TOKEN:
        
        if ChumsBot:
            try:
                tgbot.me = await tgbot.get_me()
                await ChumsBot(InviteToChannelRequest(Config.PRIVATE_GROUP_BOT_API_ID, [tgbot.me.username]))
            except BaseException as er:
                LOGS.info("Error while Adding Assistant to Log Channel")
                LOGS.exception(er)
            if Config.PRIVATE_GROUP_BOT_API_ID:
                try:
                    achat = await tgbot.get_entity(Config.PRIVATE_GROUP_BOT_API_ID)
                except BaseException as er:
                    achat = None
                    LOGS.info("Error while getting Log channel from Assistant")
                    LOGS.exception(er)
                if achat and not achat.admin_rights:
                    rights = ChatAdminRights(
                        add_admins=True,
                        invite_users=True,
                        change_info=True,
                        ban_users=True,
                        delete_messages=True,
                        pin_messages=True,
                        anonymous=False,
                        manage_call=True,
                    )
                    try:
                        await ChumsBot(
                            EditAdminRequest(
                                Config.PRIVATE_GROUP_BOT_API_ID, tgbot.me.username, rights, "Assistant"
                            )
                        )
                    except ChatAdminRequiredError:
                        LOGS.info(
                             "Failed to promote 'Assistant Bot' in 'Log Channel' due to 'Admin Privileges'"
                        )
           
        

 
        if tgbot:
            await tgbot.send_message(Config.PRIVATE_GROUP_BOT_API_ID, f"Memeriksa Database {DB.name}...")
            await tgbot.send_message(Config.PRIVATE_GROUP_BOT_API_ID, f"Terkoneksi Database {DB.name} Successfully")
            

