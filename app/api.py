from flask import Blueprint
from app.helpers import BinanceClient
import os

binance_api = Blueprint('binance_api', __name__)
api_key = os.environ.get('BINANCE_API') or 'invalid-api-key'
api_secret = os.environ.get('BINANCE_SECRET') or 'invalid-secret-key'


@binance_api.get('/')
def index():
    client = BinanceClient(api_key=api_key, api_secret=api_secret)
    return client.to_dict()
