% 1.1 Conversão RGB-YIQ-RGB (cuidado com os limites de R, G e B!)
function tarefa1_1()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    originalImage = imread(filePath);
    
    yiqImage = rgb2yiq(originalImage);
    back2RGB = yiq2rgb(yiqImage);
    
    
    fig = figure(1);
    set (fig, 'Units', 'normalized', 'Position', [0,0,1,1]);
    
    subplot(1,3,1), imshow(originalImage,[]), title('Original image')
    subplot(1,3,2), imshow(yiqImage,[]), title('YIQ image')
    subplot(1,3,3), imshow(back2RGB,[]), title('Back2RGB image')
    
end

% 1.1. Conversão RGB-YIQ-RGB
function output = rgb2yiq(input)   

  % Y = 0.299R + 0.587G + 0.114B 
  % I = 0.596R - 0.274G - 0.322B 
  % Q = 0.211R - 0.523G + 0.312B
  
    output = uint8(zeros(size(input)));
    for i=1:size(input,1)
        for j=1:size(input,2)
            output(i,j,1)= 0.299*input(i,j,1) + 0.587*input(i,j,2) + 0.114*input(i,j,3);
            output(i,j,2)= 0.596*input(i,j,1) - 0.274*input(i,j,2) - 0.322*input(i,j,3);
            output(i,j,3)= 0.211*input(i,j,1) - 0.523*input(i,j,2) + 0.312*input(i,j,3);
        end
    end
end

function output = yiq2rgb(input)   
    
  % R = Y + 0.956I + 0.621Q 
  % G = Y - 0.272I - 0.647Q 
  % B = Y - 1.106I - 1.703Q

    output=uint8(zeros(size(input)));
    for i=1:size(input,1)
        for j=1:size(input,2)
              output(i,j,1)=input(i,j,1)+0.956*input(i,j,2)+0.621*input(i,j,3);
              output(i,j,2)=input(i,j,1)-0.272*input(i,j,2)-0.647*input(i,j,3);
              output(i,j,3)=input(i,j,1)-1.106*input(i,j,2)+1.703*input(i,j,3);
        end
    end    
end 