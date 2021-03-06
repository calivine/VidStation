from gif import GIFFactory
import sys


if len(sys.argv) > 3:
    path = sys.argv[1]
    start = sys.argv[2]
    end = sys.argv[3]
    scale = sys.argv[4]
    fps = sys.argv[5]
    GIFFactory.make_gif(src=path, set=[int(start), int(end)], resize=int(scale), fps=int(fps))
elif len(sys.argv) == 3:
    path = sys.argv[1]
    scale = sys.argv[2]
    GIFFactory.make_gif(path, int(scale))
else:
    print("Usage: python make_gif.py PATH SCALE START END FPS")
