# coding=UTF-8
#1.7 Filtros de Média e Mediana de ordem escolhida pelo usuário

import numpy as np
import utils


def main():
    image = utils.load_image('lenna.png')

    mean_image = utils.image_filter(image, _mean_kernel(9))

    utils.display_single_image('Original', image)
    utils.display_multiple_images(['Mean'], [mean_image])

    utils.wait_key_and_destroy_windows()


def _mean_kernel(kernel_size):
    return np.full((kernel_size, kernel_size), 1/float(kernel_size * kernel_size))

if __name__ == "__main__":
    main()
