% 1.3. Negativo
% (intensidade na saída = 255 - intensidade na entrada)
function task1_3()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    originalImage = imread(filePath);
    negativeImage = getNegative(originalImage);
    backToOriginalImage = getNegative(negativeImage);
        
    % Ploting
    fig2=figure();        
    subplot(1,3,1), imshow(originalImage,[]), title('Original image')
    subplot(1,3,2), imshow(negativeImage,[]), title('Negative image')
    subplot(1,3,3), imshow(backToOriginalImage,[]), title('Back to original image')
       
    grayScale = rgb2gray(originalImage);
    negativeGrayScaleImage = getNegative(grayScale);
    backToGrayScale = getNegative(negativeGrayScaleImage);
    
    fig=figure();        
    subplot(1,3,1), imshow(grayScale,[]), title('Grayscale image')
    subplot(1,3,2), imshow(negativeGrayScaleImage,[]), title('Negative grayscale image')
    subplot(1,3,3), imshow(backToGrayScale,[]), title('Back to grayscale image')
    
    saveas(fig,strcat('output',filesep,mfilename,'_1.png'));
    saveas(fig2,strcat('output',filesep,mfilename,'_2.png'));
    
end

function output = getNegative(input)
    % MatLab shortcut
    % output = imcomplement(input);
    
    output = (255 - input);
end