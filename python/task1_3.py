# coding=UTF-8
# 1.3. Negativo

import cv2
import utils


def main():
    original_image = utils.load_image('lenna.png')
    negative_image = _invert_image(original_image)
    back_to_original = _invert_image(negative_image)

    utils.display_multiple_images(['Lenna', 'Negative Lenna', 'Back to Original'],
                                  [original_image, negative_image, back_to_original])

    utils.wait_key_and_destroy_windows()


def _invert_image(image):
    return 255 - image


if __name__ == "__main__":
    main()
