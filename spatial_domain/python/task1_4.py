# coding=UTF-8
# 1.4. Controle de brilho aditivo
# (valor do pixel resultante = valor do pixel original + c, c inteiro)

import utils
import color

BRIGHTNESS_ADJUSTMENT = 80


def main():
    image = utils.load_image('lenna.png')
    grayscale_image = color.rbg2gray(image)

    modified_image = image + BRIGHTNESS_ADJUSTMENT
    utils.fit_matrix_in_interval(modified_image)

    modified_grayscale_image = grayscale_image + BRIGHTNESS_ADJUSTMENT
    utils.fit_matrix_in_interval(modified_grayscale_image)

    utils.display_single_image('Original', image)
    utils.display_single_image('Modified', modified_image)

    utils.display_single_image('Original Grayscale', grayscale_image)
    utils.display_single_image('Modified Grayscale', modified_grayscale_image)

    utils.wait_key_and_destroy_windows()


if __name__ == "__main__":
    main()