% 1.8. Filtros de detecção de bordas Sobel e Laplaciano
function task1_8()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'bicycle.png');
    
    originalImage = imread(filePath);
    sobel_X_Image = sobel_X_Filter(originalImage);
    sobel_Y_Image = sobel_Y_Filter(originalImage);
    sobel_XY = sobel_X_Image + sobel_Y_Image;
    laplacianImage = laplacianFilter(originalImage, 0.5);
            
    % Ploting
    fig=figure();
    subplot(1,2,1), imshow(originalImage,[]), title('Original image')
    subplot(1,2,2), imshow(laplacianImage,[]), title('Laplacian image')
    
    fig2=figure();
    subplot(2,2,1), imshow(originalImage,[]), title('Original image')
    subplot(2,2,2), imshow(sobel_X_Image,[]), title('Sobel X image')
    subplot(2,2,3), imshow(sobel_Y_Image,[]), title('Sobel Y image')
    subplot(2,2,4), imshow(sobel_XY,[]), title('Sobel X+Y image')
    
    saveas(fig,strcat('output',filesep,mfilename,'_1.png'));
    saveas(fig2,strcat('output',filesep,mfilename,'_2.png'));
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