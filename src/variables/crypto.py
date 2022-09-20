import ccxt
import pandas as pd

exs = ['binance', 'bitrue', 'digifinex', 'gateio', 'kucoin', 'kraken']

for ex in exs:
    # Get data
    exchange = getattr (ccxt, ex) ()
    exchange.load_markets()
    data = exchange.fetch_ohlcv('BTC/USDT', '1h')
    header = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = pd.DataFrame(data, columns=header).set_index('Timestamp')
    # Save it
    symbol_out = 'BTC/USDT'.replace("/","")
    filename = '{}-{}-{}.json'.format(ex, symbol_out, '1h')
    df.to_json(filename)