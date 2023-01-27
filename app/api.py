from flask import Blueprint
from app.helpers import BinanceClient
import os

binance_api = Blueprint('binance_api', __name__)
api_key = os.environ.get('BINANCE_API_KEY') or 'invalid-api-key'
secret_key = os.environ.get('BINANCE_SECRET_KEY') or 'invalid-secret-key'
client = BinanceClient(api_key=api_key, secret_key=secret_key)


@binance_api.get('/time/')
def time():
    response = client.send_public_request('/api/v3/time')
    return response


@binance_api.get('/funding/')
@binance_api.get('/funding/<asset>')
def funding(asset=None):
    param = {'asset': asset} if asset else {}
    response = client.send_signed_request('POST', '/sapi/v1/asset/get-funding-asset', param)
    return response


@binance_api.get('/assets/')
@binance_api.get('/assets/<asset>')
def assets(asset=None):
    param = {'asset': asset} if asset else {}
    response = client.send_signed_request('POST', '/sapi/v3/asset/getUserAsset', param)
    return response
