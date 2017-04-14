import scipy.signal
import utils


def average(image, m=3, n=3):

    filter_kernel = utils.average_kernel(m) if (m == n) else utils.average_kernel(55)

    blue_mono, green_mono, red_mono = utils.split_channels(image)

    r = scipy.signal.convolve2d(red_mono, filter_kernel, mode='same', boundary='fill', fillvalue=0)
    g = scipy.signal.convolve2d(green_mono, filter_kernel, mode='same', boundary='fill', fillvalue=0)
    b = scipy.signal.convolve2d(blue_mono, filter_kernel, mode='same', boundary='fill', fillvalue=0)

    return utils.merge_channels(b, g, r)

