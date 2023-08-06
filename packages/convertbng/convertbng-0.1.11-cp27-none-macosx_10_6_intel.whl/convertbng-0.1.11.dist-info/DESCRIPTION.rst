Fast lon, lat to BNG conversion
---------------------------------------------
Uses a Rust 1.0 binary to perform fast lon, lat to BNG conversion

This module exposes two methods:

util.convertbng() – pass a lon, lat. Returns a tuple of Eastings, Northings

util.convertbng_list() – pass lists of lons, lats. Returns a list of tuples


Call them like so:

from convertbng.util import convertbng, convertbng_list


res = convertbng(lon, lat)

res_list = convertbng([lons], [lats])



This version requires Python 2.7.x / 3.4.x

