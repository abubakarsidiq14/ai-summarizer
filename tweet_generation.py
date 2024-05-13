import pandas as pd
import tweepy
auth = tweepy.OAuthHandler("api key", "api secert key")
auth.set_access_token("access key", "access secert key")
api = tweepy.API(auth)
def generate_tweet(summary):
    tweet_text = summary
    return tweet_text
def post_tweet(tweet_text):
    api.update_status(tweet_text)