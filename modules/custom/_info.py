from pyrogram import Client as app, filters
from pyrogram.types import InputMediaPhoto as IMImage, InputMediaVideo as IMVideo, \
		InputMediaAudio as IMAudio, InputMedia, InputMediaAnimation as IMAnimation, \
		InputMediaDocument as IMDocument
from utils.errors import custom_error, command_error
from utils.emojis import emojis
from utils.parse import rsfp
from utils.extensions import get as get_type
from utils.split import stbl, slbl
from utils.github import gpaan
import importlib.util
import os


@app.on_message(filters.command("mi", prefixes=".") & filters.me)
async def MAIN_module_info(app, msg):
	if len(msg.text.split()) == 1:
		return await command_error(msg, ".mi")
	text = msg.text[4:]
	if (text.startswith("https://github.com") and text.count("/") >= 4) or (text.startswith("github.com") and text.count("/") >= 2):
		if text.endswith(".git"):
			text = text[:-4]
		if text.startswith("github.com"):
			text = "https://" + text
		res = await gpaan(text)
		if res[0] == 1:
			return await custom_error(msg, exit_code=res[1]["exit_code"], description=res[1]["description"])

		project_author = res[1]["project_author"]
		project_name = res[1]["project_name"]

		folder_path = f"modules/{project_author} - {project_name}"
		if not os.path.exists(folder_path) and not os.path.isdir(folder_path):
			return await custom_error(msg, text=f"{emojis['⚠️ red']} <code>The module not found.</code>")

		
	elif " - " in text:
		folder_path = f"modules/{text}"
		if not os.path.exists(folder_path) and not os.path.isdir(folder_path):
			return await custom_error(msg, text=f"{emojis['⚠️ red']} <code>The module not found.</code>")
	else:
		return await command_error(msg, ".mi")
	file_path = f"{folder_path}/__init__.py"
	print(file_path)
	print(os.path.exists(file_path))
	if not os.path.exists(file_path):
		return await custom_error(msg, text=f"{emojis['⚠️ red']} <code>The module __init__ file not found.</code>")

	module_name = folder_path.split("/")[1]

	spec = importlib.util.spec_from_file_location(module_name, file_path)
	module = importlib.util.module_from_spec(spec)
	spec.loader.exec_module(module)
	
	module_attributes = dir(module)
	fullInfo = []
	fileInfo = []

	if "__fileInfo__" in module_attributes:
		if type(module.__fileInfo__) != list:
			fileInfo.append(module.__fileInfo__)
		else:
			fileInfo = module.__fileInfo__

	if "__fullInfo__" in module_attributes:
		if type(module.__fullInfo__) != list:
			fullInfo.append(module.__fullInfo__)
		else:
			fullInfo = module.__fullInfo__
	
	else:
		if "__info__" in module_attributes:
			fullInfo.append(f"{module.__info__}\n")

		if "__version__" in module_attributes:
			fullInfo.append(f"<b>Version:</b> <code>{module.__version__}</code>")
		
		if "__author__" in module_attributes:
			fullInfo.append(f"<b>Authors:</b> {module.__author__}")

		if "__releaseDate__" in module_attributes:
			fullInfo.append(f"<b>Release date:</b> <code>{module.__releaseDate__}</code>")

		if "__requirements__" in module_attributes:
			fullInfo.append(f"<b>Requirements:</b>\n<code>{module.__requirements__}</code>")

	if len(fullInfo) > 0 and len(fileInfo) > 0:
		await msg.edit(f"<b>{emojis['⌛️ loading']} {module_name} info loading...</b>")
		info_text = '\n'.join(fullInfo)

		media_group = []
		for file in fileInfo:
			if type(file) == str:
				if file.startswith("InputMedia") or file.startswith("IM"):
					if file.startswith("InputMedia"):
						file = "IM" + file[10:]
					_file = file.split("media=")[1].split(",")[0][1:-1]
					__file = _file

					if not __file.startswith(module_name):
						__file = module_name + "/" + __file
					if not __file.startswith("modules"):
						__file = "modules/" + __file

					media_group.append(eval(file.replace(_file, __file)))

				else:
					if not file.startswith(module_name):
						file = module_name + "/" + file
					if not file.startswith("modules"):
						file = "modules/" + file


					media_group.append(IMDocument(media=file))
			else:
				try:
					_file = file["file"]

					if not _file.startswith(module_name):
						_file = module_name + "/" + _file
					if not _file.startswith("modules"):
						_file = "modules/" + _file

					if "caption" in file:
						_caption = file["caption"]
					else:
						_caption = ""

					media_group.append(IMDocument(media=_file, caption=_caption))
				except:
					pass

		if len(info_text) > 4096:
			info_parts = await stbl(info_text, 4096)
		else:
			info_parts = [info_text]
		
		if len(media_group) > 10:
			media_parts = await slbl(media_group, 10)
		else:
			media_parts = media_group


		
		for part in info_parts:
			await msg.edit(f"<b>{emojis['ℹ️']} {module_name}\n{emojis['⌛️ loading']} 1. {info_parts.index(part)}/{len(info_parts)}...</b>")
			await app.send_message(chat_id=msg.chat.id, text=part)
		
		for part in media_parts:
			await msg.edit(f"<b>{emojis['ℹ️']} {module_name}\n{emojis['⌛️ loading']} 2. {media_parts.index(part)}/{len(media_parts)}...</b>")
			await app.send_media_group(chat_id=msg.chat.id, media=part)

		await msg.edit(f"<b>{emojis['ℹ️']} {module_name}</b>")


	
	elif len(fullInfo) == 0 and len(fileInfo) > 0:
		await msg.edit(f"<b>{emojis['⌛️ loading']} {module_name} info loading...</b>")
		
		media_group = []
		for file in fileInfo:
			if type(file) == str:
				if file.startswith("InputMedia") or file.startswith("IM"):
					if file.startswith("InputMedia"):
						file = "IM" + file[10:]
					_file = file.split("media=")[1].split(",")[0][1:-1]
					__file = _file

					if not __file.startswith(module_name):
						__file = module_name + "/" + __file
					if not __file.startswith("modules"):
						__file = "modules/" + __file

					media_group.append(eval(file.replace(_file, __file)))

				else:
					if not file.startswith(module_name):
						file = module_name + "/" + file
					if not file.startswith("modules"):
						file = "modules/" + file


					media_group.append(IMDocument(media=file))
			else:
				try:
					_file = file["file"]

					if not _file.startswith(module_name):
						_file = module_name + "/" + _file
					if not _file.startswith("modules"):
						_file = "modules/" + _file

					if "caption" in file:
						_caption = file["caption"]
					else:
						_caption = ""

					media_group.append(IMDocument(media=_file, caption=_caption))
				except:
					pass
		
		if len(media_group) > 10:
			media_parts = await slbl(media_group, 10)
		else:
			media_parts = media_group

		
		for part in media_parts:
			await msg.edit(f"<b>{emojis['ℹ️']} {module_name}\n{emojis['⌛️ loading']} 1. {media_parts.index(part)}/{len(media_parts)}...</b>")
			await app.send_media_group(chat_id=msg.chat.id, media=part)

		await msg.edit(f"<b>{emojis['ℹ️']} {module_name}</b>")

	elif len(fullInfo) > 0 and len(fileInfo) == 0:
		await msg.edit(f"<b>{emojis['⌛️ loading']} {module_name} info loading...</b>")
		info_text = '\n'.join(fullInfo)

		if len(info_text) > 4096:
			info_parts = await stbl(info_text, 4096)
		else:
			info_parts = [info_text]

		for part in info_parts:
			await msg.edit(f"<b>{emojis['ℹ️']} {module_name}\n{emojis['⌛️ loading']} 1. {info_parts.index(part)}/{len(info_parts)}</b>")
			await app.send_message(chat_id=msg.chat.id, text=part)

		await msg.edit(f"<b>{emojis['ℹ️']} {module_name}</b>")