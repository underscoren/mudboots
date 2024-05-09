from xdo import Xdo
import os

xdo = Xdo()

windowID = None

def init():
    global windowID

    windowID = xdo.search_windows(b"hackmud")

    if windowID == None or len(windowID) < 1:
        raise Exception("Cannot find hackmud window")

    if len(windowID) > 1:
        print("Warning: multiple windows titled \"hackmud\" detected. Selecting the first one")
    
    windowID = windowID[0]

def sendkeys(keys: str):
    # workaround for https://github.com/jordansissel/xdotool/issues/150
    os.system("xdotool key --clearmodifiers shift")

    if "\n" in keys:
        chunks = keys.split("\n")
        
        for (i,chunk) in enumerate(chunks):
            if len(chunk):
                xdo.enter_text_window(window=windowID, string=chunk.encode())
            
            if i != (len(chunks)-1): # ignore last chunk
                xdo.send_keysequence_window(window=windowID, keysequence="Return".encode())
    else:
        xdo.enter_text_window(window=windowID, string=keys.encode())
