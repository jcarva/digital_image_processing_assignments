% 1. Para uma imagem com baixo contraste, implemente as operações:
%   a. Equalização de histograma;
%   b. Expansão de histograma.
function task1()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    originalImage = imread(filePath);

    [~, ~, channels] = size(originalImage);

    if channels == 3
        grayIm = rgb2gray(originalImage);
    else 
        grayIm = originalImage;
    end

    histEq = histeq(grayIm, 256);    
    histExp = imadjust(grayIm,stretchlim(grayIm),[]);

    % Ploting
    fig = figure(1);
    set (fig, 'Units', 'normalized', 'Position', [0,0,1,1]);

    subplot(2,3,1), imshow(grayIm), title('Original image')
    subplot(2,3,4), imhist(grayIm), title('Image histogram')
    subplot(2,3,2), imshow(histEq), title('Image Equalization')
    subplot(2,3,5), imhist(histEq), title('Histogram Equalization')
    subplot(2,3,3), imshow(histExp), title('Image Expansion')
    subplot(2,3,6), imhist(histExp), title('Histogram Expansion')

    % saveas(fig,strcat('output',filesep,mfilename,'.png'));
end