from functions import directkeys
import time

def press(app, k):
    if type(k) == int:
        directkeys.PressKey(k)
        time.sleep(app.config['keyHold'])
        directkeys.ReleaseKey(k)
    else:
        for j in k:
            directkeys.PressKey(j)
            time.sleep(app.config['keyHold'])
            directkeys.ReleaseKey(j)
            time.sleep(app.config['keyWait'])

UP = 0xC8
DOWN = 0xD0
LEFT = 0xCB
RIGHT = 0xCD
ENTER = 0x1C
SPACE = 0x39