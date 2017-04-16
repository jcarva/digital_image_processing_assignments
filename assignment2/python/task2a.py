# coding=UTF-8

# 2. Para uma imagem com dimensões 1024x1024, calcule o tempo de processamento para:
#   a. Aplicação do Filtro da Média MxN;

import matplotlib.pyplot as plt
import filter
import utils
import timer


def main():
    image = utils.plt_load_image("lena_headey_1024.jpg")
    image = (image / float(image.max())) ** (1 / 1.0)

    print("Shape:", image.shape)
    print("Values min/max:", image.min(), image.max())

    rows, columns, channels = utils.image_shape(image)

    image_out3x3 = timer.count('[Average k=3x3]', filter.average, [image, utils.m_n_average_kernel(3, 3)])
    image_out3x25 = timer.count('[Average k=3x25]', filter.average, [image, utils.m_n_average_kernel(3, 25)])
    image_out25x3 = timer.count('[Average k=25x3]', filter.average, [image, utils.m_n_average_kernel(25, 3)])
    image_out25x25 = timer.count('[Average k=25x25]', filter.average, [image, utils.m_n_average_kernel(25, 25)])
    image_out13x53 = timer.count('[Average k=13x53]', filter.average, [image, utils.m_n_average_kernel(13, 53)])

    fig = plt.figure(figsize=(6, 4))

    sub1 = plt.subplot(2, 3, 1)
    sub1.set_title('Original')

    sub2 = plt.subplot(2, 3, 2)
    sub2.set_title('k=3x3')

    sub3 = plt.subplot(2, 3, 3)
    sub3.set_title('k=3x25')

    sub4 = plt.subplot(2, 3, 4)
    sub4.set_title('k=25x3')

    sub5 = plt.subplot(2, 3, 5)
    sub5.set_title('k=25x25')

    sub6 = plt.subplot(2, 3, 6)
    sub6.set_title('k=13x53')

    if channels == 1:
        sub1.imshow(image, cmap='gray')
        sub2.imshow(image_out3x3, cmap='gray')
        sub3.imshow(image_out3x25, cmap='gray')
        sub4.imshow(image_out25x3, cmap='gray')
        sub5.imshow(image_out25x25, cmap='gray')
        sub6.imshow(image_out13x53, cmap='gray')
    else:
        sub1.imshow(image)
        sub2.imshow(image_out3x3)
        sub3.imshow(image_out3x25)
        sub4.imshow(image_out25x3)
        sub5.imshow(image_out25x25)
        sub6.imshow(image_out13x53)

    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
