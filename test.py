#1
#data in that shapefile
'''import geopandas as gpd

shapefile_path = "/Users/indirakasichhwa/Desktop/testing/shp files/SMWC_Fields.shp"
gdf = gpd.read_file(shapefile_path)
#print(shapefile_path)
#print(gdf)
print(gdf.head())

gdf.to_excel("SMWC_1.xlsx" , index = False)
gdf.to_file("SMWC_1.json", driver="GeoJSON")

print("Data has been saved ")'''


#2
#prints out the column that we needed
# it does not  have coordinate, grometry 
'''
import geopandas as gpd
import os
import pandas as pd

shapefile_path = "/Users/indirakasichhwa/Desktop/testing/shp files/SMWC_Fields.shp"
gdf = gpd.read_file(shapefile_path)
#print(shapefile_path)
#print(gdf)
print(gdf.head())

gdf = gpd.read_file(shapefile_path)
df = gdf[['district', 'FieldID', 'FieldDesc', 'FieldAcres', 'IrrigAcres',
       'StandbyAcr', 'ParcelID', 'VolRateAdj', 'Att1', 'Att2', 'Att3', 'Att4',
       'Att5', 'ActiveDate', 'InactiveDa', 'ActiveFlag', 'Comment', 'OBJECTID',
       'Name', 'MEGA_APN', 'MAPYEAR', 'CITY', 'ZIP', 'LOT', 'GIS_Acres',
       'WA_NUM', 'WA_FLAG', 'Deed_Acres', 'Agency_ID', 'Roll_Asmt',
       'Roll_AsmtD', 'Roll_Land', 'Roll_Struc', 'Roll_TRA', 'Situs_Spac',
       'Situs_Stre', 'Situs_St_1', 'Situs_St_2', 'Situs_St_3', 'Jurisdicti',
       'MAP_PAGE', 'Roll_Acres', 'Shape__Are', 'Shape__Len', 'field_id',
       'unq_fld_id', 'AreaAC']]
df.fillna('', inplace=True)
print(df)
#print(df.to_dict('records'))
gdf.to_excel("SMWC_2.xlsx" , index = False)
gdf.to_file("SMWC_2.json", driver="GeoJSON")

'''

#3
# prints out the  geometry, centre lattitude and longitude wil all the other  columns as 1
# for centroid
'''import geopandas as gpd
import os

# Path to the single shapefile
shapefile_path = "/Users/indirakasichhwa/Desktop/testing/shp files/SMWC_Fields.shp"

# Load the shapefile
gdf = gpd.read_file(shapefile_path)
print(f"Processing: {shapefile_path}")

if 'geometry' in gdf.columns: #4326 is a geographic crs
    # Checking if the CRS is geographic
    if gdf.crs.is_geographic:
        print("Reprojecting to a projected CRS...")
        gdf = gdf.to_crs(epsg=3395)#3395 is a  projected CRS

    # Add a 'geometry_type' column
    gdf['geometry_type'] = gdf.geometry.geom_type

    # Filter only polygons and multipolygons
    polygon_gdf = gdf[gdf['geometry_type'].isin(['Polygon', 'MultiPolygon'])]
    print("Filtered Polygons and Multipolygons.")

    # Check if 'centroid' column already exists
    if 'centroid' not in gdf.columns:
        # Calculate centroids
        polygon_gdf['centroid'] = polygon_gdf.geometry.centroid
        polygon_gdf['center_latitude'] = polygon_gdf.centroid.y
        polygon_gdf['center_longitude'] = polygon_gdf.centroid.x
        print("Centroids calculated and added.")
    else:
        print("'centroid' column already exists. Skipping centroid calculation.")

    # Display the result
    print(polygon_gdf[['geometry_type', 'centroid','center_latitude', 'center_longitude']])

    # Save the processed data
    base_name = os.path.splitext(os.path.basename(shapefile_path))[0]
    excel_path = os.path.join(os.path.dirname(shapefile_path), f"{base_name}_3.xlsx")
    json_path = os.path.join(os.path.dirname(shapefile_path), f"{base_name}_3.json")

    polygon_gdf.to_excel(excel_path, index=False)
    #polygon_gdf.to_file(json_path, driver="GeoJSON")

    print(f"Processed data saved to:\nExcel: {excel_path}\nGeoJSON: {json_path}")
else:
    print("No 'geometry' column found in the shapefile.")
'''


#4
# SR ID
import geopandas as gpd
import os
shapefile_path = "/Users/indirakasichhwa/Desktop/testing/shp files/SMWC_Fields.shp"
try:
    gdf = gpd.read_file(shapefile_path)
    print(f"Processing: {shapefile_path}")

    if gdf.crs:
        print("CRS Details:", gdf.crs)
        srid = gdf.crs.to_epsg()
        if srid:
            print(f"SRID (EPSG Code): {srid}")
        else:
            print("SRID not found in the CRS.")
    else:
        print("No CRS defined for this shapefile. Please set a CRS.")

    if 'geometry' in gdf.columns:
        gdf = gdf.to_crs(epsg=4326)
        print(gdf.crs.to_epsg())
        gdf['geometry_type'] = gdf.geometry.geom_type # new geometry_type table added
        polygon_gdf = gdf[gdf['geometry_type'].isin(['Polygon', 'MultiPolygon'])]
        #print(polygon_gdf.columns)
        polygon_gdf.set_geometry("geometry")
        if 'centroid' not in polygon_gdf.columns:
            # Calculate centroids and their lat/lon
            polygon_gdf['centroid'] = polygon_gdf.geometry.centroid
            polygon_gdf['center_latitude'] = polygon_gdf.centroid.y
            polygon_gdf['center_longitude'] = polygon_gdf.centroid.x
        else:
            print("'centroid' column already exists. Skipping centroid calculation.")
    
        #print(polygon_gdf[['geometry']])
        print(polygon_gdf.columns)
        df = polygon_gdf[['district', 'FieldID', 'FieldDesc', 'FieldAcres', 'IrrigAcres',
       'StandbyAcr', 'ParcelID', 'VolRateAdj', 'Att1', 'Att2', 'Att3', 'Att4',
       'Att5', 'ActiveDate', 'InactiveDa', 'ActiveFlag', 'Comment', 'OBJECTID',
       'Name', 'MEGA_APN', 'MAPYEAR', 'CITY', 'ZIP', 'LOT', 'GIS_Acres',
       'WA_NUM', 'WA_FLAG', 'Deed_Acres', 'Agency_ID', 'Roll_Asmt',
       'Roll_AsmtD', 'Roll_Land', 'Roll_Struc', 'Roll_TRA', 'Situs_Spac',
       'Situs_Stre', 'Situs_St_1', 'Situs_St_2', 'Situs_St_3', 'Jurisdicti',
       'MAP_PAGE', 'Roll_Acres', 'Shape__Are', 'Shape__Len', 'field_id',
       'unq_fld_id', 'AreaAC',
       'center_latitude']]
        #df.fillna('', inplace=True)
        
        #print(polygon_gdf.to_geo_dict())
        #df.head(5)
        #print(df.head(5))
        gdf.to_excel("SMWC_4.xlsx" , index = False)
        #gdf.to_file("SMWC_4.json", driver="GeoJSON")

        base_name = os.path.splitext(os.path.basename(shapefile_path))[0]
        excel_path = os.path.join(os.path.dirname(shapefile_path), f"{base_name}_3.xlsx")
        json_path = os.path.join(os.path.dirname(shapefile_path), f"{base_name}_3.json")
        polygon_gdf.to_excel(excel_path, index=False)
        polygon_gdf.to_file(json_path, driver="GeoJSON")
        
        print(f"Processed data saved to:\nExcel: {excel_path}\nGeoJSON: {json_path}")
    else:
        print("No 'geometry' column found in the shapefile.")
except Exception as e:
    print(f"An error occurred: {e}")
