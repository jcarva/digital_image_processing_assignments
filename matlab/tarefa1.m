function tarefa1()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lenna.png');
    
    originalImage = imread(filePath);
    
    yiqImage = rgb2yiq(originalImage);
    back2RGB = yiq2rgb(yiqImage);
    
    figure()
    subplot(1,3,1), imshow(originalImage,[]), title('Original image')
    subplot(1,3,2), imshow(yiqImage,[]), title('YIQ image')
    subplot(1,3,3), imshow(back2RGB,[]), title('Back2RGB image')
    
end

% 1.1. Convers�o RGB-YIQ-RGB
function output = rgb2yiq(input)   

  % 0.299   0.587   0.114 
  % 0.596  -0.274  -0.322 
  % 0.211  -0.523   0.312
  
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
    
  % 1   0.956   0.621 
  % 1  -0.272  -0.647 
  % 1  -1.106   1.703

    output=uint8(zeros(size(input)));
    for i=1:size(input,1)
        for j=1:size(input,2)
              output(i,j,1)=input(i,j,1)+0.956*input(i,j,2)+0.621*input(i,j,3);
              output(i,j,2)=input(i,j,1)-0.272*input(i,j,2)-0.647*input(i,j,3);
              output(i,j,3)=input(i,j,1)-1.106*input(i,j,2)+1.703*input(i,j,3);
        end
    end    
end 