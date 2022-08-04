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

#%%
rel_hum_avg = np.mean(rel_hum,axis=0)
tropo_rh = tropo_RH(rel_hum_avg,press)

zonal_rh = np.mean(tropo_rh,axis=0)




#%%
# data for aqua planet 2x rotation
aqua_planet_rotation_2x = xr.open_dataset('/work/mh0066/m300909/mpiesm-1.2.01p7/experiments/aqua_2_rotation/outdata/aqua_2_rotation_1977_1986_echam_uv_gp_pl.nc',decode_times=True)

# prognostic variables 2x rotation
temperature_2x, u_wind_2x, v_wind_2x, rel_hum_2x, spec_hum_2x = get_variable(aqua_planet_rotation_2x,prog_var)

# radiation variables 2x rotation
olr_clr_2x, olr_2x = get_variable(aqua_planet_rotation_2x,rad_var)





#%%
# data for aqua planet 4x rotation
aqua_planet_rotation_4x = xr.open_dataset('/work/mh0066/m300909/mpiesm-1.2.01p7/experiments/aqua_4_rotation/outdata/aqua_4_rotation_1977_1986_echam_uv_gp_pl.nc',decode_times=True)

# prognostic variables 4x rotation
temperature_4x, u_wind_4x, v_wind_4x, rel_hum_4x, spec_hum_4x = get_variable(aqua_planet_rotation_4x,prog_var)

# radiation variables 4x rotation
olr_clr_4x, olr_4x = get_variable(aqua_planet_rotation_4x,rad_var)





#%%
# data for aqua planet 0.5x rotation
aqua_planet_rotation_05x = xr.open_dataset('/work/mh0066/m300909/mpiesm-1.2.01p7/experiments/aqua_0.5_rotation/outdata/aqua_0.5_rotation_1977_1986_echam_uv_gp_pl.nc',decode_times=True)

# prognostic variables 0.5x rotation
temperature_05x, u_wind_05x, v_wind_05x, rel_hum_05x, spec_hum_05x = get_variable(aqua_planet_rotation_05x,prog_var)

# radiation variables 2x rotation
olr_clr_05x, olr_05x = get_variable(aqua_planet_rotation_05x,rad_var)
# %%
