import json
import geopandas
from shapely.ops import cascaded_union, linemerge


gdf0 = geopandas.read_file(
    datapath.joinpath("floripa_adim_level_09.geojson")
)

gdf1 = geopandas.read_file(
    datapath.joinpath("floripa_adim_level_10.geojson")
)

floripa = cascaded_union(gdf0['geometry'].tolist() + gdf1['geometry'].tolist())

with open("data/floripa.geojson", "w") as f:
    f.writelines(json.dumps(floripa.boundary.__geo_interface__))
