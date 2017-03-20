# coding=UTF-8
# 1.2 Exibição de bandas individuais (R, G e B) como imagens
# monocromáticas ou coloridas (em tons de R, G ou B, respectivamente)

import numpy as np
import utils


def main():
    image = utils.load_image('lenna.png')
    utils.display_single_image('Original', image)

    blue_mono, green_mono, red_mono = utils.split_channels(image)
    utils.display_single_image('Blue channel mono', blue_mono)
    utils.display_single_image('Green channel mono', green_mono)
    utils.display_single_image('Red channel mono', red_mono)

    zeroes = np.zeros(image.shape[0:2], dtype='uint8')

    blue = utils.merge_channels(blue_mono, zeroes, zeroes)
    green = utils.merge_channels(zeroes, green_mono, zeroes)
    red = utils.merge_channels(zeroes, zeroes, red_mono)
    utils.display_single_image('Blue channel', blue)
    utils.display_single_image('Green channel', green)
    utils.display_single_image('Red channel', red)

    back_to_original = utils.merge_channels(blue_mono, green_mono, red_mono)
    utils.display_single_image('Back to Original Channel', back_to_original)

    utils.wait_key_and_destroy_windows()


if __name__ == "__main__":
    main()