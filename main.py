import time
import asyncio
from flask import Flask
import os
import asyncio


import threading
import time


class ThreadingExample(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    until the application exits.
    """

    def __init__(self, interval=1):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.interval = interval

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution
        print('startuju')

    def run(self):
        """ Method that runs forever """
        while True:
            # Do something
            print('foooooooooooo')
            os.system('python3 examples/like_and_follow_last_user_media_likers.py')
            time.sleep(5)

print('startuju script')
example = ThreadingExample()
print('startuju flask')
app = Flask(__name__)
# Bind to PORT if defined, otherwise default to 5000.
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
