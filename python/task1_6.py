# coding=UTF-8
# 1.6. Limiarização aplicada sobre Y, com limiar m e duas opções: a) m
# escolhido pelo usuáio; b) m = média de valores da banda Y;

import numpy as np
import utils
import color


def main():
    image = utils.load_image('lenna.png')
    utils.display_single_image('Original', image)
    grayscale_image = color.rbg2gray(image)

    threshold_value = 200
    mean_value = np.mean(grayscale_image)
    
    threshold_user_image = _segment_y(grayscale_image, threshold_value)
    threshold_mean_image = _segment_y(grayscale_image, mean_value)

    utils.display_single_image('Y Channel', grayscale_image)
    utils.display_single_image('Y Threshold (User ' + str(threshold_value) + ')', threshold_user_image)
    utils.display_single_image('Y Threshold (Mean ' + str(mean_value) + ')', threshold_mean_image)

    utils.wait_key_and_destroy_windows()


def _segment_y(image, m):
    output = (image > m) * 255
    return output

if __name__ == "__main__":
    main()