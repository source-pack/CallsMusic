from pyrogram import Client, filters
from pyrogram.types import Message

import tgcalls
import sira
from cache.admins import set
from helpers.wrappers import errors, admins_only


@Client.on_message(
    filters.command(["pause", "pause@Quplayerbot"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def pause(client: Client, message: Message):
    tgcalls.pytgcalls.pause_stream(message.chat.id)
    await message.reply_text("⏸ Paused.")


@Client.on_message(
    filters.command(["resume", "resume@Quplayerbot"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def resume(client: Client, message: Message):
    tgcalls.pytgcalls.resume_stream(message.chat.id)
    await message.reply_text("▶️ Resumed.")


@Client.on_message(
    filters.command(["stop", "stop@Quplayerbot"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def stop(client: Client, message: Message):
    try:
        sira.clear(message.chat.id)
    except:
        pass

    tgcalls.pytgcalls.leave_group_call(message.chat.id)
    await message.reply_text("⏹ Stopped streaming.")


@Client.on_message(
    filters.command(["next@Quplayerbot", "next"])
    & filters.group
    & ~ filters.edited
)
@errors
@admins_only
async def skip(client: Client, message: Message):
    chat_id = message.chat.id

    sira.task_done(chat_id)

    if sira.is_empty(chat_id):
        tgcalls.pytgcalls.leave_group_call(chat_id)
    else:
        tgcalls.pytgcalls.change_stream(
            chat_id, sira.get(chat_id)["file_path"]
        )

    await message.reply_text("⏩ Skipped the current song.")


@Client.on_message(
    filters.command(["admincache", "admincashe@Quplayerbot"])
)
@errors
@admins_only
async def admincache(client, message: Message):
    set(message.chat.id, [member.user for member in await message.chat.get_members(filter="administrators")])
    await message.reply_text("❇️ Admin cache refreshed!")
