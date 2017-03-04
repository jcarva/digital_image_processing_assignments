# coding=UTF-8
# 1.5. Controle de brilho multiplicativo
# (valor do pixel resultante = valor do pixel original * c, c real não negativo)

import utils

BRIGHTNESS_ADJUSTMENT = 1.8


def main():
    image = utils.load_image('lenna.png')

    modified_image = image * BRIGHTNESS_ADJUSTMENT
    utils.fit_matrix_in_interval(modified_image)

    utils.display_single_image('Original', image)
    utils.display_single_image('Modified', modified_image)

    utils.wait_key_and_destroy_windows()


if __name__ == "__main__":
    main()