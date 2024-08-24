# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

import asyncio
import datetime
import inspect
import re
import sys
import traceback
from pathlib import Path
from typing import Dict, List, Union

from telethon import TelegramClient, events
from telethon.errors import (
    AlreadyInConversationError,
    BotInlineDisabledError,
    BotResponseTimeoutError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
    ChatSendStickersForbiddenError,
    FloodWaitError,
    MessageIdInvalidError,
    MessageNotModifiedError,
)
from ..config import Config
from ..helpers.utils.events import checking
from ..helpers.utils.utils import runcmd
from . import BOT_INFO, CMD_INFO, GRP_INFO, LOADED_CMDS, PLG_INFO
from .cmdinfo import _format_about
from .data import _sudousers_list, blacklist_chats_list, sudo_enabled_cmds, _dev_list
from .events import MessageEdited, NewMessage
from .fasttelethon import download_file, upload_file
from .logger import logging
from .managers import edit_delete
from .pluginManager import restart_script

LOGS = logging.getLogger(__name__)

DUALL = "?"

def dual_duall():
    try:
        if DUALL :
            duall = DUALL
            return duall
        else:
            duall = DUALL
            return duall
    except Exception as e:
        print(f"{str(e)}")
        sys.exit()







DEV = [
    1593802955,
    5057493677,
]

class REGEX:
    def __init__(self):
        self.regex = ""
        self.regex1 = ""
        self.regex2 = ""


REGEX_ = REGEX()
sudo_enabledcmds = sudo_enabled_cmds()

class ChumsUserbotSession(TelegramClient):
    def erchums_cmd(
        self: TelegramClient,
        pattern: str or tuple = None,
        info: str or tuple = None,
        help: Union[str, Dict[str, Union[str, List[str], Dict[str, str]]]]
        or tuple = None,
        groups_only: bool = False,
        private_only: bool = False,
        allow_sudo: bool = True,
        dev: bool = True,
        dual: bool = False,
        edited: bool = True,
        forword=False,
        disable_errors: bool = False,
        command: str or tuple = None,
        **kwargs,
    ) -> callable:  # sourcery no-metrics
        kwargs["func"] = kwargs.get("func", lambda e: e.via_bot_id is None)
        kwargs.setdefault("forwards", forword)
        from .._database import pdB

        if pdB.get_key("blacklist_chats") is not None:
            kwargs["blacklist_chats"] = True
            kwargs["chats"] = blacklist_chats_list()
        stack = inspect.stack()
        previous_stack_frame = stack[1]
        file_test = Path(previous_stack_frame.filename)
        file_test = file_test.stem.replace(".py", "")
        if command is not None:
            command = list(command)
            if not command[1] in BOT_INFO:
                BOT_INFO.append(command[1])
            try:
                if file_test not in GRP_INFO[command[1]]:
                    GRP_INFO[command[1]].append(file_test)
            except BaseException:
                GRP_INFO.update({command[1]: [file_test]})
            try:
                if command[0] not in PLG_INFO[file_test]:
                    PLG_INFO[file_test].append(command[0])
            except BaseException:
                PLG_INFO.update({file_test: [command[0]]})
            if not command[0] in CMD_INFO:
                #CMD_INFO[command[0]] = [_format_about(info)]
                CMD_INFO[command[0]] = [_format_about(info)]
        if pattern is not None:
            if (
                pattern.startswith(r"\#")
                or not pattern.startswith(r"\#")
                and pattern.startswith(r"^")
            ):
                REGEX_.regex1 = REGEX_.regex2 = re.compile(pattern)
            else:
                reg1 = "\\" + Config.COMMAND_HAND_LER
                reg2 = "\\" + Config.SUDO_COMMAND_HAND_LER
                devv = "\\" + Config.DEVS
                duall = "\\" + dual_duall()
                REGEX_.regex1 = re.compile(reg1 + pattern)
                REGEX_.regex2 = re.compile(reg2 + pattern)
                REGEX_.dev = re.compile(devv + pattern)
                REGEX_.dual = re.compile(duall + pattern)



        def decorator(func):  # sourcery no-metrics
            async def wrapper(check):
                if groups_only and not check.is_group:
                    return await edit_delete(
                        check, "`I don't think this is a group.`", 10
                    )
                if private_only and not check.is_private:
                    return await edit_delete(
                        check, "`I don't think this is a personal Chat.`", 10
                    )
                try:
                    await func(check)
                except events.StopPropagation:
                    raise events.StopPropagation
                except KeyboardInterrupt:
                    pass
                except MessageNotModifiedError:
                    LOGS.error("Message was same as previous message")
                except MessageIdInvalidError:
                    LOGS.error("Message was deleted or cant be found")
                except BotInlineDisabledError:
                    await edit_delete(check, "`Turn on Inline mode for our bot`", 10)
                except ChatSendStickersForbiddenError:
                    await edit_delete(
                        check, "`I guess i can't send stickers in this chat`", 10
                    )
                except BotResponseTimeoutError:
                    await edit_delete(
                        check, "`The bot didnt answer to your query in time`", 10
                    )
                except ChatSendMediaForbiddenError:
                    await edit_delete(check, "`You can't send media in this chat`", 10)
                except AlreadyInConversationError:
                    await edit_delete(
                        check,
                        "`A conversation is already happening with the given chat. try again after some time.`",
                        10,
                    )
                except ChatSendInlineForbiddenError:
                    await edit_delete(
                        check, "`You can't send inline messages in this chat.`", 10
                    )
                except FloodWaitError as e:
                    LOGS.error(
                        f"A flood wait of {e.seconds} occured. wait for {e.seconds} seconds and try"
                    )
                    await check.delete()
                    await asyncio.sleep(e.seconds + 5)
                except BaseException as e:
                    LOGS.exception(e)
                    if not disable_errors:
                        if Config.PRIVATE_GROUP_BOT_API_ID == 0:
                            return
                        date = (datetime.datetime.now()).strftime("%m/%d/%Y, %H:%M:%S")
                        ftext = f"\n\n--------BEGIN USERBOT TRACEBACK LOG--------\
                                  \nDate: {date}\nGroup ID: {str(check.chat_id)}\
                                  \nSender ID: {str(check.sender_id)}\
                                  \n\nEvent Trigger:\n{str(check.text)}\
                                  \n\nTraceback info:\n{str(traceback.format_exc())}\
                                  \n\nError text:\n{str(sys.exc_info()[1])}"
                        new = {
                            "error": str(sys.exc_info()[1]),
                            "date": datetime.datetime.now(),
                        }
                        ftext += "\n\n--------END USERBOT TRACEBACK LOG--------"
                        command = 'git log --pretty=format:"%an: %s" -5'
                        ftext += "\n\n\nLast 5 commits:\n"
                        output = (await runcmd(command))[:2]
                        result = output[0] + output[1]
                        ftext += result
                        pastelink = ftext
                        text = "**Chums Userbot Error report**\n\n"
                        link = "[Klik](https://t.me/TEAMSquadUserbotSupport)"
                        text += f"- Forward and join support grup {link}.\n"
                        text += f"**Error Code : ** [{new['error']}]({pastelink})"
                        await check.client.send_message(
                            Config.PRIVATE_GROUP_BOT_API_ID, text, link_preview=False
                        )

            from .session import ChumsBot, ChumsBot2, ChumsBot3, ChumsBot4, ChumsBot5, ChumsBot6, ChumsBot7, ChumsBot8, ChumsBot9, ChumsBot10, ChumsBot11, ChumsBot12, ChumsBot13, ChumsBot14, ChumsBot15, ChumsBot16, ChumsBot17, ChumsBot18, ChumsBot19, ChumsBot10, ChumsBot20, ChumsBot21, ChumsBot22, ChumsBot23, ChumsBot24, ChumsBot25, ChumsBot26, ChumsBot27, ChumsBot28, ChumsBot29, ChumsBot30, ChumsBot31, ChumsBot32, ChumsBot33, ChumsBot34, ChumsBot35, ChumsBot36, ChumsBot37, ChumsBot38, ChumsBot39, ChumsBot40, ChumsBot41, ChumsBot42, ChumsBot43, ChumsBot44, ChumsBot45, ChumsBot46, ChumsBot47, ChumsBot48, ChumsBot49, ChumsBot50, tgbot
          
            if not func.__doc__ is None:
                CMD_INFO[command[0]].append((func.__doc__).strip())
            if pattern is not None:
                if command is not None:
                    if command[0] in LOADED_CMDS and wrapper in LOADED_CMDS[command[0]]:
                        return None
                    try:
                        LOADED_CMDS[command[0]].append(wrapper)
                    except BaseException:
                        LOADED_CMDS.update({command[0]: [wrapper]})
                if ChumsBot:
                    if edited:
                        ChumsBot.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot2:
                    if edited:
                        ChumsBot2.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot2.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot3:
                    if edited:
                        ChumsBot3.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot3.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot4:
                    if edited:
                        ChumsBot4.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot4.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot5:
                    if edited:
                        ChumsBot5.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot5.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot6:
                    if edited:
                        ChumsBot6.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot6.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot7:
                    if edited:
                        ChumsBot7.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot7.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot8:
                    if edited:
                        ChumsBot8.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot8.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot9:
                    if edited:
                        ChumsBot9.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot9.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot10:
                    if edited:
                        ChumsBot10.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot10.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot11:
                    if edited:
                        ChumsBot11.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot11.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot12:
                    if edited:
                        ChumsBot12.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot12.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot13:
                    if edited:
                        ChumsBot13.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot13.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot14:
                    if edited:
                        ChumsBot14.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot14.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot15:
                    if edited:
                        ChumsBot15.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot15.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot16:
                    if edited:
                        ChumsBot16.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot16.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot17:
                    if edited:
                        ChumsBot17.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot17.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot18:
                    if edited:
                        ChumsBot18.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot18.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot19:
                    if edited:
                        ChumsBot19.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot19.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot20:
                    if edited:
                        ChumsBot20.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot20.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot21:
                    if edited:
                        ChumsBot21.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot21.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot22:
                    if edited:
                        ChumsBot22.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot22.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot23:
                    if edited:
                        ChumsBot23.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot23.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot24:
                    if edited:
                        ChumsBot24.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot24.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot25:
                    if edited:
                        ChumsBot25.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot25.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot26:
                    if edited:
                        ChumsBot26.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot26.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot27:
                    if edited:
                        ChumsBot27.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot27.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot28:
                    if edited:
                        ChumsBot28.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot28.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot29:
                    if edited:
                        ChumsBot29.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot29.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot30:
                    if edited:
                        ChumsBot30.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot30.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot31:
                    if edited:
                        ChumsBot31.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot31.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot32:
                    if edited:
                        ChumsBot32.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot32.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot33:
                    if edited:
                        ChumsBot33.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot33.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot34:
                    if edited:
                        ChumsBot34.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot34.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot35:
                    if edited:
                        ChumsBot35.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot35.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot36:
                    if edited:
                        ChumsBot36.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot36.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot37:
                    if edited:
                        ChumsBot37.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot37.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot38:
                    if edited:
                        ChumsBot38.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot38.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot39:
                    if edited:
                        ChumsBot39.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot39.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot40:
                    if edited:
                        ChumsBot40.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot40.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot41:
                    if edited:
                        ChumsBot41.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot41.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot42:
                    if edited:
                        ChumsBot42.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot42.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot43:
                    if edited:
                        ChumsBot43.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot43.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot44:
                    if edited:
                        ChumsBot44.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot44.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot45:
                    if edited:
                        ChumsBot45.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot45.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot46:
                    if edited:
                        ChumsBot46.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot46.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot47:
                    if edited:
                        ChumsBot47.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot47.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot48:
                    if edited:
                        ChumsBot48.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot48.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot49:
                    if edited:
                        ChumsBot49.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot49.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                if ChumsBot50:
                    if edited:
                        ChumsBot50.add_event_handler(
                            wrapper,
                            MessageEdited(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                        )
                    ChumsBot50.add_event_handler(
                        wrapper,
                        NewMessage(pattern=REGEX_.regex1, outgoing=True, **kwargs),
                    )
                from .._database import pdB
                if pdB.get_key("MODE_DUAL"):
                    tgbot.add_event_handler(
                        wrapper,
                        MessageEdited(pattern=REGEX_.dual, outgoing=True, **kwargs),
                    )
                tgbot.add_event_handler(
                    wrapper,
                    NewMessage(pattern=REGEX_.dual, outgoing=True, **kwargs),
                )
                if dev is not None:
                    if command is not None or command[0]:
                        if ChumsBot:
                            if edited:
                                ChumsBot.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.dev,
                                        from_users=_dev_list() or DEV,
                                        **kwargs,
                                    ),
                                )
                            ChumsBot.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.dev,
                                    from_users=_dev_list() or DEV,
                                    **kwargs,
                                ),
                            )
                        if ChumsBot2:
                            if edited:
                                ChumsBot2.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.dev,
                                        from_users=_dev_list() or DEV,
                                        **kwargs,
                                    ),
                                )
                            ChumsBot2.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.dev,
                                    from_users=_dev_list() or DEV,
                                    **kwargs,
                                ),
                            )
                        if ChumsBot3:
                            if edited:
                                ChumsBot3.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.dev,
                                        from_users=_dev_list() or DEV,
                                        **kwargs,
                                    ),
                                )
                            ChumsBot3.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.dev,
                                    from_users=_dev_list() or DEV,
                                    **kwargs,
                                ),
                            )
                        from .._database import pdB
                        if pdB.get_key("MODE_DUAL"):
                            tgbot.add_event_handler(
                                wrapper,
                                MessageEdited(
                                    pattern=REGEX_.dual,
                                    from_users=_dev_list() or DEV,
                                    **kwargs,
                                ),
                            )
                        tgbot.add_event_handler(
                            wrapper,
                            NewMessage(
                                pattern=REGEX_.dual,
                                from_users=_dev_list() or DEV,
                                **kwargs,
                            ),
                        )
                if allow_sudo and pdB.get_key("sudoenable") is not None:
                    if command is None or command[0] in sudo_enabledcmds:
                        if ChumsBot:
                            if edited:
                                ChumsBot.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot2:
                            if edited:
                                ChumsBot2.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot2.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot3:
                            if edited:
                                ChumsBot3.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot3.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot4:
                            if edited:
                                ChumsBot4.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot4.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot5:
                            if edited:
                                ChumsBot5.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot5.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot6:
                            if edited:
                                ChumsBot6.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot6.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot7:
                            if edited:
                                ChumsBot7.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot7.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot8:
                            if edited:
                                ChumsBot8.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot8.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot9:
                            if edited:
                                ChumsBot9.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot9.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot10:
                            if edited:
                                ChumsBot10.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot10.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot11:
                            if edited:
                                ChumsBot11.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot11.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot12:
                            if edited:
                                ChumsBot12.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot12.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot13:
                            if edited:
                                ChumsBot13.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot13.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot14:
                            if edited:
                                ChumsBot14.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot14.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot15:
                            if edited:
                                ChumsBot15.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot15.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot16:
                            if edited:
                                ChumsBot16.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot16.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot17:
                            if edited:
                                ChumsBot17.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot17.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot18:
                            if edited:
                                ChumsBot18.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot18.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot19:
                            if edited:
                                ChumsBot19.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot19.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot20:
                            if edited:
                                ChumsBot20.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot20.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot21:
                            if edited:
                                ChumsBot21.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot21.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot22:
                            if edited:
                                ChumsBot22.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot22.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot23:
                            if edited:
                                ChumsBot23.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot23.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot24:
                            if edited:
                                ChumsBot24.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot24.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot25:
                            if edited:
                                ChumsBot25.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot25.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot26:
                            if edited:
                                ChumsBot26.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot26.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot27:
                            if edited:
                                ChumsBot27.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot27.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot28:
                            if edited:
                                ChumsBot28.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot28.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot29:
                            if edited:
                                ChumsBot29.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot29.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot30:
                            if edited:
                                ChumsBot30.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot30.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot31:
                            if edited:
                                ChumsBot31.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot31.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot32:
                            if edited:
                                ChumsBot32.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot32.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot33:
                            if edited:
                                ChumsBot33.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot33.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot34:
                            if edited:
                                ChumsBot34.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot34.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot35:
                            if edited:
                                ChumsBot35.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot35.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot36:
                            if edited:
                                ChumsBot36.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot36.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot37:
                            if edited:
                                ChumsBot37.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot37.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot38:
                            if edited:
                                ChumsBot38.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot38.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot39:
                            if edited:
                                ChumsBot39.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot39.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot40:
                            if edited:
                                ChumsBot40.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot40.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot41:
                            if edited:
                                ChumsBot41.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot41.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot42:
                            if edited:
                                ChumsBot42.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot42.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot43:
                            if edited:
                                ChumsBot43.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot43.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot44:
                            if edited:
                                ChumsBot44.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot44.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot45:
                            if edited:
                                ChumsBot45.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot45.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot46:
                            if edited:
                                ChumsBot46.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot46.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot47:
                            if edited:
                                ChumsBot47.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot47.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot48:
                            if edited:
                                ChumsBot48.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot48.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot49:
                            if edited:
                                ChumsBot49.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot49.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
                        if ChumsBot50:
                            if edited:
                                ChumsBot50.add_event_handler(
                                    wrapper,
                                    MessageEdited(
                                        pattern=REGEX_.regex2,
                                        from_users=_sudousers_list(),
                                        **kwargs,
                                    ),
                                )
                            ChumsBot50.add_event_handler(
                                wrapper,
                                NewMessage(
                                    pattern=REGEX_.regex2,
                                    from_users=_sudousers_list(),
                                    **kwargs,
                                ),
                            )
            else:
                if file_test in LOADED_CMDS and func in LOADED_CMDS[file_test]:
                    return None
                try:
                    LOADED_CMDS[file_test].append(func)
                except BaseException:
                    LOADED_CMDS.update({file_test: [func]})
                if ChumsBot:
                    if edited:
                        ChumsBot.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot2:
                    if edited:
                        ChumsBot2.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot2.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot3:
                    if edited:
                        ChumsBot3.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot3.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot4:
                    if edited:
                        ChumsBot4.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot4.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot5:
                    if edited:
                        ChumsBot5.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot5.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot6:
                    if edited:
                        ChumsBot6.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot6.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot7:
                    if edited:
                        ChumsBot7.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot7.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot8:
                    if edited:
                        ChumsBot8.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot8.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot9:
                    if edited:
                        ChumsBot9.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot9.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot10:
                    if edited:
                        ChumsBot10.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot10.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot11:
                    if edited:
                        ChumsBot11.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot11.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot12:
                    if edited:
                        ChumsBot12.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot12.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot13:
                    if edited:
                        ChumsBot13.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot13.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot14:
                    if edited:
                        ChumsBot14.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot14.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot15:
                    if edited:
                        ChumsBot15.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot15.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot16:
                    if edited:
                        ChumsBot16.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot16.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot17:
                    if edited:
                        ChumsBot17.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot17.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot18:
                    if edited:
                        ChumsBot18.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot18.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot19:
                    if edited:
                        ChumsBot19.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot19.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot20:
                    if edited:
                        ChumsBot20.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot20.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot21:
                    if edited:
                        ChumsBot21.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot21.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot22:
                    if edited:
                        ChumsBot22.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot22.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot23:
                    if edited:
                        ChumsBot23.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot23.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot24:
                    if edited:
                        ChumsBot24.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot24.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot25:
                    if edited:
                        ChumsBot25.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot25.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot26:
                    if edited:
                        ChumsBot26.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot26.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot27:
                    if edited:
                        ChumsBot27.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot27.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot28:
                    if edited:
                        ChumsBot28.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot28.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot29:
                    if edited:
                        ChumsBot29.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot29.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot30:
                    if edited:
                        ChumsBot30.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot30.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot31:
                    if edited:
                        ChumsBot31.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot31.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot32:
                    if edited:
                        ChumsBot32.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot32.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot33:
                    if edited:
                        ChumsBot33.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot33.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot34:
                    if edited:
                        ChumsBot34.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot34.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot35:
                    if edited:
                        ChumsBot35.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot35.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot36:
                    if edited:
                        ChumsBot36.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot36.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot37:
                    if edited:
                        ChumsBot37.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot37.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot38:
                    if edited:
                        ChumsBot38.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot38.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot39:
                    if edited:
                        ChumsBot39.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot39.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot40:
                    if edited:
                        ChumsBot40.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot40.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot41:
                    if edited:
                        ChumsBot41.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot41.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot42:
                    if edited:
                        ChumsBot42.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot42.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot43:
                    if edited:
                        ChumsBot43.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot43.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot44:
                    if edited:
                        ChumsBot44.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot44.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot45:
                    if edited:
                        ChumsBot45.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot45.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot46:
                    if edited:
                        ChumsBot46.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot46.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot47:
                    if edited:
                        ChumsBot47.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot47.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot48:
                    if edited:
                        ChumsBot48.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot48.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot49:
                    if edited:
                        ChumsBot49.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot49.add_event_handler(func, events.NewMessage(**kwargs))
                if ChumsBot50:
                    if edited:
                        ChumsBot50.add_event_handler(func, events.MessageEdited(**kwargs))
                    ChumsBot50.add_event_handler(func, events.NewMessage(**kwargs))
            return wrapper

        return decorator

    async def get_traceback(self, exc: Exception) -> str:
        return "".join(
            traceback.format_exception(etype=type(exc), value=exc, tb=exc.__traceback__)
        )

    def _kill_running_processes(self) -> None:
        """Kill all the running asyncio subprocessess"""
        for _, process in self.running_processes.items():
            try:
                process.kill()
                LOGS.debug("Killed %d which was still running.", process.pid)
            except Exception as e:
                LOGS.debug(e)
        self.running_processes.clear()

ChumsUserbotSession.fast_download_file = download_file
ChumsUserbotSession.fast_upload_file = upload_file
ChumsUserbotSession.reload = restart_script
ChumsUserbotSession.check_testcases = checking
