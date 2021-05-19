from config import *
from textblob import TextBlob
import tweepy
from declat import declat
from eclat import eclat
import pandas as pd


def tweepy_login():
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


if __name__ == "__main__":
    tweepy_api = tweepy_login()
    # tweets = tweepy_api.search("queen", count=1)
    userID = "BarackObama"
    tweets = tweepy_api.user_timeline(screen_name=userID,
                               # 200 is the maximum allowed count
                               count=100,
                               include_rts=False,
                               # Necessary to keep full_text
                               # otherwise only the first 140 words are extracted
                                full_text=True,
                               # tweet_mode='extended'
                               )
    result = list()
    for tweet in tweets:
        blob = TextBlob(tweet.text)
        tags = blob.tags
        filter = ['NN', 'NNP', 'NNS']
        forbidden = ['https', '@']
        filtered_tags = [tup[0] for tup in tags if tup[1] in filter and tup[0] not in forbidden]
        filtered_tags
        # print(filtered_tags)
        result.append(filtered_tags)
    # print(result)
    data = pd.DataFrame(result)
    # print(data)
    frequent_itemsets = eclat(data, min_support=1, min_length=1)
    print("\nResult:")
    print(frequent_itemsets)
