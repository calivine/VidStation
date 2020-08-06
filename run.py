from video import Clip
import sys


source = sys.argv[1]
start = sys.argv[2]
end = sys.argv[3]

clip = Clip(source, start, end)

clip.save('test.mp4')
