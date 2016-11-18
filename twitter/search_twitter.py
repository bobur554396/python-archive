import sys
import json
import tweepy
import twitter
from trending_topics import *

# Q = ' '.join(sys.argv[1])
Q = 'feminism'
MAX_PAGES = 15
RESULTS_PER_PAGE = 100

twitter_search = twitter.Twitter(domain="search.twitter.com", api_version='1.1')

twitter_search = tweepy_api().search(Q)

search_results = []
for page in range(1, MAX_PAGES+1):
    search_results += \
        twitter_search.search(q=Q, rpp=RESULTS_PER_PAGE, page=page)['results']

print json.dumps(search_results, indent=1)