% 2. Para uma imagem com dimensões 1024x1024, calcule o tempo de processamento para:
%   b. Aplicação do Filtro da Média Mx1 sobre a imagem resultante da aplicação do Filtro da Média 1xN;
function task2b()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lena_headey_1024.jpg');
    
    originalImage = imread(filePath);
    
    %1xN
    image_out1x3 = averageFilter(originalImage, [1 3]);
    image_out1x25 = averageFilter(originalImage, [1 25]);
    image_out1x53 = averageFilter(originalImage, [1 53]);
    
    
    %Mx1
    image_out3x1_on_1x3 = averageFilter(image_out1x3, [3 1]);
    image_out25x1_on_1x3 = averageFilter(image_out1x3, [25 1]);

    image_out3x1_on_1x25 = averageFilter(image_out1x25, [3 1]);
    image_out25x1_on_1x25 = averageFilter(image_out1x25, [25 1]);
    
    image_out13x1_on_1x53 = averageFilter(image_out1x53, [13 1]);
    
    
    % Ploting
    fig = figure(1);
    set (fig, 'Units', 'normalized', 'Position', [0,0,1,1]);

    subplot(2,3,1), imshow(originalImage), title('Original image')
    subplot(2,3,2), imshow(image_out3x1_on_1x3), title('k=3x1 on k=1x3')
    subplot(2,3,3), imshow(image_out25x1_on_1x3), title('k=25x1 on k=1x3')
    subplot(2,3,4), imshow(image_out3x1_on_1x25), title('k=3x1 on k=1x25')
    subplot(2,3,5), imshow(image_out25x1_on_1x25), title('k=25x1 on k=1x25')
    subplot(2,3,6), imshow(image_out13x1_on_1x53), title('k=13x1 on k=1x53')
    
    
    %saveas(fig,strcat('output',filesep,mfilename,'.png'));
end

function output = averageFilter(input, hsize)
    % MatLab shortcut
    h = fspecial('average', hsize);
    output = imfilter(input,h);
end
