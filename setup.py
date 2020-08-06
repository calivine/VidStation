import os
import subprocess


"""Installation file for setting up directory structure.
"""

media = 'media'
if os.path.exists('media'):
    print("Media directory already exists. Exiting.")
    exit()
else:
    if not os.path.exists(os.path.join(media, 'img')):
        os.makedirs(os.path.join(media, 'img/edited'))
    if not os.path.exists(os.path.join(media, 'resize')):
        os.mkdir(os.path.join(media, 'resize'))
    if not os.path.exists(os.path.join(media, 'posted')):
        os.mkdir(os.path.join(media, 'posted'))
