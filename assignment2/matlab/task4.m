% Produza uma pilha com 15 imagens da mesma paisagem com ruídos diferentes. Pode-se
% gerar um ruído aleatório para uma única imagem, utilizar uma câmera que tire várias
% fotos seguidas ou converter os frames de um vídeo de câmera estática em imagens.
% Aplique:
%   a. Filtragem por Média de Imagens;
%   b. Filtragem por Mediana de Imagens.
function task4() 
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    originalImage = imread(filePath);
        
    yiqImage = rgb2ntsc(originalImage);
    % Get grayscale image
    grayIm = yiqImage(:,:,1);
    
    numIm = 15;
    noiseImages = createNoiseImages(grayIm, numIm, 0.2);        
            
    meanImage = mean(noiseImages,3);
    meanDiff = imDiff(meanImage, grayIm);
    
    medianImage = median(noiseImages,3);
    medianDiff = imDiff(medianImage, grayIm);
        
    % Ploting
    fig = figure(1);    
    set (fig, 'Units', 'normalized', 'Position', [0,0,1,1]);
    
    subplot(2,2,1), imshow(grayIm), title('Original image')
    subplot(2,2,2), imshow(noiseImages(:,:,1)), title('Image Noise Sample')  
    subplot(2,2,3), imshow(meanImage), title(strcat('Mean Filter. Err: ',num2str(meanDiff*100,'%5.1f%%')))
    subplot(2,2,4), imshow(medianImage), title(strcat('Median Filter. Err: ',num2str(medianDiff*100,'%5.1f%%')))
          
end

function output = createNoiseImages(img, n, p)
    output = [];    
    for i = 1:n
        im = imnoise(img,'salt & pepper',p);        
        output = cat(3,output, im);        
    end
    
end

% Calculates difference between two images in percentage
function output = imDiff(I, J)    
    imDiff = I-J; 
    imSum = I+J;  
    output = 200 * mean(imDiff(:)) / mean(imSum(:));
end