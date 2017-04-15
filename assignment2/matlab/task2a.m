% 2. Para uma imagem com dimensões 1024x1024, calcule o tempo de processamento para:
%   a. Aplicação do Filtro da Média MxN;
function task2a()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lena_headey_1024.jpg');
    originalImage = imread(filePath);
    
    averageImage_3x3 = averageTimer('[Average k=3x3]', @averageFilter, originalImage, [3 3]);
    averageImage_3x25 = averageTimer('[Average k=3x25]', @averageFilter, originalImage, [3 25]);
    averageImage_25x3 = averageTimer('[Average k=25x3]', @averageFilter, originalImage, [25 3]);
    averageImage_25x25 = averageTimer('[Average k=25x25]', @averageFilter, originalImage, [25 25]);
    averageImage_13x53 = averageTimer('[Average k=13x53]', @averageFilter, originalImage, [13 53]);
    
    % Ploting
    fig = figure(1);
    set (fig, 'Units', 'normalized', 'Position', [0,0,1,1]);

    subplot(2,3,1), imshow(originalImage), title('Original image')
    subplot(2,3,2), imshow(averageImage_3x3), title('k=3x3')
    subplot(2,3,3), imshow(averageImage_3x25), title('k=3x25')
    subplot(2,3,4), imshow(averageImage_25x3), title('k=25x3')
    subplot(2,3,5), imshow(averageImage_25x25), title('k=25x25')
    subplot(2,3,6), imshow(averageImage_13x53), title('k=13x53')
    
    %saveas(fig,strcat('output',filesep,mfilename,'.png'));
end

function output = averageFilter(input, hsize)
    % MatLab shortcut
    h = fspecial('average', hsize);
    output = imfilter(input,h);
end

function output = averageTimer(name, f, arg1, arg2)
    tic;
    output = f(arg1, arg2);
    t = toc;
    fprintf('%s: %f seconds.\n', name, t);
end
