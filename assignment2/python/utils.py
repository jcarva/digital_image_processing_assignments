import cv2


def load_image(filename):
    return cv2.imread('../assets/' + filename).astype('int16')


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


def fit_matrix_in_interval(matrix, min_value=0, max_value=255):
    matrix[matrix < min_value] = min_value
    matrix[matrix > max_value] = max_value