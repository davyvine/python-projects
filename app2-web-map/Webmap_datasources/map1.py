import folium
import pandas

# load data file
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """ 
<h4>Volcano information:</h4>
Volcano name: %s<br>
Height: %s m
"""


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# base map
map = folium.Map(location=[38.58, -99.09],
                 zoom_start=6, tiles="Stamen Terrain")

# adding points or markers on the map
fgv = folium.FeatureGroup(name="Volcano")
# to add multiple markers add a for loop
# lt -> lat , ln -> lon zip distributes items 1 by 1
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, el), width=200, height=100)
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6,
                                      popup=folium.Popup(iframe), fill_color=color_producer(el), color='grey', fill_opacity=0.7))


# add third layer using another json file
fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(
    data=(open('world.json', 'r', encoding='utf-8-sig').read()),
    style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                              else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                              else 'red'}))  # fill color attribute is not in json file but a new one

# layer control
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

# save as html
map.save("Map1.html")
