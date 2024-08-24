from pyrogram import filters
from pyrogram.types import Message

from .... import app


@app.bot.on_message(filters.command("start"))
async def send_response(_, m: Message):
    await m.reply("Apa Sayang ?")


@app.bot.on_message(filters.new_chat_members & filters.group)
async def added_to_group_msg(_, m: Message):
    if m.new_chat_members[0].is_self:
        try:
            await app.bot.send_message(
                m.chat.id,
                "Terimakasih Telah Menambahkan Gw Di Group Ini !\nGunakan /help Untuk tau tentang fitur nya.",
            )
        except Exception as e:
            await app.error(m, e)
    else:
        return
