import sqlite3

async def connect(database="database.db", get_cursor=True):
	database = sqlite3.connect(database)
	if get_cursor:
		cursor = database.cursor()
		return (database, cursor)
	return database


async def restore_settings():
	db, cursor = await connect()
	cursor.execute("INSERT INTO settings VALUES (?, ?)", (3, 'True'))
	db.commit()
	db.close()
	return (3, 'True')


async def get_settings(settings):
	db, cursor = await connect()
	if settings == "errors" or settings == "error":
		result = cursor.execute(f"SELECT errors_interval, errors_delete FROM settings").fetchone()
		if result is None:
			result = await restore_settings()

	db.close()
	return result