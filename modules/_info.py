from pyrogram import Client as app, filters
from utils.emojis import emojis
from __init__ import __description__, __version__, __developers__, __chats__, __commands__

@app.on_message(filters.command(["info", "help"], prefixes=".") & filters.me)
async def MAIN_milFA_info(app, msg):
	chats = [chat.split(": ")[1] for chat in __chats__.split("\n")]
	e = f"</code>{emojis['🔼']}<code>"
	await msg.edit(f"""
<b>{emojis['ℹ️']} Info about milFA</b>
<i>{emojis['👀']} {__description__}</i>

<code>
{e}=============================={e}
{e}=======>>  VERSIION  <<======={e}
{e}==========>  </code><code>{__version__}</code><code>  <=========={e}
{e}=============================={e}
{e}=============================={e}
{e}======>>  DEVELOPERS  <<======{e}
{e}==>  </code><code>{__developers__}</code><code>  <=={e}
{e}=============================={e}
{e}=============================={e}
{e}=======>>  Telegram  <<======={e}
{e}===>  </code><code>{chats[0]}</code><code>  <==={e}
{e}=>  </code><code>{chats[1]}</code><code> <={e}
{e}===>  </code><code>{chats[2]}</code><code>  <==={e}
{e}=====>  </code><code>{chats[3]}</code><code>  <====={e}
{e}=============================={e}
</code>
""", disable_web_page_preview=True)



@app.on_message(filters.command("commands", prefixes=".") & filters.me)
async def MAIN_milFA_commands(app, msg):
	chats = [chat.split(": ")[1] for chat in __chats__.split("\n")]
	e = f"</code>{emojis['🔼']}<code>"
	await msg.edit(f"""
<b>{emojis['⚡️']} Built-in commands</b>
{__commands__}
""", disable_web_page_preview=True)