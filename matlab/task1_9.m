% 1.9. Aplicar filtros descritos na atividade
function task1_9()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    originalImage = imread(filePath);
    filter1Image = filter1(originalImage);
    filter2Image = filter2(originalImage);
    
    % Ploting
    figure();        
    subplot(1,3,1), imshow(originalImage,[]), title('Original image')
    subplot(1,3,2), imshow(filter1Image,[]), title('Filter1 image')
    subplot(1,3,3), imshow(filter2Image,[]), title('Filter2 image')
    
end

function output = filter1(input)
    % MatLab shortcut
    h = [ 0 -1 0 ; -1 5 -1 ; 0 -1 0 ];
    output = imfilter(input, h);
end

function output = filter2(input)
    % MatLab shortcut
    h = [ 0 0 0 ; 0 1 0 ; 0 0 -1 ];
    output = imfilter(input, h);
end