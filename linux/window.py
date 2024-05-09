from xdo import Xdo

xdo = Xdo()

windowID = None

def init():
    global windowID

    windowID = xdo.search_windows(b"hackmud")

    if len(windowID) < 1:
        raise Exception("Cannot find window")

    if len(windowID) > 1:
        print("Warning: multiple windows titled \"hackmud\" detected. Selecting the first one")
    
    windowID = windowID[0]

def sendkeys(keys: str):
    if "\n" in keys:
        chunks = keys.split("\n")
        
        for (i,chunk) in enumerate(chunks):
            if len(chunk):
                xdo.enter_text_window(window=windowID, string=chunk)
            
            if i != (len(chunks)-1): # ignore last chunk
                xdo.send_keysequence_window(window=windowID, keysequence="XK_Linefeed")
    else:
        xdo.enter_text_window(window=windowID, string=keys)
