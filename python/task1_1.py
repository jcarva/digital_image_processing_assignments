# coding=UTF-8
# 1.1. Conversão RGB-YIQ-RGB
# (cuidado com os limites de R, G e B!)

import cv2
import utils


def main():
    image = utils.load_image('lenna.png')

    blue, green, red = utils.split_channels(image)

    utils.display_single_image('Blue Channel', blue)
    utils.display_single_image('Green Channel', green)
    utils.display_single_image('Red Channel', red)

    back_to_original = utils.merge_channels(blue, green, red)

    utils.display_single_image('Merged', back_to_original)

    utils.wait_key_and_destroy_windows()


# From https://www.mathworks.com/help/images/ref/ntsc2rgb.html
def _yiq2rgb(image):
    conversion = [[0.299, 0.587, 0.114],
             [0.596, -0.274, -0.322],
             [0.211, -0.523, 0.312]]


# From https://www.mathworks.com/help/images/ref/rgb2ntsc.html
def _rgb2yiq(image):
    conversion = [1]


if __name__ == "__main__":
    main()
