import matplotlib.pyplot as plt
import filter
import utils


def main():
    image = utils.plt_load_image("lenna.png")

    rows, columns, channels = utils.image_shape(image)

    image_out3x3 = filter.average(image, utils.m_n_average_kernel(3, 3))
    image_out3x25 = filter.average(image, utils.m_n_average_kernel(3, 25))
    image_out25x3 = filter.average(image, utils.m_n_average_kernel(25, 3))
    image_out25x25 = filter.average(image, utils.m_n_average_kernel(25, 25))
    image_out33x13 = filter.average(image, utils.m_n_average_kernel(33, 13))

    fig = plt.figure(figsize=(6, 4))

    sub1 = plt.subplot(2, 3, 1)
    sub1.set_title('Original')

    sub2 = plt.subplot(2, 3, 2)
    sub2.set_title('Average k=3x3')

    sub3 = plt.subplot(2, 3, 3)
    sub3.set_title('Average k=3x25')

    sub4 = plt.subplot(2, 3, 4)
    sub4.set_title('Average k=25x3')

    sub5 = plt.subplot(2, 3, 5)
    sub5.set_title('Average k=25x25')

    sub6 = plt.subplot(2, 3, 6)
    sub6.set_title('Average k=33x13')

    if channels == 1:
        sub1.imshow(image, cmap='gray')
        sub2.imshow(image_out3x3, cmap='gray')
        sub3.imshow(image_out3x25, cmap='gray')
        sub4.imshow(image_out25x3, cmap='gray')
        sub5.imshow(image_out25x25, cmap='gray')
        sub6.imshow(image_out33x13, cmap='gray')
    else:
        sub1.imshow(image)
        sub2.imshow(image_out3x3)
        sub3.imshow(image_out3x25)
        sub4.imshow(image_out25x3)
        sub5.imshow(image_out25x25)
        sub6.imshow(image_out33x13)

    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
