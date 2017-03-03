% 1.3. Negativo
% (intensidade na saída = 255 - intensidade na entrada)
function task1_3()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    originalImage = imread(filePath);
    negativeImage = getNegative(originalImage);
    backToOriginalImage = getNegative(negativeImage);
        
    % Ploting
    figure();        
    subplot(1,3,1), imshow(originalImage,[]), title('Original image')
    subplot(1,3,2), imshow(negativeImage,[]), title('Negative image')
    subplot(1,3,3), imshow(backToOriginalImage,[]), title('Back to original image')
    
end

function output = getNegative(input)
    % MatLab shortcut
    % output = imcomplement(input);
    
    output = (255 - input);
end