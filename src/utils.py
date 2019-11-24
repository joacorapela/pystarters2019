
import os
import matplotlib.pyplot as plt

def getDataSubset(data, condColName1, condValue1, condColName2, condValue2):
    if condColName1 not in data.columns:
        errorMsg = "{} is not in {}".format(condColName1, data.columns.values.tolist())
        raise RuntimeError(errorMsg)
    if condColName2 not in data.columns.values:
        errorMsg = "{} is not in {}".format(condColName2, data.columns.values.tolist())
        raise RuntimeError(errorMsg)
    dataSubset = data.loc[(data[condColName1]==condValue1) & (data[condColName2]==condValue2),:]
    return dataSubset

def savefig(figFilename):
    try:
        plt.savefig(figFilename)
    except FileNotFoundError:
        dirname = os.path.dirname(figFilename)
        print("File {} not found. Attempting to create directory {}".format(figFilename, dirname))
        os.mkdir(dirname)
        plt.savefig(figFilename)

