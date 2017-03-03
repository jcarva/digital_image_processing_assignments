import cv2
import numpy as np

def load_image(filename):
    return cv2.imread('../assets/' + filename)


def display_single_image(title, image):
    cv2.imshow(title, image)


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
    n_cols = blue[0].size
    n_rows = blue[1].size

    output = []

    for col in range(0, n_cols):
        output.append([None] * n_rows)

        for row in range(0, n_rows):
            output[col][row] = [blue[col][row], green[col][row], red[col][row]]

    return np.array(output)


def display_multiple_images(titles, images):
    if len(titles) != len(images):
        print("The length of titles and images are not compatible")
        return False
    else:
        for i in range(0, len(images)):
            cv2.imshow(titles[i], images[i])

