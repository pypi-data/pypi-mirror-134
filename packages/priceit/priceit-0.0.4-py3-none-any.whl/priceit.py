import requests
import datetime

def time2period(s):
    return int(datetime.datetime.strptime(s,'%Y-%m-%d').timestamp()-18000)

def getprice(ticker):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    URL = 'https://query1.finance.yahoo.com/v7/finance/quote?&symbols=' + ticker + '&fields=extendedMarketChange,extendedMarketChangePercent,extendedMarketPrice,extendedMarketTime,regularMarketChange,circulatingSupply,regularMarketChangePercent,regularMarketPrice,regularMarketTime,ask,askSize,bid,bidSize,dayHigh,dayLow,regularMarketDayHigh,regularMarketDayLow,regularMarketVolume,volume,quoteType'
    try:
        page = requests.get(URL, headers=headers)
        result = page.json()
        s = result['quoteResponse']['result'][0]['regularMarketTime']
        price_symbol = result['quoteResponse']['result'][0]['symbol']
        price_time = datetime.datetime.fromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S')
        price_quote = result['quoteResponse']['result'][0]['regularMarketPrice']
        price_market = result['quoteResponse']['result'][0]['quoteSourceName']

    except:
        price_symbol = ticker
        price_time ='0'
        price_quote ='0'
        price_market = 'Price Not Found'
    return [price_symbol, price_quote, price_market, price_time]

def histprice(ticker, startdate, enddate, interval='1d'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    period1 = str(time2period(startdate))
    period2 = str(time2period(enddate))
    URL = 'https://query1.finance.yahoo.com/v8/finance/chart/'+ticker+'?formatted=true&lang=en-CA&region=CA&includeAdjustedClose=true&interval='+interval+'&period1='+period1+'&period2='+period2+'&events=capitalGain%7Cdiv%7Csplit&useYfid=true&corsDomain=ca.finance.yahoo.com'
    page = requests.get(URL, headers=headers)
    r = page.json()
    currency = r['chart']['result'][0]['meta']['currency']
    symbol = r['chart']['result'][0]['meta']['symbol']
    exchangeName = r['chart']['result'][0]['meta']['exchangeName']
    timestamp = r['chart']['result'][0]['timestamp']
    timestamp =[datetime.datetime.fromtimestamp(item+3600*5).strftime('%Y-%m-%d') for item in timestamp]
    volume = r['chart']['result'][0]['indicators']['quote'][0]['volume']
    high = r['chart']['result'][0]['indicators']['quote'][0]['high']
    low = r['chart']['result'][0]['indicators']['quote'][0]['low']
    close = r['chart']['result'][0]['indicators']['quote'][0]['close']
    open = r['chart']['result'][0]['indicators']['quote'][0]['open']
    adjclose = r['chart']['result'][0]['indicators']['adjclose'][0]['adjclose']
    result = {'currency': currency, 'symbol': symbol, 'exchangeName': exchangeName,
              'data': {'timestamp': timestamp, 'volume': volume, 'high': high, 'low': low, 'close': close, 'open': open,
                       'adjclose': adjclose}}

    return result

def tickerlist(exchange = 'NASDAQ'):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
        "Upgrade-Insecure-Requests": "1", "DNT": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}
    URL = 'https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=10000&exchange='+exchange
    page = requests.get(URL, headers=headers, timeout=5, allow_redirects=True)
    result = page.json()
    data = result['data']['table']['rows']
    symbol = [s['symbol'].rstrip() for s in data]
    name = [s['name'].rstrip() for s in data]
    result = {'symbol': symbol, 'name': name}
    return result