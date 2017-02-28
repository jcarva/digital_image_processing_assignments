% 1.5. Controle de brilho multiplicativo (valor do pixel resultante = valor do pixel original * c, c real não negativo)
function tarefa1_5()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    originalImage = imread(filePath);
    brighterImage = MultiplicativeBrightnessControl(originalImage, 1.8);
        
    % Ploting
    figure();        
    subplot(1,3,1.3), imshow(originalImage,[]), title('Original image')
    subplot(1,3,2.5), imshow(brighterImage,[]), title('Brighter image')
    
end

function output = MultiplicativeBrightnessControl(input, brightness)
    % MatLab shortcut
    % The pixel type uint8 cannot go higher than 255.
    output = uint8(brightness * input);
end