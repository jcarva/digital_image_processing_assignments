% 1.4. Controle de brilho aditivo
% (valor do pixel resultante = valor do pixel original + c, c inteiro)
function task1_4()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    BRIGHTNESS_ADJUSTMENT = 60;
    
    originalImage = imread(filePath);
    modifiedImage = AdditiveBrightnessControl(originalImage, BRIGHTNESS_ADJUSTMENT);
      
    % Ploting
    fig=figure();        
    subplot(1,3,1.3), imshow(originalImage,[]), title('Original image')
    subplot(1,3,2.5), imshow(modifiedImage,[]), title('Modified image')
       
    grayscaleImage  = rgb2gray(originalImage);
    modifiedGrayscaleImage = AdditiveBrightnessControl(grayscaleImage, BRIGHTNESS_ADJUSTMENT);
    
    fig2=figure();        
    subplot(1,3,1.3), imshow(grayscaleImage,[]), title('Original Grayscale')
    subplot(1,3,2.5), imshow(modifiedGrayscaleImage,[]), title('Modified Grayscale')
    
    saveas(fig,strcat('output',filesep,mfilename,'_1.png'));
    saveas(fig2,strcat('output',filesep,mfilename,'_2.png'));
end

function output = AdditiveBrightnessControl(input, brightness)
    % MatLab shortcut
    % The pixel type uint8 cannot go higher than 255.
    output = uint8(brightness + input);
end