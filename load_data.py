from config import *
import tweepy


def tweepy_login():
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


if __name__ == "__main__":
    tweepy_api = tweepy_login()
    tweets = tweepy_api.search("queen", count=1)
    print(tweets)
