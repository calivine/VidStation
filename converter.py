import cv2
import os
import random
import sys
from config import *

os.chdir(SOURCE_DIR)
v = None
if len(sys.argv) < 2:
    print("Usage: python app.py FILENAME")
    exit()
else:
    v = str(sys.argv[1])

count = 0
vidcap = cv2.VideoCapture(v)

success, image = vidcap.read()

fps = vidcap.get(cv2.CAP_PROP_FPS)
total_frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
markers = total_frames // 10
progress_marker = 0
print("Loading {} total frames.\nVideo FPS: {}".format(total_frames, round(fps, 1)))
os.chdir('C:')
os.chdir(OUTPUT_DIR)
img_dir = str(random.randint(1, 1000)) + "_" + str(round(fps, 1))
os.mkdir(img_dir)
os.chdir(img_dir)
while success:

    # zeroes = "0" * (8 - len(str(count)))
    frame = "frame{:s}{:d}.jpg".format("0" * (8 - len(str(count))), count)

    cv2.imwrite(frame, image)
    success, image = vidcap.read()
    count += 1
    if progress_marker >= markers:
        print("Reading frame: {}".format(vidcap.get(cv2.CAP_PROP_POS_FRAMES)))
        progress_marker = 0
    else:
        progress_marker += 1

print("Done.\n{:s} was created.".format(img_dir))
