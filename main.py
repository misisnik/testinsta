import time
import asyncio
from flask import Flask
import os
import asyncio

app = Flask(__name__)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)


async def do_some_work(x):
    await os.system('python3 examples/like_and_follow_last_user_media_likers.py')

loop = asyncio.get_event_loop()
loop.run_until_complete(do_some_work(5))