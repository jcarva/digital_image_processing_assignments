% 1.7. Filtros de Média e Mediana de ordem escolhida pelo usuário
function tarefa1_7()
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
    input = rgb2gray(input);
    output = medfilt2(input, [alpha alpha]);
end