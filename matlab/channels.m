img = imread('C:\Users\italo\Pictures\lenna.png');
red = img(:,:,1); 
green = img(:,:,2);
blue = img(:,:,3);

a = zeros(size(img, 1), size(img, 2));

just_red = cat(3, red, a, a);
just_green = cat(3, a, green, a);
just_blue = cat(3, a, a, blue);
concat_img = cat(3, red, green, blue);

figure, imshow(img), title('Original image')

figure, imshow(red), title('Red channel')
figure, imshow(green), title('Green channel')
figure, imshow(blue), title('Blue channel')

figure, imshow(just_red), title('Red channel')
figure, imshow(just_green), title('Green channel')
figure, imshow(just_blue), title('Blue channel')

figure, imshow(concat_img), title('Back to original image')