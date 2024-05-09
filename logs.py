from sys import platform
from os import environ, path

hackmudDir = ""
if platform == "win32":
    hackmudDir = path.join(environ["APPDATA"],"hackmud")
elif platform == "linux":
    hackmudDir = path.join(path.expanduser("~"),"/.config/hackmud/")

shelltxt = path.join(hackmudDir, "shell.txt")