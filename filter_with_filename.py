from PIL import Image
import numpy as np

img = Image.open("img2.jpg")
mosaic_resolution = 10
gradations = 50


def get_average_color(pixels: [],
                      height: int,
                      width: int,
                      mosaic_resolution: int):
    average_color = int((pixels[height:height + mosaic_resolution,
                         width:width + mosaic_resolution]).sum() // 3)
    average_color //= mosaic_resolution * mosaic_resolution
    return average_color


def repainting(pixels: [],
               height: int,
               width: int,
               mosaic_resolution: int,
               gradations: int,
               average_color: int):
    pixels[height:height + mosaic_resolution,
    width:width + mosaic_resolution] = \
        int(average_color // gradations) * gradations


def get_mosaic_image(img: Image,
                     mosaic_resolution: int,
                     gradations: int):
    pixels = np.array(img)
    height = len(pixels)
    width = len(pixels[1])
    for i in range(0, height, mosaic_resolution):
        for j in range(0, width, mosaic_resolution):
            average_color = get_average_color(pixels, i, j, mosaic_resolution)
            repainting(pixels, i, j, mosaic_resolution, gradations, average_color)
    res_image = Image.fromarray(pixels)
    return res_image


res = get_mosaic_image(img, mosaic_resolution, gradations)
res.save("res.jpg")
