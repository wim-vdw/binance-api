import hmac
import hashlib
import time
import requests
from urllib.parse import urlencode

BASE_URL = 'https://api.binance.com'


def hashing(query_string, secret):
    return hmac.new(secret.encode('utf-8'),
                    query_string.encode('utf-8'),
                    hashlib.sha256).hexdigest()


def get_timestamp():
    return int(time.time() * 1000)


def dispatch_request(http_method, api_key):
    session = requests.Session()
    session.headers.update({'Content-Type': 'application/json;charset=utf-8', 'X-MBX-APIKEY': api_key})
    return {
        'GET': session.get,
        'DELETE': session.delete,
        'PUT': session.put,
        'POST': session.post,
    }.get(http_method, 'GET')


class BinanceClient:
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def send_public_request(self, endpoint, payload=None):
        if not payload:
            payload = {}
        query_string = urlencode(payload, doseq=True)
        url = BASE_URL + endpoint
        if query_string:
            url = url + '?' + query_string
        response = dispatch_request('GET', self.api_key)(url=url)
        return response.json()

    def send_signed_request(self, http_method, endpoint, payload=None):
        if not payload:
            payload = {}
        query_string = urlencode(payload, doseq=True)
        if query_string:
            query_string = '{}&timestamp={}'.format(query_string, get_timestamp())
        else:
            query_string = 'timestamp={}'.format(get_timestamp())
        url = BASE_URL + endpoint + '?' + query_string + '&signature=' + hashing(query_string, self.secret_key)
        params = {'url': url, 'params': {}}
        response = dispatch_request(http_method, self.api_key)(**params)
        return response.json()
