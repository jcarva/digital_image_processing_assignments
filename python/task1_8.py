# coding=UTF-8
#1.8. Filtros de detecção de bordas Sobel e Laplaciano

import utils
import filter


def main():
    image = utils.load_image('lenna.png')

    laplacian_image = filter.apply_kernel(image, [[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    sobel_x_image = filter.apply_kernel(image, [[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    sobel_y_image = filter.apply_kernel(image, [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    sobel_addition = sobel_x_image + sobel_y_image
    utils.fit_matrix_in_interval(sobel_addition)

    utils.display_single_image('Original', image)
    utils.display_multiple_images(['Sobel_X Lenna', 'Sobel_Y Lenna', 'Sobel X + Y', 'Laplacian Lenna'],
                                  [sobel_x_image, sobel_y_image, sobel_addition, laplacian_image])

    utils.wait_key_and_destroy_windows()


if __name__ == "__main__":
    main()
