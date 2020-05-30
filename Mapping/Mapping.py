import folium
import pandas as pd
def color_pick(fuel):
    if fuel=="Coal":
        return "red"
    elif fuel=="Hydro":
        return "blue"
    elif fuel=="Nuclear":
        return "green"
    else:
        return "pink"

map1=folium.Map(location=[26.505,80.3713],zoom_start=6)

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("world.json","r",encoding="utf-8-sig").read(),style_function=lambda x: {"fillColor":"green" if x['properties']['POP2005']<10000000 else "orange" if 10000000<=x['properties']['POP2005']<20000000 else "red"}))

#COAL************************
file=pd.read_csv("coal.csv")
lat=list(file["latitude"])
lon=list(file["longitude"])
name=list(file["name"])

fgr=folium.FeatureGroup(name="RED   Coal")

for lt,ln,nam in zip(lat,lon,name):
    fgr.add_child(folium.CircleMarker(location=(lt,ln),popup=nam,tooltip=nam,radius=7,color="gray",fill_color="red",fill_opacity=0.7))

#HYDRO*************************
file=pd.read_csv("hydro.csv")
lat=list(file["latitude"])
lon=list(file["longitude"])
name=list(file["name"])

fgb=folium.FeatureGroup(name="BLUE   Hydro")

for lt,ln,nam in zip(lat,lon,name):
    fgb.add_child(folium.CircleMarker(location=(lt,ln),popup=nam,tooltip=nam,radius=7,color="gray",fill_color="blue",fill_opacity=0.7))

#NUCLEAR***************************
file=pd.read_csv("nuclear.csv")
lat=list(file["latitude"])
lon=list(file["longitude"])
name=list(file["name"])

fgg=folium.FeatureGroup(name="GREEN   Nuclear")

for lt,ln,nam in zip(lat,lon,name):
    fgg.add_child(folium.CircleMarker(location=(lt,ln),popup=nam,tooltip=nam,radius=7,color="gray",fill_color="green",fill_opacity=0.7))

#SOLAR**********************************
file=pd.read_csv("solar.csv")
lat=list(file["latitude"])
lon=list(file["longitude"])
name=list(file["name"])

fgpi=folium.FeatureGroup(name="PINK   Solar")

for lt,ln,nam in zip(lat,lon,name):
    fgpi.add_child(folium.CircleMarker(location=(lt,ln),popup=nam,tooltip=nam,radius=7,color="gray",fill_color="gray",fill_opacity=0.7))


map1.add_child(fgp)
map1.add_child(fgr)
map1.add_child(fgb)
map1.add_child(fgg)
map1.add_child(fgpi)
map1.add_child(folium.LayerControl())

map1.save("Web-mapping.html")
