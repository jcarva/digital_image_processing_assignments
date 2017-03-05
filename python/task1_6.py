# coding=UTF-8
# 1.2 Exibição de bandas individuais (R, G e B) como imagens
# monocromáticas ou coloridas (em tons de R, G ou B, respectivamente)

import numpy as np
import utils


def main():
    image = utils.load_image('lenna.png')
    utils.display_single_image('Original', image)

    grayscale_image = _rbg2gray(image)
    segmented_image = _segment_y_mean(grayscale_image)
    utils.display_single_image('Y Channel', grayscale_image)
    utils.display_single_image('Y Channel Segmented', segmented_image)    

    utils.wait_key_and_destroy_windows()

def _segment_y_mean(image):
    m = np.mean(image)
    print "M: %d" % m
    return _segment_y(image, m)    

def _segment_y(image, m):
    #output = np.empty_like(image)
    output = (image > m).astype(int)*256
    print output
    return output

def _rbg2gray(image):
    # https://en.wikipedia.org/wiki/Grayscale
    # Y ′ = 0.299 R ′ + 0.587 G ′ + 0.114 B
    
    #output = np.empty_like(image[:,:,2])
    output = np.zeros(image.shape[0:2], dtype='uint8')
    blue, green, red = utils.split_channels(image)
    output = 0.299 * red + 0.587 * green + 0.114 * blue

    utils.fit_matrix_in_interval(output)

    return output

if __name__ == "__main__":
    main()