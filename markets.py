import numpy as np
import pandas_datareader as pdr
import datetime
from threading import Thread

results = []

def get_data(symbol):
    global results
    markets  = {
            'MMM' : '3M',
            'AMGN' : 'AMGEN',
            'CVX' : 'CHEVRON',
            'CSCO' : 'CISCO SYSTEMS',
            'KO' : 'COCA COLA',
            'DOW' : 'DOW',
            'IBM' : 'IBM',
            'MRK' : 'MERCK',
            'VZ' : 'VERIZON',
            'WBA' : 'WALGREENS BOOTS'
      
        }
    start = datetime.datetime(2020, 1, 1)
    end = datetime.datetime.now()
    data = pdr.get_data_yahoo(symbol, start, end)
    total = []
    nums = range(2, 252)
    for x in nums:
        if data['Adj Close'][-1] > data['Adj Close'][-x]:
            result = 1
        else:
            result = -1
        total.append(result)
    total = (sum(total))
    if total > 125:
        score = 'STRONG BUY'
    elif total > 0 and total < 125:
        score = 'BUY'
    elif total < 0 and total > -125:
        score = 'SELL'
    elif total < -125:
        score = 'STRONG SELL'
    else:
        score = 'FLAT'
    result = [score, markets[symbol]]
    if result not in results:
        results.append(result)
        results.sort(key=lambda x: x[1])

    
def get_trend():
    global results

    threads = []
    num_threads = 10
    tickers = ['MMM', 'AMGN', 'CVX', 'CSCO', 'KO', 'DOW', 'IBM', 'MRK', 'VZ', 'WBA']

    for i in range(num_threads):
        for x in tickers:
            thread = Thread(target=get_data, args=(x,))
            threads.append(thread)

    for thread in threads:
        thread.start()

    return results