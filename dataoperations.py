import pandas as pd

def data_cleansing(tickers, currentData, pastData, pastPastData):

    try:
        currentCombined = pd.DataFrame(currentData)
        pastCombined = pd.DataFrame(pastData)
        pastPastCombined = pd.DataFrame(pastPastData)

        '''
        for ticker in tickers:
            currentCombined = currentCombined[~currentCombined[ticker].str.contains("[a-z]").fillna(False)]
            pastCombined = pastCombined[~pastCombined[ticker].str.contains("[a-z]").fillna(False)]
            pastPastCombined = pastPastCombined[~pastPastCombined[ticker].str.contains("[a-z]").fillna(False)]
        '''

        currentCombined[tickers] = currentCombined[tickers].replace({',': ''}, regex=True)
        currentCombined[tickers] = currentCombined[tickers].replace({'M': 'E+03'}, regex=True)
        currentCombined[tickers] = currentCombined[tickers].replace({'B': 'E+06'}, regex=True)
        currentCombined[tickers] = currentCombined[tickers].replace({'T': 'E+09'}, regex=True)
        currentCombined[tickers] = currentCombined[tickers].replace({'%': 'E-2'}, regex=True)
        pastCombined[tickers] = pastCombined[tickers].replace({',': ''}, regex=True)
        pastCombined[tickers] = pastCombined[tickers].replace({'M': 'E+03'}, regex=True)
        pastCombined[tickers] = pastCombined[tickers].replace({'B': 'E+06'}, regex=True)
        pastCombined[tickers] = pastCombined[tickers].replace({'T': 'E+09'}, regex=True)
        pastCombined[tickers] = pastCombined[tickers].replace({'%': 'E-2'}, regex=True)
        pastPastCombined[tickers] = pastPastCombined[tickers].replace({',': ''}, regex=True)
        pastPastCombined[tickers] = pastPastCombined[tickers].replace({'M': 'E+03'}, regex=True)
        pastPastCombined[tickers] = pastPastCombined[tickers].replace({'B': 'E+06'}, regex=True)
        pastPastCombined[tickers] = pastPastCombined[tickers].replace({'T': 'E+09'}, regex=True)
        pastPastCombined[tickers] = pastPastCombined[tickers].replace({'%': 'E-2'}, regex=True)

        for ticker in currentCombined:
            currentCombined[ticker] = pd.to_numeric(currentCombined[ticker].values, errors='coerce')
            pastCombined[ticker] = pd.to_numeric(pastCombined[ticker].values, errors='coerce')
            pastPastCombined[ticker] = pd.to_numeric(pastPastCombined[ticker].values, errors='coerce')

        return currentCombined, pastCombined, pastPastCombined

    except:
        print("\nError in data cleansing...")

