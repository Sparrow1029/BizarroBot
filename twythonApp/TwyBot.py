from twython import Twython
from config import keys
from trumpasaurus import trumpsaurus
from time import sleep
import re

twitter = Twython(keys['CONSUMER_KEY'], keys['CONSUMER_SECRET'],
                 keys['ACCESS_TOKEN'], keys['ACCESS_SECRET'])

trump = twitter.get_user_timeline(screen_name='realDonaldtrump',
                                  count=5,tweet_mode='extended')

bizarro = twitter.get_home_timeline()


twitter.verify_credentials()
for t in trump:
    print(t['full_text'])
sleep(2)
antonyms = trumpsaurus().antonyms


def swap_words(tweet, wordDict):
    """Here's the bizarro switcher"""
    orig_text = tweet['full_text'].lower()

    # Removing links for now till I parse json object to relink hyperlinks
    links = re.compile(r'http|https://.*')
    orig_text = links.sub('', orig_text)

    # Found this on SO for swapping words out. It creates a huge list of
    # OR `|` statements based on the dict keys for `re.sub`
    pattern = re.compile(r'\b(' + '|'.join(wordDict.keys()) + r')\b')
    result = pattern.sub(lambda x: wordDict[x.group()], orig_text)
    return str(result)


for tweet in trump:
        reversed_tweet = swap_words(tweet, antonyms)
        print(reversed_tweet)
        # THIS doesn't work
        # if reversed_tweet not in [s['text'] for s in bizarro]:
        post = twitter.update_status(status=reversed_tweet)
        #     print(post)
        # else:
        #     print('Tweet already exists.')
        sleep(4)

# TODO: Add handling for already existing statuses.
# TODO: More specific about:
#           - Checking rate-limit and staying within it
#           - Including #hashtags and @handles and media links
# TODO: Better regex and maintaining case of words
# TODO: EVENTUALLY run a cron job on the server to check for new Trump
#           tweets and run the script
