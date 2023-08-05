from astropy import coordinates as ac
from lunarsky import spice_utils as su
from lunarsky.time import Time
from astropy.time import TimeDelta
import spiceypy as spice

su.furnish_kernels()
t0 = Time("J2000")
t1 = t0 + TimeDelta(5.5, format="jd")
lat = ac.Latitude("45d")
lon = ac.Longitude("0d")
fname = su.lunar_surface_ephem(lat, lon)  # , t0, t1)

spice.furnsh(fname)


# Covering full range from J2000 to now -- 38M, takes a few seconds.
