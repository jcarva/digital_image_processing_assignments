% 1.2 Exibição de bandas individuais (R, G e B) como imagens
% monocromáticas ou coloridas (em tons de R, G ou B, respectivamente)
function task1_2()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    originalImage = imread(filePath);
    
    [redCh, greenCh, blueCh] = separateChannels(originalImage);
    
    zeroes = zeros(size(originalImage, 1), size(originalImage, 2));
    [redColor, greenColor, blueColor] = getColoredImage(redCh, greenCh, blueCh, zeroes);
    
    concatImage = cat(3, redCh, greenCh, blueCh);

    % Ploting
    fig = figure(1);
    set (fig, 'Units', 'normalized', 'Position', [0,0,1,1]);
    
    subplot(2,4,1), imshow(originalImage), title('Original image')

    subplot(2,4,2), imshow(redCh), title('Red channel mono')
    subplot(2,4,3), imshow(greenCh), title('Green channel mono')
    subplot(2,4,4), imshow(blueCh), title('Blue channel mono')

    subplot(2,4,5), imshow(redColor), title('Red channel')
    subplot(2,4,6), imshow(greenColor), title('Green channel')
    subplot(2,4,7), imshow(blueColor), title('Blue channel')

    subplot(2,4,8), imshow(concatImage), title('Back to original image')
    
end

function [redCh, greenCh, blueCh] = separateChannels(input)
    redCh = input(:,:,1); 
    greenCh = input(:,:,2);
    blueCh = input(:,:,3);
end

function [justRed, justGreen, justBlue] = getColoredImage(redCh, greenCh, blueCh, zeroes)    
    justRed = cat(3, redCh, zeroes, zeroes);
    justGreen = cat(3, zeroes, greenCh, zeroes);
    justBlue = cat(3, zeroes, zeroes, blueCh);
end