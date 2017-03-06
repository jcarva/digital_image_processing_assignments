import numpy as np
import utils


def apply_kernel(image, kernel):
    kernel_size = len(kernel[0])
    border_size = kernel_size//2
    rows, columns, channels = utils.image_shape(image)

    resized_image = utils.copy_add_border(image, border_size, 127)
    output = np.zeros((rows, columns, channels), dtype=np.int)

    for c in range(border_size, columns + border_size):
        for r in range(border_size, rows + border_size):
            region = resized_image[r - border_size:r + border_size + 1, c - border_size:c + border_size + 1]

            if channels == 1:
                output[r - border_size, c - border_size] = np.sum(region[:, :] * kernel)
            else:
                output[r - border_size, c - border_size] = np.array([np.sum(region[:, :, 0] * kernel),
                                                                     np.sum(region[:, :, 1] * kernel),
                                                                     np.sum(region[:, :, 2] * kernel)])

    utils.fit_matrix_in_interval(output)
    return np.uint8(output)


def median_filter(image, size):
    border_size = size//2
    rows, columns, channels = image.shape
    resized_image = utils.copy_add_border(image, border_size, 127)
    output = np.zeros((rows, columns, channels), dtype=np.int)

    for c in range(border_size, columns + border_size):
        for r in range(border_size, rows + border_size):
            valid_pixel = resized_image[r - border_size:r + border_size + 1, c - border_size:c + border_size + 1]
            output[r - border_size, c - border_size] = np.array([np.median(valid_pixel[:, :, 0]),
                                                                 np.median(valid_pixel[:, :, 1]),
                                                                 np.median(valid_pixel[:, :, 2])])

    utils.fit_matrix_in_interval(output)
    return np.uint8(output)