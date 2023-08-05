import astropy.coordinates as ac
from astropy.utils import data as adata
from lunarsky.time import Time
from astropy.time import TimeDelta
import astropy.units as u
from lunarsky import LunarTopo
from lunarsky.moon import MoonLocation
import numpy as np

import pylab as pl
import spiceypy as spice

# TODO -- Add this furnsh to spice setup for transformations:
# path = adata.cache_contents()['https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de430.bsp']
# spice.furnsh(path)


loc = MoonLocation.from_selenodetic(lat=22, lon=0.5)
ts1 = np.arange(
    Time("2025-01-01T00:00:00"), Time("2025-02-01T00:00:00"), TimeDelta(5 * u.h)
).astype(Time)
ts2 = np.arange(
    Time("2025-02-01T00:00:00"), Time("2025-03-01T00:00:00"), TimeDelta(5 * u.h)
).astype(Time)

# getsun = lambda ts: [float(ac.get_body("sun",t_).transform_to(LunarTopo(location=loc, obstime=t_)).alt/u.deg) for t_ in ts]
getsun = lambda ts: [
    float(
        ac.get_body("sun", t_).transform_to(LunarTopo(location=loc, obstime=t_)).alt
        / u.deg
    )
    for t_ in ts
]

obj = ac.SkyCoord(ra=15 * u.deg, dec=20 * u.deg, frame="icrs")
getobj = lambda ts: [
    float(obj.transform_to(LunarTopo(location=loc, obstime=t_)).alt / u.deg) for t_ in ts
]

# fulltime = np.hstack((ts1, ts2))
fulltime = ts1  # np.hstack((ts1, ts2))
ets = np.array([(ft - Time("J2000")).sec for ft in fulltime])

ft_sec = np.array([(ft - fulltime[0]).sec for ft in fulltime])
sun_alt_deg = getsun(fulltime)
obj_alt_deg = getobj(fulltime)

kname = "pck/earth_latest_high_prec.bpc"
_naif_kernel_url = "https://naif.jpl.nasa.gov/pub/naif/generic_kernels"
kurl = [_naif_kernel_url + "/" + kname]
kernpath = adata.download_files_in_parallel(
    kurl, cache=True, show_progress=False, pkgname="lunarsky"
)
spice.furnsh(kernpath)
path = adata.cache_contents()[
    "https://naif.jpl.nasa.gov/pub/naif/generic_kernels/spk/planets/de430.bsp"
]
spice.furnsh(path)

# Get sun position in J2000 from spice
sun_vecs = np.asarray(
    [spice.spkpos("SUN", et, "J2000", "None", "301098")[0] for et in ets]
)
mats = np.asarray([spice.pxform("J2000", "LUNAR-TOPO", et) for et in ets])
sun_vecs = (sun_vecs.T / np.linalg.norm(sun_vecs, axis=1)).T  # Normalize
# import IPython; IPython.embed()
sun_topo = np.einsum("xyz,xz->xy", mats, sun_vecs)

sun_top = LunarTopo(location=loc).realize_frame(ac.CartesianRepresentation(sun_topo.T))

sun_alt_deg_spc = sun_top.alt.deg

# Fourier analysis
# ks = np.fft.fftshift(np.fft.fftfreq(ft_sec.size, d=1/24))
# _sun = np.fft.fftshift(np.fft.fft(sun_alt_deg))
# _obj = np.fft.fftshift(np.fft.fft(obj_alt_deg))
# pl.plot(ks, np.abs(_sun)**2)
# pl.plot(ks, np.abs(_obj)**2)

# ( Difference between peak and trough in sec * 2 / (24 * 3600)) == Period in days
print(
    "Astropy sun pos: ",
    np.abs(ets[np.argmax(sun_alt_deg)] - ets[np.argmin(sun_alt_deg)]) / (3600 * 12),
)
print(
    "SPICE sun pos: ",
    np.abs(ets[np.argmax(sun_alt_deg_spc)] - ets[np.argmin(sun_alt_deg_spc)])
    / (3600 * 12),
)
print(
    "Astropy obj pos: ",
    np.abs(ets[np.argmax(obj_alt_deg)] - ets[np.argmin(obj_alt_deg)]) / (3600 * 12),
)

# NOTE
#!!!  Key difference:
#   The get_sun() function gives the Sun's position in gcrs, including its distance.
#   Transforming to ICRS gives the Sun's position relative to SSB.
#   The vector we need is pointing from the lunar surface position to the Sun. The matrix changes the components from J2000 axes to Lunar Topo axes. This is what is returned by spkpos.

#   GCRS vector
#   To get the correct answer from astropy:
#       > Get GCRS position of the Sun.
#       > Get GCRS position of the lunar surface point.
#       > Subtract the two and normalize.?


import IPython

IPython.embed()
