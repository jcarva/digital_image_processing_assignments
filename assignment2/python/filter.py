import scipy.signal
import utils


def average(image, kernel):

    rows, columns, channels = utils.image_shape(image)

    if channels == 1:
        return scipy.signal.convolve2d(image, kernel, mode='same', boundary='fill', fillvalue=0)
    else:
        blue_mono, green_mono, red_mono = utils.split_channels(image)

        r = scipy.signal.convolve2d(red_mono, kernel, mode='same', boundary='fill', fillvalue=0)
        g = scipy.signal.convolve2d(green_mono, kernel, mode='same', boundary='fill', fillvalue=0)
        b = scipy.signal.convolve2d(blue_mono, kernel, mode='same', boundary='fill', fillvalue=0)

        return utils.merge_channels(b, g, r)

