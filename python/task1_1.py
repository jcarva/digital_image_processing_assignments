# coding=UTF-8
# 1.1. Conversão RGB-YIQ-RGB
# (cuidado com os limites de R, G e B!)

import numpy as np
import utils


def main():
    image = utils.load_image('lenna.png')

    yiq = _rgb2yiq(image)
    back_to_original = _yiq2rgb(yiq)

    utils.display_single_image('Original', image)
    utils.display_single_image('YIQ', yiq)
    utils.display_single_image('Back to Original', back_to_original)

    utils.save_image('yiq.png', yiq)

    utils.wait_key_and_destroy_windows()


def _rgb2yiq(image):
    output = np.empty_like(image, dtype='int16')
    blue, green, red = utils.split_channels(image)

    # From https://www.mathworks.com/help/images/ref/rgb2ntsc.html
    # Y = 0.299 R + 0.587 G + 0.114 B
    # I = 0.596 R - 0.274 G - 0.322 B
    # Q = 0.211 R - 0.523 G + 0.312 B

    # TODO: Write on report about int8 overflowing negative
    # values to positive

    output[:, :, 2] = 0.299 * red + 0.587 * green + 0.114 * blue
    output[:, :, 1] = 0.596 * red - 0.274 * green - 0.322 * blue
    output[:, :, 0] = 0.211 * red - 0.523 * green + 0.312 * blue

    utils.fit_matrix_in_interval(output, 0, 255)
    output = output.astype('uint8')

    return output


def _yiq2rgb(image):
    output = np.empty_like(image, dtype='int16')
    q, i, y = utils.split_channels(image)

    # From https://www.mathworks.com/help/images/ref/ntsc2rgb.html
    # R = 1 Y  + 0.956 I + 0.621 Q
    # G = 1 Y  - 0.272 I - 0.647 Q
    # B = 1 Y  - 1.106 I + 1.703 Q

    output[:, :, 2] = y + 0.956 * i + 0.621 * q
    output[:, :, 1] = y - 0.272 * i - 0.647 * q
    output[:, :, 0] = y - 1.106 * i + 1.703 * q

    utils.fit_matrix_in_interval(output, 0, 255)
    output = output.astype('uint8')

    return output


if __name__ == "__main__":
    main()
