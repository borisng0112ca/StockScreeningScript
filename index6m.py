import yfinance as yf
import datetime as dt
import pandas as pd

def sixMonthIndex(tickers, percent):

    try:
        start = dt.datetime.today() - dt.timedelta(180)
        end = dt.datetime.today()
        cl_price = pd.DataFrame()
        
        print('\n')
        for ticker in tickers:
            cl_price[ticker]= yf.download(ticker, start, end, period = "6mo")["Adj Close"]

        list6m = cl_price.iloc[-1] / cl_price.iloc[0]
        list6m.sort_values(ascending = False, inplace = True)
        print("\n6 month Index")
        print(list6m)

        finalList = list(list6m.index.values)
        finalList = finalList[:int(len(finalList)*percent)]

        return finalList

    except:
        print("\nError in 6-month Index calculation...")
        return []