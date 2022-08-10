#%%
import sys
sys.path.insert(0,'/work/mh0066/m300909/Aquaplanet_changed_rotation/src/')


import numpy as np
import xarray as xr
from basic_functions import *


#%%
# data for aqua planet control run
aqua_planet_rotation_1x = xr.open_dataset('/work/mh0066/m300909/mpiesm-1.2.01p7/'
                                            'experiments/aqua_control/outdata/aqua_'
                                            'control_1977_1986_echam_uv_gp_pl.nc',decode_times=True)

lat, lon, press = get_dimension(aqua_planet_rotation_1x)

# prognostic variables control run
prog_var = ['st','u','v','relhum','q']
temperature, u_wind, v_wind, rel_hum, spec_hum = get_variable(aqua_planet_rotation_1x,prog_var)

# radiation variables control run
rad_var = ['traf0','trad0']
olr_clr, olr = get_variable(aqua_planet_rotation_1x,rad_var)

#%%
# Relative Humidity control run
rel_hum_avg_1x = np.mean(rel_hum,axis=0)
tropo_rh_1x = tropo_RH(rel_hum_avg_1x,press)
zonal_rh_1x = np.mean(tropo_rh_1x,axis=1)




#%%
# data for aqua planet 2x rotation
aqua_planet_rotation_2x = xr.open_dataset('/work/mh0066/m300909/mpiesm-1.2.01p7/experiments/aqua_2_rotation/outdata/aqua_2_rotation_1977_1986_echam_uv_gp_pl.nc',decode_times=True)

# prognostic variables 2x rotation
temperature_2x, u_wind_2x, v_wind_2x, rel_hum_2x, spec_hum_2x = get_variable(aqua_planet_rotation_2x,prog_var)

# radiation variables 2x rotation
olr_clr_2x, olr_2x = get_variable(aqua_planet_rotation_2x,rad_var)

#%%
# Relative Humidity 2x rotation
rel_hum_avg_2x = np.mean(rel_hum_2x,axis=0)
tropo_rh_2x = tropo_RH(rel_hum_avg_2x,press)
zonal_rh_2x = np.mean(tropo_rh_2x,axis=1)



#%%
# data for aqua planet 4x rotation
aqua_planet_rotation_4x = xr.open_dataset('/work/mh0066/m300909/mpiesm-1.2.01p7/experiments/aqua_4_rotation/outdata/aqua_4_rotation_1977_1986_echam_uv_gp_pl.nc',decode_times=True)

# prognostic variables 4x rotation
temperature_4x, u_wind_4x, v_wind_4x, rel_hum_4x, spec_hum_4x = get_variable(aqua_planet_rotation_4x,prog_var)

# radiation variables 4x rotation
olr_clr_4x, olr_4x = get_variable(aqua_planet_rotation_4x,rad_var)

#%%
# Relative Humidity 4x rotation
rel_hum_avg_4x = np.mean(rel_hum_4x,axis=0)
tropo_rh_4x = tropo_RH(rel_hum_avg_4x,press)
zonal_rh_4x = np.mean(tropo_rh_4x,axis=1)



#%%
# data for aqua planet 0.5x rotation
aqua_planet_rotation_05x = xr.open_dataset('/work/mh0066/m300909/mpiesm-1.2.01p7/experiments/aqua_0.5_rotation/outdata/aqua_0.5_rotation_1977_1986_echam_uv_gp_pl.nc',decode_times=True)

# prognostic variables 0.5x rotation
temperature_05x, u_wind_05x, v_wind_05x, rel_hum_05x, spec_hum_05x = get_variable(aqua_planet_rotation_05x,prog_var)

# radiation variables 0.5x rotation
olr_clr_05x, olr_05x = get_variable(aqua_planet_rotation_05x,rad_var)

#%%
# Relative Humidity 0.5x rotation
rel_hum_avg_05x = np.mean(rel_hum_05x,axis=0)
tropo_rh_05x = tropo_RH(rel_hum_avg_05x,press)
zonal_rh_05x = np.mean(tropo_rh_05x,axis=1)

#%%
# Corrcoeff 0.5x b/w Tropospheric RH and clear sky OLR
tropo_rh_full_05x = tropo_RH(rel_hum_05x,press)
corrcoeff_trh_olrclr_05x = linregress_corrcoeff(tropo_rh_full_05x,olr_clr_05x)

#%%
# Plot Tropospheric Relative humidity 
label = ['0.5\u03A9', '    \u03A9', '  2\u03A9', '  4\u03A9']
color = ['tomato','darkgray','cornflowerblue','darkblue']

tropo_relhum = np.empty((4,len(lat)),dtype = float)
tropo_relhum[0] = zonal_rh_05x; tropo_relhum[1] = zonal_rh_1x; 
tropo_relhum[2] = zonal_rh_2x; tropo_relhum[3] = zonal_rh_4x; 
plot_zonal_rh = zonal_line_plot(lat, tropo_relhum, label, color, 'RH', 'Tropospheric Relative Humidity')

#%% 