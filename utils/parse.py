async def rsfp(text) -> str: # replace symbols for parse
	return str(text).replace('>', '&gt;').replace('<', '&lt;')