# coding=UTF-8
# 1.1. Conversão RGB-YIQ-RGB
# (cuidado com os limites de R, G e B!)

import cv2
import utils

img = utils.load_image('lenna.png')

utils.display_single_image('Lenna', img)