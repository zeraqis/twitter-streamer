from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import os

credentials_dict = json.loads(os.environ['APP_CREDENTIALS'])

# Variables that contains the user credentials to access Twitter API
access_token = credentials_dict['access_token']
access_token_secret = credentials_dict['access_token_secret']
consumer_key = credentials_dict['consumer_key']
consumer_secret = credentials_dict['consumer_secret']


# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':
    listener = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)

    stream.filter(track=['blockchain', 'btc', 'bitcoin'])
