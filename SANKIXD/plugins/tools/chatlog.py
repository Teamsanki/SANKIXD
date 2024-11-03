import random
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import LOGGER_ID as LOG_GROUP_ID
from SANKIXD import app 
from pyrogram.errors import RPCError
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, aiohttp
from pathlib import Path
from pyrogram.enums import ParseMode

photo = [
    "https://telegra.ph/file/1949480f01355b4e87d26.jpg",
    "https://telegra.ph/file/3ef2cc0ad2bc548bafb30.jpg",
    "https://telegra.ph/file/a7d663cd2de689b811729.jpg",
    "https://telegra.ph/file/6f19dc23847f5b005e922.jpg",
    "https://telegra.ph/file/2973150dd62fd27a3a6ba.jpg",
]

@app.on_message(filters.new_chat_members, group=2)
async def join_watcher(_, message):    
    chat = message.chat
    link = await app.export_chat_invite_link(chat.id)
    for member in message.new_chat_members:
        if member.id == app.id:
            count = await app.get_chat_members_count(chat.id)
            msg = (
                f"𝐘𝐨𝐮𝐫 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐑𝐞𝐚𝐜𝐡𝐞𝐝 𝐎𝐧𝐞 𝐦𝐨𝐫𝐞 𝐆𝐫𝐨𝐮𝐩\n\n"
                f"⦿ 𝐂𝐡𝐚𝐭 𝐋𝐢𝐧𝐤 ➺ {chat.title}\n"
                f"⦿ 𝐂𝐡𝐚𝐭 𝐈𝐃 ➺ {chat.id}\n"
                f"⦿ 𝐂𝐡𝐚𝐭 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 ➺ @{chat.username}\n"
                f"⦿ 𝐂𝐡𝐚𝐭 𝐋𝐢𝐧𝐤 ➺ [ᴄʟɪᴄᴋ]({link})\n"
                f"⦿ 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ➺ {count}\n"
                f"⦿ 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ➺ {message.from_user.mention}"
            )
            await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=msg, reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(f"sᴇᴇ ɢʀᴏᴜᴘ👀", url=f"{link}")]
            ]))

@app.on_message(filters.left_chat_member)
async def on_left_chat_member(_, message: Message):
    if (await app.get_me()).id == message.left_chat_member.id:
        remove_by = message.from_user.mention if message.from_user else "𝐔ɴᴋɴᴏᴡɴ 𝐔sᴇʀ"
        title = message.chat.title
        username = f"@{message.chat.username}" if message.chat.username else "𝐏ʀɪᴠᴀᴛᴇ 𝐂ʜᴀᴛ"
        chat_id = message.chat.id
        left = f"✫ <b><u>𝐎𝐨𝐩𝐬 𝐘𝐨𝐮𝐫 𝐌𝐮𝐬𝐢𝐜 𝐁𝐨𝐭 𝐈𝐬 𝐑𝐞𝐦𝐨𝐯𝐞𝐝</u></b> ✫\n\n⦿ 𝐂𝐡𝐚𝐭 𝐍𝐚𝐦𝐞 ➺ {title}\n\n⦿ 𝐂𝐡𝐚𝐭 𝐈𝐝 ➺ {chat_id}\n\n⦿ 𝐑𝐞𝐦𝐨𝐯𝐞𝐝 𝐁𝐲 ➺ {remove_by}\n\n⦿ 𝐁𝐨𝐭 ➺ @{app.username}"
        await app.send_photo(LOG_GROUP_ID, photo=random.choice(photo), caption=left)
        
