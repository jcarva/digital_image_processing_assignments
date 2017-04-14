import scipy.signal
import matplotlib.pyplot as plt

import utils

def main():
    image = plt.imread('../assets/lenna.png')

    filter_kernel = utils.average_kernel(25)

    blue_mono, green_mono, red_mono = utils.split_channels(image)

    r = scipy.signal.convolve2d(red_mono, filter_kernel, mode='same', boundary='fill', fillvalue=0)
    g = scipy.signal.convolve2d(green_mono, filter_kernel, mode='same', boundary='fill', fillvalue=0)
    b = scipy.signal.convolve2d(blue_mono, filter_kernel, mode='same', boundary='fill', fillvalue=0)

    image_out = utils.merge_channels(b, g, r)

    fig, (original, average) = plt.subplots(1, 2)

    original.imshow(image)
    original.set_title('Original')
    average.imshow(image_out)
    average.set_title('Average')
    plt.show()

if __name__ == "__main__":
    main()