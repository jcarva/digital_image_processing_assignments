% 1.8. Filtros de detecção de bordas Sobel e Laplaciano
function tarefa1_8()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    originalImage = imread(filePath);
    sobelImage = sobelFilter(originalImage);
    laplacianImage = laplacianFilter(originalImage, 0.5);
    
        
    % Ploting
    figure();        
    subplot(1,3,1), imshow(originalImage,[]), title('Original image')
    subplot(1,3,2), imshow(sobelImage,[]), title('Sobel image')
    subplot(1,3,3), imshow(laplacianImage,[]), title('Laplacian image')
    
end

function output = sobelFilter(input)
    % MatLab shortcut
    h = fspecial('sobel');
    output = imfilter(input,h);
end

function output = laplacianFilter(input, alpha)
    % MatLab shortcut
    h = fspecial('laplacian', alpha);
    output = imfilter(input,h);
end