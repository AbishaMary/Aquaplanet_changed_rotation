import numpy as np
import xarray as xr
from itertools import islice
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
from scipy.stats import linregress


def get_dimension(data):

    " Extraction of the dimensions in arrays for the given data file "
    
    " Returns the latitude, longitude and pressure levels (in hPa)" 
    " in numpy arrays"

    " Parameters:" 
    " file_path  : data file "

    latitude = np.array(data['lat'])
    longitude = np.array(data['lon'])
    pressure_level = np.array(data['plev'])
    pressure_level = pressure_level/100
    return latitude,longitude,pressure_level


def get_variable(data,variable):

    " Extraction of required variables from the data file "

    " Returns the variables asked for in numpy arrays "

    " Parameters: "
    " file_path : data file "
    " variables : name of the variables as mentioned in the file "
  
    for i in range(len(variable)):
        var = np.array(data[variable[i]])[12:]
        yield var


def tropo_RH(rh,press):

    " Calculates the tropospjeric relative humidity with a"
    " weighing function having a maximum weight in the middle troposphere"

    " Returns an array of tropospheric relative humidity"

    " Paramters: "
    " rh: 3D relative humidity"
    " press: pressure levels in hPa"

    num = np.empty(np.shape(rh),dtype=float)
    den = np.empty(len(press),dtype=float)

    # maximum weight at 500hPa
    max_wt_press = press[np.argwhere(press==500).flatten()[0]]
    
    for i in range(len(press)):
        den[i] = np.exp(-2 * ( np.log(press[i]) - np.log(max_wt_press)) ** 2)* (press[i] - max_wt_press)
        
        # RH is a time average 
        if len(press) == len(rh): 
            num[i] = np.exp(-2 * ( np.log(press[i,None,None]) - np.log(max_wt_press)) ** 2) * rh[i,:,:] * (press[i,None,None] - max_wt_press)
        # RH has time dimension
        else: 
            num[:,i,:,:] = np.exp(-2 * ( np.log(press[None,i,None,None]) - np.log(max_wt_press)) ** 2) * rh[:,i,:,:] * (press[None,i,None,None] - max_wt_press)
    
    if len(press) == len(rh):
        tropo_rh = np.sum(num,axis=0)/np.sum(den)
    else:
        tropo_rh = np.sum(num,axis=1)/np.sum(den)  
    return tropo_rh


def zonal_line_plot(x, var, label, color, unit, title):

    " Plots the 1D array of any variables as a line plot for"
    " all the experiements"

    " Does not return any value rather it plots"

    " Parameters:"
    " x : 1D array of x values"
    " var : 1D array of any of the model parameters corresponding to y values"

    fig,ax = plt.subplots(figsize=(9,5))
    for i in range(len(var)):
        ax.plot(x, var[i], label = label[i], linewidth = 2, color = color[i])
        ax.xaxis.set_major_formatter(EngFormatter(unit=u"°"))
        ax.tick_params(axis='both', which='major', labelsize=12)
        ax.tick_params(axis='both', which='minor', labelsize=12)
        ax.set_ylabel(unit, fontsize=14)
        ax.set_title(title, fontsize='16')
        plt.legend(fontsize=12)
    
    
def linregress_corrcoeff(x,y):

    " Caluclates the Pearson correlation coefficient from line regression"

    " Returns an array of correlation coefficient values that corresponds to zonal values"

    " Parameter:"
    " x : 2D array of values time x lat"
    " y : same as x"

    if len(np.shape(x)) == 3:
        x = np.mean(x,axis=2)
        y = np.mean(y,axis=2)

    corrcoeff = np.empty(np.shape(x)[1],dtype=float)

    for i in range(np.shape(x)[1]):
        a,b,corrcoeff[i],d,e = linregress(x,y)
        
    return corrcoeff
