# coding=UTF-8
import numpy as np
import color
import utils
import noise
import time
import stats


def main():
	image = utils.load_image('lenna.png')
	grayscale_image = color.rbg2gray(image)
	noise_images = []

	for i in range(0, 15):
		noise_images.append(noise.salt_pepper(grayscale_image, 0.1))

	noise_images = np.array(noise_images)
	
	t = time.clock()
	
	mean_image = _multiple_images_processing(noise_images, mean)
	
	tt = time.clock()
	print "Mean time %s." % (tt-t)

	median_image = _multiple_images_processing(noise_images, stats.median)
	
	tt = time.clock()
	print "Median time %s." % (tt-t)
	
	utils.display_single_image('Original', grayscale_image)
	utils.display_single_image('Noise sample',  noise_images[0])
	utils.display_single_image('Mean result', mean_image)
	utils.display_single_image('Median result', median_image)

    #utils.save_image('yiq.png', yiq)

	utils.wait_key_and_destroy_windows()

def mean(ls):
	sum = 0
	for i in ls:
		sum=sum+i
	return sum/(len(ls))

def _multiple_images_processing(images, f):	
	result = np.empty_like(images[0,:,:])

	for i in range(0, images.shape[1]):
		for j in range(0, images.shape[2]):
			pixels = images[:,i,j]
			result[i,j] = f(pixels)	

	return result


if __name__ == "__main__":
	main()
