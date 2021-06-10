import pandas as pd

def fscoreCalculation(currentCombined, pastCombined, pastPastCombined, originalTickers, percent):

    try:
        originalTickers = currentCombined.columns

        fscore = {}
        for ticker in originalTickers:

            ROA_FS = int(currentCombined.loc["Net Income available to common shareholders", ticker] / ((currentCombined.loc["Total Assets", ticker] + pastCombined.loc["Total Assets", ticker]) / 2) > 0)
            CFO_FS = int(currentCombined.loc["Operating Cash Flow", ticker] > 0)
            ROA_D_FS = int(
                currentCombined.loc["Net Income available to common shareholders", ticker] / (currentCombined.loc["Total Assets", ticker] + pastCombined.loc["Total Assets", ticker]) / 2 >
                pastCombined.loc["Net Income available to common shareholders", ticker] / (pastCombined.loc["Total Assets", ticker] + pastPastCombined.loc["Total Assets", ticker]) / 2)

            CFO_ROA_FS = int(
                currentCombined.loc["Operating Cash Flow", ticker] / currentCombined.loc["Total Assets", ticker] > currentCombined.loc["Net Income available to common shareholders", ticker] / (
                (currentCombined.loc["Total Assets", ticker] + pastCombined.loc["Total Assets", ticker]) / 2))

            LTD_FS = int((currentCombined.loc["Long Term Debt", ticker] + currentCombined.loc["Other long-term liabilities", ticker]) < (
                        pastCombined.loc["Long Term Debt", ticker] + pastCombined.loc["Other long-term liabilities", ticker]))


            CR_FS = int((currentCombined.loc["Total Current Assets", ticker] / currentCombined.loc["Total Current Liabilities", ticker]) > (
                        pastCombined.loc["Total Current Assets", ticker] / pastCombined.loc["Total Current Liabilities", ticker]))

            DILUTION_FS = int(currentCombined.loc["Common Stock", ticker] <= pastCombined.loc["Common Stock", ticker])

            GM_FS = int((currentCombined.loc["Gross Profit", ticker] / currentCombined.loc["Total Revenue", ticker]) > (
                        pastCombined.loc["Gross Profit", ticker] / pastCombined.loc["Total Revenue", ticker]))

            ATO_FS = int(
                currentCombined.loc["Total Revenue", ticker] / ((currentCombined.loc["Total Assets", ticker] + pastCombined.loc["Total Assets", ticker]) / 2) >
                pastCombined.loc["Total Revenue", ticker] / ((pastCombined.loc["Total Assets", ticker] + pastPastCombined.loc["Total Assets", ticker]) / 2))

            fscore[ticker] = [ROA_FS, CFO_FS, ROA_D_FS, CFO_ROA_FS, LTD_FS, CR_FS, DILUTION_FS, GM_FS, ATO_FS]

        fscore_df = pd.DataFrame(fscore,index=["PosROA", "PosCFO", "ROAChange", "Accruals", "Leverage", "Liquidity", "Dilution","GM", "ATO"])
        fscore_df = fscore_df.transpose()
        fscore_df['Sum'] =  fscore_df[["PosROA", "PosCFO", "ROAChange", "Accruals", "Leverage", "Liquidity", "Dilution", "GM", "ATO"]].sum(axis=1)
        fscore_df.sort_values(by=["Sum"], inplace = True, ascending=False)
        print('\n',fscore_df)

        filteredTickers = fscore_df.index
        filteredTickers = filteredTickers[:int(len(filteredTickers)*percent)]

        return list(filteredTickers)

    except:
        print("\nError in F-Score calculation...")
        return []