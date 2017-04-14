# coding=UTF-8

import utils
import color
import histogram as hist
import matplotlib.pyplot as plt

def main():
    image = utils.load_image('lenna.png')
    image = color.rbg2gray(image)
    histogram = hist.extract(image)

    equalized_image = hist.equalize(histogram, image)
    equalized_histogram = hist.extract(equalized_image)

    plt.figure(1)
    plt.bar(range(0, 255), histogram)
    plt.title('Original Histogram')

    plt.figure(2)
    plt.bar(range(0, 255), equalized_histogram)
    plt.title('Equalized Histogram')

    plt.show(block=False)

    utils.display_single_image('Original', image)
    utils.display_single_image('Equalized', equalized_image)

    utils.wait_key_and_destroy_windows()


if __name__ == "__main__":
    main()