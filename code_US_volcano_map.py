# importing folium libary in order to operate on leaflet maps objects
import folium
import pandas
# loading data to the code
data = pandas.read_csv("Volcanoes.txt")
# creating a variables responsible for particular features of the map
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

def color_producer(elevation): 
    """ function to change color of the marker depending of the height""" 
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
# html code to input link to google search + height and to create Figure object, to plot things into it
html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""
# using Map method to create starting point for the map
map = folium.Map(location = [38.58,-99.89], zoom_start = 3)

# create layer of the tiles
fgt = folium.FeatureGroup(name = "Tiles")
fgt.add_child(folium.TileLayer("Stamen Terrain"))
# create special layer related to markers
fgv = folium.FeatureGroup(name = "Volcanoes")
for lt, ln, lv, name in zip(lat,lon,elev,name): 
    # zip function distributes items from 2 lists equally / it iterates through 2 lists at the same time
    iframe = folium.IFrame(html = html % (name, name, lv), width = 200, height = 100) 
    fgv.add_child(folium.Marker(location = [lt,ln], radius = 6, popup = folium.Popup(iframe),
    fill_color = color_producer(lv),color = 'grey', fill_opacity = 0.7))

# creating separarte layer related to Population
fgp = folium.FeatureGroup(name = "Population")

# add child class to change the colors of the particular countries on the map depending on population parameter
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(),
style_function=lambda x: {'fillColor':'red' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 30000000 else 'blue'}))

# add a Volcanoes feature group to parent object
map.add_child(fgv) 
# add a Population feature group to parent object
map.add_child(fgp) 
# add a Tiles feature group to parent object
map.add_child(fgt) 
# adding special layer in order to put tick on and off different child layers
map.add_child(folium.LayerControl())
# saving resulting map file 
map.save("volcano_map_in_the_us.html")
