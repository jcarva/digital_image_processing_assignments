# coding=UTF-8
# 1.1. Conversão RGB-YIQ-RGB
# (cuidado com os limites de R, G e B!)

import numpy as np
import utils


def main():
    image = utils.load_image('lenna.png')

    yiq = utils.rgb2yiq(image)
    back_to_original = utils.yiq2rgb(yiq)

    utils.display_single_image('Original', image)
    utils.display_single_image('YIQ', yiq)
    utils.display_single_image('Back to Original', back_to_original)

    utils.save_image('yiq.png', yiq)

    utils.wait_key_and_destroy_windows()


if __name__ == "__main__":
    main()
