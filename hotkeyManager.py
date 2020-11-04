import keyboard
from functionsList import *

class HotkeyManager:
    def __init__(self, app):
        self.app = app
        self.binds = [['insert+l', lambda: callLester.execute(), 'Calling Lester...', "Called Lester!"],
            ['insert+o', lambda: callPegasus.execute(), 'Calling Pegasus..', 'Called Pegasus!'],
            ['insert+k', lambda: callMechanic.execute(), 'Calling Mechanic...', "Called Mechanic!"],
            ['insert+0', lambda: cleanSession.execute(self.app.process), 'Cleaning Session...', "Cleaned session!"]]

        for bind in self.binds:
            keyboard.add_hotkey(bind[0], self.exec, args=[bind])

    def exec(self, b):
        self.app.log(b[2])
        b[1]()
        self.app.log(b[3])