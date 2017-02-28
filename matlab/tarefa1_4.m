% 1.4. Controle de brilho aditivo (valor do pixel resultante = valor do pixel original + c, c inteiro)
function tarefa1_4()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    originalImage = imread(filePath);
    brighterImage = AdditiveBrightnessControl(originalImage, 60);
        
    % Ploting
    figure();        
    subplot(1,3,1.3), imshow(originalImage,[]), title('Original image')
    subplot(1,3,2.5), imshow(brighterImage,[]), title('Brighter image')
    
end

function output = AdditiveBrightnessControl(input, brightness)
    % MatLab shortcut
    % The pixel type uint8 cannot go higher than 255.
    output = uint8(brightness + input);
end