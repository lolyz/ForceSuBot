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
            [InlineKeyboardButton(text = 'âŠðððąð­âŠ', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):
        url = "https://github.com/lolyz/ForceSuBot/issues/new"
        button = [
            [InlineKeyboardButton(text = 'ðððĐððð­ð ððĄðð§ð§ððĨð', url="https://t.me/LgViral")],
            [InlineKeyboardButton(text = 'ððððð­ðŪðŦð ðððŠðŪððŽð­ & ððŽðŽðŪððŽðĪŠ', url=url)],
            [InlineKeyboardButton(text = 'ðððŪðĐðĐðĻðŦð­ ððð', url="https://youtube.com/channel/UCY7bwQmyLpocbk5_p2RvzYQ")],
            [InlineKeyboardButton(text = 'ðððððĪð', callback_data = f"help+{pos-1}")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = 'ðððððĪ', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'ðððąð­âŠ', callback_data = f"help+{pos+1}")
            ],
        ]
    return button
