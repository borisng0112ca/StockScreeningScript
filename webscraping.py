import requests
from bs4 import BeautifulSoup

def getFinancialData(tickers):
	
	yahooURL = 'https://ca.finance.yahoo.com/quote/'
	currentData = {}
	pastData = {}
	pastPastData = {}

	print('\n****Value Investing Stock Screener V1.1****\n')
	for ticker in tickers:
		try:
			temp_dir1 = {}
			temp_dir2 = {}
			temp_dir3 = {}

			print("Scraping financial data for "+ ticker)
			# getting balance sheet data from yahoo finance for the given ticker
			url = yahooURL +ticker+'/balance-sheet?p='+ticker
			page = requests.get(url)
			page_content = page.content
			soup = BeautifulSoup(page_content,'html.parser')
			tabl = soup.find_all("div", {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
			for t in tabl:
				rows = t.find_all("div", {"class" : "rw-expnded"})
				for row in rows:
					temp_dir1[row.get_text(separator='|').split("|")[0]]=row.get_text(separator='|').split("|")[1]
					temp_dir2[row.get_text(separator='|').split("|")[0]] = row.get_text(separator='|').split("|")[2]
					temp_dir3[row.get_text(separator='|').split("|")[0]] = row.get_text(separator='|').split("|")[3]

			#getting income statement data from yahoo finance for the given ticker
			url = yahooURL +ticker+'/financials?p='+ticker
			page = requests.get(url)
			page_content = page.content
			soup = BeautifulSoup(page_content,'html.parser')
			tabl = soup.find_all("div", {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
			for t in tabl:
				rows = t.find_all("div", {"class" : "rw-expnded"})
				for row in rows:
					temp_dir1[row.get_text(separator='|').split("|")[0]] = row.get_text(separator='|').split("|")[1]
					temp_dir2[row.get_text(separator='|').split("|")[0]] = row.get_text(separator='|').split("|")[2]
					temp_dir3[row.get_text(separator='|').split("|")[0]] = row.get_text(separator='|').split("|")[3]

			#getting cashflow statement data from yahoo finance for the given ticker
			url = yahooURL +ticker+'/cash-flow?p='+ticker
			page = requests.get(url)
			page_content = page.content
			soup = BeautifulSoup(page_content,'html.parser')
			tabl = soup.find_all("div", {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
			for t in tabl:
				rows = t.find_all("div", {"class" : "rw-expnded"})
				for row in rows:
					temp_dir1[row.get_text(separator='|').split("|")[0]] = row.get_text(separator='|').split("|")[1]
					temp_dir2[row.get_text(separator='|').split("|")[0]] = row.get_text(separator='|').split("|")[2]
					temp_dir3[row.get_text(separator='|').split("|")[0]] = row.get_text(separator='|').split("|")[3]

			#getting key statistics data from yahoo finance for the given ticker
			url = yahooURL +ticker+'/key-statistics?p='+ticker
			page = requests.get(url)
			page_content = page.content
			soup = BeautifulSoup(page_content,'html.parser')
			tabl = soup.findAll("div", {"class": "Mstart(a) Mend(a)"})
			for t in tabl:
				rows = t.find_all("tr")
				for row in rows:
					if len(row.get_text(separator='|').split("|")[0:2])>0:
						temp_dir1[row.get_text(separator='|').split("|")[0]] = row.get_text(separator='|').split("|")[-1]

			#combining all extracted information with the corresponding ticker
			currentData[ticker] = temp_dir1
			pastData[ticker] = temp_dir2
			pastPastData[ticker] = temp_dir3

		except:
			print("Error scraping data for " + ticker)

	return currentData, pastData, pastPastData


