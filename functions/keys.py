from functions import directkeys
import time

def press(k):
    if type(k) == int:
        directkeys.PressKey(k)
        time.sleep(0.01)
        directkeys.ReleaseKey(k)
    else:
        for j in k:
            directkeys.PressKey(j)
            time.sleep(0.01)
            directkeys.ReleaseKey(j)
            time.sleep(0.05)

UP = 0xC8
DOWN = 0xD0
LEFT = 0xCB
RIGHT = 0xCD
ENTER = 0x1C
SPACE = 0x39