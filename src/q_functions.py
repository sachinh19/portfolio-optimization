
from util import *
import constants as const
import os

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
EFFECT : Writes values from Q into a notepad file.
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
qLearning : List, Float, Float, List, Float
GIVEN : A list denoting currentState,
        The current and next value of the Portfolio
        The action to be taken.
        alpha denotes the learning rate.
EFFECT : Updates Q-value to the new value found.
'''
def qLearning(Q,current_state, init_value, next_value, action, alpha):

    if next_value < init_value:
        rsa = - init_value
    else:
        rsa =  next_value - init_value
    stateId = generateId(current_state)
    nextStateId = generateId(strToList(str(action)))
    qsa = getQValue(Q,stateId, nextStateId)

    optQValue = const.NEG_INFINITY

    if Q.has_key(nextStateId):
        for eachAction in Q[nextStateId].keys():
            q_val = Q[nextStateId][eachAction]
            if q_val > optQValue:
                optQValue = q_val
    if optQValue == const.NEG_INFINITY:
        optQValue = 0

    new_q = (1 - alpha) * qsa + alpha * (rsa + const.GAMMA * optQValue)
    putQValue(Q,stateId, nextStateId, float(new_q))
