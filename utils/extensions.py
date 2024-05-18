image = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".tiff", ".svg"]
video = [".mp4", ".mov", ".avi", ".wmv", ".mkv", ".flv", ".webm", ".3gp", ".mpeg"]
audio = [".mp3", ".wav", ".ogg", ".flac", ".aac", ".wma", ".m4a", ".opus"]
animation = [".gif", ".webp", ".apng"]
voice = [".ogg", ".opus", ".mp3", ".wav"]
video_note = [".mp4", ".webm"]


async def is_image(file):
	ext = "." + file.lower().split(".")[-1]
	return ext in image


async def is_video(file):
	ext = "." + file.lower().split(".")[-1]
	return ext in video


async def is_audio(file):
	ext = "." + file.lower().split(".")[-1]
	return ext in audio


async def is_animation(file):
	ext = "." + file.lower().split(".")[-1]
	return ext in animation


async def is_voice(file):
	ext = "." + file.lower().split(".")[-1]
	return ext in voice


async def is_video_note(file):
	ext = "." + file.lower().split(".")[-1]
	return ext in video_note


async def is_document(file):
	return not (is_image(file) or is_video(file) or is_audio(file) or is_animation(file) or is_voice(file) or is_video_note(file))



async def get(file):
	if await is_image(file):
		return "image"
	elif await is_video(file):
		return "video"
	elif await is_audio(file):
		return "audio"
	elif await is_animation(file):
		return "animation"
	elif await is_voice(file):
		return "voice"
	elif await is_video_note(file):
		return "video_note"
	else:
		return "document"