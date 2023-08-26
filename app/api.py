from flask import Blueprint, request
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
    params = {'asset': asset} if asset else {}
    response = client.send_signed_request('POST', '/sapi/v1/asset/get-funding-asset', params)
    return response if not asset else \
        (response[0] if response else ({'message': f'No funding for {asset}'}, 404))


@binance_api.get('/assets/')
@binance_api.get('/assets/<asset>')
def assets(asset=None):
    params = {'asset': asset} if asset else {}
    response = client.send_signed_request('POST', '/sapi/v3/asset/getUserAsset', params)
    return response if not asset else \
        (response[0] if response else ({'message': f'No assets for {asset}'}, 404))


@binance_api.get('/generic/')
def generic():
    payload = request.json
    signed = payload.get('signed', False)
    method = payload.get('method')
    endpoint = payload.get('endpoint')
    params = payload.get('params', {})
    if not signed:
        response = client.send_public_request(endpoint, params)
    else:
        response = client.send_signed_request(method, endpoint, params)
    return response
