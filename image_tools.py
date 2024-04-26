import os
from PIL import Image, ImageDraw, ImageChops
from colors import sgmc_colors,lith6_1 ,lith6_2, lith4_3
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
    img_name = "326.png"
    if id_pattern == 555:
        img_name = "326.png"
    if id_pattern == 480:
        img_name = "352.png"
    else:
        img_name = "315.png"
    image_path = os.path.join(folder, img_name) 
    return Image.open(image_path)

def get_pattern_color(id_color: int):
    if id_color in sgmc_colors:
        return sgmc_colors[id_color]
    elif id_color in lith6_1:
        return lith6_1[id_color]
    elif id_color in lith6_2:
        return lith6_2[id_color]
    elif id_color in lith4_3:
        return lith4_3[id_color]
    return (255, 0, 0, 255)

def get_pattern_bg(id_background: int):
    if id_background in sgmc_colors:
        return sgmc_colors[id_background]
    elif id_background in lith6_1:
        return lith6_1[id_background]
    elif id_background in lith6_2:
        return lith6_2[id_background]
    elif id_background in lith4_3:
        return lith4_3[id_background]
    return (255, 255, 255, 255)

def create_image(polygons: list[MapPoly], w, h):
    image = Image.new('RGBA', (w, h), (255, 255, 255, 0))
    

    for i, polygon in enumerate(polygons):
        # if i > 1:
        #     break
        pattern = get_pattern(polygon.id_pattern)
        change_color(pattern, get_pattern_color(polygon.id_color))
        patterm_image = get_patterned_image(pattern, w, h, get_pattern_bg(polygon.id_background))
        poly_image = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        ImageDraw.Draw(poly_image).polygon([tuple(x) for x in polygon.pixel_feature], outline='black', fill='white')
        composite = Image.composite(patterm_image, image, poly_image)
        image.paste(composite, (0,0), composite)

    image.save('output.png')