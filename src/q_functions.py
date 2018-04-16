

''' IMPORT STATEMENTS '''
import copy
import random
from random import randint
import numpy as np
import os

import constants as const
from data_retrieval import retrieve_data
from state_functions import *
from util import *
import time

'''
Explore And Exploit function
'''

def exploreAndExploit():
    Q = {}
    ''' Initialize required variables '''    
    day = 0
    iterations = 0
    data = retrieve_data()
    stocks  = const.STOCKS
    numShares = const.INITIAL_NUM_SHARES
    
    ''' Complete State of the Problem '''
    currentPrice = getStockPrices(data, stocks, const.EXPLORE_BEGIN_DAY)
    currentValue = getTotalValue(numShares, currentPrice)
    currentState = calculateState(numShares, currentPrice)
    currentStateId = generateId(currentState)

    print "############### INITIAL VALUES ######################"
    print  "Initial State : ", currentState
    print "Initial Id : ", currentStateId
    actions = getPossibleActions(strToList(str(currentState)))
    initializeQ(Q,currentStateId, actions)
    
    
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
        prevPrice = getStockPrices(data, stocks, 0)
        initialNumShares = prevShares
        
        ''' Trading over daily data '''
#         test = 0
        for day in range(const.EXPLORE_BEGIN_DAY + 1,const.EXPLORE_END_DAY):
            
            
            
            numShares = prevShares
            currentPrice = prevPrice
            
            currentValue = getTotalValue(numShares, currentPrice)
            currentState = calculateState(numShares, currentPrice)
            
            #epsilon = const.DECAY * const.EXPLORATION_ITERATIONS / (const.DECAY * const.EXPLORATION_ITERATIONS + iterations)
            epsilon = 1
            currentStateId = generateId(currentState)
#             print "0 : " + str((time.time() - test))
#             test = time.time()
            
            actions = getPossibleActions(currentState)
            
#             print "1 : " + str((time.time() - test))
#             test = time.time()
            
            stateAction = {}
            for eachAction in actions:
                idState = generateId(eachAction)
                stateAction[idState] = eachAction

            probable_actions = []
            probable_actions.append(random.choice(actions))
            
#             print "2 : " + str((time.time() - test))
#             test = time.time()
            
            optQValue = const.NEG_INFINITY
            optimalAction = None
            if Q.has_key(currentStateId):
                for stateId in Q[currentStateId].keys():
                    q_val = Q[currentStateId][stateId]
                    if q_val > optQValue and stateAction.has_key(stateId):
                        optQValue = q_val
                        optimalAction = stateAction[stateId]

            action = None
            if optimalAction == None:
                action = probable_actions[0]
            else:
                probable_actions.append(optimalAction)
                choice = np.random.choice([0,1],p=[epsilon,1.0-epsilon])
                action = probable_actions[choice]
            
#             print "3 : " + str((time.time() - test))
#             test = time.time()
            
            nextPrice = getStockPrices(data, stocks, day)
            nextNumShares = getNumShares(action, currentPrice, currentValue)
            nextValue = getTotalValue(nextNumShares, nextPrice)
            initValue = getTotalValue(initialNumShares, nextPrice)

            qLearning(Q,currentState, initValue, nextValue, action, const.ALPHA)

            prevPrice = nextPrice
            prevShares = nextNumShares
            iterations += 1
            
#             print "4 : " + str((time.time() - test))
#             test = time.time()
            
    ''' End of Explore Phase '''        
    
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
        
        if optQValue != float("-inf") and optQValue < 0:
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


'''
initializeQ : List, List of Lists
GIVEN  :  A state and all possible actions on that state.
EFFECT :  Initialize the values of
'''
def initializeQ(Q,state,actions):
    Q[str(state)] = {}
    for eachAction in actions:
        Q[str(state)][str(eachAction)] = 0

'''
getQValue : List, List -> Float
GIVEN : A List representing the current state of portfolio.
        A List representing the action to be performed on that state.
RETURNS: The Q-value corresponding to the state,action pair.
'''
def getQValue(Q,state,action):
    if Q.has_key(str(state)):
        if Q[str(state)].has_key(str(action)):
            return Q[str(state)][str(action)]
    return 0

'''
putQValue : List, List, Float
GIVEN : A List representing the current state of the portfolio
        A List representing the action which will be performed on it.
        A Float representing the value of the
EFFECT : A new value is added/appended in the Q list.
'''
def putQValue(Q,state,action,value):
    if Q.has_key(str(state)):
        Q[str(state)][str(action)] = value
    else:
        Q[str(state)] = {str(action):value}



'''
printQvalues :
EFFECT : Writes values from Q into a text file under output directory.
'''
def printQvalues(Q):
    filePath = os.path.abspath(const.FILE_STORE_Q_VALUES)
    fileObj = open(filePath,"w+")
    for each_state in Q.keys():
        tempStr = each_state + " : "
        for eachAction in Q[each_state].keys():
            tempStr += eachAction + " -> " + str(Q[each_state][eachAction]) + ", "
        tempStr += "\n"
        fileObj.write(tempStr)
    fileObj.close()



'''
qLearning : List, Float, String, Float, List, Float
GIVEN : A list denoting currentState,
        The current and next value of the Portfolio
        The unique 5-character id of the current state.
        alpha denotes the learning rate.
EFFECT : Updates Q-value to the new value found.
'''
def qLearning(Q,current_state, current_value, next_value, action, alpha):    

    if next_value - current_value < 0:
        rsa = - current_value
    else:
        rsa = next_value - current_value

    stateId = generateId(current_state)
    nextStateId = generateId(strToList(str(action)))
    qsa = getQValue(Q,stateId, nextStateId)
    
    optQValue = const.NEG_INFINITY
    if Q.has_key(nextStateId):
        for each_action in Q[nextStateId].keys():
            q_val = Q[nextStateId][each_action]
            if q_val > optQValue:
                optQValue = q_val
                
    if optQValue == const.NEG_INFINITY:
        optQValue = 0
    
    new_q = (1 - alpha) * qsa + alpha * (rsa + const.GAMMA * optQValue)
    putQValue(Q,stateId, nextStateId, float(new_q))
    
    
    
    

    