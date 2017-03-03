import cv2


def load_image(filename):
    return cv2.imread('../assets/' + filename)


def display_single_image(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def display_multiple_images(titles, images):
    if len(titles) != len(images):
        print("The length of titles and images are not compatible")
        return False
    else:
        for i in range(0, len(images)):
            cv2.imshow(titles[i], images[i])

        cv2.waitKey(0)
        cv2.destroyAllWindows()