# coding=UTF-8
#1.7 Filtros de Média e Mediana de ordem escolhida pelo usuário

import utils
import filter


def main():
    image = utils.load_image('lenna.png')

    average_image = filter.apply_kernel(image, utils.average_kernel(9))

    # TODO add median

    utils.display_single_image('Original', image)
    utils.display_multiple_images(['Average'], [average_image])

    utils.wait_key_and_destroy_windows()

if __name__ == "__main__":
    main()
