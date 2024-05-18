import asyncio
from .emojis import emojis
from .parse import rsfp

commands = {
".lm": ".lm <i>github project link</i>",
".rlm": ".rlm <i>github project link</i>",
".ulm": ".ulm <i>github project link / project author - project name</i>",
".mi": ".mi <i>github project link / project author - project name</i>",
".serrors": ".serrors [interval|delete] [option]",
".serrors interval": ".serrors interval <i>Seconds (0+)</i>",
".serrors delete": ".serrors delete [True|False]"
}

custom_commands = {
# custom commands dict
# it was created just to be
#         ¯\_(ツ)_/¯
# if you have no ideas for using it
}

async def create_error(title=None, exit_code=None, description=None):
	res = ""
	if title != None:
		res += f"<b>{emojis['🚫']} {title}</b>"
	if exit_code != None:
		res += f"\n{emojis['⛔️']} Exit code: <code>{exit_code}<code>"
	if description != None:
		res += f"\n{emojis['⚠️ red']} <code>{await rsfp(description)}</code>"
	return res



async def command_error(msg, command):
	with open("modules/settings/errors.txt", "r") as f:
		text = f.read()
		interval = int(text.split("startline1::: ")[1].split(" :::endline1")[0].split(" = ")[1])
		delete = eval(text.split("startline2::: ")[1].split(" :::endline2")[0].split(" = ")[1])
	if interval > 0:
		emoji = emojis['🚫']
		error = commands[command]
		await msg.edit(f"{emoji} {error}")
		await asyncio.sleep(interval)
	if delete:
		await msg.delete()


async def custom_command_error(msg, command): # 17 ¯\_(ツ)_/¯ 19
	with open("modules/settings/errors.txt", "r") as f:
		text = f.read()
		interval = int(text.split("startline1::: ")[1].split(" :::endline1")[0].split(" = ")[1])
		delete = eval(text.split("startline2::: ")[1].split(" :::endline2")[0].split(" = ")[1])
	if interval > 0:
		emoji = emojis['🚫']
		if not command in custom_commands:
			error = command
		else:
			error = custom_commands[command]
		await msg.edit(f"{emoji} {error}")
		await asyncio.sleep(interval)
	if delete:
		await msg.delete()



async def custom_error(msg, text=None, title=None, exit_code=None, description=None):
	if text != None:
		error = text
	elif title != None or exit_code != None or description != None:
		error = await create_error(title, exit_code, description)
	else:
		raise TypeError("'custom_error' function must contain at least 2 arguments, counting 'msg' argument.")
	with open("modules/settings/errors.txt", "r") as f:
		file_text = f.read()
		interval = int(file_text.split("startline1::: ")[1].split(" :::endline1")[0].split(" = ")[1])
		delete = eval(file_text.split("startline2::: ")[1].split(" :::endline2")[0].split(" = ")[1])
	if interval > 0:
		await msg.edit(error)
		await asyncio.sleep(interval)
	if delete:
		await msg.delete()