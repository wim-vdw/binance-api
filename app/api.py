from flask import Blueprint

binance_api = Blueprint('binance_api', __name__)


@binance_api.get('/')
def index():
    return {'name': 'Binance REST API'}
