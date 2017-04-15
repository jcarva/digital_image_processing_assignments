import random
import numpy as np


def salt_pepper(image, p):
    output = np.zeros(image.shape, np.int)

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()

            if rdn < p:
                rdn = random.random()
                output[i][j] = (rdn > 0.5) * 255
            else:
                output[i][j] = image[i][j]

    return output