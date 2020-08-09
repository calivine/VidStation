from moviepy.editor import *
from config import *
import os


class Clip:

    bitrate = {
        '60.0': {
            '1080': '13000',
            '720': '6500',
            '540': '4500'
        },
        '30.0': {
            '1080': '7000',
            '720': '3500',
            '540': '2500'
        },
        '25.0': {
            '1080': '6500',
            '720': '3250',
            '540': '2250',
            '408': '2000'
        },
        '24.0': {
            '1080': '6000',
            '720': '3000',
            '540': '2000'
        }
    }

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
        print(self.clip.fps, self.clip.h)
        self.fps = round(self.clip.fps, 0)
        print(self.fps)
        self.br = self.bitrate[str(self.fps)][str(self.clip.h)] + 'k'

    def save(self, dest):
        """Save Clip of a Video file

        Parameters
        -------------
        dest:String,
            Destination file or path.
        """

        self.clip.write_videofile(dest, bitrate=self.br)


class Webm:

    def __init__(self, source, **kwargs):
        self.source = source
        self.video = VideoFileClip(source)
        self.fps = kwargs.pop("fps", "24")
        self.bitrate = kwargs.pop("bitrate", "3000k")
        self._save_webm()

    def _save_webm(self):
        self.video.write_videofile(self.source+'0.webm', fps=int(self.fps), bitrate=self.bitrate)
