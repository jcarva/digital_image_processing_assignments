# coding=UTF-8
#1.8. Filtros de detecção de bordas Sobel e Laplaciano

import utils


def main():
    image = utils.load_image('lenna.png')

    laplacian_image = utils.image_filter(image, [[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    sobel__x_image = utils.image_filter(image, [[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    sobel__y_image = utils.image_filter(image, [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    utils.display_single_image('Original', image)
    utils.display_multiple_images(['Sobel_X Lenna', 'Sobel_Y Lenna', 'Laplacian Lenna'],
                                  [sobel__x_image, sobel__y_image, laplacian_image])

    utils.wait_key_and_destroy_windows()


if __name__ == "__main__":
    main()
