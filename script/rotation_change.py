import sys
sys.path.insert(0,'/work/mh0066/m300909/Aquaplanet_changed_rotation/src/')


import numpy as np
import xarray as xr
from basic_functions import *


# data for aqua planet control run
aqua_planet_rotation_1x = xr.open_dataset('/work/mh0066/m300909/mpiesm-1.2.01p7/'
                                            'experiments/aqua_control/outdata/aqua_'
                                            'control_1977_1986_echam_uv_gp_pl.nc',decode_times=True)

lat, lon, press = get_dimension(aqua_planet_rotation_1x)

# prognostic variables 
prog_var = ['st','u','v','relhum','q']
temperature, u_wind, v_wind, rel_hum, spec_hum = get_variable(aqua_planet_rotation_1x,prog_var)

# radiation variables
rad_var = ['traf0','trad0']
olr_clr, olr = get_variable(aqua_planet_rotation_1x,rad_var)


