async def stbl(text, length) -> list: # split text by length
	parts = []
	for i in range(0, len(text), length):
		parts.append(text[i:i+length])
	return parts


async def slbl(list, length) -> list: # split list by length
	parts = []
	for i in range(0, len(list), length):
		parts.append(list[i:i+length])
	return parts