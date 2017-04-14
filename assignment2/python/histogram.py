import numpy as np


def extract(image):
    histogram = np.zeros(256, dtype=np.int)

    for pixel in np.nditer(image):
        histogram[pixel] += 1

    return histogram


# http://www.songho.ca/dsp/histogram/histogram.html
def equalize(histogram, image):
    output = np.empty_like(image)

    total_pixels = image.shape[0] * image.shape[1]
    max_intensity = 255.0  # L - 1

    lut = np.empty_like(histogram)
    sum = 0

    for index, value in enumerate(histogram):
        sum += value
        lut[index] = round(sum * max_intensity / total_pixels)

    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            output[i, j] = lut[image[i, j]]

    return output


def expand(histogram, image):
    output = np.empty_like(image)

    max_intensity = 255.0  # L - 1

    min = np.min(image)
    max = np.max(image)

    print("Expansion min, max: " + str(min) + ", " + str(max))

    lut = np.empty_like(histogram)

    for index, value in enumerate(histogram):
        lut[index] = round((index - min) / float(max - min) * max_intensity)

    for i in range(0, image.shape[0]):
        for j in range(0, image.shape[1]):
            output[i, j] = lut[image[i, j]]

    return output
