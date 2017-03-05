# coding=UTF-8
# 1.6. Limiarizao aplicada sobre Y, com limiar m e duas opes: a) m
# escolhido pelo usuio; b) m = mia de valores da banda Y;

import numpy as np
import utils


def main():
    image = utils.load_image('lenna.png')
    utils.display_single_image('Original', image)
    grayscale_image = _rbg2gray(image)

    threshold_value = 200
    mean_value = np.mean(grayscale_image)
    
    threshold_user_image = _segment_y(grayscale_image, threshold_value)
    threshold_mean_image = _segment_y(grayscale_image, mean_value)

    utils.display_single_image('Y Channel', grayscale_image)
    utils.display_single_image('Y Threshold (User ' + str(threshold_value) + ')', threshold_user_image)
    utils.display_single_image('Y Threshold (Mean ' + str(mean_value) + ')', threshold_mean_image)

    utils.wait_key_and_destroy_windows()


def _segment_y(image, m):
    output = (image > m)*255    
    return output

def _rbg2gray(image):
    # https://en.wikipedia.org/wiki/Grayscale
    # Y ′ = 0.299 R ′ + 0.587 G ′ + 0.114 B

    blue, green, red = utils.split_channels(image)
    output = 0.299 * red + 0.587 * green + 0.114 * blue

    utils.fit_matrix_in_interval(output)

    return output

if __name__ == "__main__":
    main()