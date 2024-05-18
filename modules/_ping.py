from pyrogram import Client as app, filters
from datetime import datetime
from utils.emojis import emojis


@app.on_message(filters.command("ping", prefixes=".") & filters.me)
async def MAIN_ping(app, msg):
	start_time = datetime.now()
	await app.get_me()
	end_time = datetime.now()

	response_time = end_time - start_time
	await msg.edit(f"{emojis['⚡️']} Telegram response speed: <b><i>{round(response_time.total_seconds()*1000)} ms</i></b>")