% 2. Reproduza, utilizando o MATLAB e outra linguagem de programação de sua
% escolha, o exemplo apresentado na página 3 deste documento
% (ImageProcessing Toolbox User'sGuide - UsingMedianFiltering). Repita, no
% MATLAB, para ruído 'gaussian' e 'speckle', explicando o que são estes
% tipos de ruído.Discuta o experimento no relatório
function task2_0()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    I = imread(filePath);
    I = rgb2gray(I);
    
    % Apply Noise
    SP = imnoise(I,'salt & pepper',0.02);
    
    % Filter the noisy image with an averaging filter and display the results.
    SPAvrg = filter2(fspecial('average',3),SP)/255;
    
    % Now use a median filter to filter the noisy image and display the results. Notice
    % that medfilt2 does a better job of removing noise, with less blurring of edges.
    SPMed = medfilt2(SP,[3 3]);    
    
    % Gaussian Noise
    G = imnoise(I,'gaussian',0.02);
    GAvrg = filter2(fspecial('average',3),G)/255;
    GMed = medfilt2(G,[3 3]);   
    
    % Speckle Noise
    S = imnoise(I,'speckle',0.02);
    SAvrg = filter2(fspecial('average',3),S)/255;
    SMed = medfilt2(S,[3 3]);   
    
    % Ploting
    fig = figure(1); set (fig, 'Units', 'normalized', 'Position', [0,0,1,1]);    
    %subplot(4,3,1), imshow(I,[]), title('Original image')
    subplot(1,3,1), imshow(SP,[]), title('Salt&Pepper Noise')
    subplot(1,3,2), imshow(SPAvrg,[]), title('Average Filter')
    subplot(1,3,3), imshow(SPMed,[]), title('Median Filter')
    
    fig = figure(2); set (fig, 'Units', 'normalized', 'Position', [0,0,1,1]);   
    subplot(1,3,1), imshow(G,[]), title('Gaussian Noise')
    subplot(1,3,2), imshow(GAvrg,[]), title('Average Filter')
    subplot(1,3,3), imshow(GMed,[]), title('Median Filter')
    
    fig = figure(3); set (fig, 'Units', 'normalized', 'Position', [0,0,1,1]);   
    subplot(1,3,1), imshow(S,[]), title('Speckle Noise')
    subplot(1,3,2), imshow(SAvrg,[]), title('Average Filter')
    subplot(1,3,3), imshow(SMed,[]), title('Median Filter')
    
end