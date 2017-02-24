% 1.3. Negativo (intensidade na saída = 255 – intensidade na entrada)
function tarefa1_3()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    originalImage = imread(filePath);
    
    negativeImage = getNegative(originalImage);
        
    % Ploting
    figure();    
    subplot(1,2,1), imshow(originalImage,[]), title('Original image')
    subplot(1,2,2), imshow(negativeImage,[]), title('Negative')    
    
end

function output = getNegative(input)
    %input = im2double(input)
    %recCh = input(:,:,1);
    output = zeros(size(input));

    for idx = 1:numel(input)
        output(idx)=255-input(idx);
    end
    
end