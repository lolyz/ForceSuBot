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

        "šš¼šæš°š² š¦ššÆšš°šæš¶šÆš².\nšš¼šæš°š² š“šæš¼šš½ šŗš²šŗšÆš²šæš šš¼ š·š¼š¶š» š® šš½š²š°š¶š³š¶š° š°šµš®š»š»š²š¹ šÆš²š³š¼šæš² šš²š»š±š¶š»š“ šŗš²ššš®š“š²š š¶š» ššµš² š“šæš¼šš½.\nš šš¶š¹š¹ šŗššš² šŗš²šŗšÆš²šæš š¶š³ ššµš²š š»š¼š š·š¼š¶š»š²š± šš¼ššæ š°šµš®š»š»š²š¹ š®š»š± šš²š¹š¹ ššµš²šŗ šš¼ š·š¼š¶š» ššµš² š°šµš®š»š»š²š¹ š®š»š± šš»šŗššš² ššµš²šŗšš²š¹š³ šÆš š½šæš²ššš¶š»š“ š® šÆšššš¼š»",
        
        "šš¢šŖ š§š¢ š¦šš§-šØš£ ?.\n\nš·ļøšš¼š¹š¹š¼š š§šµš²šš² š¦šš²š½šš·ļø.\n\nā : `Add Me On Your Group Or Channel! And make ADMIN with all Permission!`.\n\nā : `Next You Type in Group` /ForceSubscribe `with your channel username!`.\n\nššš«šš š£šš : `/ForceSubscribe @SiPmks`.\n\nšš”š¢š§š:\nć `Private Channel Not supported!`.\nć `And Only Group Owner Can Setup me!`",
        
        "āļøššš©ššššššš šš¢š š šš”ššāļø.\n\nāŖ /ForceSubscribe - To get the current settings.\nāŖ /ForceSubscribe no/off/disable -To turn of ForceSubscribe.\nāŖ /ForceSubscribe clear - To unmute all members who muted by me.\nāŖ /ForceSubscribe (channel username) - To turn on and setup the channel.\n\nššØš­š : /FSub is an alias of /ForceSubscribe.\n\nš² ššš©šš¢š£šš„ š²: @SiPmks",
        
        "šššššš ššš.\n\nš¤ š š¬ š”šš š : <a href='https://t.me/ForceSuBot'>Force Subscriber Bot</a>.\n\nšššš”ššØššš : <code>Python3</code>.\n\nš² ššš©šš¢š£šš„ : <a href='https://t.me/SiPmks'>SiPmks</a>.\n\nš£šššš”š”šš : <a href='https://t.me/LgViral'>Lagi Viral</a>.\n\n š­š¦šš„š©šš„ : <a href='https://Heroku.com/'>Heroku</a>.\n\nā­š¦š¢šØš„šš šš¢šš : <a href='https://t.me/SiPmks'>Price Now</a>"
      ]

      START_MSG = "**Hello [{}](tg://user?id={})**\n\nšš ššš§ ššØš«šš ššš¦ššš«š¬ ššØ ššØš¢š§ š šš©ššš¢šš¢š šš”šš§š§šš„.\n\nššššØš«š šš«š¢š­š¢š§š  ššš¬š¬šš šš¬ šš§ šš”š šš«šØš®š©.\n\nšššš«š§ ššØš«š šš² šš„š¢šš¤š¢š§š š /help"
