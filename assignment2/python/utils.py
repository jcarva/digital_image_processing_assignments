import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_image(filename):
    return cv2.imread('../assets/' + filename).astype('int16')


def plt_load_image(filename):
    return plt.imread('../assets/' + filename)


def display_single_image(title, image):
    cv2.imshow(title, image.astype('uint8'))


def wait_key_and_destroy_windows():
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def split_channels(image):
    """
    :param image: RGB image
    :return: B, G, R channels
    """
    return image[:, :, 0], \
        image[:, :, 1], \
        image[:, :, 2]


def merge_channels(blue, green, red):
    # Same as np.dstack((blue, green, red))
    n_rows = blue[0].size
    n_cols = blue[1].size

    output = []

    for row in range(0, n_rows):
        output.append([None] * n_cols)

        for col in range(0, n_cols):
            output[row][col] = [blue[row][col], green[row][col], red[row][col]]

    return np.array(output)


def fit_matrix_in_interval(matrix, min_value=0, max_value=255):
    matrix[matrix < min_value] = min_value
    matrix[matrix > max_value] = max_value


def m_n_average_kernel(m, n):
    return np.full((m, n), 1/float(m * n))


def image_shape(image):
    if len(image.shape) == 3:
        rows, columns, channels = image.shape
    else:
        rows, columns = image.shape
        channels = 1

    return rows, columns, channels

