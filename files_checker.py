import os

if not os.path.exists("switch.txt"):
	with open("switch.txt", "w") as f:
		f.write("")


default_text = """
startline1::: interval = 3 :::endline1
startline2::: delete = True :::endline2
"""

try:
	with open("modules/settings/errors.txt", "r") as f:
		text = f.read()
		interval = int(text.split("startline1::: ")[1].split(" :::endline1")[0].split(" = ")[1])
		if interval < 0:
			error(error)
		delete = eval(text.split("startline2::: ")[1].split(" :::endline2")[0].split(" = ")[1])
		if delete != True and delete != False:
			error(error)
except:
	with open("modules/settings/errors.txt", "w") as f:
		f.write(default_text)