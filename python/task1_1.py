# 1.1. Conversao RGB-YIQ-RGB
# (cuidado com os limites de R, G e B!)

import cv2
import utils

img = utils.load_image('lenna.png')

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()