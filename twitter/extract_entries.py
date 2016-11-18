import json
import twitter_text
from trending_topics import *


def get_entities(tweet):

    extractor = twitter_text.Extractor(tweet['text'])

    entities = {}
    entities['user_mentions'] = []
    for um in extractor.extract_mentioned_screen_names_with_indices():
        entities['user_mentions'].append(um)

    entities['hashtags'] = []
    for ht in extractor.extract_hashtags_with_indices():
        ht['text'] = ht['hashtag']
        del ht['hashtag']
        entities['hashtags'].append(ht)

    entities['urls'] = []
    for url in extractor.extract_urls_with_indices():
        entities['urls'].append(url)

    return entities

if __name__ == '__main__':
    tweets = get_user_timeline()

    for tweet in tweets:
        tweet['entities'] = get_entities(tweet)
    '''
        File "/Users/terences/PycharmProjects/sandbox/twitter/extract_entries.py", line 8, in get_entities
        extractor = twitter_text.Extractor(tweet['text'])
    TypeError: 'Status' object has no attribute '__getitem__'
    '''
    print json.dumps(tweets, indent=1)