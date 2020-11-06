import time

from functions.keys import press, UP, DOWN, LEFT, RIGHT, ENTER, SPACE

def execute(app):
    press(app, UP)
    time.sleep(app.config['phonePullWait'])
    press(app, [UP, RIGHT, ENTER, SPACE, RIGHT, RIGHT, ENTER, RIGHT, DOWN, ENTER, LEFT, ENTER, LEFT, ENTER, ENTER, ENTER, DOWN, DOWN, ENTER, DOWN, LEFT, ENTER, UP, RIGHT, ENTER, DOWN, ENTER, SPACE])