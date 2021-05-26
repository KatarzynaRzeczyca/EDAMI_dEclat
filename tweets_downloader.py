from config import *
import tweepy
import json


def tweepy_login():
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


if __name__ == "__main__":
    tweepy_api = tweepy_login()
    userID = "GOP"
    tweets = tweepy_api.user_timeline(screen_name=userID, count=200, include_rts=False, tweet_mode='extended')
    print("Number of tweets: ", len(tweets))
    assert len(tweets) > 0

    data = {'tweets': []}
    for tweet in tweets:
        tweet_text = tweet.full_text
        data['tweets'].append(tweet_text)
        print(tweet_text)

    with open('tweets.txt', 'w') as outfile:
        json.dump(data, outfile)
