

from db_reader import get_polygons
from geojson import Feature
from turfpy.measurement import bbox
from geometry_tools import populate_pixel_features
from image_tools import create_image

x = 2775195.38081054
y = 5240590.731858477
offset = 6000

extent = [
    x + offset,
    y + offset,
    x - offset,
    y - offset
]
ex = Feature(geometry={"coordinates": [
    [[x + offset, y + offset], [x + offset, y - offset],
    [x - offset, y - offset], [x - offset, y + offset],
    ]], "type": "Polygon"})

polygons = get_polygons(extent)

w = 2000
raw_extent = bbox(ex)
height = raw_extent[3] - raw_extent[1] 
width = raw_extent[2] - raw_extent[0] 
h = int(w * height / width)
scale = w / width

polygons = populate_pixel_features(polygons, ex, w, h, scale, raw_extent)
create_image(polygons, w, h)