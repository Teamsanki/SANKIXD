from pyrogram.enums import ParseMode

from SANKIXD import app
from SANKIXD.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        logger_text = f"""
<b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>

<b>⦿ 𝐂𝐡𝐚𝐭 𝐈𝐃 ➺ :</b> <code>{message.chat.id}</code>
<b>⦿ 𝐂𝐡𝐚𝐭 𝐍𝐚𝐦𝐞 ➺ :</b> {message.chat.title}
<b>⦿ 𝐂𝐡𝐚𝐭 𝐋𝐢𝐧𝐤 ➺ :</b> @{message.chat.username}

<b>⦿ 𝐈𝐝 ➺ :</b> <code>{message.from_user.id}</code>
<b>⦿ 𝐔𝐬𝐞𝐫 ➺ :</b> {message.from_user.mention}
<b>⦿ 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 ➺ :</b> @{message.from_user.username}

<b>⦿ 𝐒𝐞𝐚𝐫𝐜𝐡𝐞𝐝 ➺ :</b> {message.text.split(None, 1)[1]}
<b>sᴛʀᴇᴀᴍᴛʏᴘᴇ :</b> {streamtype}"""
        if message.chat.id != LOGGER_ID:
            try:
                await app.send_message(
                    chat_id=LOGGER_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
