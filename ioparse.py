import optparse


class Parser:

    def __init__(self):
        self.p = optparse.OptionParser()
        self._load_options()
        self._set_defaults()

    def _load_options(self):
        self.p.add_option("-s", action="store", dest="source")
        self.p.add_option("--source", action="store", dest="source")
        self.p.add_option("-g", action="store", dest="gif")
        self.p.add_option("--gif", action="store", dest="gif")
        self.p.add_option("-r", action="store", dest="resize")
        self.p.add_option("--resize", action="store", dest="resize")
        self.p.add_option("-i", action="store", dest="sequence")
        self.p.add_option("--image", action="store", dest="sequence")
        self.p.add_option("--start", action="store", dest="start")
        self.p.add_option("--end", action="store", dest="end")
        self.p.add_option("-b", action="store", dest="bitrate")
        self.p.add_option("--bitrate", action="store", dest="bitrate")
        self.p.add_option("-f", action="store", dest="fps")
        self.p.add_option("--fps", action="store", dest="fps")
        self.p.add_option("-w", action="store", dest="webm")
        self.p.add_option("--webm", action="store", dest="webm")

    def _set_defaults(self):
        self.p.set_defaults(resize=1,
                            source=None,
                            gif=False,
                            sequence=False,
                            start=1,
                            end=30,
                            webm=False,
                            image=False)

    def get_args(self):
        opts, args = self.p.parse_args()
        return opts
