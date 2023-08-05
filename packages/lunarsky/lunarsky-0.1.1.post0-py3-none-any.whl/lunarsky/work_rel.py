"""
Try to construct the relativistic aberration on top of SPICE transformation.

http://malcolmdshuster.com/Pub_2003j_J_aber_AAS.pdf
"""

import numpy as np
from astropy import coordinates as ac
from astropy.time import Time
from astropy.utils.data import download_files_in_parallel
from lunarsky.spice_utils import topo_frame_def, furnish_kernels
import spiceypy as spice


# Transform a SkyCoord from ICRS to AltAz, first using astropy and then using SPICE
# Astropy transformation

icrs = ac.SkyCoord.from_name("crab")

# t0 = Time("J2000")
t0 = Time.now()
loc = ac.EarthLocation.of_site("CHIME")
altaz = icrs.transform_to(ac.AltAz(obstime=t0, location=loc))
print(altaz)


# Spice transformation


# Furnish standard and Moon kernels
furnish_kernels()

# Add needed Earth kernel
kname = "pck/earth_latest_high_prec.bpc"
_naif_kernel_url = "https://naif.jpl.nasa.gov/pub/naif/generic_kernels"
kurl = [_naif_kernel_url + "/" + kname]
kernpath = download_files_in_parallel(
    kurl, cache=True, show_progress=False, pkgname="lunarsky"
)
spice.furnsh(kernpath)

# Add earth topo frame
framename, idnum, frame_dict, latlon = topo_frame_def(
    loc.lat.deg, loc.lon.deg, moon=False
)
frame_strs = ["{}={}".format(k, v) for (k, v) in frame_dict.items()]
spice.lmpool(frame_strs)

# Do transformation
et = (t0 - Time("J2000")).sec
mat = spice.pxform("J2000", framename, et)

icrs_cart = icrs.icrs.cartesian.xyz


newrepr = icrs.icrs.cartesian.transform(mat)

spice_altaz = ac.AltAz(obstime=t0, location=loc).realize_frame(newrepr)
print(spice_altaz)
import IPython

IPython.embed()
