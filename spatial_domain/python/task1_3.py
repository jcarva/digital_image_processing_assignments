# coding=UTF-8
# 1.3. Negativo
# (intensidade na saída = 255 - intensidade na entrada)

import utils
import color


def main():
    original_image = utils.load_image('lenna.png')

    grayscale_image = color.rbg2gray(original_image)
    negative_grayscale_image = _invert_image(grayscale_image)
    back_to_grayscale = _invert_image(negative_grayscale_image)

    negative_color_image = _invert_image(original_image)
    back_to_original = _invert_image(negative_color_image)

    utils.display_multiple_images(['Lenna', 'Negative Color Lenna', 'Back to Original'],
                                  [original_image, negative_color_image, back_to_original])

    utils.display_multiple_images(['Grayscale Lenna', 'Negative Grayscale', 'Back to Grayscale'],
                                  [grayscale_image, negative_grayscale_image, back_to_grayscale])

    utils.wait_key_and_destroy_windows()


def _invert_image(image):
    return 255 - image.astype('uint8')


if __name__ == "__main__":
    main()
