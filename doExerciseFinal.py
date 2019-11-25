
import ipdb
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append("../src")
import plotFunctions
import stats
import utils

def getSlopePValueLegend(stats, legendPattern="p={:.4f}"):
    legend = legendPattern.format(stats[1])
    return legend

def getSlopeCILegend(stats, legendPattern="95% CI=[{:.2f},{:.2f}]"):
    legend = legendPattern.format(stats[0], stats[1])
    return legend

dataFilename = "data/All_three_exp_conditions_3.csv"
figFilename = "figures/absSpeedVsSpikesFinal.png"
df = pd.read_csv(dataFilename, index_col=0)

print(df.columns.values)
# 'Expt #', 'Cell #', 'Speed', 'Bin(i)', 'Bin(i+1)', 'Bin(i+2)', 'Bin(i+3)', 
# 'Bin(i+4)', 'Bin(i+5)', 'Trial Condition', 'Region', 'Layer', 'Cell Type'

trialConditions = df.loc[:, "Trial Condition"].unique()
print(trialConditions)
# ['Vestibular' 'VisVes' 'Visual']

regions = df.loc[:, "Region"].unique()
print(regions)
# ['SUB' nan 'V1' 'SC' 'RSPg' 'RSPd' 'Hip']

f, axes = plt.subplots(1, len(trialConditions), sharey=True)
for i, trialCondition in enumerate(trialConditions):
    dfSubset = utils.getDataSubset(data=df,
                                   condColName1="Trial Condition",
                                   condValue1=trialCondition,
                                   condColName2="Region",
                                   condValue2="V1")
    x = abs(dfSubset["Speed"])
    y = dfSubset["Bin(i)"]

#     plotFunctions.plotRegressionPanel(ax=axes[i], x=x, y=y,
#                                       coefsAndStatsFn=stats.getCoefsAndPValues,
#                                       statsLegendFn=getSlopePValueLegend,
#                                       title=trialCondition)

    plotFunctions.plotRegressionPanel(ax=axes[i], x=x, y=y,
                                      coefsAndStatsFn=stats.getCoefsAndSlopeCI,
                                      statsLegendFn=getSlopeCILegend,
                                      title=trialCondition)

utils.savefig(figFilename)
f.show()

ipdb.set_trace()
