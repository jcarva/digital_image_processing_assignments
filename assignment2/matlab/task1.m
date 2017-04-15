% 1. Para uma imagem com baixo contraste, implemente as operações:
%   a. Equalização de histograma;
%   b. Expansão de histograma.
function task1()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    originalImage = imread(filePath);
        
    yiqImage = rgb2ntsc(originalImage);
    % Get grayscale image
    grayIm = yiqImage(:,:,1);
        
    histEq = histeq(grayIm);    
    histExp = imadjust(grayIm,stretchlim(grayIm),[]);
    
    % Ploting
    figure();        
    subplot(1,2,1), imshow(grayIm), title('Original image')
    subplot(1,2,2), imhist(grayIm), title('Image histogram')
    figure();
    subplot(1,2,1), imshow(histEq), title('Image Equalization')  
    subplot(1,2,2), imhist(histEq), title('Histogram Equalization')     
    figure();
    subplot(1,2,1), imshow(histExp), title('Image Expansion')  
    subplot(1,2,2), imhist(histExp), title('Histogram Expansion') 

    
    %saveas(fig,strcat('output',filesep,mfilename,'.png'));
end