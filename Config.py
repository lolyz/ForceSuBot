import os

class Config():
  ENV = bool(os.environ.get('ENV', False))
  if ENV:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
    DATABASE_URL = os.environ.get("DATABASE_URL", None)
    APP_ID = os.environ.get("APP_ID", 6)
    API_HASH = os.environ.get("API_HASH", None)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS").split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))
  else:
    BOT_TOKEN = ""
    DATABASE_URL = ""
    APP_ID = ""
    API_HASH = ""
    SUDO_USERS = list(set(int(x) for x in ''.split()))
    SUDO_USERS.append(939425014)
    SUDO_USERS = list(set(SUDO_USERS))


class Messages():
      HELP_MSG = [
        ".",

        "𝗙𝗼𝗿𝗰𝗲 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲.\n𝗙𝗼𝗿𝗰𝗲 𝗴𝗿𝗼𝘂𝗽 𝗺𝗲𝗺𝗯𝗲𝗿𝘀 𝘁𝗼 𝗷𝗼𝗶𝗻 𝗮 𝘀𝗽𝗲𝗰𝗶𝗳𝗶𝗰 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗯𝗲𝗳𝗼𝗿𝗲 𝘀𝗲𝗻𝗱𝗶𝗻𝗴 𝗺𝗲𝘀𝘀𝗮𝗴𝗲𝘀 𝗶𝗻 𝘁𝗵𝗲 𝗴𝗿𝗼𝘂𝗽.\n𝗜 𝘄𝗶𝗹𝗹 𝗺𝘂𝘁𝗲 𝗺𝗲𝗺𝗯𝗲𝗿𝘀 𝗶𝗳 𝘁𝗵𝗲𝘆 𝗻𝗼𝘁 𝗷𝗼𝗶𝗻𝗲𝗱 𝘆𝗼𝘂𝗿 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗮𝗻𝗱 𝘁𝗲𝗹𝗹 𝘁𝗵𝗲𝗺 𝘁𝗼 𝗷𝗼𝗶𝗻 𝘁𝗵𝗲 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗮𝗻𝗱 𝘂𝗻𝗺𝘂𝘁𝗲 𝘁𝗵𝗲𝗺𝘀𝗲𝗹𝗳 𝗯𝘆 𝗽𝗿𝗲𝘀𝘀𝗶𝗻𝗴 𝗮 𝗯𝘂𝘁𝘁𝗼𝗻",
        
        "𝗛𝗢𝗪 𝗧𝗢 𝗦𝗘𝗧-𝗨𝗣 ?.\n\n🏷️𝗙𝗼𝗹𝗹𝗼𝘄 𝗧𝗵𝗲𝘀𝗲 𝗦𝘁𝗲𝗽𝘀🏷️.\n\n❒ : `Add Me On Your Group Or Channel! And make ADMIN with all Permission!`.\n\n❒ : `Next You Type in Group` /ForceSubscribe `with your channel username!`.\n\n👉𝗘𝗫𝗔𝗠𝗣𝗟𝗘 : `/ForceSubscribe @SiPmks`.\n\n🛑𝗡𝗢𝗧𝗘:\n〇 `Private Channel Not supported!`.\n〇 `And Only Group Owner Can Setup me!`",
        
        "⚙️👇𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗👇⚙️.\n\n➪ /ForceSubscribe - To get the current settings.\n➪ /ForceSubscribe no/off/disable -To turn of ForceSubscribe.\n➪ /ForceSubscribe clear - To unmute all members who muted by me.\n➪ /ForceSubscribe (channel username) - To turn on and setup the channel.\n\n𝐍𝐨𝐭𝐞 : /FSub is an alias of /ForceSubscribe.\n\n👲 𝗗𝗘𝗩𝗟𝗢𝗣𝗘𝗥 👲: @SiPmks",
        
        "📑𝐀𝐁𝐎𝐔𝐓 𝐌𝐄📑.\n\n🤖 𝗠𝗬 𝗡𝗔𝗠𝗘 : <a href='https://t.me/ForceSuBot'>Force Subscriber Bot</a>.\n\n📜𝗟𝗔𝗡𝗚𝗨𝗔𝗚𝗘 : <code>Python3</code>.\n\n👲 𝗗𝗘𝗩𝗟𝗢𝗣𝗘𝗥 : <a href='https://t.me/SiPmks'>SiPmks</a>.\n\n📣𝗖𝗛𝗔𝗡𝗡𝗘𝗟 : <a href='https://t.me/LgViral'>Lagi Viral</a>.\n\n 📭𝗦𝗘𝗥𝗩𝗘𝗥 : <a href='https://Heroku.com/'>Heroku</a>.\n\n⭕𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href='https://t.me/SiPmks'>Price Now</a>"
      ]

      START_MSG = "**Hello [{}](tg://user?id={})**\n\n🙋𝐈 𝐂𝐚𝐧 𝐅𝐨𝐫𝐜𝐞 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐓𝐨 𝐉𝐨𝐢𝐧 𝐀 𝐒𝐩𝐞𝐜𝐢𝐟𝐢𝐜 𝐂𝐡𝐚𝐧𝐧𝐞𝐥.\n\n𝐁𝐞𝐟𝐨𝐫𝐞 𝐖𝐫𝐢𝐭𝐢𝐧𝐠 𝐌𝐞𝐬𝐬𝐚𝐠𝐞𝐬 𝐈𝐧 𝐓𝐡𝐞 𝐆𝐫𝐨𝐮𝐩.\n\n𝐋𝐞𝐚𝐫𝐧 𝐌𝐨𝐫𝐞 𝐁𝐲 𝐂𝐥𝐢𝐜𝐤𝐢𝐧𝐠👉 /help"
