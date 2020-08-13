import optparse


class Parser:

    def __init__(self):
        self.p = optparse.OptionParser()
        self._load_options()
        self._set_defaults()

    def _load_options(self):
        self.p.add_option("-S", action="store", dest="source")
        self.p.add_option("--source", action="store", dest="source")
        self.p.add_option("-g", action="store_true", dest="gif")
        self.p.add_option("--gif", action="store_true", dest="gif")
        self.p.add_option("-r", action="store", dest="resize")
        self.p.add_option("--resize", action="store", dest="resize")
        self.p.add_option("-i", action="store", dest="sequence")
        self.p.add_option("--image", action="store", dest="sequence")
        self.p.add_option("-s", action="store", dest="start")
        self.p.add_option("--start", action="store", dest="start")
        self.p.add_option("-e", action="store", dest="end")
        self.p.add_option("--end", action="store", dest="end")
        self.p.add_option("-w", action="store_true", dest="webm")
        self.p.add_option("--webm", action="store_true", dest="webm")
        self.p.add_option("-c", action="store", dest="clips")
        self.p.add_option("--clips", action="store", dest="clips")
        self.p.add_option("-a", action="store_true", dest="auto")
        self.p.add_option("--auto", action="store_true", dest="auto")
        self.p.add_option("-l", action="store", dest="length", nargs=3)
        self.p.add_option("--length", action="store", dest="length", nargs=3)

    def _set_defaults(self):
        self.p.set_defaults(resize=1,
                            source=None,
                            gif=False,
                            sequence=False,
                            start=None,
                            end=None,
                            webm=False,
                            image=False,
                            clips=None,
                            auto=False,
                            length=(10, 4, 0)
                            )

    def get_args(self):
        opts, args = self.p.parse_args()
        return opts
