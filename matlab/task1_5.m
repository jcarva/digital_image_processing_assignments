% 1.5. Controle de brilho multiplicativo 
% (valor do pixel resultante = valor do pixel original * c, c real não negativo)
function task1_5()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    BRIGHTNESS_ADJUSTMENT = 1.8;
    
    originalImage = imread(filePath);
    modifiedImage = MultiplicativeBrightnessControl(originalImage, BRIGHTNESS_ADJUSTMENT);
        
    % Ploting
    figure();        
    subplot(1,3,1.3), imshow(originalImage,[]), title('Original image')
    subplot(1,3,2.5), imshow(modifiedImage,[]), title('Modified image')
    
    grayscaleImage  = rgb2gray(originalImage);
    modifiedGrayscaleImage = MultiplicativeBrightnessControl(grayscaleImage, BRIGHTNESS_ADJUSTMENT);
    
    figure();        
    subplot(1,3,1.3), imshow(grayscaleImage,[]), title('Original Grayscale')
    subplot(1,3,2.5), imshow(modifiedGrayscaleImage,[]), title('Modified Grayscale')
    
end

function output = MultiplicativeBrightnessControl(input, brightness)
    % MatLab shortcut
    % The pixel type uint8 cannot go higher than 255.
    output = uint8(brightness * input);
end