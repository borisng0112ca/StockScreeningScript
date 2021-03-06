import pandas as pd

def eyCalculation(currentCombined, percent):

    try:
        magic_df = pd.DataFrame()
        temp_df = pd.DataFrame()
        temp_df["EBITDA"] = currentCombined.loc["EBITDA", :]
        temp_df["Depreciation & amortization"] = currentCombined.loc["Depreciation & amortization", :]
        temp_df["Market Cap (intraday)"] = currentCombined.loc["Market Cap (intraday)"]
        temp_df["Long Term Debt"] = currentCombined.loc["Long Term Debt"]
        temp_df["Total Current Assets"] = currentCombined.loc["Total Current Assets"]
        temp_df["Total Current Liabilities"] = currentCombined.loc["Total Current Liabilities"]
        temp_df = temp_df.dropna()

        # Earnings Yield
        magic_df["EBIT"] = temp_df["EBITDA"] - temp_df["Depreciation & amortization"]
        magic_df["Enterprise Value"] = temp_df["Market Cap (intraday)"] + temp_df["Long Term Debt"] \
                                       - (temp_df["Total Current Assets"] - temp_df["Total Current Liabilities"])
        magic_df["Earnings Yield"] = magic_df["EBIT"] / magic_df["Enterprise Value"]
        magic_df["EY Rank"] = magic_df["Earnings Yield"].rank(ascending=False, na_option='bottom')
        magic_df.sort_values(by=["EY Rank"], inplace=True)
        print('\n',magic_df.loc[:, ["EY Rank", "Earnings Yield"]])

        tickers = magic_df.index.values
        tickers = tickers[:int(len(tickers)*percent)]

        # magic_df.drop(magic_df.index[len(tickers)//5:], inplace=True)

        return list(tickers)

    except:
        print("\nError in Earnings Yield calculation...")
        return []