from pyrogram import Client as app, filters
import asyncio
from utils.emojis import emojis


@app.on_message(filters.command(["stop_milfa", "off_milfa"], prefixes=".") & filters.me)
async def MAIN_stop_bot(app, msg):
	app.running = False
	asyncio.create_task(app.stop())
	await msg.edit(f"{emojis['❌']} milFA has been switched off")
	exit(1)


@app.on_message(filters.command("restart_milfa", prefixes=".") & filters.me)
async def MAIN_restart_bot(app, msg):
	app.running = True
	app.restarting_message = {"msg_id": msg.id, "chat_id": msg.chat.id}
	with open("switch.txt", "w") as f:
		f.write(f"""
startline1::: running = {app.running} :::endline1
startline2::: restarting_message = {app.restarting_message} :::endline2
""")
	await msg.edit(f"{emojis['⌛️ loading']} milFA is restarting...")
	asyncio.create_task(app.stop())
	exit(0)