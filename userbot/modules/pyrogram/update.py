# Copyright (C) 2021 PandaUserbot <https://github.com/ilhammansiz/PandaX_Userbot>
# maintaince 2023 pyrogram & telethon
# jangan di hapus ga semuanya dihapus lu paham 😏
# Pembaruan 2023 skala besar dengan menggabungkan 2 basis telethon and pyrogram.
# Dibuat dari berbagai userbot yang pernah ada.
# t.me/pandac0de t.me/pandauserbot

import os
import asyncio
import sys
from os import remove
import re
import asyncio
import sys
import shutil
import subprocess

from pyrogram import Client, filters
from pyrogram.types import Message

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError

from ... import app
from ..._helper import gen



_REPO = app.UPSTREAM_REPO


async def gen_chlog(repo, diff):
    ch_log = ""
    dateform = "On %d/%m/%y at %H:%M:%S"
    for data in repo.iter_commits(diff):
        ch_log += f"**#{data.count()}** : {data.committed_datetime.strftime(dateform)} : [{data.summary}]({TRON_REPO.rstrip('/')}/commit/{data}) by `{data.author}`\n"
    return ch_log


async def install_requirements():
    try:
        process = await asyncio.create_subprocess_shell(
            " ".join(
                [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
            ),
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()
        return process.returncode
    except Exception as e:
        return repr(e)


@app.on_message(gen("update", allow=["sudo", "channel"]))
async def update_handler(_, m):
    cmd = False
    errtext = "Some problem occurred:\n\n"

    await app.send_edit(
        m, "Checking for updates, please wait . . .", text_type=["mono"]
    )

    if app.long(m) > 1:
        cmd = m.command

    try:
        repo = Repo()
    except NoSuchPathError as e:
        await app.send_edit(m, f"{errtext}`{e}`")
        return repo.__del__()

    except GitCommandError as e:
        await app.send_edit(m, f"{errtext}`{e}`")
        return repo.__del__()

    except InvalidGitRepositoryError:
        repo = Repo.init()
        origin = repo.create_remote("upstream", _REPO)
        origin.fetch()
        repo.create_head("master", origin.refs.master)
        repo.heads.master.set_tracking_branch(origin.refs.master)
        repo.heads.master.checkout(True)
    ACTIVE_BRANCH = repo.active_branch.name
    if ACTIVE_BRANCH != "update":
        await app.send_edit(
            m,
            f"**[ UPDATER ]:** You are on [ {ACTIVE_BRANCH} ]\n\nPlease change to `master` branch.`",
        )
        return repo.__del__()

    try:
        repo.create_remote("upstream", _REPO)
    except BaseException:
        pass
    ups_rem = repo.remote("upstream")
    ups_rem.fetch(ACTIVE_BRANCH)
    changelog = await gen_chlog(repo, f"{ACTIVE_BRANCH}")
    if cmd is False:
        if changelog:
            changelog_str = f"**New update is available for [{ACTIVE_BRANCH}]({_REPO}/tree/{ACTIVE_BRANCH}):\n\n[CHANGE LOG]:**\n\n{changelog}"
            if len(changelog_str) > 4096:
                await app.send_edit(
                    m,
                    "Changelog is too big, view the file below to see it.",
                    text_type=["mono"],
                    delme=6,
                )
                file = open("up_output.txt", "w+")
                file.write(changelog_str)
                file.close()
                await app.send_document(
                    m.chat.id,
                    "up_output.txt",
                    caption="**[ STATUS ]:** Do `.update now` to update.",
                )
                remove("up_output.txt")
            else:
                return await app.reply(
                    m,
                    f"{changelog_str}\n\n[ UPDATE ]: Do `.update now` to update.",
                    disable_web_page_preview=True,
                )
        else:
            await m.reply(
                m,
                f"**[ STATUS ]:** Your bot is upto date !\n**[ VERSION ]:** `{app.userbot_version}`\n**[ BRANCH ]:** [{ACTIVE_BRANCH}]({_REPO}/tree/{ACTIVE_BRANCH})",
                disable_web_page_preview=True,
            )
            return repo.__del__()

    if app.HEROKU_API_KEY:
        import heroku3

        heroku = heroku3.from_key(app.HEROKU_API_KEY)
        heroku_app = None
        heroku_applications = heroku.apps()
        if not app.HEROKU_APP_NAME:
            await app.send_edit(
                m,
                "Please set up the [ HEROKU_APP_NAME ] variable to be able to update userbot.",
                text_type=["mono"],
                delme=4,
            )
            return repo.__del__()

        for apps in heroku_applications:
            if apps.name == app.HEROKU_APP_NAME:
                heroku_app = apps
                break

        if heroku_app is None:
            await app.send_edit(
                m,
                "Invalid Heroku credentials for updating userbot.",
                text_type=["mono"],
                delme=4,
            )
            return repo.__del__()

        m = await app.send_edit(
            m,
            "Userbot update in progress, please wait for few minutes . . .",
            text_type=["mono"],
        )
        ups_rem.fetch(ACTIVE_BRANCH)
        repo.git.reset("--hard", "FETCH_HEAD")
        heroku_git_url = heroku_app.git_url.replace(
            "https://", "https://api:" + app.HEROKU_API_KEY + "@"
        )

        if "heroku" in repo.remotes:
            remote = repo.remote("heroku")
            remote.set_url(heroku_git_url)
        else:
            remote = repo.create_remote("heroku", heroku_git_url)

        try:
            remote.push(refspec=f"HEAD:refs/heads/{ACTIVE_BRANCH}", force=True)
        except GitCommandError as e:
            app.log.error(e)

        await app.send_edit(
            m, "Successfully Updated, initialing . . .", text_type=["mono"], delme=8
        )

    else:
        try:
            ups_rem.pull(ACTIVE_BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        await install_requirements()
        await app.send_edit(
            m,
            "Successfully updated Userbot!\nBot is restarting . . .",
            text_type=["mono"],
            delme=8,
        )

def check_command(command):
    return shutil.which(command) is not None

@app.on_message(gen("up", allow=["sudo", "channel"]))
async def ngapdate(client, message):
  pros = await message.reply(
        f"<blockquote> <b>Memeriksa pembaruan resources ..</b></blockquote>"
    )
  out = subprocess.check_output(["git", "pull"]).decode("UTF-8")
  teks = f"<b>❒ Status resources :</b>\n"
  memeg = f"<b>Perubahan logs </b>"
  if "Already up to date." in str(out):
        return await pros.edit(f"<blockquote>{teks}┖ {out}</blockquote>")
  elif len(out) > 4096:
          anuk = await pros.edit(
            f"<blockquote> <b>Hasil akan dikirimkan dalam bentuk file ..</b></blockquote>"
        )
  anuk = None
  with open("output.txt", "w+") as file:
            file.write(out)

           # X = f"<blockquote> <b>Perubahan logs </b></blockquote>"
  #await client.send_document(
  #        message.chat.id,
  #        "output.txt",
  #        caption=f"{X}",
   #       reply_to_message_id=message.id,
   #       )
  os.remove("output.txt")
  format_line = [f"┣ {line}" for line in out.splitlines()]
  if format_line:
    format_line[-1] = f"┖ {format_line[-1][2:]}"
    format_output = "\n".join(format_line)
  await pros.edit(f"<blockquote>{memeg}\n\n{teks}{format_output}</blockquote>")
  os.execl(sys.executable, sys.executable, "erbanget.py")
  

app.CMD_HELP.update(
    {
        "update": (
            "update",
            {
                "update": "To check if new update is available or not.",
                "update [ now ]": "To update userbot to latest version.",
                "up": "Tampilan Baru",
            },
        )
    }
)
