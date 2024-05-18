from pyrogram import Client as app, filters
from utils.emojis import emojis
from utils.errors import command_error


@app.on_message(filters.command("serrors", prefixes=".") & filters.me)
async def MAIN_settings_errors_show(app, msg):
	split = msg.text.lower().split()
	if len(split) == 1:
		with open("modules/settings/errors.txt", "r") as f:
			text = f.read()
			interval = int(text.split("startline1::: ")[1].split(" :::endline1")[0].split(" = ")[1])
			delete = eval(text.split("startline2::: ")[1].split(" :::endline2")[0].split(" = ")[1])
		return await msg.edit(f"""
<b><i>{emojis['⚙️']} Setting: Errors</i></b>
{emojis['⏳ waiting']} Interval: <b><i>{interval}</i></b>
{emojis['🗑']} Delete: <b><i>{delete}</i></b>
""")
	elif len(split) == 2:
		if split[1] == "interval":
			with open("modules/settings/errors.txt", "r") as f:
				text = f.read()
				interval = int(text.split("startline1::: ")[1].split(" :::endline1")[0].split(" = ")[1])
			return await msg.edit(f"""
<b><i>{emojis['⚙️']} Setting: Errors</i></b>
{emojis['⏳ waiting']} Interval: <b><i>{interval}</i></b>
""")

		elif split[1] == "delete":
			with open("modules/settings/errors.txt", "r") as f:
				text = f.read()
				delete = eval(text.split("startline2::: ")[1].split(" :::endline2")[0].split(" = ")[1])
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
		with open("modules/settings/errors.txt", "r") as f:
			lines = f.readlines()
		lines[1] = f"startline1::: interval = {interval} :::endline1\n"
		with open("modules/settings/errors.txt", "w", encoding='utf-8') as f:
			f.write(''.join(lines))
		await msg.edit(f"{emojis['✔️']} Errors interval has been updated: <b><i>{interval} s</i></b>")
	
	elif split[0] == "delete":
		if not split[1] == "true" and not split[1] == "false":
			return await command_error(msg, ".serrors delete")
		if split[1] == "true":
			delete = True
		elif split[1] == "false":
			delete = False
		with open("modules/settings/errors.txt", "r") as f:
			lines = f.readlines()
		lines[2] = f"startline2::: delete = {delete} :::endline2\n"
		print(lines)
		with open("modules/settings/errors.txt", "w", encoding='utf-8') as f:
			f.write(''.join(lines))
		await msg.edit(f"{emojis['✔️']} Errors deleting has been updated: <b><i>{delete}</i></b>")
	else:
		return await command_error(msg, ".serrors")