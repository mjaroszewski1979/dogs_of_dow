import numpy as np
import pandas_datareader as pdr
import datetime
from threading import Thread

results = []

def get_data(symbol):
    global results
    markets  = {
            'AMGN' : 'AMGEN',
            'CSCO' : 'CISCO SYSTEMS',
            'CVX' : 'CHEVRON',
            'IBM' : 'IBM',
            'KO' : 'COCA COLA',
            'MMM' : '3M',
            'MRK' : 'MERCK',
            'VZ' : 'VERIZON',
            'WBA' : 'WALGREENS BOOTS',
            'DOW' : 'DOW'
      
        }
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime.now()
    data = pdr.get_data_yahoo(symbol, start, end)
    total = []
    nums = range(2, 252)
    for x in nums:
        if data['Close'][1] > data['Close'][x]:
            result = 1
        else:
            result = -1
        total.append(result)
    total = (sum(total))
    result = [total, markets[symbol]]
    if result not in results:
        results.append(result)
        results.sort(key=lambda x: x[0], reverse=True)

    
def get_trend():
    global results

    threads = []
    num_threads = 10
    tickers = ['AMGN', 'CSCO', 'CVX', 'IBM', 'KO', 'MMM', 'MRK', 'VZ', 'WBA', 'DOW']

    for i in range(num_threads):
        for x in tickers:
            thread = Thread(target=get_data, args=(x,))
            threads.append(thread)

    for thread in threads:
        thread.start()

    return results