import hmac
import hashlib
import time

BASE_URL = 'https://api.binance.com'


def hashing(query_string, secret):
    return hmac.new(secret.encode('utf-8'),
                    query_string.encode('utf-8'),
                    hashlib.sha256).hexdigest()


def get_timestamp():
    return int(time.time() * 1000)


class BinanceClient:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    def to_dict(self):
        return {
            'api_key': self.api_key,
            'api_secret': self.api_secret,
        }
