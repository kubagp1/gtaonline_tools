import time
import psutil
import keyboard

import logger, hotkeyManager

class App:
    def __init__(self):
        self.logger = logger.Logger(self)
        self.log = self.logger.log

        self.processName = "GTA5.exe"
        # self.processName = input()
        self.process = None
        while not self.process:
            self.logger.log("Searching for GTA5.exe process...")
            for proc in psutil.process_iter():
                if proc.name() == self.processName:
                    self.process = proc
                    self.logger.log("Found GTA5.exe process!")

        self.hotkeyManager = hotkeyManager.HotkeyManager(self)

        self.logger.log("GTA Online Toolkit v1.0 started!")
        self.logger.log("Press ctrl+q to quit.")
        keyboard.wait('ctrl+q')
        self.logger.log("Stopping...")

if __name__ == "__main__":
    app = App()