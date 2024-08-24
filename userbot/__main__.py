# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# Import Panda Userbot
# Recode by Ilham Mansiz
# t.me/PandaUserbot
# ••••••••••••••••••••••√•••••••••••••√√√••••••••

import sys
import userbot
from userbot import LOGS, Database, Config
import contextlib
from .Session.multisession_ import *

cmdhr = Config.COMMAND_HAND_LER



from . import resources


"""
async def memulai():
    await resources.buka(f"telethon")
    await resources.bukabot(f"assistant")
"""

def start():
    userbot.LOOP.run_until_complete(resources.ClientMultiTelethon())
    userbot.LOOP.run_until_complete(resources.memulai())
    #userbot.LOOP.run_until_complete(resources.cloneplugins())
    #userbot.LOOP.run_until_complete(resources.clonevc())
    userbot.LOOP.run_until_complete(resources.join())
    LOGS.info(f"꧁༺ Chums Userbot ༻꧂\n⚙️ Version:{userbot.__version__} [TELAH DIAKTIFKAN]")
    if ChumsBot:
        ChumsBot.send_message(PRIVATE, THON_ON.format(ChumsBot.me.username, userbot.__version__, cmdhr, total))
    if ChumsBot2:
        ChumsBot2.send_message(PRIVATE, THON_ON.format(ChumsBot2.me.username, userbot.__version__, cmdhr, total))
    if ChumsBot3:
        ChumsBot3.send_message(PRIVATE, THON_ON.format(ChumsBot3.me.username, userbot.__version__, cmdhr, total))
             


if __name__ == "__main__":
    if pdB.get_key("SESSION") or Database.SESSION:
        usersss = Telethon()
        total = 50 - usersss
        start()
        LOGS.info(f"Total Clients = {total} Users")
    if pdB.get_key("PyroSESSION") or Database.PyroSESSION:
        Pyrogram()
        
    
if ChumsBot:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot.run_until_disconnected()
        else:
            ChumsBot.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot2:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot2.run_until_disconnected()
        else:
            ChumsBot2.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot3:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot3.run_until_disconnected()
        else:
            ChumsBot3.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot4:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot4.run_until_disconnected()
        else:
            ChumsBot4.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot5:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot5.run_until_disconnected()
        else:
            ChumsBot5.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot6:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot6.run_until_disconnected()
        else:
            ChumsBot6.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)



if ChumsBot7:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot7.run_until_disconnected()
        else:
            ChumsBot7.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)



if ChumsBot8:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot8.run_until_disconnected()
        else:
            ChumsBot8.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot9:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot9.run_until_disconnected()
        else:
            ChumsBot9.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot10:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot10.run_until_disconnected()
        else:
            ChumsBot10.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot11:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot11.run_until_disconnected()
        else:
            ChumsBot11.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot12:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot12.run_until_disconnected()
        else:
            ChumsBot12.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot13:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot13.run_until_disconnected()
        else:
            ChumsBot13.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot14:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot14.run_until_disconnected()
        else:
            ChumsBot14.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot15:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot15.run_until_disconnected()
        else:
            ChumsBot15.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot16:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot16.run_until_disconnected()
        else:
            ChumsBot16.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot17:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot17.run_until_disconnected()
        else:
            ChumsBot17.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot18:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot18.run_until_disconnected()
        else:
            ChumsBot18disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot19:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot19.run_until_disconnected()
        else:
            ChumsBot19.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot20:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot21.run_until_disconnected()
        else:
            ChumsBot21.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot21:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot21.run_until_disconnected()
        else:
            ChumsBot21.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot22:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot22.run_until_disconnected()
        else:
            ChumsBot22.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot23:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot23.run_until_disconnected()
        else:
            ChumsBot23.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot24:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot24.run_until_disconnected()
        else:
            ChumsBot24.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot25:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot25.run_until_disconnected()
        else:
            ChumsBot25.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot26:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot26.run_until_disconnected()
        else:
            ChumsBot26.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot27:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot27.run_until_disconnected()
        else:
            ChumsBot27.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot28:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot28.run_until_disconnected()
        else:
            ChumsBot28.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot29:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot29.run_until_disconnected()
        else:
            ChumsBot29.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot30:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot30.run_until_disconnected()
        else:
            ChumsBot30.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot31:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot31.run_until_disconnected()
        else:
            ChumsBot31.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot32:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot32.run_until_disconnected()
        else:
            ChumsBot32.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot33:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot33.run_until_disconnected()
        else:
            ChumsBot33.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot34:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot34.run_until_disconnected()
        else:
            ChumsBot34.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot36:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot36.run_until_disconnected()
        else:
            ChumsBot36.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot37:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot37.run_until_disconnected()
        else:
            ChumsBot37.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot38:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot38.run_until_disconnected()
        else:
            ChumsBot38.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot39:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot39.run_until_disconnected()
        else:
            ChumsBot39.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot40:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot40.run_until_disconnected()
        else:
            ChumsBot40.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot41:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot41.run_until_disconnected()
        else:
            ChumsBot41.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot42:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot42.run_until_disconnected()
        else:
            ChumsBot42.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot43:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot43.run_until_disconnected()
        else:
            ChumsBot43.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot44:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot44.run_until_disconnected()
        else:
            ChumsBot44.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot45:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot45.run_until_disconnected()
        else:
            ChumsBot45.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot46:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot46.run_until_disconnected()
        else:
            ChumsBot46.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot47:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot47.run_until_disconnected()
        else:
            ChumsBot47.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot48:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot48.run_until_disconnected()
        else:
            ChumsBot48.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)

if ChumsBot49:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot49.run_until_disconnected()
        else:
            ChumsBot49.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
if ChumsBot35:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot35.run_until_disconnected()
        else:
            ChumsBot35.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
        
if ChumsBot50:
    try:
        if len(sys.argv) in {1, 3, 4}:
            with contextlib.suppress(ConnectionError):
                ChumsBot50.run_until_disconnected()
        else:
            ChumsBot50.disconnect()    
    except Exception as e:
        LOGS.info(str(e), exc_info=True)
        sys.exit(1)
