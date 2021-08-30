import os 
from os import error
import logging
import pyrogram
import time
from decouple import config
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

PARADISE_2021 = Client(
    "Paradise-2021-Official-bot",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_TEXT = """ Hi {},Im @Paradise2021Lk Official Bot. Join My Group And Channel
"""

GROUP_INFO_TEXT = """
**☝️ශ‍රී ලාංකිකත්වයට🇱🇰පරෝගාමීව☝️**

💢අසභ්‍ය  බැහැ👊
⭕️ආරවුල්  බැහැ👊
💢ලන්ක් බැහැ 👊
⭕️ඉන්බොක්ස් වද හිංසා ✋ බැහැ👊

නිදහසේ චැට්  කරන්න
`📚 Education `
`🎬Film`
`🎶Music `
`🤠Jobs........(Links Are Available)`

__සිංහල හදවත ❤️ අපේ කමට__
__ශ්‍රී ලාංකිකයි🇱🇰💕__

~ @Paradise2021Lk
"""

CHANNEL_INFO_TEXT = """
**🗿වංශකතාව⚖️  ග‍රන්ථාරූඩ✍️ කරන ආශ්වාස☘️🍃 ප‍රාශ්වාස_________+🌈️🌤☁️🌧️**
**විසි හතර 🧭 පැය.**

`2021-07-17`
`23:30`

~ @paradischanal
"""

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Group', url='https://t.me/Paradise2021Lk'),
        InlineKeyboardButton('Channel', url='https://t.me/paradischanal')
        ],
        [
        InlineKeyboardButton('Group Info 🎨',callback_data='paradise_ginfo'),
        ],
        [InlineKeyboardButton('Channel Info 🎭',callback_data="paradise_cinfo")
        ]]
  
)
CLOSE_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('Back',callback_data='cbclose'),
        ]]
    )


@PARADISE_2021.on_callback_query() # callbackQuery()
async def cb_data(bot, update):  
    if update.data == "paradise_ginfo":
        await update.message.edit_text(
            text=GROUP_INFO_TEXT,
            reply_markup=CLOSE_BUTTON,
            disable_web_page_preview=True
        )
    elif update.data == "paradise_cinfo":
        await update.message.edit_text(
            text=CHANNEL_INFO_TEXT,
            reply_markup=CLOSE_BUTTON,
            disable_web_page_preview=True
        )
    else:
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            disable_web_page_preview=True,
            reply_markup=START_BUTTON
        )
        
@PARADISE_2021.on_message(filters.command(["start"]) & filters.private)
async def start_private(bot, update):
    text = START_TEXT.format(update.from_user.mention)
    reply_markup = START_BUTTON
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup,
        quote=True
    )        
    
PARADISE_2021.run()    
