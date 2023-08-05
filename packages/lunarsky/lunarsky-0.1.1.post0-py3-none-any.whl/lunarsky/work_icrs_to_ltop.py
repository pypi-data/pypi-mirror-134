import astropy.coordinates as ac
from astropy.utils import data as adata
from lunarsky.time import Time
from astropy.time import TimeDelta
import astropy.units as u
from astropy.utils import data as adata
from lunarsky import LunarTopo
from lunarsky.moon import MoonLocation
import numpy as np

import pylab as pl
import spiceypy as spice

# kname = 'pck/earth_latest_high_prec.bpc'
# _naif_kernel_url = 'https://naif.jpl.nasa.gov/pub/naif/generic_kernels'
# kurl = [_naif_kernel_url + '/' + kname]
# kernpath = adata.download_files_in_parallel(kurl, cache=True, show_progress=False, pkgname='lunarsky')
# spice.furnsh(kernpath)


path = adata.cache_contents()[
    "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de430.bsp"
]
spice.furnsh(path)

print(spice.ktotal("SPK"))

tt = Time.now()
obj = ac.SkyCoord(ra=15 * u.deg, dec=20 * u.deg, frame="icrs")
sun = ac.get_sun(tt).transform_to("icrs")

loc = MoonLocation.from_selenodetic(lat=22, lon=0.5)
ltp = LunarTopo(location=loc, obstime=tt)

sun_top = sun.transform_to(ltp)
obj_top = obj.transform_to(ltp)

sun_top_sp = (
    spice.spkgeo(10, (tt - Time("J2000")).sec, "LUNAR-TOPO", 301098)[0][:3] * u.km
)

import IPython

IPython.embed()
