from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 سلام {message.from_user.first_name}!</b>
 دا من ربات پخش موزیک هستم. از من در گروه استفاده کن.

""",

    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        " مایل به سرچ در یوتیوب؟ ",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ بله", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "خیر ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
