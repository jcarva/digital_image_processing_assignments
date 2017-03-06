# coding=UTF-8
#1.7 Filtros de Média e Mediana de ordem escolhida pelo usuário

import numpy as np
import utils


def main():
    image = utils.load_image('lenna.png')

    average_image = utils.image_filter(image, _average_kernel(9))

    utils.display_single_image('Original', image)
    utils.display_multiple_images(['Average'], [average_image])

    utils.wait_key_and_destroy_windows()


def _average_kernel(kernel_size):
    return np.full((kernel_size, kernel_size), 1/float(kernel_size * kernel_size))

if __name__ == "__main__":
    main()
