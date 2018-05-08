
''' IMPORT STATEMENTS '''
import copy
import random
from random import randint
import numpy as np

from data_retrieval import retrieve_data
from state_functions import *
from q_functions import *
from util import *
import constants as const

'''
Run function
'''
def __init__():

    ''' Initialize required variables '''
    Q = {}
    day = 0
    data = retrieve_data()
    stocks  = const.STOCKS
    numShares = const.INITIAL_NUM_SHARES
    currentPrice = getStockPrices(data, stocks, const.EXPLORE_BEGIN_DAY)
    currentValue = getTotalValue(numShares, currentPrice)
    currentState = calculateState(numShares, currentPrice)
    currentStateid = generateId(currentState)

    print "############### INITIAL VALUES ######################"
    print  "Initial State : ", currentState
    print "Initial Id : ", currentStateid

    
    
    ''' Iterate to Explore '''
    for itr in range(1,const.EXPLORATION_ITERATIONS):
        print "Explore Iteration : ", itr

        ''' assign random share values for each stock to portfolio '''
        shareA = random.randrange(0,40,4)
        shareB = random.randrange(0,150,15)
        shareC = random.randrange(0,3000,300)
        shareD = random.randrange(0,150,15)
        shareE = random.randrange(0,1000,100)
        prevShares = [shareA,shareB,shareC,shareD,shareE]
        initialNumShares = prevShares
        prevPrice = getStockPrices(data, stocks, 0)
        
        ''' Trading over daily data '''
        for day in range(const.EXPLORE_BEGIN_DAY + 1,const.EXPLORE_END_DAY):
            numShares = prevShares
            currentPrice = prevPrice
            currentValue = getTotalValue(numShares, currentPrice)
            currentState = calculateState(numShares, currentPrice)
            actions = getPossibleActions(currentState)

            action = random.choice(actions)  
            
            currentStateId = generateId(currentState)
            nextPrice = getStockPrices(data, stocks, day)
            nextNumShares = getNumShares(action, currentPrice, currentValue)
            nextValue = getTotalValue(nextNumShares, nextPrice)
            initValue = getTotalValue(initialNumShares, nextPrice)
            
            qLearning(Q,currentState, initValue, nextValue, action, const.ALPHA)

            prevPrice = nextPrice
            prevShares = nextNumShares

    print "Length of Q States ",len(Q.keys())
    print "******************************"
    prevShares = const.INITIAL_NUM_SHARES
    prevPrice = getStockPrices(data, stocks, const.EXPLORE_END_DAY)
    currentValue = getTotalValue(prevShares, currentPrice)
    currentState = calculateState(prevShares, currentPrice)
    print currentState,currentValue
    
    for day in range(const.EXPLOIT_BEGIN_DAY,const.EXPLOIT_END_DAY+1):
        numShares = prevShares
        currentPrice = prevPrice
        currentValue = getTotalValue(numShares, currentPrice)
        currentState = calculateState(numShares, currentPrice)
        currentStateId = generateId(currentState)
        print currentStateId
        actions = getPossibleActions(currentState)

        stateAction = {}
        for eachAction in actions:
            idState = generateId(eachAction)
            stateAction[idState] = eachAction


        optQValue = const.NEG_INFINITY
        action = None
        if Q.has_key(currentStateId):
            optimalAction = None
            for stateId in Q[currentStateId].keys():
                q_val = Q[currentStateId][stateId]
                if q_val > optQValue and stateAction.has_key(stateId):
                    optQValue = q_val
                    optimalAction = stateAction[stateId]

            action = optimalAction
        
        if optQValue!=const.NEG_INFINITY and optQValue < 0:
            action = actions[0]
        
        if action == None:
            action = random.choice(actions)
                
        nextPrice = getStockPrices(data, stocks, day)
        nextNumShares = getNumShares(action, currentPrice, currentValue)
        nextValue =  getTotalValue(nextNumShares, nextPrice)
        initValue = getTotalValue(const.INITIAL_NUM_SHARES,nextPrice)
        
        qLearning(Q,currentState, initValue, nextValue, action, const.ALPHA)


        print "Action : ", action
        print nextNumShares
        print nextValue
        prevPrice = nextPrice
        prevShares = nextNumShares
    
    
    
    
    print "######### EXPLOIT END VALUES #####################"
    print "State - ", currentState
    print "Number of Shares - ", nextNumShares
    print "Value - ", nextValue

    print "######### BENCHMARK VALUES ########################"
    print "Value - Explore Begin Day - ", getTotalValue(const.INITIAL_NUM_SHARES, getStockPrices(data, stocks, const.EXPLORE_BEGIN_DAY))
    print "Value - Explore End Day - ", getTotalValue(const.INITIAL_NUM_SHARES, getStockPrices(data, stocks, const.EXPLORE_END_DAY))
    print "Value - Exploit End Day - ", getTotalValue(const.INITIAL_NUM_SHARES, getStockPrices(data, stocks, const.EXPLOIT_END_DAY))

    printQvalues(Q)
    return nextValue


if __name__ == "__main__":
    __init__()
