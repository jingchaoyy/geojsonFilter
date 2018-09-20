"""
Created on 9/20/2018
@author: Jingchao Yang
"""

import json

with open(
        "C:\\Users\\no281\\Documents\\STCSpark_Exp\\GeoSpark\\MA_gis_osm_landuse_MA_gis_osm_buildings_overlap_KDBTREE\\part-00006") as f:
    gj = json.load(f)

features = gj['features']

print(features)



with open('C:\\Users\\no281\\Documents\\STCSpark_Exp\\GeoSpark\\filtered\\test.json', 'w') as outfile:
    prefix = '{"type": "FeatureCollection","features": ['
    # json.dump(prefix, outfile)
    outfile.write(prefix)
    for i in range(len(features)):
        print(features[i])
        type = features[i]['geometry']['type']
        if type == 'Polygon':
            if i < len(features)-1:
                json.dump(features[i], outfile)
                outfile.write(',')
            else:
                json.dump(features[i], outfile)
    sufix = ']}'
    outfile.write(sufix)
