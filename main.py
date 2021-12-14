import tkinter as tk
import logging

from connectors.binance_futures import BinanceFuturesClient

logger = logging.getLogger()

logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':

    binance = BinanceFuturesClient("61f9472a2e2b9027ea5fa69045a83b62adc2706d23ff9b89c0550bbe5d9c55e5", "a8afaf411b4410aa0942af1a289989826595f5f21abbf9975b2fea67078de6c2", True)
    #print(binance.get_hisorical_candles("BTCUSDT", "1h"))
    #print(binance.get_bid_ask("BTCUSDT"))
    #print(binance.get_balance())
    #print(binance.place_order("BTCUSDT", "BUY", 0.01, "LIMIT", 50000, "GTC"))
    #print(binance.get_order_status("BTCUSDT", 2943236588))
    #print(binance.cancel_order("BTCUSDT", 2943236588))

    root = tk.Tk()
    root.mainloop()
