
import ipdb
import os
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

dataFilename = "../data/All_three_exp_conditions_3.csv"
figFilename = "figures/absSpeedVsSpikesV1.png"
data = pd.read_csv(dataFilename, index_col=0)

print(data.columns.values)
# 'Expt #', 'Cell #', 'Speed', 'Bin(i)', 'Bin(i+1)', 'Bin(i+2)', 'Bin(i+3)', 
# 'Bin(i+4)', 'Bin(i+5)', 'Trial Condition', 'Region', 'Layer', 'Cell Type'

trialConditions = data.loc[:, "Trial Condition"].unique()
print(trialConditions)
# ['Vestibular' 'VisVes' 'Visual']

regions = data.loc[:, "Region"].unique()
print(regions)
# ['SUB' nan 'V1' 'SC' 'RSPg' 'RSPd' 'Hip']

# We will make a figure with len(trialConditions)==3 panels
f, axes = plt.subplots(1, len(trialConditions), sharey=True)

### Start first panel

# Extract the subset of the data corresponding to vestibular-only stimulation
# and recordings from V1
dataSubset = data.loc[(data["Trial Condition"]=="Vestibular") & (data["Region"]=="V1"),:]

# Plot the spikes counts in Bin(i) as a function of the absolute value of
# the stimulation speed
axes[0].scatter(abs(dataSubset["Speed"]), dataSubset["Bin(i)"], c="lightgray")
axes[0].set_title("Vestibular")

# Estimate the regression line
regressors = sm.add_constant(abs(dataSubset["Speed"]))
   # fit.params contains the regression coefficients
   # fit.pvalues contains the regression coefficients pvalues
fit = sm.OLS(dataSubset["Bin(i)"], regressors).fit()

# Plot the regression line
legend = "p={:.4f}".format(fit.pvalues[1])
axes[0].plot(abs(dataSubset["Speed"]), fit.params[0]+abs(dataSubset["Speed"])*fit.params[1], color="red", label=legend)
axes[0].legend(loc="upper left")

axes[0].set_title("Vestibular")
axes[0].set_xlabel("Abs(Speed)")
axes[0].set_ylabel("Spike Count")

### End first panel

### Start second panel

# Extract the subset of the data corresponding to vestibular-only stimulation
# and recordings from V1
dataSubset = data.loc[(data["Trial Condition"]=="VisVes") & (data["Region"]=="V1"),:]

# Plot the spikes counts in Bin(i) as a function of the absolute value of
# the stimulation speed
axes[1].scatter(abs(dataSubset["Speed"]), dataSubset["Bin(i)"], c="lightgray")
axes[1].set_title("Vestibular")

# Estimate the regression line
regressors = sm.add_constant(abs(dataSubset["Speed"]))
   # fit.params contains the regression coefficients
   # fit.pvalues contains the regression coefficients pvalues
fit = sm.OLS(dataSubset["Bin(i)"], regressors).fit()

# Plot the regression line
legend = "p={:.4f}".format(fit.pvalues[1])
axes[1].plot(abs(dataSubset["Speed"]), fit.params[0]+abs(dataSubset["Speed"])*fit.params[1], color="red", label=legend)
axes[1].legend(loc="upper left")

axes[1].set_title("VisVes")
axes[1].set_xlabel("Abs(Speed)")
axes[1].set_ylabel("Spike Count")

### End second panel

### Start third panel

# Extract the subset of the data corresponding to vestibular-only stimulation
# and recordings from V1
dataSubset = data.loc[(data["Trial Condition"]=="Visual") & (data["Region"]=="V1"),:]

# Plot the spikes counts in Bin(i) as a function of the absolute value of
# the stimulation speed
axes[2].scatter(abs(dataSubset["Speed"]), dataSubset["Bin(i)"], c="lightgray")
axes[2].set_title("Vestibular")

# Estimate the regression line
regressors = sm.add_constant(abs(dataSubset["Speed"]))
   # fit.params contains the regression coefficients
   # fit.pvalues contains the regression coefficients pvalues
fit = sm.OLS(dataSubset["Bin(i)"], regressors).fit()

# Plot the regression line
legend = "p={:.4f}".format(fit.pvalues[1])
axes[2].plot(abs(dataSubset["Speed"]), fit.params[0]+abs(dataSubset["Speed"])*fit.params[1], color="red", label=legend)
axes[2].legend(loc="upper left")

axes[2].set_title("Visual")
axes[2].set_xlabel("Abs(Speed)")
axes[2].set_ylabel("Spike Count")

### End second panel

plt.savefig(figFilename)

f.show()

ipdb.set_trace()
