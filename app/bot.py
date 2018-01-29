from infinityList import InfList
import requests
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth1, OAuth2
import base64
from config import keys
from urllib.parse import urlencode, quote


base_url = 'https://api.twitter.com/'
client_key = keys['CONSUMER_KEY']
client_secret = keys['CONSUMER_SECRET']
app_key = keys['ACCESS_TOKEN']
app_secret = keys['ACCESS_SECRET']


def get_bearer_token(client_key, client_secret, base_url):
    """Function to create bearer token for user oauth."""
    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')
    auth_url = '{}oauth2/token'.format(base_url)
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    auth_data = {'grant_type': 'client_credentials'}

    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

    if auth_resp.status_code == 200 and auth_resp.json().keys():
        # This is the '3-legged'(?) bearer token
        return auth_resp.json()['access_token']
    elif auth_resp.status_code != 200:
        raise RuntimeError('Bad status code: {}'.format(auth_resp.status_code))
    elif auth_resp.json().keys() is None:
        print('No keys.')


# This is just me messing around. Will move somewhere else.
def paginate_tweets(statuses):
    """Yield tweets from timeline for pagination."""
    print("'n'+enter for next tweet, 'b'+enter for previous")
    paginated = InfList([t['full_text'] for t in statuses])
    while True:
        print(paginated.current(), end='\n\n')
        key_press = input()
        if key_press.lower() == 'q':
            return
        elif key_press == '.':
            paginated.next()
            continue
        elif key_press == ',':
            paginated.prev()
            continue


# TODO: Make Thesaurus module
def bizarrify(tweet):
    words = tweet.split()
    print(words)

# Establish our bearer token for this session.
access_token = get_bearer_token(client_key, client_secret, base_url)

auth_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

# Collect tweets from Trump's account
user_params = {
    'screen_name': 'realDonaldTrump',
    'count': '10',
    'tweet_mode': 'extended'
}

status_url = '{}1.1/statuses/user_timeline.json'.format(base_url)

timel_resp = requests.get(status_url, headers=auth_headers, params=user_params)

print(timel_resp.status_code)

""" TESTING """
# from pprint import pprint
# data = timeline.json()
# for y in data:
#     pprint(y)
#     print('\n' + y['full_text'])
#     print('\n\n')

timeline_statuses = timel_resp.json()
tweets = [t['full_text'] for t in timeline_statuses]
for tweet in tweets:
    bizarrify(tweet)

"""MAKE POSTS"""

oauth = OAuth1(client_key, client_secret, app_key, app_secret)
text = {
    "I'm fond of very LARGE hands."
}
post_url = '{}1.1/statuses/update.json'.format(base_url)

post_headers = {
    'User-Agent': 'Bizarro-Trump',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

test = requests.post(post_url, headers=post_headers, params=tweet, auth=oauth)
print(test.status_code, test.headers, test.json())
