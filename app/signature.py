from config import keys
from urllib.parse import quote
from datetime import datetime
from uuid import uuid1
from base64 import b64encode
from Crypto.Hash import SHA, HMAC
import requests

client_key = keys['CONSUMER_KEY']
client_secret = keys['CONSUMER_SECRET']
access_token = keys['ACCESS_TOKEN']
access_secret = keys['ACCESS_SECRET']

api_url = 'https://api.twitter.com/'
post_url = '{}1.1/statuses/update.json'.format(api_url)

now = int((datetime.utcnow()-datetime.fromtimestamp(0)).total_seconds())
nonce = uuid1().hex

method = 'POST'
url = quote(post_url, safe='_-')

text = "Hello. I have HUGE hands."

params = {
    'include_entities': 'true',
    'oauth_consumer_key': client_key,
    'oauth_nonce': nonce,
    'oauth_signature_method': 'HMAC-SHA1',
    'oauth_timestamp': now,
    'oauth_token': access_token,
    'oauth_version': '1.0',
    'status': quote(text)
}


param_string = '&'.join(['{}={}'.format(k,params[k]) for k in sorted(params.keys())])

base_string = '&'.join([method, url, quote(param_string, safe='-_')])

# Signature
def gen_signature(client_secret, access_secret, base_string):
    key = '&'.join([client_secret, access_secret]).encode('ascii')
    string_to_sign = base_string.encode('utf-8')
    hmac = HMAC.new(key, string_to_sign, SHA)

    return b64encode(hmac.digest()).decode()

oauth_signature = gen_signature(client_secret, access_secret, base_string)

oauth_params = {
    'oauth_consumer_key': client_key,
    'oauth_nonce': nonce,
    'oauth_signature_method': 'HMAC-SHA1',
    'oauth_timestamp': now,
    'oauth_token': access_token,
    'oauth_version': '1.0',
    'oauth_signature': oauth_signature
}
auth = ', '.join(['{}={}'.format(k,oauth_params[k]) for k in
                  sorted(oauth_params.keys())])

auth_headers = {
    'User-Agent': 'Bizarro-Trump',
    'Content-Type': 'application/x-www.form-urlencoded',
    'Authorization': 'OAuth {}'.format(auth)
}

post = requests.post(url=post_url, data=text, headers=auth_headers)
print(post.status_code, post.content, post.text)
