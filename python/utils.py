import cv2


def load_image(filename):
    return cv2.imread('../assets/' + filename)


def display_single_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()