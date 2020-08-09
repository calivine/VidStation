from video import Clip, Webm
from gif import GIFFactory
import sys
import os
from config import *
import subprocess
from ioparse import Parser

p = Parser().get_args()
print(os.getcwd())
home = os.getcwd()

source = p.source
start = p.start
end = p.end

# Move Into Video Source Directory
os.chdir(SOURCE_DIR)

# Create Clip from Source, from Start to End.
clip = Clip(source, start, end)
# os.chdir(OUTPUT_DIR)
destination = '{}{}_c_{}'.format(start, end, source)

print(destination)
# Save Clip
clip.save(destination)

# Return back to Program's Location
os.chdir(home)

if p.sequence:
    subprocess.run(['python', 'converter.py', destination])

if p.gif:
    GIFFactory.make_gif()
elif p.webm:
    os.chdir(SOURCE_DIR)
    Webm(destination, fps=clip.fps, bitrate=clip.br)
