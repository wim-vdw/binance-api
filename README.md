# Binance Python client and Rest API
## Use Binance client in Python
```python
from app.helpers import BinanceClient

API_KEY = [your Binance API key]
SECRET_KEY = [your Binance secret key]
client = BinanceClient(api_key=API_KEY, secret_key=SECRET_KEY)

# Send a public request.
response = client.send_public_request('/api/v3/time')
print(response)

# Send a signed request.
response = client.send_signed_request('POST', '/sapi/v1/asset/get-funding-asset')
print(response)

# Send a signed request with additional parameters.
params = {'asset': 'BNB'}
response = client.send_signed_request('POST', '/sapi/v1/asset/get-funding-asset', params)
print(response)
```
## Build and run Rest API in Docker
```shell
$ docker build -t myapi .
$ export BINANCE_API_KEY=[your Binance API key]
$ export BINANCE_SECRET_KEY=[your Binance secret key]
$ docker run --rm --name binanceapi -p 80:80 -e BINANCE_API_KEY -e BINANCE_SECRET_KEY myapi 
$ curl http://localhost/api/assets/
$ curl http://localhost/api/assets/BTC
```
