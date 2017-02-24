% Crossplatform path
assetsDir = ['..' filesep 'assets' filesep];
fileName = strcat(assetsDir, 'lenna.png');

my_image = im2double(imread(fileName));
my_image = my_image(:,:,1);

image_thresholded = zeros(size(my_image));
% loop over all rows and columns
for ii=1:size(my_image,1)
    for jj=1:size(my_image,2)
        % get pixel value
        pixel=my_image(ii,jj);
          % check pixel value and assign new value
          if pixel<0.5
              new_pixel=0;
          elseif pixel>3
              new_pixel=256;
          else
              new_pixel = pixel;
          end
          % save new pixel value in thresholded image
          image_thresholded(ii,jj)=255-pixel;
      end
  end
% display result
figure()
subplot(1,2,1)
imshow(my_image,[])
title('original image')
subplot(1,2,2)
imshow(image_thresholded,[])
title('thresholded image')