import folium
import geopandas


m = folium.Map()

for k, shape in waterways_edges.iterrows():
    sim_geo = geopandas.GeoSeries(
        shape["geometry"]
    ).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j)
    folium.Popup(f"{shape['name']}").add_to(geo_j)
    geo_j.add_to(m)

for k, shape in natwater_edges.iterrows():
    sim_geo = geopandas.GeoSeries(
        shape["geometry"]
    ).simplify(tolerance=0.001)
    geo_j = sim_geo.to_json()
    geo_j = folium.GeoJson(data=geo_j)
    folium.Popup(f"{shape['name']}").add_to(geo_j)
    geo_j.add_to(m)


m.fit_bounds(m.get_bounds())
m.save("index.html")
