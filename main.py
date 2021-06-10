import webscraping
import dataoperations
import roc
import earningsyield
import fscore
import index6m

if __name__ == '__main__':

   #stocks to be filtered
   # startingTickers = ["TSLA", "AAPL", "GOOG", "GME", "PLTR", "AMC", "IBM", "AC.TO", "FB"]
   startingTickers = ["TSLA", "AAPL", "GOOG", "GME", "PLTR", "AMC",]

   #Retreive and store primitive data
   currentData, pastData, pastPastData = webscraping.getFinancialData(startingTickers)

   #data operations
   currentCombined, pastCombined, pastPastCombined = dataoperations.data_cleansing(startingTickers, currentData, pastData, pastPastData)
   del currentData, pastData, pastPastData

   #filter 1 (ROC Top 50%)
   rocTickers = roc.rocCalculation(currentCombined)

   #filter 2 (Earnings Yield Top 20%)
   eyTickers = earningsyield.eyCalculation(currentCombined)

   #filter 3 (F-Score Top 40%)
   fscoreTickers = fscore.fscoreCalculation(currentCombined, pastCombined, pastPastCombined, startingTickers)

   #filter 4 (Momentum 6m Top 20%)
   index6mTickers = index6m.sixMonthIndex(startingTickers)

   finalTickers = []

   #stocks that passed the 4 filters will be the remaining stocks
   for ticker in startingTickers:
      if (ticker in rocTickers) and (ticker in eyTickers) and (ticker in index6mTickers) and (ticker in fscoreTickers):
          finalTickers.append(ticker)

   print("\nStocks remaining after 4 filters:")
   if len(finalTickers) == 0:
      print("0 stocks passed.\n")
   else:
      print(finalTickers,'\n')
