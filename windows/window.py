from pywinauto.application import Application
import re

app = None

def init():
    global app 
    app = Application().connect(title="hackmud", class_name="UnityWndClass")

def sendkeys(keys: str):
    if app is None:
        raise Exception("input handler not initialized")
    
    keys = re.sub(r"[{}]", lambda match: "{" + match.group() + "}", keys)
    keys = keys.replace("\n","{ENTER}") # pywinauto shorthand for enter key
    keys = keys.replace(" ", "{VK_SPACE}") # apparently spacebar needs to be manually escaped

    app.UnityWndClass.type_keys(keys)