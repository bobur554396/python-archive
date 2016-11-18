import tweepy
import json

APP_NAME = 'Test APITerence'
CONSUMER_KEY = 'wLLapZxpKhgsYQWEia5BTxLrP'
CONSUMER_SECRET = 'xfNA85FHAyUTITVYxZIQWmq0dNfhqAQCOINwCiWjKoXz89ZEpq'

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token("1525867898-Jvr0HdkpHSrzKSzkqaCWqea3V7lAiYP5Rk5OAxA",
                      "OKMUOxA9uzRbM7aDHCBzd4m7ntV7rrqNPs2NcGNi3IXIX")
api = tweepy.API(auth)

qprogramming = api.search("computer science")

print len(qprogramming)

# for status in tweepy.Cursor(qprogramming:
for status in qprogramming:
    mac = json.dumps(status._json, indent=1)
    twitter_json = status._json
    # print mac
    # print twitter_json["user"]["location"]
    print twitter_json["created_at"]
    # if twitter_json["geo"] is not None:
    #     print twitter_json["geo"]
