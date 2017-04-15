import numpy as np

import utils
import stats
import color
import filter


def main():
    image = utils.load_image('lenna.png')
    image = color.rbg2gray(image)

    np_median_3 = filter.median(image, 3, np.median)
    np_median_9 = filter.median(image, 9, np.median)
    np_median_15 = filter.median(image, 15, np.median)

    qs_median_3 = filter.median(image, 3, stats.median)
    qs_median_9 = filter.median(image, 9, stats.median)
    qs_median_15 = filter.median(image, 15, stats.median)

    utils.display_single_image('Original', image)

    utils.display_single_image('np Median 3', np_median_3)
    utils.display_single_image('np Median 9', np_median_9)
    utils.display_single_image('np Median 15', np_median_15)

    utils.display_single_image('QuickSelect Median 3', qs_median_3)
    utils.display_single_image('QuickSelect Median 9', qs_median_9)
    utils.display_single_image('QuickSelect Median 15', qs_median_15)

    utils.wait_key_and_destroy_windows()


if __name__ == "__main__":
    main()