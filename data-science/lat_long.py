import pandas as pd
import gmplot
#key=AIzaSyDmVT43htBcazX5AIreTbQwo2v_c3bAKT4

f = open("/Users/terences/Desktop/us-poi-subset.txt")

#map using entries[0] as keys
entries = [x.split('\t') for x in f.readlines()]
entry_lats = []
entry_longs = []
for entry in entries[1:]:
    entry_lats.append(float(entry[3]))
    entry_longs.append(float(entry[4]))
entry_tbl = pd.DataFrame(entries[1:], columns=entries[0])
# print entry_tbl

#map using citylines[0]
# wc = open("/Users/terences/Desktop/worldcitiespop.txt")
# citylines = [x.split(',') for x in wc.readlines()]
# print citylines[5]
# city_tbl = pd.DataFrame(citylines[1:], columns=citylines[0])
# print city_tbl


# send data to pandas colums
# load list of cities and their lat longs
#
gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)
gmap.scatter(entry_lats, entry_longs, 'conflowerblue')

gmap.draw("mymap.html")
