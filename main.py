from pyrogram import Client, filters, enums, idle
import datetime
import asyncio
from config import api_id, api_hash, owner_id
from utils.emojis import emojis

if api_id == "None" or api_id == None:
	print("""ERROR
Please enter your api id in config.py
If you don't have an api id, visit https://core.telegram.org/api/obtaining_api_id
""")

if api_hash == "None" or api_hash == None:
	print("""ERROR
Please enter your api hash in config.py
If you don't have an api hash, visit https://core.telegram.org/api/obtaining_api_id
""")

if (api_id == "None" or api_id == None) or (api_hash == "None" or api_hash == None):
	exit(1)


app = Client("milFA", api_id, api_hash, plugins=dict(root="modules"))
app.set_parse_mode(enums.ParseMode.HTML)

with open("switch.txt", 'r') as f:
	switch = f.read()
	app.running = eval(switch.split("startline1::: ")[1].split(" :::endline1")[0].split(" = ")[1])
	app.restarting_message = eval(switch.split("startline2::: ")[1].split(" :::endline2")[0].split(" = ")[1])

app.start()
if app.restarting_message == None:
	app.send_message("me", f"{emojis['✔️']} milFA has been switched on")
else:
	try:
		app.edit_message_text(chat_id=app.restarting_message["chat_id"], message_id=app.restarting_message["msg_id"], text=f"{emojis['✔️']} milFA has been restarted")
	except:
		app.send_message("me", f"{emojis['✔️']} milFA has been restarted")

idle()

app.send_message("me", f"{emojis['❌']} milFA has been switched off")

app.stop()
exit(1)