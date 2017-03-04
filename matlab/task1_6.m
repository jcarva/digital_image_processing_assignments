% 1.6. Limiarização aplicada sobre Y, com limiar m e duas opções: a) m
% escolhido pelo usuário; b) m = média de valores da banda Y;
function task1_6()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    grayScaleImage = rgb2gray(imread(filePath));
    
    FIXED_M = 100;    
         
    % Segmented Y channel with fixed M
    fixedMOutput = binarySegmention(grayScaleImage, FIXED_M);
        
    % Segmented Y channel with M = mean(Y)
    meanM = mean(grayScaleImage(:));
    meanMOutput = binarySegmention(grayScaleImage, meanM);

    % Ploting
    figure();        
    subplot(3,1,1), imshow(grayScaleImage), title('Original image')    
    subplot(3,1,2), imshow(fixedMOutput), title(strcat('Segmented Y with Fixed M = ',num2str(FIXED_M)))        
    subplot(3,1,3), imshow(meanMOutput), title(strcat('Segmented Y with M = mean(Y) = ',num2str(meanM)))
    
end

function output = binarySegmention(input, m)
    output = (input>m);            
end
