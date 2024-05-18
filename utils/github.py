import os
import shutil
from git import Repo
from urllib.parse import urlparse
import traceback



async def gpaan(url) -> tuple: # get project author and name
	try:
		parsed_url = urlparse(url)
		path_parts = parsed_url.path.strip("/").split("/")
		author = path_parts[0]
		project_name = path_parts[1]
		return (0, {"project_author": author, "project_name": project_name})
	except Exception as e:
		return (1, str(e))


async def download_project(url) -> tuple:
	try:
		res = await gpaan(url)
		print(res)
		if res[0] == 1:
			return res

		project_author = res[1]["project_author"]
		project_name = res[1]["project_name"]

		project_folder = os.path.join("modules", f"{project_author} - {project_name}")
		os.makedirs(project_folder, exist_ok=True)
		
		Repo.clone_from(url, project_folder)
		await remove_ignored_files(project_folder)
		return (0, {"project_author": project_author, "project_name": project_name, "project_folder": project_folder})
	except Exception as e:
		try:
			return (1, {"exit_code": e.args[1], "description": str(e.args[2])[2:-3]})
		except:
			return (1, {"exit_code": 1, "description": str(e)})



async def remove_ignored_files(destination_path):
	try:
		if not os.path.exists(f"{destination_path}/.gitignore"):
			return
		with open(f"{destination_path}/.gitignore", "r", encoding='utf-8') as f:
			ignored_files = f.read().split("\n")
		
		ignored_files = list(filter(lambda x: x != "", ignored_files))
		ignored_files = list(filter(lambda x: x != " ", ignored_files))

		for ignored_file in ignored_files:
			print(ignored_file)
			try:
				ignored_file_path = os.path.join(destination_path, ignored_file)
				if os.path.exists(ignored_file_path):
					if os.path.isdir(ignored_file_path):
						shutil.rmtree(ignored_file_path)
					else:
						os.remove(ignored_file_path)
			except:
				print(traceback.format_exc())
		os.remove(f"{destination_path}/.gitignore")
	except:
		print(traceback.format_exc())