from pyrogram import Client as app, filters
import asyncio
from utils.github import download_project, gpaan
from utils.errors import command_error, custom_error
from utils.emojis import emojis
from utils.parse import rsfp
import os
import shutil
import subprocess
import traceback



@app.on_message(filters.command(["lm", "dm"], prefixes=".") & filters.me)
async def MAIN_load_custom_module(app, msg):
	if len(msg.text.split()) == 1:
		return await command_error(msg, ".lm")
	text = msg.text[4:]
	if (text.startswith("https://github.com") and text.count("/") >= 4) or (text.startswith("github.com") and text.count("/") >= 2):
		await msg.edit(f"{emojis['⌛️ loading']} Installing the module...")
		if text.endswith(".git"):
			text = text[:-4]
		if text.startswith("github.com"):
			text = "https://" + text
		res = await download_project(text)
		print(res)
		if res[0] == 1:
			return await custom_error(msg, title="Module installation failed", exit_code=res[1]["exit_code"], description=res[1]["description"])

		if os.path.exists(f"{res[1]['project_folder']}/requirements.txt"):
			await msg.edit(f"{emojis['⌛️ loading']} Installing requirements...")
			try:
				subprocess.run(["pip", "install", "-r", f"{res[1]['project_folder']}/requirements.txt"])
			except:
				return await custom_error(msg, title="The module was installed, but an error occurred when installing the requirements", description=await rsfp(traceback.format_exc()))

		await msg.edit(f"{emojis['✔️']} The <b><i>'{await rsfp(res[1]['project_name'])}'</i></b> module <i>(by {await rsfp(res[1]['project_author'])})</i> has been installed!\n{emojis['⌛️ loading']} Restarting milFA...")
		app.running = True
		app.restarting_message = {"msg_id": msg.id, "chat_id": msg.chat.id}
		with open("switch.txt", "w") as f:
			f.write(f"""
startline1::: running = {app.running} :::endline1
startline2::: restarting_message = {app.restarting_message} :::endline2
""")
		asyncio.create_task(app.stop())
		exit(0)
	else:
		return await command_error(msg, ".lm")




@app.on_message(filters.command(["rlm", "rdm"], prefixes=".") & filters.me)
async def MAIN_reload_custom_module(app, msg):
	if len(msg.text.split()) == 1:
		return await command_error(msg, ".rlm")
	text = msg.text[5:]
	if (text.startswith("https://github.com") and text.count("/") >= 4) or (text.startswith("github.com") and text.count("/") >= 2):
		await msg.edit(f"{emojis['⌛️ loading']} Reinstalling the module...")
		if text.endswith(".git"):
			text = text[:-4]
		if text.startswith("github.com"):
			text = "https://" + text
		res = await gpaan(text)
		if res[0] == 1:
			return await custom_error(msg, title="Module reinstallation failed", exit_code=res[1]["exit_code"], description=res[1]["description"])

		project_author = res[1]["project_author"]
		project_name = res[1]["project_name"]

		folder_path = f"modules/{project_author} - {project_name}"
		if os.path.isdir(folder_path):
			try:
				subprocess.run(['rmdir', '/s', '/q', folder_path.replace("/", "\\")], shell=True)
			except Exception as e:
				return await custom_error(msg, title="Module reinstallation failed", description=str(e))
		

		res = await download_project(text)
		if res[0] == 1:
			return await custom_error(msg, title="Module reinstallation failed", exit_code=res[1]["exit_code"], description=res[1]["description"])

		if os.path.exists(f"{res[1]['project_folder']}/requirements.txt"):
			await msg.edit(f"{emojis['⌛️ loading']} Installing requirements...")
			try:
				subprocess.run(["pip", "install", "-r", f"{res[1]['project_folder']}/requirements.txt"])
			except:
				return await custom_error(msg, title="The module was installed, but an error occurred when installing the requirements", description=await rsfp(traceback.format_exc()))

		await msg.edit(f"{emojis['✔️']} The <b><i>'{await rsfp(res[1]['project_name'])}'</i></b> module <i>(by {await rsfp(res[1]['project_author'])})</i> has been reinstalled!\n{emojis['⌛️ loading']} Restarting milFA...")
		app.running = True
		app.restarting_message = {"msg_id": msg.id, "chat_id": msg.chat.id}
		with open("switch.txt", "w") as f:
			f.write(f"""
startline1::: running = {app.running} :::endline1
startline2::: restarting_message = {app.restarting_message} :::endline2
""")
		asyncio.create_task(app.stop())
		exit(0)
	else:
		return await command_error(msg, ".rlm")




@app.on_message(filters.command(["ulm", "udm"], prefixes=".") & filters.me)
async def MAIN_unload_custom_module(app, msg):
	if len(msg.text.split()) == 1:
		return await command_error(msg, ".ulm")
	text = msg.text[5:]
	if (text.startswith("https://github.com") and text.count("/") >= 4) or (text.startswith("github.com") and text.count("/") >= 2):
		await msg.edit(f"{emojis['⌛️ loading']} Uninstalling the module...")
		if text.endswith(".git"):
			text = text[:-4]
		if text.startswith("github.com"):
			text = "https://" + text
		res = await gpaan(text)
		if res[0] == 1:
			return await custom_error(msg, title="Module uninstallation failed", exit_code=res[1]["exit_code"], description=res[1]["description"])

		project_author = res[1]["project_author"]
		project_name = res[1]["project_name"]

		folder_path = f"modules/{project_author} - {project_name}"
		if not os.path.isdir(folder_path):
			return await custom_error(msg, title="Module uninstallation failed", description="The module not found.")
		
		try:
			subprocess.run(['rmdir', '/s', '/q', folder_path.replace("/", "\\")], shell=True)
		except Exception as e:
			return await custom_error(msg, title="Module uninstallation failed", description=str(e))
		
		await msg.edit(f"{emojis['✔️']} The <b><i>{await rsfp(res[1]['project_name'])}</i></b> module <i>(by {await rsfp(res[1]['project_author'])})</i> has been uninstalled!\n{emojis['⌛️ loading']} Restarting milFA...")
		app.running = True
		app.restarting_message = {"msg_id": msg.id, "chat_id": msg.chat.id}
		with open("switch.txt", "w") as f:
			f.write(f"""
startline1::: running = {app.running} :::endline1
startline2::: restarting_message = {app.restarting_message} :::endline2
""")
		asyncio.create_task(app.stop())
		exit(0)
	elif " - " in text:
		await msg.edit(f"{emojis['⌛️ loading']} Uninstalling the module...")

		folder_path = f"modules/{text}"
		if not os.path.isdir(folder_path):
			return await custom_error(msg, title="Module uninstallation failed", description="The module not found.")
		
		print(['rmdir', '/s', '/q', folder_path.replace("/", "\\")])
		try:
			subprocess.run(['rmdir', '/s', '/q', folder_path.replace("/", "\\")], shell=True)
		except Exception as e:
			return await custom_error(msg, title="Module uninstallation failed", description=str(e))

		await msg.edit(f"{emojis['✔️']} The <i>'{await rsfp(text.split(' - ')[1])}'</i> module <i>(by {await rsfp(text.split(' - ')[0])})</i> has been uninstalled!\n{emojis['⌛️ loading']} Restarting milFA...")
		app.running = True
		app.restarting_message = {"msg_id": msg.id, "chat_id": msg.chat.id}
		with open("switch.txt", "w") as f:
			f.write(f"""
startline1::: running = {app.running} :::endline1
startline2::: restarting_message = {app.restarting_message} :::endline2
""")
		asyncio.create_task(app.stop())
		exit(0)
	else:
		return await command_error(msg, ".ulm")