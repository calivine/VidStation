from video import Clip, Webm, GIF, VideoEditor
from config import *
from ioparse import Parser

import sys
import os
import random

p = Parser().get_args()

# source = p.source
source = sys.argv[1]+'.mp4'
start = None
end = None

"""
if p.start is not None:
    if ':' in p.start:
        ts = p.start.split(':')
        start = int(ts[0]) * 60 + int(ts[1])
    if ':' in p.end:
        ts = p.end.split(':')
        end = int(ts[0]) * 60 + int(ts[1])
"""
# Move Into Video Source Directory
os.chdir(SOURCE_DIR)

if p.auto:
    source_file = Clip(source)
    timestamps = source_file.make_time_stamps(int(p.length[0]), int(p.length[1]), int(p.length[2]))
    to_be_processed = []
    for c in timestamps:
        new_clip = Clip(source, c[0], c[1])
        to_be_processed.append(new_clip.clip)

    ve = VideoEditor()
    source = "comp{}_{}".format(str(random.randint(1, 10000)), source)
    print(source)
    ve.paste_clips(source, to_be_processed)
if p.gif:
    if p.start is not None:
        GIF(source, start, end)
    else:
        GIF(source)
if p.webm:
    if p.start is not None:
        print(source)
        Webm(source, start, end)
    else:
        Webm(os.path.join('clips', source))

"""

    # Clip source video at start and end points provided in Clips list.
    # append to video clip list to be provided to method which concatenates into one video.
        Clip()

"""
if p.clips is not None:
    clip_list = []
    print(p.clips)
    clip_list_raw = p.clips[1:-1]
    print(clip_list_raw)
    cll = clip_list_raw.split(",")
    print(cll)
    cll.reverse()
    print(cll)

    st = True
    while len(cll) > 0:
        ts = cll.pop()
        if st:
            start = ts
            st = False
        else:
            end = ts
            st = True
            clip_list.append([start, end])
    print(clip_list)
    to_be_processed = []
    for c in clip_list:
        print(c)
        new_clip = Clip(source, c[0], c[1])
        to_be_processed.append(new_clip.clip)
        print(new_clip)
        print(to_be_processed)
    ve = VideoEditor()
    ve.paste_clips("comp_{}".format(source), to_be_processed)
