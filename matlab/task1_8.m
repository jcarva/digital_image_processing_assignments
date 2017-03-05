% 1.8. Filtros de detecção de bordas Sobel e Laplaciano
function task1_8()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    originalImage = imread(filePath);
    sobel_X_Image = sobel_X_Filter(originalImage);
    sobel_Y_Image = sobel_Y_Filter(originalImage);
    laplacianImage = laplacianFilter(originalImage, 0.5);
            
    % Ploting
    figure();
    subplot(2,4,2), imshow(originalImage,[]), title('Original image')
    subplot(2,4,3), imshow(laplacianImage,[]), title('Laplacian image')
    

    subplot(2,4,6), imshow(sobel_X_Image,[]), title('Sobel X image')
    subplot(2,4,7), imshow(sobel_Y_Image,[]), title('Sobel Y image')
    
end

function output = sobel_X_Filter(input)
    % MatLab shortcut
    h = fspecial('sobel');
    output = imfilter(input, h);
end

function output = sobel_Y_Filter(input)
    % MatLab shortcut
    h = fspecial('sobel');
    output = imfilter(input, h');
end

function output = laplacianFilter(input, alpha)
    % MatLab shortcut
    h = fspecial('laplacian', alpha);
    output = imfilter(input, h);
end