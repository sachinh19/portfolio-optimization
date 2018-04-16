import pandas as pd
import os
import glob
import constants as const


def read_csv(filePath,data):
    x1 = pd.read_csv(filePath)
    fileName = os.path.basename(filePath).split(".csv")[0]
    data_set = []
    for i in x1.index:
        data_set.append((x1["Date"][i],x1["Open"][i]))

    data[fileName] = data_set


def retrieve_data():
    data = {}
    count = 0
    dirPath = os.path.abspath(const.DATA_DIRECTORY)
    for filePath in glob.glob(os.path.join(dirPath,"*.csv")):
        count += 1
        read_csv(filePath,data)
        
    return data

if __name__ == "__main__":
    retrieve_data()
