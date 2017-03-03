% 1.6. Limiarização aplicada sobre Y, com limiar m e duas opções: a) m
% escolhido pelo usuário; b) m = média de valores da banda Y;
function task1_6()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    originalImage = imread(filePath);
    
    FIXED_M = 0.2;
    yiqImage = rgb2ntsc(originalImage);
         
    % Segmented Y channel with fixed M
    [segmentedY1, rgb1, m1] = binarySegmention(yiqImage, FIXED_M);
        
    % Segmented Y channel with M = mean(Y)
    [segmentedY2, rgb2, m2] = binarySegmention(yiqImage);

    % Ploting
    figure();        
    subplot(3,2,1), imshow(originalImage), title('Original image')
    subplot(3,2,3), imshow(segmentedY1), title(strcat('Y Channel Fixed M= ',num2str(m1)))
    subplot(3,2,4), imshow(rgb1), title('Back to RGB')   
    subplot(3,2,5), imshow(segmentedY2), title(strcat('Y Channel M = mean(Y) = ',num2str(m2)))
    subplot(3,2,6), imshow(rgb2), title('Back to RGB Mean')
end

function [segmentedY, rgb, m] = binarySegmention(input, m)
    yCh = input(:,:,1);
    if ~exist('m','var')    
      m = mean(yCh(:));      
    end  
    
    segmentedY = (yCh>m);
    
    input(:,:,1) = segmentedY;
    rgb = ntsc2rgb(input);
end
