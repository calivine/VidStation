import optparse


class Parser:

    def __init__(self):
        self.p = optparse.OptionParser()
        self._load_options()

    def _load_options(self):
        self.p.add_option("-s", action="store", dest="source")
        self.p.add_option("--source", action="store", dest="source")
        self.p.add_option("-g", action="store", dest="gif")
        self.p.add_option("--gif", action="store", dest="gif")
        self.p.add_option("-r", action="store", dest="resize")
        self.p.add_option("--resize", action="store", dest="resize")
        self.p.set_defaults(resize=1, source=None, gif=False)


    def get_args(self):
        opts, args = self.p.parse_args()
        return opts
