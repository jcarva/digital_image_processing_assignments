# coding=UTF-8

import utils
import histogram as hist
import matplotlib.pyplot as plt

def main():
    image = utils.plt_load_image('underexposed2.jpg')

    histogram = hist.extract(image)

    equalized_image = hist.equalize(histogram, image)
    equalized_histogram = hist.extract(equalized_image)

    expanded_image = hist.expand(histogram, image)
    expanded_histogram = hist.extract(expanded_image)

    plt.figure(1)
    plt.xlim([0, 255])
    plt.bar(range(0, 256), histogram)
    plt.title('Image histogram')

    plt.figure(2)
    plt.xlim([0, 255])
    plt.bar(range(0, 256), equalized_histogram)
    plt.title('Histogram Equalization')

    plt.figure(3)
    plt.xlim([0, 255])
    plt.bar(range(0, 256), expanded_histogram)
    plt.title('Histogram Expansion')

    plt.show(block=False)

    utils.display_single_image('Original Image', image)
    utils.save_image('python_hist_original_img.png', image)
    utils.display_single_image('Image Equalization', equalized_image)
    utils.save_image('python_hist_equalization_img.png', equalized_image)
    utils.display_single_image('Image Expansion', expanded_image)
    utils.save_image('python_hist_expansion_img.png', expanded_image)

    utils.wait_key_and_destroy_windows()


if __name__ == "__main__":
    main()