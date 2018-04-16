
''' IMPORT STATEMENTS '''
from q_functions import exploreAndExploit
import constants as const
import time


def __init__():
    
    lstResult = []
    for i in range(0,const.RUNS):
        startTime = time.time()
        op = exploreAndExploit()
        endTime = time.time()
        rt = endTime - startTime
        lstResult.append("Run " + str(i) + " -> " + str(op) + "||| Run Time " + str(i) + " -> " + str(rt))
    
    print "########## RESULTS #############"
    for index in lstResult:
        print index
    print "################################"


if __name__ == "__main__":
    __init__()   
    
    
