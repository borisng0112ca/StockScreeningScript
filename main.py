import webscraping
import dataOperations
import roc
import earningsYield
import Fscore
import index6m


#test unit
originalTickers = ["TXG.TO","DCBO.TO","LIF.TO","UFS.TO","TD.TO", "RY.TO", "CM.TO"]


#Retreive and store primitive data
currentData = {}
pastData = {}
pastPastData = {}
webscraping.getFinancialData(originalTickers, currentData, pastData, pastPastData)

#data operations with pandas and data_cleansing function made in dataOperations.py
tuples = dataOperations.data_cleansing(originalTickers, currentData, pastData, pastPastData)
currentCombined = tuples[0]
pastCombined = tuples[1]
pastPastCombined = tuples[2]
#del currentData, pastData, pastPastData, tuples

#filter 1

rocResults = roc.filter1(currentCombined)
roc_df = rocResults[0]
rocTickers = rocResults[1] #tickers after ROC filter

#filter 2

eyResults = earningsYield.filter2(currentCombined)
ey_df = eyResults[0]
eyTickers = eyResults[1]  #tickers after earnings yield filter

#filter 3

fscoreResults = Fscore.fscoreCalculation(currentCombined, pastCombined, pastPastCombined, originalTickers)
fscore_df = fscoreResults[0]
fscoreTickers = fscoreResults[1]

#filter 4
index6mTickers = index6m.sixMonthIndex(originalTickers) #tickers after index 6months filter
finalTickers = []


for ticker in originalTickers:
   if (ticker in rocTickers) and (ticker in eyTickers) and (ticker in index6mTickers) and (ticker in fscoreTickers):
       finalTickers.append(ticker)

print("Stocks remaining after 4 filters:")
print(finalTickers)