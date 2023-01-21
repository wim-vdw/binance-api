from flask import Blueprint
from app.helpers import BinanceClient
import os

binance_api = Blueprint('binance_api', __name__)
api_key = os.environ.get('BINANCE_API_KEY') or 'invalid-api-key'
secret_key = os.environ.get('BINANCE_SECRET_KEY') or 'invalid-secret-key'


@binance_api.get('/')
def index():
    client = BinanceClient(api_key=api_key, secret_key=secret_key)
    response = client.send_public_request('/api/v3/time')
    return response
