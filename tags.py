import random


class Hashtags:

    def __init__(self, hashes):
        """Hashtag: Represents a list of available tags from seperate library.

        Parameters
        -------------
        hashes:List,
            List of hashtags to be used.
        """
        self.hashtags = hashes

    def get_random_tags(self, size=1):
        return random.choices(self.hashtags, k=size)
