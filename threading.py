import threading
import time

def thread_worker():
    print('my thread has entered the "running" state')

    #Not running state
    time.sleep(10)

    print('My thread is terminating')

myThread = threading.Thread(target=thread_worker)

myThread.start()

myThread.join()

