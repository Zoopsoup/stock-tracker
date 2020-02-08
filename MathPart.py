import yfinance as yf
import matplotlib.pyplot as plt

def stockPriceCalculator(name, initAmount, startDate, endDate):
    numOfStocks = 0
    initInvestment = 0.00
    initStockPrice = 0.00
    endStockPrice = 0.00
    endValueOfInvestment = 0.00
    investmentGain = 0.00
    percentageGain = 0.00


    initStockPrice = stockPriceLocator(name, startDate)
    endStockPrice = stockPriceLocator(name, endDate)

    numOfStocks = int(initAmount/initStockPrice)
    print ("The value of the stock on " + startDate + " was $" + str(initStockPrice))
    initInvestment = numOfStocks * initStockPrice
    print("You were able to buy " + str(numOfStocks) + " stocks at $" + str(initInvestment))

    endValueOfInvestment = round((numOfStocks * endStockPrice), 2)
    print ("The value of the stock on " + endDate + " was $" + str(endStockPrice))
    print("Your investment was worth $" + str(endValueOfInvestment) + " on " + endDate)

    investmentGain = round((endValueOfInvestment - initInvestment), 2)
    print("Your investment gained $" + str(investmentGain))

    percentageGain = round(((endValueOfInvestment - initInvestment)/initInvestment) * 100, 2)
    print("That's a " + str(percentageGain) + "% gain!")


def stockPriceLocator(name1, date):
    stockName = yf.Ticker(name1)
    stockPrice = 0.00

    stockDataTable = stockName.history(start = date, end = date)
    print (stockDataTable)
    stockPrice = float(stockDataTable.loc[date, "Close"])
    return stockPrice

def stockPlotter(name2, startDate2, endDate2):
    stockName = yf.Ticker(name2)
    dateList = []
    priceList = []
    stockDataTable = stockName.history(start = startDate2, end = endDate2)
    for row in stockDataTable.itertuples():
        dateList.append(row.Index)
        priceList.append(row.Close)
    print (dateList)
    print (priceList)

stockPriceCalculator("TSLA", 1000, "2020-02-03", "2020-02-07")
stockPlotter("TSLA", "2020-02-03", "2020-02-07")