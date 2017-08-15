"""
    instabot example

    Workflow:
        Like and follow users who liked the last media of input users.
"""

import sys
import os
from tqdm import tqdm
import argparse
from os import environ
from flask import Flask

app = Flask(__name__)
app.run(environ.get('PORT'))


sys.path.append(os.path.join(sys.path[0], '../'))
from instabot import Bot

bot = Bot()
bot.login(username='petrju123456', password='testovaciucet',
          proxy=None  )

for username in ['pauliegarand']:
    medias = bot.get_user_medias(username, filtration=False)
    if len(medias):
        likers = bot.get_media_likers(medias[0])
        for liker in tqdm(likers):
            print(bot.like_user(liker, amount=2))
            print('foooo')
            bot.follow(liker)
