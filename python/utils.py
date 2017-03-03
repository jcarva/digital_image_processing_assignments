import cv2

def load_image(filename):
    return cv2.imread('../assets/' + filename)


def display_single_image(title, image):
    cv2.imshow(title, image)

def wait_key_and_destroy_windows():
    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''
Return B, G, R channels
'''
def split_channels(image):
    return image[:,:,0], image[:,:,1], image[:,:,2]

def display_multiple_images(titles, images):
    if len(titles) != len(images):
        print("The length of titles and images are not compatible")
        return False
    else:
        for i in range(0, len(images)):
            cv2.imshow(titles[i], images[i])

        cv2.waitKey(0)
        cv2.destroyAllWindows()
