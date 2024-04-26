from db_reader import get_polygons
from geojson import Feature
from turfpy.measurement import bbox
from geometry_tools import populate_pixel_features
from image_tools import create_image

x = 2775195
y = 5240590
offset = 6000
w_pixels = 2000

ex = Feature(geometry={"coordinates": [
    [[x + offset, y + offset], [x + offset, y - offset],
    [x - offset, y - offset], [x - offset, y + offset],
    ]], "type": "Polygon"})
raw_extent = bbox(ex)
h_pixels = int(w_pixels * (raw_extent[3] - raw_extent[1] ) / (raw_extent[2] - raw_extent[0] ))
scale = w_pixels / (raw_extent[2] - raw_extent[0] )

polygons = get_polygons(raw_extent)
polygons = populate_pixel_features(polygons, ex, w_pixels, h_pixels, scale, raw_extent)
create_image(polygons, w_pixels, h_pixels)