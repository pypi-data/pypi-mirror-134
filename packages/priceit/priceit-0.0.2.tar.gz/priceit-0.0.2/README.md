# PRICEIT

Author: David WANG

Version 0.0.2

To extract realtime or history price data of stocks or crypto currencies. 
(Please note this package is based on free API (e.g. Yahoo Finance). There may be a little time lag (seconds or minutes) for some market.)


## Installation:
```bash
pip install priceit
```

## Usage:
(1) To get realtime TSLA price
```python
from priceit import *

ticker ='TSLA'
print(getprice(ticker))
```
Result:
```
['TSLA', 1049.61, 'Delayed Quote', '2022-01-14 16:00:04']
```
(Sample above is taken during weekend, when the market is close. So it shows 'Delayed Quote'. Try this when market is open, and you can get realtime quote (almost realtime). Please allow seconds or minutes time lag for certain market.)

(2) To get history daily price of BTC-USD from 2022-01-12 to 2022-01-14
```python
from priceit import *

ticker = 'BTC-USD'
startdate = '2022-01-12'
enddate = '2022-01-14'
print(histprice(ticker,startdate,enddate))
```
Result:
```
{'currency': 'USD', 'symbol': 'BTC-USD', 'exchangeName': 'CCC', 'data': {'timestamp': ['2022-01-12', '2022-01-13', '2022-01-14'], 'volume': [33499938689, 47691135082, 23577403399], 'high': [44135.3671875, 44278.421875, 43346.6875], 'low': [42528.98828125, 42447.04296875, 41982.6171875], 'close': [43949.1015625, 42591.5703125, 43099.69921875], 'open': [42742.1796875, 43946.7421875, 42598.87109375], 'adjclose': [43949.1015625, 42591.5703125, 43099.69921875]}}
```
## Notes:
- This project is being built up. More functions will be added.
- If to get realtime price, please limit your frequency of data extraction. We should cherish the free resources, like Yahoo Finance.

## About the Author
I am currently in Grade 11 (as at 15 Jan 2022). I have great interests in AI trading and real world simulation. I am summarizing my free data sources in this project. And hopefully this can save some of your time in data extraction. 
