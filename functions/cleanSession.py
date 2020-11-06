import psutil, time

def execute(app):
    app.process.suspend()
    time.sleep(app.config['sessionCleanTime'])
    app.process.resume()