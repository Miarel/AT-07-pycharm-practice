from PIL import Image
import numpy as np
import doctest

img = Image.open("img2.jpg")
mosaic_resolution = 10
gradations = 50


def get_average_color(pixels: [],
                      height: int,
                      width: int,
                      mosaic_resolution: int):
    """
    Среди пикселей мозайки из большой ячейки находим среднюю яркость и возвращаем её
    :param pixels: трехмерный массив, где два измерения — таблица с пикселями, а пиксель — что-то то типа массива [12, 240, 123], содержащего компоненты RGB
    :param height: высота изображения
    :param width: ширина изображения
    :param mosaic_resolution: размер мозайки в формате n*n
    :return: возвращает среднюю яркость

    """
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
    """
    Закрашиваем пиксели в цвет средней яркости, приведенный к ступеньке(градации)
    :param pixels: трехмерный массив, где два измерения — таблица с пикселями, а пиксель — что-то то типа массива [12, 240, 123], содержащего компоненты RGB
    :param height: высота изображения
    :param width: ширина изображения
    :param mosaic_resolution: размер мозайки в формате n*n
    :param gradations: градации серого
    :param average_color: средняя яркость
    :return: меняет цвет пикселя

    """
    pixels[height:height + mosaic_resolution,
    width:width + mosaic_resolution] = \
        int(average_color // gradations) * gradations


def get_mosaic_image(img: Image,
                     mosaic_resolution: int,
                     gradations: int):
    """
    Делаем изображение пиксельным и черно-белым и возвращаем результат
    :param img: изображение
    :param mosaic_resolution: размер мозайки в формате n*n
    :param gradations: градации серого
    :return: возвращает результат в виде изображения
    """
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

if __name__ == 'main':
    doctest.testmod()