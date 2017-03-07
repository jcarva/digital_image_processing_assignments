% 1.6. Limiarização aplicada sobre Y, com limiar m e duas opções: a) m
% escolhido pelo usuário; b) m = média de valores da banda Y;
function task1_6()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    originalImage = imread(filePath);
    
    FIXED_M = 0.2;
    yiqImage = rgb2ntsc(originalImage);
    grayScaleImage = yiqImage(:,:,1);
         
    % Segmented Y channel with fixed M
    fixedMOutput = binarySegmention(grayScaleImage, FIXED_M);
    fixedMImage = yiqImage;
    fixedMImage(:,:,1) = fixedMOutput;
    fixedMBack2RGB = ntsc2rgb(fixedMImage);
        
    % Segmented Y channel with M = mean(Y)
    meanM = mean(grayScaleImage(:));
    meanMOutput = binarySegmention(grayScaleImage, meanM);
    meanMImage = yiqImage;
    meanMImage(:,:,1) = fixedMOutput;
    meanMBack2RGB = ntsc2rgb(meanMImage);

    % Ploting
    fig=figure();        
    subplot(1,3,1), imshow(originalImage), title('Original image')    
    subplot(1,3,2), imshow(fixedMOutput), title(strcat('Segmented Y with Fixed M = ',num2str(FIXED_M)))        
    subplot(1,3,3), imshow(fixedMBack2RGB), title('Back to RGB')
       
    fig2=figure();        
    subplot(1,3,1), imshow(originalImage), title('Original image')        
    subplot(1,3,2), imshow(meanMOutput), title(strcat('Segmented Y with M = mean(Y) = ',num2str(meanM)))
    subplot(1,3,3), imshow(meanMBack2RGB), title('Back to RGB')
    
    saveas(fig,strcat('output',filesep,mfilename,'_1.png'));
    saveas(fig2,strcat('output',filesep,mfilename,'_2.png'));
end

function output = binarySegmention(input, m)
    output = (input>m);            
end
