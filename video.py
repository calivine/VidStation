from moviepy.editor import *


class Clip:


    def __init__(self, source, start=None, end=None):
        """Create a Clip of a Video.

        Parameters
        -------------
        source:String,
            Source file or path.
        start:Integer,
            Starting position of clip in seconds.
        end:Integer,
            Ending position of clip in seconds.
        """
        self.source = source
        self.clip = VideoFileClip(source).subclip((start),(end))

    def save(self, dest):
        """Save Clip of a Video file

        Parameters
        -------------
        dest:String,
            Destination file or path.
        """
        self.clip.write_videofile(dest, bitrate="3000k")
