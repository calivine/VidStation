from bot import TwitterBot
from message import Message
from config import *
from pathlib import Path
from timer import Timer
import os
import subprocess

MAX_SIZE = 3072

bot = TwitterBot(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

os.chdir('media')

# Delete any '.DS_Store files'
subprocess.run(["find", ".", "-name", ".DS_Store", "-delete"])

for gif in os.listdir('.'):
    # Get the size of the file
    gif_size = (Path(gif).stat().st_size) // 1000
    print("{} ({} kb)".format(gif, gif_size))

    if os.path.isdir(gif):
        print("Not a .GIF, skipping.")
    elif gif_size > MAX_SIZE:
        print("File size is over limit by {} kb".format(gif_size - MAX_SIZE))
        # Move file to Resize folder.
        print("Moving {:s} to resize directory\n".format(gif))
        os.rename(gif, os.path.join("resize", gif))
    else:
        bot.tweet(Message().body, gif)

        print("Tweet sent.\nMoving {:s}".format(gif))

        os.rename(gif, os.path.join("posted", gif))

        Timer.sleep()
