import os
from PIL import Image, ImageDraw, ImageChops
from colors import sgmc_colors
from models import MapPoly

def change_color(image: Image, color: tuple[int]):
    width, height = image.size

    for x in range(width):
        for y in range(height):
            pixel_color = image.getpixel((x, y))
            
            if pixel_color[3] > 100:
                image.putpixel((x, y), color)
            else:
                image.putpixel((x, y), (0, 0, 0, 0))

def get_patterned_image(pattern: Image, w, h, bg_color):
    patterm_image = Image.new('RGBA', (w, h), bg_color)
    pattern_width = pattern.width
    pattern_height = pattern.height
    for x in range(0, w, pattern_width):
        for y in range(0, h, pattern_height):
            patterm_image.paste(pattern, (x, y), pattern)
    return patterm_image

def get_pattern(id_pattern: int):
    folder = "images"
    image_path = os.path.join(folder, "326.png") # os.path.join(folder, id_pattern + ".png")
    return Image.open(image_path)

def get_pattern_color(id_color: int):
    if id_color in sgmc_colors:
        return sgmc_colors[id_color]
    return (255, 0, 0, 255)

def get_pattern_bg(id_background: int):
    if id_background in sgmc_colors:
        return sgmc_colors[id_background]
    return (255, 255, 255, 100)

def create_image(polygons: list[MapPoly], w, h):
    image = Image.new('RGBA', (w, h), (255, 255, 255, 0))
    for polygon in polygons:
        pattern = get_pattern(polygon.id_pattern)
        change_color(pattern, get_pattern_color(polygon.id_color))
        patterm_image = get_patterned_image(pattern, w, h, get_pattern_bg(polygon.id_background))
        poly_image = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        ImageDraw.Draw(poly_image).polygon([tuple(x) for x in polygon.pixel_feature], outline='black', fill='white')
        composite = Image.composite(patterm_image, image, poly_image)
        image.paste(composite, (0,0), composite)
        break

    image.save('output.png')