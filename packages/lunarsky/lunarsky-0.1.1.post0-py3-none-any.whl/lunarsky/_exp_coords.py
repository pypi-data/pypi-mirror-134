# coding: utf-8
from lunarsky import spice_utils as su
import numpy as np
import spiceypy as spice

su.furnish_kernels()
spice.furnsh("lunar_point.bsp")
from astropy.time import Time

_J2000 = Time("J2000")
from astropy.time import Time, TimeDelta

times = Time.now() + np.arange(30) * TimeDelta(1, format="jd")
times
res = [spice.spkez(301098, (tt - _J2000).sec, "J2000", "None", 301)[0] for tt in times]
res = np.asarray(
    [spice.spkez(301098, (tt - _J2000).sec, "J2000", "None", 301)[0] for tt in times]
)
res.shape
res
import pylab as pl

get_ipython().run_line_magic("matplotlib", "")
dts = np.array([(tt - _J2000).sec for tt in times])
pl.scatter(res[:, 0], res[:, 1])
pl.scatter(dts, res[:, 1])
pl.scatter(res[:, 0], res[:, 2])
pl.scatter(dts, res[:, 4])
res = np.asarray(
    [spice.spkez(301098, (tt - _J2000).sec, "ITRS93", "None", 399)[0] for tt in times]
)
res = np.asarray(
    [spice.spkez(301098, (tt - _J2000).sec, "J2000", "None", 399)[0] for tt in times]
)
from astropy.utils.data import download_files_in_parallel

kname = "pck/earth_latest_high_prec.bpc"
_naif_kernel_url = "https://naif.jpl.nasa.gov/pub/naif/generic_kernels"
kurl = [_naif_kernel_url + "/" + kname]
kernpath = download_files_in_parallel(
    kurl, cache=True, show_progress=False, pkgname="lunarsky"
)
spice.furnsh(kernpath)
res = np.asarray(
    [spice.spkez(301098, (tt - _J2000).sec, "ITRS93", "None", 399)[0] for tt in times]
)
res = np.asarray(
    [spice.spkez(301098, (tt - _J2000).sec, "ITRF93", "None", 399)[0] for tt in times]
)
times = Time("2017-10-28:03:30:00") + np.arange(30) * TimeDelta(1, format="jd")
times = Time("2017-10-28T03:30:00") + np.arange(30) * TimeDelta(1, format="jd")
dts = np.array([(tt - _J2000).sec for tt in times])
res = np.asarray(
    [spice.spkez(301098, (tt - _J2000).sec, "ITRF93", "None", 399)[0] for tt in times]
)
su.furnish_kernels()
spice.gnpool("*301*", 0, 100)
spice.gnpool("*", 0, 500)
spice.ktotal("SPK")
from astropy.utils import data

data.cache_contents()
spice.furnsh(
    "/home/alanman/.astropy/cache/download/url/81759d1ce79568c123429fb8d589a7c6/contents"
)
res = np.asarray(
    [spice.spkez(301098, (tt - _J2000).sec, "ITRF93", "None", 399)[0] for tt in times]
)
RES
res
pl.scatter(res[:, 0], res[:, 2])
pl.scatter(res[:, 0], res[:, 1])
times = Time.now() + np.arange(30) * TimeDelta(1, format="jd")
dts = np.array([(tt - _J2000).sec for tt in times])
res = np.asarray(
    [spice.spkez(301098, (tt - _J2000).sec, "ITRF93", "None", 399)[0] for tt in times]
)
pl.scatter(res[:, 0], res[:, 2])
lat = 45.0
lon = 0
fd = su.topo_frame_def(lat, lon)
fd
fd[1]
get_ipython().run_line_magic("pinfo", "spice.pcpool")
from lunarsky.topo import _spice_setup

_spice_setup(lat, lon)
spice.gnpool("*", 0, 500)
fd
dts
topos = np.asarray(
    [
        spice.spkez(301098, (tt - _J2000).sec, "LUNAR-TOPO", "None", 301098)[0]
        for tt in times
    ]
)
topos
topos = np.asarray(
    [spice.spkez(10, (tt - _J2000).sec, "LUNAR-TOPO", "None", 301098)[0] for tt in times]
)
topos
pl.scatter(dts, topos[:, 0])
pl.scatter((dts - dts[0]) / (3600 * 24), topos[:, 0])
times = Time.now() + np.arange(35) * TimeDelta(0.5, format="jd") * 2
times = Time.now() + np.arange(35 * 2) * TimeDelta(0.5, format="jd")
ets = np.array([(tt - _J2000).sec for tt in times])
topos = np.asarray(
    [spice.spkez(10, (tt - _J2000).sec, "LUNAR-TOPO", "None", 301098)[0] for tt in times]
)
pl.scatter((ets - ets[0]) / (3600 * 24), topos[:, 0])
topos = np.asarray(
    [spice.spkez(399, (tt - _J2000).sec, "LUNAR-TOPO", "None", 301098)[0] for tt in times]
)
pl.scatter((ets - ets[0]) / (3600 * 24), topos[:, 0])
topos = np.asarray(
    [spice.spkez(10, (tt - _J2000).sec, "LUNAR-TOPO", "None", 301098)[0] for tt in times]
)
pl.scatter((ets - ets[0]) / (3600 * 24), topos[:, 0])
topos = np.asarray(
    [spice.spkez(999, (tt - _J2000).sec, "LUNAR-TOPO", "None", 301098)[0] for tt in times]
)
topos = np.asarray(
    [spice.spkez(899, (tt - _J2000).sec, "LUNAR-TOPO", "None", 301098)[0] for tt in times]
)
topos = np.asarray(
    [spice.spkez(499, (tt - _J2000).sec, "LUNAR-TOPO", "None", 301098)[0] for tt in times]
)
mats = np.asarray([spice.spkez("J2000", "LUNAR-TOPO", et)[0] for et in ets])
mats = np.asarray([spice.pxform("J2000", "LUNAR-TOPO", et)[0] for et in ets])
get_ipython().run_line_magic("pinfo", "spice.pxfrm2")
get_ipython().run_line_magic("pinfo", "spice.pxform")
from astropy import coordinates as ac

src = ac.SkyCoord.from_name("crab")
src.icrs.cartesian.xyz.to_value("m")
src.icrs.cartesian.xyz
svec = src.icrs.cartesian.xyz.value
mats.shape
crab_topo = np.dot(mats, svec)
pl.scatter((ets - ets[0]) / (3600 * 24), crab_topo[:, 0])
pl.scatter((ets - ets[0]) / (3600 * 24), crab_topo[0, :])
crab_topo.shape
mats = np.asarray([spice.pxform("J2000", "LUNAR-TOPO", et) for et in ets])
mats.shape
crab_topo = np.dot(mats, svec)
crab_topo.shape
pl.scatter((ets - ets[0]) / (3600 * 24), crab_topo[:, 0])
crab_topo
pl.scatter((ets - ets[0]) / (3600 * 24), crab_topo[:, 1])
pl.scatter((ets - ets[0]) / (3600 * 24), crab_topo[:, 2])
get_ipython().run_line_magic("pinfo", "spice.pxform")
topos = np.asarray(
    [spice.spkez(499, (tt - _J2000).sec, "LUNAR-TOPO", "None", 301098)[0] for tt in times]
)
topos = np.asarray(
    [spice.spkez(10, (tt - _J2000).sec, "LUNAR-TOPO", "None", 301098)[0] for tt in times]
)
topos.shape
topo_sun = np.asarray([t[:3] / np.linalg.norm(t[:3]) for t in topos])
topo_sun.shape
pl.scatter((ets - ets[0]) / (3600 * 24), crab_topo[:, 2])
pl.scatter((ets - ets[0]) / (3600 * 24), topo_sun[:, 2])
ets[np.argmax(topo_sun[:, 2])] - ets[np.argmin(topo_sun[:, 2])]
np.abs(ets[np.argmax(topo_sun[:, 2])] - ets[np.argmin(topo_sun[:, 2])]) / (3600 * 24)
np.abs(ets[np.argmax(topo_sun[:, 2])] - ets[np.argmin(topo_sun[:, 2])]) / (3600 * 12)
np.abs(ets[np.argmax(crab_topo[:, 2])] - ets[np.argmin(crab_topo[:, 2])]) / (3600 * 12)
sun_vecs = np.asarray(
    [ac.get_sun(tt).transform_to(ac.ICRS()).cartesian.xyz.value for tt in times]
)
sun_vecs.shape
sun_vecs
np.linalg.norm(sun_vecs, axis=1)
np.linalg.norm(sun_vecs, axis=0)
sun_vecs = np.asarray(
    [ac.get_sun(tt).transform_to(ac.ICRS()).cartesian.xyz for tt in times]
)
sun_vecs.shape
sun_vecs[0]
ac.get_sun(times[0])
ac.get_sun(times[0]).transform_to(ac.ICRS())
sun_vecs /= np.linalg.norm(sun_vecs, axis=1)
sun_vecs /= np.linalg.norm(sun_vecs, axis=0)
sun_vecs.shape
np.linalg.norm(sun_vecs, axis=1)
np.linalg.norm(sun_vecs, axis=0)
sun_vecs = np.asarray(
    [ac.get_sun(tt).transform_to(ac.ICRS()).cartesian.xyz for tt in times]
)
sun_vecs /= np.linalg.norm(sun_vecs, axis=1).T
sun_vecs = (sun_vecs.T / np.linalg.norm(sun_vecs, axis=1)).T
sun_vecs.shape
np.linalg.norm(sun_vecs, axis=1)
sun_topo = np.dot(mats, sun_vecs)
sun_topo = np.dot(mats, sun_vecs.T)
sun_topo.shape
sun_topo = np.dot(mats, sun_vecs)
sun_topo = np.einsum("xyz,xz->xy", mats, sun_vecs)
sun_topo.shape
pl.scatter((ets - ets[0]) / (3600 * 24), sun_topo[:, 2])
np.abs(ets[np.argmax(sun_topo[:, 2])] - ets[np.argmin(sun_topo[:, 2])]) / (3600 * 12)
np.abs(ets[np.argmax(topo_sun[:, 2])] - ets[np.argmin(topo_sun[:, 2])]) / (3600 * 12)
sun_vecs = np.asarray([None for et in ets])
get_ipython().run_line_magic("pinfo", "spice.spkpos")
sun_vecs = np.asarray([spice.spkpos(10, et, "J2000", "None", 301098)[0] for et in ets])
sun_vecs = np.asarray([spice.spkpos("SUN", et, "J2000", "None", 301098)[0] for et in ets])
sun_vecs = np.asarray(
    [spice.spkpos("SUN", et, "J2000", "None", "301098")[0] for et in ets]
)
sun_vecs.shape
sun_vecs = (sun_vecs.T / np.linalg.norm(sun_vecs, axis=1)).T
sun_vecs.shape
np.linalg.norm(sun_vecs, axis=1)
ap_sun_vecs = np.asarray(
    [ac.get_sun(tt).transform_to(ac.ICRS()).cartesian.xyz for tt in times]
)
ap_sun_vecs = (ap_sun_vecs.T / np.linalg.norm(ap_sun_vecs, axis=1)).T
sun_vecs
ap_sun_vecs
sun_vecs
ap_sun_vecs
sun_vecs
ap_sun_vecs
sun_topo = np.einsum("xyz,xz->xy", mats, sun_vecs)
pl.scatter((ets - ets[0]) / (3600 * 24), sun_topo[:, 2])
np.abs(ets[np.argmax(sun_topo[:, 2])] - ets[np.argmin(sun_topo[:, 2])]) / (3600 * 12)
ap_sun_topo = np.einsum("xyz,xz->xy", mats, ap_sun_vecs)
np.abs(ets[np.argmax(ap_sun_topo[:, 2])] - ets[np.argmin(ap_sun_topo[:, 2])]) / (
    3600 * 12
)
test
test = topo_frame_def(15, 0)
test = su.topo_frame_def(15, 0)
test
get_ipython().run_line_magic("pinfo", "spice.pcpool")
spice.gcpool("LAT_LON")
spice.gcpool("TOPO_LAT_LON", 1, 100)
spice.gcpool("TOPO_LAT_LON", 1, 200)
spice.gcpool("TOPO_LAT_LON", 0, 200)
test
test = su.topo_frame_def(15, 0)
test
from lunarsky import LunarTopo

get_ipython().run_line_magic("pinfo", "LunarTopo")
get_ipython().run_line_magic("pinfo", "LunarTopo.realize_frame")
sun_topo
test = LunarTopo.realize_frame(sun_topo)
get_ipython().set_next_input("test = LunarTopo.realize_frame")
get_ipython().run_line_magic("pinfo", "LunarTopo.realize_frame")
test = LunarTopo().realize_frame(data)
test = ac.CartesianRepresentation(sun_topo)
test = ac.CartesianRepresentation(sun_topo.T)
test
t2 = LunarTopo().realize_frame(test)
t2
