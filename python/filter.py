import numpy as np
import utils


def apply_kernel(image, kernel):
    return _filter(image, kernel)


def median_filter(image, size):
    kernel = np.full((size, size), 1)
    return _filter(image, kernel, np.median)


def _filter(image, kernel, operation=np.sum):
    kernel_size = len(kernel[0])
    border_size = kernel_size // 2
    rows, columns, channels = utils.image_shape(image)

    resized_image = utils.copy_add_border(image, border_size, 127)
    output = np.zeros((rows, columns, channels), dtype=np.int)

    for c in range(border_size, columns + border_size):
        for r in range(border_size, rows + border_size):
            region = resized_image[r - border_size:r + border_size + 1, c - border_size:c + border_size + 1]

            if channels == 1:
                output[r - border_size, c - border_size] = np.sum(region[:, :] * kernel)
            else:
                output[r - border_size, c - border_size] = np.array([operation(region[:, :, 0] * kernel),
                                                                     operation(region[:, :, 1] * kernel),
                                                                     operation(region[:, :, 2] * kernel)])

    utils.fit_matrix_in_interval(output)

    return np.uint8(output)

