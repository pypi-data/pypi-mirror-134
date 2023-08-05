import astropy.coordinates as ac
from lunarsky.time import Time
from lunarsky import LunarTopo
from lunarsky.moon import MoonLocation

loc = MoonLocation.from_selenodetic(lat=22, lon=0.5)
t0 = Time.now()
t0.location = loc
bod = ac.get_body("jupiter", t0)
res = bod.transform_to(LunarTopo(location=loc, obstime=t0))
print(res)
import IPython

IPython.embed()
