% Crossplatform path
assetsDir = ['..' filesep 'assets' filesep];
filePath = strcat(assetsDir, 'lenna.png');

img = imread(filePath);
red = img(:,:,1); 
green = img(:,:,2);
blue = img(:,:,3);

a = zeros(size(img, 1), size(img, 2));

just_red = cat(3, red, a, a);
just_green = cat(3, a, green, a);
just_blue = cat(3, a, a, blue);
concat_img = cat(3, red, green, blue);

figure()
subplot(2,4,1)
imshow(img), title('Original image')

subplot(2,4,2), imshow(red), title('Red channel')
subplot(2,4,3), imshow(green), title('Green channel')
subplot(2,4,4), imshow(blue), title('Blue channel')

subplot(2,4,5), imshow(just_red), title('Red channel')
subplot(2,4,6), imshow(just_green), title('Green channel')
subplot(2,4,7), imshow(just_blue), title('Blue channel')

subplot(2,4,8), imshow(concat_img), title('Back to original image')