from pyrogram import Client as app, filters
from utils.emojis import emojis
from utils.errors import command_error
from utils.db import connect, get_settings


@app.on_message(filters.command("serrors", prefixes=".") & filters.me)
async def MAIN_settings_errors_show(app, msg):
	split = msg.text.lower().split()
	if len(split) == 1:
		interval, delete = await get_settings("errors")
		return await msg.edit(f"""
<b><i>{emojis['⚙️']} Setting: Errors</i></b>
{emojis['⏳ waiting']} Interval: <b><i>{interval}</i></b>
{emojis['🗑']} Delete: <b><i>{delete}</i></b>
""")
	elif len(split) == 2:
		if split[1] == "interval":
			interval = (await get_settings("errors"))[0]
			return await msg.edit(f"""
<b><i>{emojis['⚙️']} Setting: Errors</i></b>
{emojis['⏳ waiting']} Interval: <b><i>{interval}</i></b>
""")

		elif split[1] == "delete":
			delete = (await get_settings("errors"))[1]
			return await msg.edit(f"""
<b><i>{emojis['⚙️']} Setting: Errors</i></b>
{emojis['🗑']} Delete: <b><i>{delete}</i></b>
""")

		else:
			return await command_error(msg, ".serrors")

	split = split[1:]
	if split[0] == "interval":
		if not split[1].isdigit():
			return await command_error(msg, ".serrors interval")
		elif int(split[1]) < 0:
			split[1] = "0"
		interval = int(split[1])
		db, cursor = await connect()
		cursor.execute(f"UPDATE settings SET errors_interval = {interval}")
		db.commit()
		db.close()
		await msg.edit(f"{emojis['✔️']} Errors interval has been updated: <b><i>{interval} s</i></b>")
	
	elif split[0] == "delete":
		if not split[1] == "true" and not split[1] == "false":
			return await command_error(msg, ".serrors delete")
		if split[1] == "true":
			delete = True
		elif split[1] == "false":
			delete = False
		db, cursor = await connect()
		cursor.execute(f"UPDATE settings SET errors_delete = '{delete}'")
		db.commit()
		db.close()
		await msg.edit(f"{emojis['✔️']} Errors deleting has been updated: <b><i>{delete}</i></b>")
	else:
		return await command_error(msg, ".serrors")