# coding=UTF-8
# 2. Reproduza, utilizando o MATLAB e outra linguagem de programação de sua
# escolha, o exemplo apresentado na página 3 deste documento
# (ImageProcessing Toolbox User'sGuide - UsingMedianFiltering).
# Discuta o experimento no relatório

import utils
import filter
import numpy as np
import noise


def main():
    image = utils.load_image('lenna.png')

    sp_image = noise.salt_pepper(image, 0.05)
    utils.display_single_image('Salt&Pepper Noise', sp_image)

    filter1 = filter.apply_kernel(sp_image, utils.average_kernel(3))
    utils.display_single_image('Average Filter', filter1)

    filter2 = filter.median_filter(sp_image, 3)
    utils.display_single_image('Median Filter', filter2)

    utils.wait_key_and_destroy_windows()


if __name__ == "__main__":
    main()
