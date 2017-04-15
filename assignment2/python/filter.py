import scipy.signal
import numpy as np
import utils


def average(image, kernel):
    rows, columns, channels = utils.image_shape(image)

    if channels == 1:
        return scipy.signal.convolve2d(image, kernel, mode='same', boundary='fill', fillvalue=0)
    else:
        blue_mono, green_mono, red_mono = utils.split_channels(image)

        r = scipy.signal.convolve2d(red_mono, kernel, mode='same', boundary='fill', fillvalue=0)
        g = scipy.signal.convolve2d(green_mono, kernel, mode='same', boundary='fill', fillvalue=0)
        b = scipy.signal.convolve2d(blue_mono, kernel, mode='same', boundary='fill', fillvalue=0)

        return utils.merge_channels(b, g, r)


def median(image, kernel_size, operation=np.median):
    border_size = kernel_size // 2
    rows, columns, channels = utils.image_shape(image)

    resized_image = copy_add_border(image, border_size, 0)
    output = np.zeros((rows, columns, channels), dtype=np.int)

    for c in range(border_size, columns + border_size):
        for r in range(border_size, rows + border_size):
            region = resized_image[r - border_size:r + border_size + 1, c - border_size:c + border_size + 1]

            if channels == 1:
                output[r - border_size, c - border_size] = operation(region[:, :])
            else:
                output[r - border_size, c - border_size] = np.array([operation(region[:, :, 0]),
                                                                     operation(region[:, :, 1]),
                                                                     operation(region[:, :, 2])])

    utils.fit_matrix_in_interval(output)

    return np.uint8(output)


def copy_add_border(image, border_size=1, color=0):
    border_size *= 2
    rows, columns, channels = utils.image_shape(image)
    output = np.full((rows + border_size, columns + border_size, channels), color, dtype=np.int)

    for c in range(border_size, columns + border_size):
        for r in range(border_size, rows + border_size):
            output[r - border_size//2, c - border_size//2] = image[r - border_size, c - border_size]

    utils.fit_matrix_in_interval(output)
    return np.uint8(output)