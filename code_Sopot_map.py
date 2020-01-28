# importing folium libary in order to operate on leaflet maps objects
import folium
# calling folium child class in order to create Map object with determined parameters 
map = folium.Map(location = [54.4420055,18.4777282], zoom_start = 12, tiles = "Stamen Terrain")
# calling folium child class in order to create special layer of the features as an other object
fg = folium.FeatureGroup(name = "My Map") 
# adding elements to the fg object which is an example of the FeatureGroup child class object
for coordinates in [[54.454868, 18.551107],[52.454868, 19.551107]]:
    """ Special method of the FeatureGroup object to add marker in determined location"""
    fg.add_child(folium.Marker(location = coordinates, popup = "Sopot", icon = folium.Icon(color = "green")))
# calling a special method in order to add marker to the class
map.add_child(fg)
# saving a newly created map
map.save("map_Sopot.html")