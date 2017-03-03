% 1.4. Controle de brilho aditivo
% (valor do pixel resultante = valor do pixel original + c, c inteiro)
function task1_4()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    BRIGHTNESS_ADJUSTMENT = 60;
    
    originalImage = imread(filePath);
    modifiedImage = AdditiveBrightnessControl(originalImage, BRIGHTNESS_ADJUSTMENT);
        
    % Ploting
    figure();        
    subplot(1,3,1.3), imshow(originalImage,[]), title('Original image')
    subplot(1,3,2.5), imshow(modifiedImage,[]), title('Modified image')
    
end

function output = AdditiveBrightnessControl(input, brightness)
    % MatLab shortcut
    % The pixel type uint8 cannot go higher than 255.
    output = uint8(brightness + input);
end