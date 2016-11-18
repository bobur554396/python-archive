import os
import sys
import datetime
import time
import json
import twitter
import tweepy
import urllib2
from auth import *

APP_NAME = 'Test APITerence'
CONSUMER_KEY = 'wLLapZxpKhgsYQWEia5BTxLrP'
CONSUMER_SECRET = 'xfNA85FHAyUTITVYxZIQWmq0dNfhqAQCOINwCiWjKoXz89ZEpq'

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

def run_dmc():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token("1525867898-Jvr0HdkpHSrzKSzkqaCWqea3V7lAiYP5Rk5OAxA", "OKMUOxA9uzRbM7aDHCBzd4m7ntV7rrqNPs2NcGNi3IXIX")
    api = tweepy.API(auth)
    trends1 = api.trends_place(1)

    # while True:
    for i in range(0, 10):
        now = str(datetime.datetime.now())

        trends = json.dumps(trends1, indent=1)
        f = open(os.path.join(os.getcwd(), 'out', 'trends_data', now), 'w')
        f.write(trends)
        f.close()

        print >> sys.stderr, "Wrote data file", f.name
        print >> sys.stderr, "Zzz..."
        time.sleep(60) # 60 seconds

def get_trending_tweets():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token("1525867898-Jvr0HdkpHSrzKSzkqaCWqea3V7lAiYP5Rk5OAxA",
                          "OKMUOxA9uzRbM7aDHCBzd4m7ntV7rrqNPs2NcGNi3IXIX")
    api = tweepy.API(auth)
    return api.trends_place(1)

def get_user_timeline():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token("1525867898-Jvr0HdkpHSrzKSzkqaCWqea3V7lAiYP5Rk5OAxA",
                          "OKMUOxA9uzRbM7aDHCBzd4m7ntV7rrqNPs2NcGNi3IXIX")
    api = tweepy.API(auth)
    timeline = api.home_timeline()[0]

    return timeline

def tweepy_api():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token("1525867898-Jvr0HdkpHSrzKSzkqaCWqea3V7lAiYP5Rk5OAxA",
                          "OKMUOxA9uzRbM7aDHCBzd4m7ntV7rrqNPs2NcGNi3IXIX")
    return tweepy.API(auth)
