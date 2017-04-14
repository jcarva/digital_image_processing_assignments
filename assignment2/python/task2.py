import matplotlib.pyplot as plt
import filter

def main():
    image = plt.imread('../assets/lenna.png')

    image_out3x3 = filter.average(image, 3, 3)
    image_out25x25 = filter.average(image, 25, 25)

    fig = plt.figure(figsize=(4, 4))

    sub1 = fig.add_subplot(221)
    sub1.set_title('Original')
    sub1.imshow(image)

    sub2 = fig.add_subplot(222)
    sub2.set_title('Average k=3x3')
    sub2.imshow(image_out3x3)

    sub3 = fig.add_subplot(223)
    sub3.set_title('Average k=25x25')
    sub3.imshow(image_out25x25)

    plt.show()

if __name__ == "__main__":
    main()
