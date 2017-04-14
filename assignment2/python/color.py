# coding=UTF-8

import numpy as np
import utils

def rbg2gray(image):
    # https://en.wikipedia.org/wiki/Grayscale
    # Y ′ = 0.299 R ′ + 0.587 G ′ + 0.114 B

    blue, green, red = utils.split_channels(image)
    output = 0.299 * red + 0.587 * green + 0.114 * blue

    utils.fit_matrix_in_interval(output)

    return output.astype(np.uint8)

