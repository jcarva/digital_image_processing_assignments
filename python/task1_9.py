# coding=UTF-8
#1.9 Aplicar filtros descritos na atividade

import utils
import filter


def main():
    image = utils.load_image('lenna.png')

    filter1 = filter.apply_kernel(image, [[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    filter2 = filter.apply_kernel(image, [[0, 0, 0], [0, 1, 0], [0, 0, -1]])

    utils.display_single_image('Original', image)
    utils.display_multiple_images(['Filter1', 'Filter2'], [filter1, filter2])

    utils.wait_key_and_destroy_windows()


if __name__ == "__main__":
    main()
