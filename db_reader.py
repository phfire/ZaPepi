import psycopg2
import json
from geojson import Feature

from models import MapPoly

def get_polygons(extent: list[float]) -> list[MapPoly]:
    conn = psycopg2.connect(
        database='100gmap', 
        user='postgres',
        password='qweqwe',
        host='localhost')
    curs = conn.cursor()



    postgis_extent = "ST_MakeEnvelope(%s, %s, %s, %s, 3857)" % tuple(extent)

    sql = f"""\
    SELECT ST_AsGeoJSON(geometry), id_color, id_background, id_pattern
    FROM geology.map_polygons
    WHERE ST_Intersects(geometry, {postgis_extent})"""
    curs.execute(sql)

    rows: list[MapPoly] = []

    for row in curs.fetchall():
        j = json.loads(row[0])
        p = Feature(geometry=j)
        # coordinates = [tuple(x) for x in j['coordinates'][0]]
        # holes = j['coordinates'][1:]
        # hole_coordinates = [[tuple(x) for x in hole] for hole in holes]
        # p = Polygon(coordinates, hole_coordinates)
        rows.append(MapPoly(p, row[1], row[2], row[3]))

    return rows