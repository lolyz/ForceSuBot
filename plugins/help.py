import logging
from Config import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)

@Client.on_message(filters.private & filters.incoming & filters.command(['start']))
def _start(client, message):
    client.send_message(message.chat.id,
        text=tr.START_MSG.format(message.from_user.first_name, message.from_user.id),
        parse_mode="markdown",
        reply_to_message_id=message.message_id
        )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_notification = True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = '➪𝐍𝐞𝐱𝐭➪', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = "https://github.com/lolyz/ForceSuBot/issues/new"
        button = [
            [InlineKeyboardButton(text = '🔊𝐔𝐩𝐝𝐚𝐭𝐞 𝐂𝐡𝐚𝐧𝐧𝐞𝐥🔊', url="https://t.me/LgViral")],
            [InlineKeyboardButton(text = '😍𝐅𝐞𝐚𝐭𝐮𝐫𝐞 𝐑𝐞𝐪𝐮𝐞𝐬𝐭 & 𝐈𝐬𝐬𝐮𝐞𝐬🤪', url=url)],
            [InlineKeyboardButton(text = '💝𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐘𝐓💝', url="https://youtube.com/channel/UCY7bwQmyLpocbk5_p2RvzYQ")],
            [InlineKeyboardButton(text = '🔙𝐁𝐚𝐜𝐤🔙', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '🔙𝐁𝐚𝐜𝐤', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = '𝐍𝐞𝐱𝐭➪', callback_data = f"help+{pos+1}")
            ],
        ]
    return button
