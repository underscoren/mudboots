from pygtail import Pygtail
from autokey import sendkeys
from time import sleep, time
import logs
import re

shellLogOffset = "shell.txt.offset"

# ignore logs previously unread
def skipLog():
    if len(shellLogOffset) > 0:
        temp = Pygtail(logs.shelltxt, offset_file=shellLogOffset)
        temp.read()
        temp.update_offset_file()

# force a flush and read the logs
def getLogs():
    rawLog = ""
    cleanLog = ""

    xmlre = re.compile(r"</?color(?:=#\w+)?>")

    sendkeys("flush")


    start = time()
    timeout = 10 #10s timeout

    while True:
        if (time() - start) > timeout:
            raise TimeoutError("Command processing exceeded 10s")

        sendkeys("\n")
        sleep(0.1)

        tail = Pygtail(logs.shelltxt, offset_file=shellLogOffset)
        ignoreNext = False
        for line in tail:
            #print(repr(line))
            rawLog += line
            
            # ignore autocomplete
            if line in "<color=#9B9B9BFF>-autocompletes added-</color>\n": 
                continue

            # ignore this and the next line
            if line == "Window contents have been written to disk successfully.\n":
                ignoreNext = True
                continue

            if ignoreNext:
                ignoreNext = False
                continue

            if line == "<color=#FFFFFFFF>>><color=#9B9B9BFF>flush</color></color>":
                tail.read()
                tail.update_offset_file()
                return (rawLog, cleanLog)

            cleanLog += xmlre.sub("", line)

# Sends the command and returns the response from the server
# manually flushes after the command is sent to force contents to be saved
def sendCommand(command: str):
    skipLog()
    sendkeys(command + "\n")
    sleep(0.25)
    return getLogs()
    
# enters hadline by bruteforcing the address
def enter_hardline():
    skipLog()
    sendkeys("kernel.hardline\n")
    sleep(12)
    
    for _ in range(3*4):
        sendkeys("0123456789")
        sleep(0.1)
    
    sleep(12)
    return getLogs()
