% 1.7. Filtros de Média e Mediana de ordem escolhida pelo usuário
function task1_7()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    originalImage = imread(filePath);
    averageImage = averageFilter(originalImage, 16);
    medianImage = medianFilter(originalImage, 16);
    
    % Ploting
    figure();        
    subplot(1,3,1), imshow(originalImage,[]), title('Original image')
    subplot(1,3,2), imshow(averageImage,[]), title('Average image')
    subplot(1,3,3), imshow(medianImage,[]), title('Median image')
    
end

function output = averageFilter(input, hsize)
    % MatLab shortcut
    h = fspecial('average', hsize);
    output = imfilter(input,h);
end

function output = medianFilter(input, alpha)
    % MatLab shortcut
    output(:,:,1) = medfilt2(input(:,:,1), [alpha alpha]);
    output(:,:,2) = medfilt2(input(:,:,2), [alpha alpha]);
    output(:,:,3) = medfilt2(input(:,:,3), [alpha alpha]);
end