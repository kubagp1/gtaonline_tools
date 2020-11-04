import psutil, time

def execute(process):
    process.suspend()
    time.sleep(10)
    process.resume()