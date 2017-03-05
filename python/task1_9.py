# coding=UTF-8
#1.9 Aplicar filtros descritos na atividade

import cv2
import utils
import numpy as np


def main():
    image = utils.load_image('lenna.png')

    filter1 = filter(image, [[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    filter2 = filter(image, [[0, 0, 0], [0, 1, 0], [0, 0, -1]])

    utils.display_single_image('Original', image)
    utils.display_multiple_images(['Filter1', 'Filter2'], [filter1, filter2])

    utils.wait_key_and_destroy_windows()


def filter(image, kernel):
    kernel_size = len(kernel[0])
    border_size = kernel_size//2
    width, height, chanels = image.shape
    resized_image = cv2.copyMakeBorder(image,
                              border_size,
                              border_size,
                              border_size,
                              border_size,
                              cv2.BORDER_REFLECT_101)
    output = np.zeros((width, height, chanels), np.int)

    for h in range(border_size, height+border_size):
        for w in range(border_size, width+border_size):

            valid_pixel = resized_image[w-border_size:w+border_size+1, h-border_size:h+border_size+1]
            output[w-border_size, h-border_size] = np.array([np.sum(valid_pixel[:, :, 0]*kernel),
                                                             np.sum(valid_pixel[:, :, 1]*kernel),
                                                             np.sum(valid_pixel[:, :, 2]*kernel)])

    utils.fit_matrix_in_interval(output)
    return np.uint8(output)

if __name__ == "__main__":
    main()
