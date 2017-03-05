import cv2
import numpy as np


def load_image(filename):
    return cv2.imread('../assets/' + filename).astype('int16')


def save_image(filename, image):
    cv2.imwrite('../output/' + filename, image)


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


def copy_add_border(image, border_size=1, color=0):
    border_size *= 2
    rows, columns, chanels = image.shape
    output = np.full((rows+border_size, columns+border_size, chanels), color, dtype=np.int)

    for c in range(border_size, columns+border_size):
        for r in range(border_size, rows+border_size):
            output[r - border_size//2, c - border_size//2] = image[r-border_size, c-border_size]

    fit_matrix_in_interval(output)
    return np.uint8(output)


def display_multiple_images(titles, images):
    if len(titles) != len(images):
        print("The length of titles and images are not compatible")
        return False
    else:
        for i in range(0, len(images)):
            cv2.imshow(titles[i], images[i])

