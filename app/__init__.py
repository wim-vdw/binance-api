from flask import Flask


def create_app():
    app = Flask(__name__)
    from app.api import binance_api
    app.register_blueprint(binance_api, url_prefix='/api')

    return app
