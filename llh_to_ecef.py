# llh_to_ecef.py
#
# Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km.
#  
# Parameters:
# lat_deg: Latitude in degrees
# lon_deg: Longitude in degrees
# hae_km: Height Above Ellipsoid in kilometers
# Output:
#  Prints the converged x, y, and z coordinates (km)
#
# Written by DT
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.137
E_E = 0.081819221456


# initialize script arguments
lat_deg = float('nan')    # Latitude in degrees
lon_deg = float('nan')    # Longitude in degrees
hae_km = float('nan')     # Height above ellipsoid in km

# parse script arguments
if len(sys.argv) == 4:
    lat_deg = float(sys.argv[1])
    lon_deg = float(sys.argv[2])
    hae_km = float(sys.argv[3])
else:
    print('Usage: python3 llh_to_ecef.py lat_deg lon_deg hae_km')
    exit()

# write script below this line

# Convert to radians
lat_rad = math.radians(lat_deg)
lon_rad = math.radians(lon_deg)

# initialize lat_rad, r_lon_km, r_z_km
C_E = R_E_KM / math.sqrt(1 - E_E**2 * math.sin(lat_rad)**2)

r_x_km = (C_E + hae_km) * math.cos(lat_rad) * math.cos(lon_rad)
r_y_km = (C_E + hae_km) * math.cos(lat_rad) * math.sin(lon_rad)
r_z_km = ((1 - E_E**2) * C_E + hae_km) * math.sin(lat_rad)

print(r_x_km)
print(r_y_km)
print(r_z_km)