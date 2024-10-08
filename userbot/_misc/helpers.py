# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot


import logging
from typing import Union

from telethon.tl import types
from telethon.utils import get_display_name

from .events import NewMessage

LOGGER = logging.getLogger("ErUbot")


def printUser(entity: types.User) -> None:
    """Print the user's first name + last name upon start"""
    user = get_display_name(entity)
    LOGGER.warning("Successfully logged in as {0}".format(user))


async def get_chat_link(
    arg: Union[types.User, types.Chat, types.Channel, NewMessage.Event], reply=None
) -> str:
    if isinstance(arg, (types.User, types.Chat, types.Channel)):
        entity = arg
    else:
        entity = await arg.get_chat()

    if isinstance(entity, types.User):
        if entity.is_self:
            name = 'Kamu "Menyimpan Pesan"'
        else:
            name = get_display_name(entity) or "Deleted Account?"
        extra = f"[{name}](tg://user?id={entity.id})"
    else:
        if hasattr(entity, "username") and entity.username is not None:
            username = "@" + entity.username
        else:
            username = entity.id
        if reply is not None:
            if isinstance(username, str) and username.startswith("@"):
                username = username[1:]
            else:
                username = f"c/{username}"
            extra = f"[{entity.title}](https://t.me/{username}/{reply})"
        else:
            if isinstance(username, int):
                username = f"`{username}`"
                extra = f"{entity.title} ( {username} )"
            else:
                extra = f"[{entity.title}](tg://resolve?domain={username})"
    return extra
