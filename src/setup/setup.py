import json
import os
from shutil import copytree, rmtree


with open("./setup.json", "r", encoding="utf-8") as f:
	settings = json.loads(f.read())
p = settings["path"].replace(r"%appdata%", os.getenv('APPDATA'))

if not os.path.exists(p):
	os.makedirs(p)

with open(p+"\\Tezuem.exe", "wb") as f:
	with open("./files/tezuem.exe", "rb") as g:
		f.write(g.read())

if not os.path.exists(os.getenv("APPDATA")+"\\Tezuem"):
	os.makedirs(os.getenv("APPDATA")+"\\Tezuem")
with open(os.getenv("APPDATA")+"\\Tezuem\\path", "w") as f:
	f.write(p)

if os.path.exists(p+"\\libs"):
	rmtree(p+"\\libs")
copytree("./libs", p+"\\libs")

