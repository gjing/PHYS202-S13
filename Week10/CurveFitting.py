import numpy as np

def LinearLeastSquaresFit(x,y):
    """Take in arrays representing (x,y) values for a set of linearly varying data and an array of weights w. 
    perform a linear least squares regression. Return the resulting slope and intercept
    parameters of the best fit line with their uncertainties"""
    n = len(x)
    xavg = np.mean(x)
    yavg = np.mean(y)
    xsquare = np.mean(x ** 2)
    xy = np.mean(x * y)
    slope = (xy - (xavg * yavg)) / (xsquare - (xavg**2))
    intercept = ((xsquare * yavg) - (xavg * xy))/(xsquare - xavg**2)
    usquare = np.mean((y - (slope*x + intercept))**2)
    slerr = (1/(n-2) * (usquare / (xsquare - xavg**2)))**.5
    interr = (1/(n-2) * (usquare * xsquare)/(xsquare - xavg**2))**.5
    return slope, intercept, slerr, interr

def WeightedLinearLeastSquaresFit(x,y,weight):
    """Take in arrays representing (x,y) values for a set of linearly varying data and an array of weights w. 
    perform a weighted linear least squares regression. Return the resulting slope and intercept
    parameters of the best fit line with their uncertainties"""
    w = sum(weight)
    weightless=True
    for i in weight:
        if i!=1:
            weightless=False
    if weightless:
        return LinearLeastSquaresFit(x,y)
    wx = sum(weight*x)
    wxsq = sum(weight*x**2)
    wy = sum(weight*y)
    wxy = sum(weight*x*y)
    slope = (wxsq*wy-wx*wxy)/(w*wxsq-wx**2)
    intercept = (w*wxy-wx*wy)/(w*wxsq-wx**2)
    slerr = (w/(w*wxsq-wx**2))**.5
    interr = (wxsq/(w*wxsq-wx**2))**.5
    return slope, slerr, intercept, interr
