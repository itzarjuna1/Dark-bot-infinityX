from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import MUSIC_BOT_NAME
from Oneforall import app


@app.on_message(filters.command(["alive"]))
async def start(client: Client, message: Message):
    await message.reply_video(
        video=f"https://files.catbox.moe/l0r3oo.mp4",
        caption=f"❤️ ʜᴇʏ {message.from_user.mention}\n\n🔮 ɪ ᴀᴍ {MUSIC_BOT_NAME}\n\n✨ ɪ ᴀᴍ ғᴀsᴛ ᴀɴᴅ ᴩᴏᴡᴇʀғᴜʟ ᴍᴜsɪᴄ ᴩʟᴀʏᴇʀ ʙᴏᴛ ᴡɪᴛʜ sᴏᴍᴇ ᴀᴡᴇsᴏᴍᴇ ғᴇᴀᴛᴜʀᴇs.\n\n💫 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ ᴊᴏɪɴ ᴏᴜʀ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ🤍...\n\n━━━━━━━━━━━━━━━━━━❄",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Infinity", url=f"https://t.me/Destiny_Infinity_Og"
                    ),
                    InlineKeyboardButton(
                        text="☆ ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/infinitygx_bot_support"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="☆ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/who_cares_qt"
                    ),
                ],
                [InlineKeyboardButton("✯ ᴄʟᴏsᴇ ✯", callback_data="close")],
            ]
        ),
    )
