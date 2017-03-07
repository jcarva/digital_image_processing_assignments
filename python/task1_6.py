# coding=UTF-8
# 1.6. Limiarização aplicada sobre Y, com limiar m e duas opções: a) m
# escolhido pelo usuáio; b) m = média de valores da banda Y;

import numpy as np
import utils
import color


def main():
    image = utils.load_image('lenna.png')

    yiq_image = color.rgb2yiq(image)
    grayscale_image = color.yiq2rgb(image)[:, :, 0]

    threshold_value = 255 * 0.2
    mean_value = np.mean(grayscale_image)

    threshold_user_image = _segment(grayscale_image, threshold_value)
    original_threshold_user_image = np.copy(yiq_image)
    original_threshold_user_image[:, :, 0] = threshold_user_image
    original_threshold_user_image = color.yiq2rgb(original_threshold_user_image)

    threshold_mean_image = _segment(grayscale_image, mean_value)
    original_threshold_mean_image = np.copy(yiq_image)
    original_threshold_mean_image[:, :, 0] = threshold_mean_image
    original_threshold_mean_image = color.yiq2rgb(original_threshold_mean_image)

    utils.display_single_image('Original Image', image)
    utils.display_single_image('YIQ Image', yiq_image)
    utils.display_single_image('Y Channel', grayscale_image)

    utils.display_single_image('Y Threshold (User ' + str(threshold_value) + ')', threshold_user_image)
    utils.display_single_image('Back to Original (User ' + str(threshold_value) + ')', original_threshold_user_image)

    utils.display_single_image('Y Threshold (Mean ' + str(mean_value) + ')', threshold_mean_image)
    utils.display_single_image('Back to Original (Mean ' + str(mean_value) + ')', original_threshold_mean_image)

    utils.wait_key_and_destroy_windows()


def _segment(image, m):
    output = (image > m) * 255
    return output

if __name__ == "__main__":
    main()