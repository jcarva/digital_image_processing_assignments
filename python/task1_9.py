# coding=UTF-8
#1.9 Aplicar filtros descritos na atividade

import cv2
import utils
import numpy as np


def main():
    image = utils.load_image('lenna.png')

    filter1 = _filter(image, [[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    filter2 = _filter(image, [[0, 0, 0], [0, 1, 0], [0, 0, -1]])

    utils.display_single_image('Original', image)
    utils.display_multiple_images(['Filter1', 'Filter2'], [filter1, filter2])

    utils.wait_key_and_destroy_windows()


def _filter(image, kernel):
    kernel_size = len(kernel[0])
    border_size = kernel_size//2
    rows, columns, chanels = image.shape
    resized_image = utils.copy_add_border(image, border_size, 127)
    output = np.zeros((rows, columns, chanels), dtype=np.int)

    for c in range(border_size, columns+border_size):
        for r in range(border_size, rows+border_size):
            valid_pixel = resized_image[r-border_size:r+border_size+1, c-border_size:c+border_size+1]
            output[r-border_size, c-border_size] = np.array([np.sum(valid_pixel[:, :, 0]*kernel),
                                                             np.sum(valid_pixel[:, :, 1]*kernel),
                                                             np.sum(valid_pixel[:, :, 2]*kernel)])

    utils.fit_matrix_in_interval(output)
    return np.uint8(output)

if __name__ == "__main__":
    main()
