# coding: utf-8

## For the correct transformation -- subtract position (ICRS) of lunar station from the (ICRS) position of the source before applying the rotation.

sun_icrs_spc = (
    spice.spkpos("10", (tt - Time("J2000")).sec, "J2000", "None", "301098")[0] * units.km
)
sun_icrs_ap = ac.get_sun(tt).transform_to("icrs").cartesian.xyz
sun_icrs_ap
sun_icrs_spc
lsp_icrs = spice.spkpos("301098", ets[0], "J2000", "None", "0")[0] * units.km
lsp_icrs
sun_icrs_ap - lsp_icrs
(sun_icrs_ap - lsp_icrs).to("km")
sun_icrs_spc
