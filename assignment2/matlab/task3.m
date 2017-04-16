% 3. Para uma imagem com dimensões 1024x1024, calcule o tempo de processamento para:
%   a. Aplicação do Filtro da Mediana 15x15 utilizando uma função de sort para
% ordenar a janela de pixels e encontrar a mediana.
%   b. Aplicação do Filtro da Mediana 15x15 utilizando uma função de mediana O(n)
% para encontrar a mediana. Sugestão: QuickSelect ou Median of Medians.

% https://www.mathworks.com/matlabcentral/fileexchange/29453-nth-element

function task3()
    assetsDir = ['..' filesep 'assets' filesep];
    filePath = strcat(assetsDir, 'lena_headey_1024.jpg');
    originalImage = imread(filePath);
    
    [~, ~, channels] = size(originalImage);

    if channels == 3
        grayIm = rgb2gray(originalImage);
    else 
        grayIm = originalImage;
    end
    
    sortedMedian3 = timer('[Sorted Median 3]', @nlfilter, grayIm, [3 3], @sortedMedian);
    sortedMedian9 = timer('[Sorted Median 9]', @nlfilter, grayIm, [9 9], @sortedMedian);
    sortedMedian15 = timer('[Sorted Median 15]', @nlfilter, grayIm, [15 15], @sortedMedian);
    
    quickMedian3 = timer('[Quick Median 3]', @nlfilter, grayIm, [3 3], @quickMedian);
    quickMedian9 = timer('[Quick Median 9]', @nlfilter, grayIm, [9 9], @quickMedian);
    quickMedian15 = timer('[Quick Median 15]', @nlfilter, grayIm, [15 15], @quickMedian);
    
    fig = figure(1);
    set (fig, 'Units', 'normalized', 'Position', [0,0,1,1]);

    subplot(2,2,1), imshow(grayIm), title('Original image')
    subplot(2,2,2), imshow(quickMedian3), title('Quick Median 3x3')
    subplot(2,2,3), imshow(quickMedian9), title('Quick Median 9x9')
    subplot(2,2,4), imshow(quickMedian15), title('Quick Median 15x15')
end    
 
function output = quickMedian(x)
    output = fast_median(x(:));
end

function output = sortedMedian(x)
    sorted = sort(x(:));
    [len, ~] = size(sorted);
    position = floor(len / 2);
    
    if (mod(len, 2) == 1)
        output = sorted(position);
    else
        output = (sorted(position-1) + sorted(position))/2;
    end
end

function output = timer(name, f, image, size, fun)
    tic;
    output = f(image, size, fun);
    t = toc;
    fprintf('%s: %f seconds.\n', name, t);
end