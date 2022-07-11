import yfinance as yf

stocks = ['AAPL', 'MSFT', 'AMD']



for stock in stocks:
    info = yf.Ticker(stock).stats()
    print(info)