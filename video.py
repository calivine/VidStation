from moviepy.editor import *
from config import *
import os


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
        self.clip = VideoFileClip(source).subclip((start), (end))

    def save(self, dest):
        """Save Clip of a Video file

        Parameters
        -------------
        dest:String,
            Destination file or path.
        """

        self.clip.write_videofile(dest, bitrate="3000k")


class Webm:

    def __init__(self, source, **kwargs):
        self.source = source
        self.video = VideoFileClip(source)
        self.fps = kwargs.pop("fps", "24")
        self.bitrate = kwargs.pop("bitrate", "3000k")
        self._save_webm()

    def _save_webm(self):
        self.video.write_videofile(self.source+'0.webm', fps=int(self.fps), bitrate=self.bitrate)


