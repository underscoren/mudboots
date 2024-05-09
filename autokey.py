from sys import platform

if platform == "win32":
    import windows.window as inputHandler
elif platform == "linux":
    import linux.window as inputHandler
else:
    raise NotImplementedError("Unsupported platform "+platform)

inputHandler.init()

def sendkeys(keys: str):
    inputHandler.sendkeys(keys)