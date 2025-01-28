import geopandas as gpd
import os
shapefile_path = "/Users/indirakasichhwa/Desktop/testing/shp files/SMWC_Fields.shp"
gdf = gpd.read_file(shapefile_path)

gdf = gdf.to_crs(epsg=4326)
gdf['geometry_type'] = gdf.geometry.geom_type
if 'centroid' not in gdf.columns:
    # Calculate centroids and their lat/lon
    gdf['centroid'] = gdf.geometry.centroid
    gdf['center_latitude'] = gdf.centroid.y
    gdf['center_longitude'] = gdf.centroid.x
else:
    print("'centroid' column already exists. Skipping centroid calculation.")
required_columns = list(set(gdf.columns.values) - set(['centroid']))
gdf = gdf[required_columns]
base_name = os.path.splitext(os.path.basename(shapefile_path))[0]
json_path = os.path.join(os.path.dirname(shapefile_path), f"{base_name}_5.json")
gdf.to_file(json_path, driver="GeoJSON")

print(f"Processed data saved to:\nGeoJSON: {json_path}")
