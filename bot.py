import tweepy



class TwitterBot:

    def __init__(self, consumer, consumer_secret, access, access_secret):
        """
            Twitter Bot
            Initialize bot with Twitter consumer and access tokens.
            Authorizes use of API.
        """
        self.consumer = consumer
        self.consumer_secret = consumer_secret
        self.access = access
        self.access_secret = access_secret

        self.api = self._log_in()

    def _log_in(self):
        auth = tweepy.OAuthHandler(self.consumer, self.consumer_secret)
        auth.set_access_token(self.access, self.access_secret)
        return tweepy.API(auth)

    def tweet(self, message, file=None):
        """Sends a tweet using Tweepy API.

        Parameters:
        ------------
        message:String,
            The text to be tweeted out.
        file=None:String,
            If this is not None, it should be a filename or path
            to be tweeted out with the message. Must be under 3072kb.
        """
        if file is None:
            self._tweet(message)
        else:
            print("Sending tweet with gif: {:s}".format(file))
            self._tweet_media(message, file)

    def _tweet(self, message):
        try:
            self.api.update_status(message)
        except tweepy.TweepError as te:
            print(te.response.text)

    def _tweet_media(self, message, file):
        try:
            self.api.update_with_media(file, message)
        except tweepy.TweepError as te:
            print(te.response.text)
