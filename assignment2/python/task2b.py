# coding=UTF-8

# 2. Para uma imagem com dimensões 1024x1024, calcule o tempo de processamento para:
#   b. Aplicação do Filtro da Média Mx1 sobre a imagem resultante da aplicação do Filtro da Média 1xN;

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

    #1xN
    image_out1x3 = timer.count('[Average k=1x3]', filter.average, [image, utils.m_n_average_kernel(1, 3)])
    image_out1x25 = timer.count('[Average k=1x25]', filter.average, [image, utils.m_n_average_kernel(1, 25)])

    image_out1x53 = timer.count('[Average k=1x53]', filter.average, [image, utils.m_n_average_kernel(1, 53)])

    #Mx1
    image_out3x1_on_1x3 = timer.count('[Average k=3x1 on k=1x3]', filter.average, [image_out1x3, utils.m_n_average_kernel(3, 1)])
    image_out25x1_on_1x3 = timer.count('[Average k=25x1 on k=1x3]', filter.average, [image_out1x3, utils.m_n_average_kernel(25, 1)])

    image_out3x1_on_1x25 = timer.count('[Average k=3x1 on k=1x25]', filter.average, [image_out1x25, utils.m_n_average_kernel(3, 1)])
    image_out25x1_on_1x25 = timer.count('[Average k=25x1 on k=1x25]', filter.average, [image_out1x25, utils.m_n_average_kernel(25, 1)])

    image_out13x1_on_1x53 = timer.count('[Average k=13x1 on k=1x53]', filter.average, [image_out1x53, utils.m_n_average_kernel(13, 1)])

    fig = plt.figure(figsize=(6, 4))

    sub1 = plt.subplot(2, 3, 1)
    sub1.set_title('Original')

    sub2 = plt.subplot(2, 3, 2)
    sub2.set_title('k=3x1 on k=1x3')

    sub3 = plt.subplot(2, 3, 3)
    sub3.set_title('k=3x1 on k=1x25')

    sub4 = plt.subplot(2, 3, 4)
    sub4.set_title('k=25x1 on k=1x3')

    sub5 = plt.subplot(2, 3, 5)
    sub5.set_title('k=25x1 on k=1x25')

    sub6 = plt.subplot(2, 3, 6)
    sub6.set_title('k=13x1 on k=1x53')

    if channels == 1:
        sub1.imshow(image, cmap='gray')
        sub2.imshow(image_out3x1_on_1x3, cmap='gray')
        sub3.imshow(image_out3x1_on_1x25, cmap='gray')
        sub4.imshow(image_out25x1_on_1x3, cmap='gray')
        sub5.imshow(image_out25x1_on_1x25, cmap='gray')
        sub6.imshow(image_out13x1_on_1x53, cmap='gray')
    else:
        sub1.imshow(image)
        sub2.imshow(image_out3x1_on_1x3)
        sub3.imshow(image_out3x1_on_1x25)
        sub4.imshow(image_out25x1_on_1x3)
        sub5.imshow(image_out25x1_on_1x25)
        sub6.imshow(image_out13x1_on_1x53)

    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
