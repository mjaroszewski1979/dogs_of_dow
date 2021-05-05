import numpy as np
import pandas_datareader as pdr
import datetime
from threading import Thread

results = []

def get_data(symbol):
    global results
    markets  = {
            'AXP' : 'AMERICAN EXPRESS',
            'AMGN' : 'AMGEN',
            'AAPL' : 'APPLE',
            'BA' : 'BOEING',
            'CAT' : 'CATERPILLAR',
            'CSCO' : 'CISCO SYSTEMS',
            'CVX' : 'CHEVRON',
            'GS' : 'GOLDMAN SACHS',
            'HD' : 'HOME DEPOT',
            'HON' : 'HONEYWELL',
            'IBM' : 'IBM',
            'INTC' : 'INTEL',
            'JNJ' : 'JOHNSON & JOHNSON',
            'KO' : 'COCA COLA',
            'JPM' : 'JPMORGAN CHASE',
            'MCD' : "MC DONALS'S",
            'MMM' : '3M',
            'MRK' : 'MERCK',
            'MSFT' : 'MICROSOFT',
            'NKE' : 'NIKE',
            'PG' : 'PROCTER & GAMBLE',
            'TRV' : 'TRAVELERS',
            'UNH' : 'UNITEDHEALTH',
            'CRM' : 'SALESFORCE.COM',
            'VZ' : 'VERIZON',
            'V' : 'VISA',
            'WBA' : 'WALGREENS BOOTS',
            'WMT' : 'WALMART',
            'DIS' : 'DISNEY',
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
    num_threads = 30
    tickers = ['AXP', 'AMGN', 'AAPL', 'BA', 'CAT', 'CSCO', 'CVX', 'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'KO', 'JPM', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'CRM', 'VZ', 'V', 'WBA', 'WMT', 'DIS', 'DOW']

    for i in range(num_threads):
        for x in tickers:
            thread = Thread(target=get_data, args=(x,))
            threads.append(thread)

    for thread in threads:
        thread.start()

    return results