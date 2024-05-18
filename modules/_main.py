from pyrogram import Client as app, filters
from utils.emojis import emojis


@app.on_message(filters.command("set_id", prefixes=".") & filters.me)
async def MAIN_set_owner_id(app, msg):
	me = await app.get_me()
	with open("config.py", "r", encoding='utf-8') as f:
		lines = f.readlines()
	lines[2] = f"owner_id = {me.id}"
	with open("config.py", "w", encoding='utf-8') as f:
		f.write(''.join(lines))
	
	emoji = emojis["✔️"]
	await msg.edit(f"{emoji} ID has been set! (<code>{me.id}</code>)")