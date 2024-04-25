from PIL import Image, ImageDraw

from models import MapPoly

def create_image(polygons: list[MapPoly], w, h):
    image = Image.new('RGB', (w, h), color='white')

    
    draw = ImageDraw.Draw(image)
    for polygon in polygons:
        draw.polygon([tuple(x) for x in polygon.pixel_feature], outline='black')

    image.save('output.png')