from datetime import datetime

class Logger:
    def __init__(self, app):
        self.app = app
    
    def log(self, c):
        print('[{}] {}'.format(datetime.now().strftime("%d-%m-%Y %H:%M.%S"), c))