# coding=UTF-8
# 2.0

import cv2
import utils
import random
import numpy as np


def main():
    image = utils.load_image('lenna.png')

    sp_image = _salt_pepper(image, 0.05)
    utils.display_single_image('Salt&Pepper Noise', sp_image)    

    print _mean_filter(3)

    # filter1 = _filter(sp_image, [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])
    # utils.display_single_image('Mean Filter', filter1)    

    # filter2 = _filter(sp_image, [[0.0, 0.125, 0.0], [0.125, 0.25, 0.125], [0.0, 0.125, 0.0]])
    # utils.display_single_image('Median Filter', filter2)    

    utils.wait_key_and_destroy_windows()


def _salt_pepper(image, p):
    output = np.zeros(image.shape,np.uint8)    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()            
            if rdn < p:                
                rdn = random.random()
                output[i][j] = (rdn>0.5)*255                            
            else:
                output[i][j] = image[i][j]
    return output

if __name__ == "__main__":
    main()
