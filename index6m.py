import yfinance as yf
import datetime as dt
import pandas as pd

def sixMonthIndex(tickers):
    start = dt.datetime.today() - dt.timedelta(180)
    end = dt.datetime.today()
    cl_price = pd.DataFrame()
    
    print('\n')
    for ticker in tickers:
        cl_price[ticker]= yf.download(ticker, start, end, period = "6mo")["Adj Close"]

    finalList = cl_price.iloc[-1] / cl_price.iloc[0]
    finalList.sort_values(ascending = False, inplace = True)
    print("\n6 month Index")
    print(finalList)
    finalList = finalList[:len(finalList)//3]
    return finalList
