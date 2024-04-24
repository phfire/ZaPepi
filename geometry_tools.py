from turfpy.transformation import intersect
from geojson import Feature

from models import MapPoly

def populate_pixel_features(polygons: list[MapPoly], extent: Feature, raw_extent: list[float]) -> list[MapPoly]:

    for polygon in polygons:
        intersected_poly = intersect([polygon.feature, extent])
        if not intersected_poly:
            continue
        poly_coords = intersected_poly['geometry']['coordinates']
        coordinates =[]
        if(intersected_poly['geometry']['type'] == 'Polygon'):
            poly_coords = [poly_coords]
        for poly_coord in poly_coords:
            for x, y in poly_coord[0]:
                coordinates.append([x,y])
        polygon.pixel_feature = coordinates
    return [polygon for polygon in polygons if polygon.pixel_feature]