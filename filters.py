from pyrogram.filters import Filter

class Text(Filter):
	def __init__(self, equals=None, startswith=None, contains=None, endswith=None, ignore_case=True):
		self.equals = equals
		self.startswith = startswith
		self.contains = contains
		self.endswith = endswith
		self.ignore_case = ignore_case

	def case(self, text):
		if self.ignore_case:
			return text.lower()
		return text

	async def __call__(self, _, message):
		result = []
		try:
			if self.ignore_case:
				text = message.text.lower()
			else:
				text = message.text

			if self.equals != None:
				if type(self.equals) != list:
					self.equals = [self.equals]
				result.append(any(text == self.case(part) for part in self.equals))

			if self.startswith != None:
				if type(self.startswith) != list:
					self.startswith = [self.startswith]
				result.append(any(text.startswith(self.case(part)) for part in self.startswith))

			if self.contains != None:
				if type(self.contains) != list:
					self.contains = [self.contains]
				result.append(any(self.case(part) in text for part in self.contains))

			if self.endswith != None:
				if type(self.endswith) != list:
					self.endswith = [self.endswith]
				result.append(any(text.endswith(self.case(part)) for part in self.endswith))

			if self.equals == None and self.startswith == None and self.contains == None and self.endswith == None:
				raise TypeError("'Text' filter must contain at least one argument [equals|startswith|contains|endswith]")
		except Exception as e:
			print(e)

		if False in result or len(result) == 0:
			return False
		else:
			return True


class Command(Filter):
	def __init__(self, command, prefixes=["/"], ignore_mention=False, ignore_case=True):
		self.command = command
		self.prefixes = prefixes
		self.ignore_mention = ignore_mention
		self.ignore_case = ignore_case

	def case(self, text):
		if self.ignore_case:
			return text.lower()
		return text

	async def __call__(self, _, message):
		if type(self.command) != list:
			self.command = [self.command]
		
		if not (self.prefixes == None or self.prefixes == "None"):
			_command = self.command
			__command = []
			for prefix in self.prefixes:
				for command in _command:
					if prefix == " ":
						prefix = ""
					__command.append(self.case(f"{prefix}{command}"))
		else:
			__command = []
			for command in self.command:
				__command.append(self.case(command))
		
		command = self.case(message.text)
		
		if not self.ignore_mention and str(message.chat.type) != "ChatType.PRIVATE":
			if (not command.split()[0].lower().endswith("@chapcha2_chat_bot")) and "@" in command.split()[0]:
				return False
			elif command.split()[0].lower().endswith("@chapcha2_chat_bot"):
				command = command.split()
				command[0] = command[0][:command[0].lower().find("@chapcha2_chat_bot")]
		elif command.split()[0].lower().endswith("@chapcha2_chat_bot"):
			command = command.split()
			command[0] = command[0][:command[0].lower().find("@chapcha2_chat_bot")]
		
		if type(command) != list:
			command = command.split()

		if command[0] in __command:
			return True
		else:
			return False
