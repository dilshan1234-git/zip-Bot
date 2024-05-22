# ©️ LISA-KOREA | @LISA_FAN_LK | NT_BOT_CHANNEL | LISA-KOREA/UnZip-Bot

# [⚠️ Do not change this repo link ⚠️] :- https://github.com/LISA-KOREA/UnZip-Bot



from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup




@Client.on_message(filters.command("start"))
async def start(client, message):
    reply_markup = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("join වෙලා බලන්න", url="https://t.me/NT_BOT_CHANNEL"),
        ],
        [
            InlineKeyboardButton("👥 Support Group", url="https://t.me/NT_BOTS_SUPPORT"),
            InlineKeyboardButton("👩‍💻 Developer", url="https://t.me/LISA_FAN_LK"),
        ] 
   ]
  )
    start_message = (
        "Hello!\n\n"
        "zip එකක් එවලා බලන්න.සමහරවිට unzip වෙයි 🔥."
    )
    await message.reply(start_message, reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def help_command(client, message):
    help_message = (
        "Here are the commands you can use:\n\n"
        "/start - Start the bot and get the welcome message\n"
        "/help - Get help on how to use the bot\n\n"
        "To unzip a file, simply send me a ZIP file and I will extract its contents and send them back to you.\n\n"
        "©️ Channel : @NT_BOT_CHANNEL"
    )
    await message.reply(help_message)
    
