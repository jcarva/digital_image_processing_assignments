# coding=UTF-8
# 1.3. Negativo

import cv2
import utils

def task1_3():
    originalImage = utils.load_image('lenna.png')
    negativeImage = getNegative(originalImage)
    utils.display_multiple_images(['Lenna', 'Negative Lena'], [originalImage, negativeImage])

def getNegative(input):
    return (255 - input)

task1_3()