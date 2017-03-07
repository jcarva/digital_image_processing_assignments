% 1.1 Conversão RGB-YIQ-RGB
% (cuidado com os limites de R, G e B!)
function task1_1()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    originalImage = imread(filePath);    
    yiqImage = rgb2ntsc(originalImage);
    back2RGB = ntsc2rgb(yiqImage);
    
    % Ploting
    fig=figure();    
    subplot(1,3,1), imshow(originalImage,[]), title('Original image')
    subplot(1,3,2), imshow(yiqImage,[]), title('YIQ image')
    subplot(1,3,3), imshow(back2RGB,[]), title('Back to RGB image')
    strcat('output',filesep,mfilename,'.png')
    
    saveas(fig,strcat('output',filesep,mfilename,'.png'));
end