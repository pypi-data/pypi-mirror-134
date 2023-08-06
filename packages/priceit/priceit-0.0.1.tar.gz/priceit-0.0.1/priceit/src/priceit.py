import requests
import datetime

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

if __name__ == '__main__':
    print(getprice('BTC-USD'))