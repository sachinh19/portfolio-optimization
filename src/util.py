'''
generateId : List -> String
This function returns the unique id of the given state
GIVEN  : A List of stock proportion in percentages, denoting the state.
RETURNS: A String, derived from given stock percentage list, now the stateId.
'''
def generateId(lst):
    stateId = ""
    for element in lst:
        int1 = element / 5
        if element % 5 != 0:
            int1 += 1
        stateId += chr(65+int(int1))
    return stateId

'''
strToList : String -> List
GIVEN : A String of comma separated values
RETURNS : A list representing a state
'''
def strToList(str):
    lst = []
    for element in str.split("[")[1].split("]")[0].split(","):
        element = float(element)
        lst.append(element)
    return lst
