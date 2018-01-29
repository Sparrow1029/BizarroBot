from bot import access_token
import requests

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
