from twython import Twython
from config import keys
from trumpasaurus import trumpsaurus
from time import sleep
import re

twitter = Twython(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'],
                 keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])

Trump = twitter.get_user_timeline(screen_name='realDonaldTrump',
                                  count=5,tweet_mode='extended')
twitter.verify_credentials()
for t in Trump:
    print(t['full_text'])
sleep(2)
antonyms = trumpsaurus().antonyms


def swap_words(tweet, wordDict):
    orig_text = tweet['full_text'].lower()
    links = re.compile(r'[http|https]://.*')
    orig_text = links.sub('', orig_text)
    pattern = re.compile(r'\b(' + '|'.join(wordDict.keys()) + r')\b')
    result = pattern.sub(lambda x: wordDict[x.group()], orig_text)
    return str(result)


for tweet in Trump:
        reversed_tweet = swap_words(tweet, antonyms)
        print(reversed_tweet)
        post = twitter.update_status(status=reversed_tweet)
        print(post)
        sleep(4)
  # words = list(map(lambda x: x.lower(), orig_text.split()))
    # to_replace = []

    # for word in words:
    #     mo = re.match(r'\b\w*\b', word)
    #     if mo:
    #         print(mo.group(0))
    #         if mo.group(0) in antonyms.keys():
    #             to_replace.append(mo.group(0))
    # print(to_replace)
