# coding=UTF-8

# 3. Para uma imagem com dimensões 1024x1024, calcule o tempo de processamento para:
#   a. Aplicação do Filtro da Mediana 15x15 utilizando uma função de sort para
# ordenar a janela de pixels e encontrar a mediana.
#   b. Aplicação do Filtro da Mediana 15x15 utilizando uma função de mediana O(n)
# para encontrar a mediana. Sugestão: QuickSelect ou Median of Medians.

import numpy as np
import utils
import stats
import color
import timer
import filter


def main():
    image = utils.load_image('lena_headey_1024.jpg')
    image = color.rbg2gray(image)

    median_3 = timer.count('Median 3', filter.median, [image, 3, stats.median])
    np_median_3 = timer.count('NP Median 3', filter.median, [image, 3, np.median])
    qs_median_3 = timer.count('QuickSelect Median 3', filter.median, [image, 3, stats.quick_median])

    median_9 = timer.count('Median 9', filter.median, [image, 9, stats.median])
    np_median_9 = timer.count('NP Median 9', filter.median, [image, 9, np.median])
    qs_median_9 = timer.count('QuickSelect Median 9', filter.median, [image, 9, stats.quick_median])

    median_15 = timer.count('Median 15', filter.median, [image, 15, stats.median])
    np_median_15 = timer.count('NP Median 15', filter.median, [image, 15, np.median])
    qs_median_15 = timer.count('QuickSelect Median 15', filter.median, [image, 15, stats.quick_median])

    utils.display_single_image('Original', image)

    utils.display_single_image('Median 3', median_3)
    utils.display_single_image('Median 9', median_9)
    utils.display_single_image('Median 15', median_15)

    utils.display_single_image('np Median 3', np_median_3)
    utils.display_single_image('np Median 9', np_median_9)
    utils.display_single_image('np Median 15', np_median_15)

    utils.display_single_image('QuickSelect Median 3', qs_median_3)
    utils.display_single_image('QuickSelect Median 9', qs_median_9)
    utils.display_single_image('QuickSelect Median 15', qs_median_15)

    utils.wait_key_and_destroy_windows()


if __name__ == "__main__":
    main()