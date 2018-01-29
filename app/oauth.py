import requests
import base64
from config import keys

base_url = 'https://api.twitter.com/'
client_key = keys['CONSUMER_KEY']
client_secret = keys['CONSUMER_SECRET']

#def get_bearer_token(client_key, client_secret, base_url):


key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')
b64_encoded_key = base64.b64encode(key_secret)
b64_encoded_key = b64_encoded_key.decode('ascii')

auth_url = '{}oauth2/token'.format(base_url)

auth_headers = {
    'Authorization': 'Basic {}'.format(b64_encoded_key),
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
}

auth_data = {
    'grant_type': 'client_credentials'
}

auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

print(auth_resp.status_code)
print(auth_resp.json().keys())

# This is the '3-legged'(?) bearer token
access_token = auth_resp.json()['access_token']

search_headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

search_params = {
    'q': 'General Election',
    'result_type': 'recent',
    'count': 2
}

search_url = '{}1.1/search/tweets.json'.format(base_url)

search_resp = requests.get(search_url, headers=search_headers,
                           params=search_params)
print(search_resp.status_code)

tweet_data = search_resp.json()
for x in tweet_data['statuses']:
    print(x['text'] + '\n')

# Try to collect tweets from Trump's account
user_params = {
    'screen_name': 'realDonaldTrump',
    'count': '10',
    'tweet_mode': 'extended'
}

status_url = '{}1.1/statuses/user_timeline.json'.format(base_url)

timel_resp = requests.get(status_url, headers=search_headers, params=user_params)

print(timel_resp.status_code)

""" TESTING """
# from pprint import pprint
# data = timeline.json()
# for y in data:
#     pprint(y)
#     print('\n' + y['full_text'])
#     print('\n\n')

timeline_statuses = timel_resp.json()

for tweet in timeline_statuses:
    print(tweet['full_text'], end='\n\n')
