import os
from threading import Timer

def action():
    browserExe = "chrome.exe"
    os.system("taskkill /f /im " + browserExe)

t = Timer(3300.0, action)
t.start()