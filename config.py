import re
import os
import time
from os import environ

# Shortlink API configuration
API = environ.get("API", "e32725a33a1ba7ce1e349c531ea2182faf3e2e9d") # shortlink api
URL = environ.get("URL", "arolinks.com") # shortlink domain without https://
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/howuseme/7") # how to open link 
BOT_USERNAME = environ.get("BOT_USERNAME", "KGN_4GBFILERENAME_BOT") # bot username without @
VERIFY = environ.get("VERIFY", "True") == "True"  # Convert string to boolean

id_pattern = re.compile(r'^.\d+$')

class Config(object):
    # pyro client config
    API_ID = os.environ.get("API_ID", "")  # ⚠️ Required
    API_HASH = os.environ.get("API_HASH", "")  # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")  # ⚠️ Required

    # premium 4g renaming client
    STRING_API_ID = os.environ.get("STRING_API_ID", "")
    STRING_API_HASH = os.environ.get("STRING_API_HASH", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")

    # database config
    DB_NAME = os.environ.get("DB_NAME", "")
    DB_URL = os.environ.get("DB_URL", "")  # ⚠️ Required

    # other configs
    BOT_UPTIME = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/9c910cbc74144b3b2efce.jpg")
    ADMIN = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMIN', '').split()]  # ⚠️ Required
    
    FORCE_SUB = os.environ.get("FORCE_SUB", "KGN_BOTZ") # ⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))  # ⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '105'))
    BANNED_USERS = set(int(x) for x in os.environ.get(
        "BANNED_USERS", "1234567890").split())

    # wes response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))

    # Add the missing attributes
    VERIFY = VERIFY
    BOT_USERNAME = BOT_USERNAME
    VERIFY_TUTORIAL = VERIFY_TUTORIAL


class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hɪ {} ♡゙,\n\n◈ I Aᴍ A Pᴏᴡᴇʀғᴜʟ Fɪʟᴇ Rᴇɴᴀᴍᴇʀ Bᴏᴛ.
◈ I Cᴀɴ Rᴇɴᴀᴍᴇ Fɪʟᴇs ᴜᴘᴛᴏ 4GB, Cʜᴀɴɢᴇ Tʜᴜᴍʙɴᴀɪʟs, Cᴏɴᴠᴇʀᴛ Bᴇᴛᴡᴇᴇɴ Vɪᴅᴇᴏ Aɴᴅ Fɪʟᴇ, Aɴᴅ Sᴜᴘᴘᴏʀᴛ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟs Aɴᴅ Cᴀᴘᴛɪᴏɴs.\n\n• Mᴀɪɴᴛᴀɪɴᴇᴅ Bʏ : @KGN_BOTZ"""

    ABOUT_TXT = """<b>╭───────────⍟
• ᴍy ɴᴀᴍᴇ : {}
• ᴘʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/ExE_AQUIB>ᴀǫᴜɪʙ</a>
• ɴᴇᴛᴡᴏʀᴋ : <a href=https://t.me/chrunchyrool>ᴋɢɴ ɴᴇᴛᴡᴏʀᴋs</a>
• ᴄʜᴀᴛ ɢʀᴏᴜᴘ: <a href=https://t.me/+zlb3ReuJ40tjMDA1>sᴜᴘᴘᴏʀᴛ</a>
• ᴍʏ ᴏᴡɴᴇʀ / ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/KGN_BOTZ>ᴋɢɴ ʙᴏᴛᴢ</a>
╰───────────────⍟ """

    HELP_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
<b>•></b> /start Tʜᴇ Bᴏᴛ Aɴᴅ Sᴇɴᴅ Aɴy Pʜᴏᴛᴏ Tᴏ Aᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟy Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
<b>•></b> /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ.


📑 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u></b>

<b>•></b> /set_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Sᴇᴛ ᴀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /see_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
<b>•></b> /del_caption - Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ
Exᴀᴍᴩʟᴇ:- <code> /set_caption 📕 Fɪʟᴇ Nᴀᴍᴇ: {filename}
💾 Sɪᴢᴇ: {filesize}
⏰ Dᴜʀᴀᴛɪᴏɴ: {duration} </code>

✏️ <b><u>Hᴏᴡ Tᴏ Rᴇɴᴀᴍᴇ A Fɪʟᴇ</u></b>
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           


<b>➜ ᴘᴏᴡᴇʀᴇᴅ ʙʏ:</b> <a href=https://t.me/KGN_BOTZ>ᴋɢɴ ʙᴏᴛᴢ</a>
"""

    SEND_METADATA = """
❪ SET CUSTOM METADATA ❫

☞ Fᴏʀ Exᴀᴍᴘʟᴇ:-

◦ <code> -map 0 -c:s copy -c:a copy -c:v copy -metadata title="Powered By:- @KGN_BOTZ" -metadata author="@KGN_BOTZ" -metadata:s:s title="Subtitled By :- @KGN_BOTZ" -metadata:s:a title="By :- @KGN_BOTZ" -metadata:s:v title="By:- @KGN_BOTZ" </code>

📥 Fᴏʀ Hᴇʟᴘ Cᴏɴᴛ. @ExE_AQUIB
"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱➜
➜ 🗃️ sɪᴢᴇ: {1} | {2}
➜ ⏳️ ᴅᴏɴᴇ : {0}%
➜ 🚀 sᴘᴇᴇᴅ: {3}/s
➜ ⏰️ ᴇᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➜ </b>"""
