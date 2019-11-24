
import numpy as np
import statsmodels.api as sm
import bootstrapped.bootstrap as bs
import ipdb

def getCoefsAndPValues(x, y):
    regressors = sm.add_constant(x)
    fit = sm.OLS(y, regressors).fit()
    return fit.params, fit.pvalues

def getCoefsAndSlopeCI(x, y, nIterations=10000):

    def getSlope(data):
        x = data[:,0]
        y = data[:,1]
        regressors = sm.add_constant(x)
        fit = sm.OLS(y, regressors).fit()
        return [fit.params[1]]

    regressors = sm.add_constant(x)
    fit = sm.OLS(y, regressors).fit()
    coefs = fit.params

    bootData = np.column_stack((x,y))
    bootRes = bs.bootstrap(bootData, stat_func=getSlope, num_iterations=nIterations)
    return coefs, (bootRes.lower_bound, bootRes.upper_bound)

