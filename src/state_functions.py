import copy
import constants as const

'''
getPossibleActions : List -> ActionsList
GIVEN : A list, which represents the state
RETURNS : A list of Possible Actions on given state.
'''
def getPossibleActions(lst):
    actions = []
    actions.append(lst)
    for index1 in range(0,len(lst)):
        for index2 in range(0,len(lst)):
            x = copy.deepcopy(lst)
            if x[index2] - const.ACTION_EXCHANGE_PERCENT  >= 0 and index1 != index2:
                x[index1] += const.ACTION_EXCHANGE_PERCENT * const.BROKERAGE
                x[index2] -= const.ACTION_EXCHANGE_PERCENT
                actions.append(x)
    return actions


'''
getNumShares : List, List, Float -> List
GIVEN :  A list representing current state,
         A list Price of the five stocks,
         Total value of portfolio
RETURNS : A list of 5 elements denoting the number
        of shares of each stock based on given input.
'''
def getNumShares(lst,currentPrice,value):
    numShares = []
    for index in range(0,len(lst)):
        num = ((lst[index] / 100.0) * value) / currentPrice[index]
        numShares.append(num)
    return numShares


'''
getTotalValue : List, List -> Float
GIVEN : A list having the number of shares of each stock.
        A list denoting the price of each stock on a particular day.
RETURNS : The total value of the portfolio based on given input.
'''
def getTotalValue(numShares, currentPrice):
    totalValue = 0
    for index in range(0,len(numShares)):
        totalValue += numShares[index] * currentPrice[index]
    return totalValue


'''
calculateState : List, List -> Float
GIVEN : A list having the number of shares of each stock.
        A list of the current prices of each stock.
RETURNS : The state calculated based on the totalValue and input parameters.
'''
def calculateState(numShares, currentPrice):
    totalValue = getTotalValue(numShares, currentPrice)
    state = []
    for index in range(0,len(numShares)):
        sharePercent = (numShares[index] * currentPrice[index] / totalValue) * 100
        state.append(sharePercent)
    return state


'''
getStockPrices : Dictionary, List, Integer -> List
GIVEN : A Dictionary storing the day-to-day prices of all stocks.
        A List of strings denoting the names of the stocks to search.
        An Integer denoting the day for which the price is to be searched.
RETURNS : A List of Prices for each stock for the given day.
'''
def getStockPrices(data,stocks,day):
    lst = []
    for eachStock in stocks:
        lst.append(data[eachStock][day][1])
    return lst
