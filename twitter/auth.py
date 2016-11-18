import os
import sys
import twitter

from twitter.oauth import write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance

access_token_secret = '0407034'
def oauth_login(app_name="", consumer_key="", consumer_secret="", token_file="out/twitter.oauth"):
    try:
        (access_token, access_token_secret) = read_token_file(token_file)
    except:
        (access_token, access_token_secret) = oauth_dance(app_name, consumer_key, consumer_secret)

        if not os.path.isdir('out'):
            os.mkdir('out')

        write_token_file(token_file, access_token, access_token_secret)

        print >> sys.stderr, "OAuth Success. Token file stored to", token_file

    return twitter.Twitter(domain='api.twitter.com', api_version='1', auth=twitter.oauth.OAuth(access_token, access_token_secret, consumer_key, consumer_secret))

if __name__ == '__main__':
    APP_NAME= 'Test APITerence'
    CONSUMER_KEY = 'wLLapZxpKhgsYQWEia5BTxLrP'
    CONSUMER_SECRET = 'xfNA85FHAyUTITVYxZIQWmq0dNfhqAQCOINwCiWjKoXz89ZEpq'

    oauth_login(APP_NAME, CONSUMER_KEY, CONSUMER_SECRET)