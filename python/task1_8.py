# coding=UTF-8
#1.8. Filtros de detecção de bordas Sobel e Laplaciano

import cv2
import utils


def main():
    original_image = utils.load_image('lenna.png')
    sobel__x_image = _sobel_x_filter(original_image, 0.4, 5)
    sobel__y_image = _sobel_y_filter(original_image, 0.4, 5)
    laplacian_image = _laplacian_filter(original_image, 0.4, 5)

    utils.display_multiple_images(['Lenna', 'Sobel_X Lenna', 'Sobel_Y Lenna', 'Laplacian Lenna'],
                                  [original_image, sobel__x_image, sobel__y_image, laplacian_image])

    utils.wait_key_and_destroy_windows()


def _sobel_x_filter(image, scale=0.5, kernel_size=3, ddepth=cv2.CV_32F, delta=0):
    return cv2.Sobel(image, scale=scale, dx=1, dy=0, ksize=kernel_size, ddepth=ddepth, delta=delta, borderType=cv2.BORDER_DEFAULT)


def _sobel_y_filter(image, scale=0.5, kernel_size=3, ddepth=cv2.CV_32F, delta=0):
    return cv2.Sobel(image, scale=scale, dx=0, dy=1, ksize=kernel_size, ddepth=ddepth, delta=delta, borderType=cv2.BORDER_DEFAULT)


def _laplacian_filter(image, scale=0.5, kernel_size=3, ddepth=cv2.CV_32F, delta=0):
    return cv2.Laplacian(image, scale=scale, ksize=kernel_size, ddepth=ddepth, delta=delta)


if __name__ == "__main__":
    main()
