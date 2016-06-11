%% Entrenamiento
clc; clear all;
% Inicializacion de las 13 Fotos de lunares para el entrenamiento
RGB(:,:,:,1) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\Foto 1.png');
RGB(:,:,:,2) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\Foto 2.png');
RGB(:,:,:,3) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\Foto 3.png');
RGB(:,:,:,4) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\Foto 4.png');
RGB(:,:,:,5) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\Foto 5.png');
RGB(:,:,:,6) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\Foto 6.png');
RGB(:,:,:,7) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\Foto 7.png');
RGB(:,:,:,8) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\Foto 8.png');
RGB(:,:,:,9) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\Foto 9.png');
RGB(:,:,:,10) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\Foto 10.png');
RGB(:,:,:,11) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\Foto 11.png');
RGB(:,:,:,12) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\Foto 12.png');
RGB(:,:,:,13) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\Foto 13.png');

% Contadores de la cantidad de pixeles de Lunares y Pieles a usar
contL = [0 0 0];
contP = [0 0 0];
% Vector para guardar la suma de las amplitudes de los pixeles para el Material A y B
 a = uint64([0 ; 0 ; 0]);
 b = uint64([0 ; 0 ; 0]);
for s = 1:7 % Para ir recorriendo las 13 Imagenes
mascaraL = roipoly(RGB(:,:,:,s)); % Asignar una mascara para el Lunar
mascaraP = roipoly(RGB(:,:,:,s)); % Asignar una mascara para la Piel
%  mascaraL = roipoly(img); % Asignar una mascara para el Lunar
%  mascaraP = roipoly(img); % Asignar una mascara para la Piel

    for k = 1:3 % Recorre los colores de la Imagen Red, Green y Blue
        for i = 1:480 % Recorre el eje Vertical de la Matriz 
            for j = 1:640 % Recorre el eje horizontal de la Matriz 
            if(mascaraL(i,j)==1) % si el pixel es de tipo Lunar
                a(k,1) = a(k,1) + uint64(RGB(i,j,k,s)); % se suma la Amplitud
                contL(k) = contL(k) + 1; % se cuenta la cantidad de pixeles Lunares
            end
            if(mascaraP(i,j)==1) % si el pixel es de tipo Lunar
            b(k,1) = b(k,1) + uint64(RGB(i,j,k,s)); % se suma la Amplitud
            contP(k) = contP(k) +1; % se cuenta la cantidad de pixeles Piel
            end
            end
        end
    end
end
A = double([a(1)/contL(1) a(2)/contL(2) a(3)/contL(3)]); % Se obtiene el Promedio del Material A (Lunar) para RGB
B = double([b(1)/contP(1) b(2)/contP(2) b(3)/contP(3)]); % Se obtiene el Promedio del Material B (Piel) para RGB
% Se determina el RHO a utilizar
RHO = [A(1)/B(1) A(1)/B(2) A(1)/B(3) A(2)/B(1) A(2)/B(2) A(2)/B(3) A(3)/B(1) A(3)/B(2) A(3)/B(3)];

%% Detector de borde 
tic
borde = 255*ones(480,640); % se genera una matriz que sera la imagen resultante
imagen = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\Prueba2.png'); % se carga una imagen
R = double(imagen(:,:,1)); % se Guarda la Matriz Red de la imagen
G = double(imagen(:,:,2)); % se Guarda la Matriz Green de la imagen
B = double(imagen(:,:,3)); % se Guarda la Matriz Blue de la imagen

Ep = .3; % Parametro de tolerancia
% Tomar todas las matrices de 3x3 contenidas en la imagen
for i=2:479 % Recorrer el eje Vertical de la Matriz, de modo de tomar valores existentes en la matriz
   for j=2:639 % Recorrer el eje Horizontales de la Matriz, de modo de tomar valores existentes en la matriz
       % Rho de la muestra del supuesto borde de forma Horizontal del material A respecto al B
       rhoH1 = [R(i+1,j)/R(i-1,j) R(i+1,j)/G(i-1,j) R(i+1,j)/B(i-1,j) ...
           G(i+1,j)/R(i-1,j) G(i+1,j)/G(i-1,j) G(i+1,j)/B(i+1,j) B(i-1,j)/R(i+1,j)...
           B(i+1,j)/G(i-1,j) B(i+1,j)/B(i-1,j)];
       % Rho de la muestra del supuesto borde de forma Horizontal del material B respecto al A
       rhoH2 = [R(i-1,j)/R(i+1,j) R(i-1,j)/G(i+1,j) R(i-1,j)/B(i+1,j) ...
           G(i-1,j)/R(i+1,j) G(i-1,j)/G(i+1,j) G(i-1,j)/B(i+1,j) B(i-1,j)/R(i+1,j)...
           B(i-1,j)/G(i+1,j) B(i-1,j)/B(i+1,j)];
       % Rho de la muestra del supuesto borde de forma Vertical del material A respecto al B
       rhoV1 = [R(i,j+1)/R(i,j-1) R(i,j+1)/G(i,j-1) R(i,j+1)/B(i,j-1) ...
           G(i,j+1)/R(i,j-1) G(i,j+1)/G(i,j-1) G(i,j+1)/B(i,j-1) B(i,j+1)/R(i,j-1) ...
           B(i,j+1)/G(i,j-1) B(i,j+1)/B(i,j-1)];
       % Rho de la muestra del supuesto borde de forma Vertical del material B respecto al A
       rhoV2 = [R(i,j-1)/R(i,j+1) R(i,j-1)/G(i,j+1) R(i,j-1)/B(i,j+1) ...
            G(i,j-1)/R(i,j+1) G(i,j-1)/G(i,j+1) G(i,j-1)/B(i,j+1) B(i,j-1)/R(i,j+1) ...
            B(i,j-1)/G(i,j+1) B(i,j-1)/B(i,j+1)];
       % Rho de la muestra del supuesto borde de forma Diagonal del material A respecto al B
       rhoD11 = [R(i-1,j-1)/R(i+1,j+1) R(i-1,j-1)/G(i+1,j+1) R(i-1,j-1)/B(i+1,j+1) ...
           G(i-1,j-1)/R(i+1,j+1) G(i-1,j-1)/G(i+1,j+1) G(i-1,j-1)/B(i+1,j+1) B(i-1,j-1)/R(i+1,j+1) ...
           B(i-1,j-1)/G(i+1,j+1) B(i-1,j-1)/B(i+1,j+1)];
        % Rho de la muestra del supuesto borde de forma Diagonal del material B respecto al A
       rhoD12 = [ R(i+1,j+1)/R(i-1,j-1) R(i+1,j+1)/G(i-1,j-1) R(i+1,j+1)/B(i-1,j-1) ...
           G(i+1,j+1)/R(i-1,j-1) G(i+1,j+1)/G(i-1,j-1) G(i+1,j+1)/B(i-1,j-1) B(i+1,j+1)/R(i-1,j-1) ...
           B(i+1,j+1)/G(i-1,j-1) B(i+1,j+1)/B(i-1,j-1)];
        % Rho de la muestra del supuesto borde de forma Diagonal del material A respecto al B
       rhoD21 = [R(i-1,j+1)/R(i+1,j-1) R(i-1,j+1)/G(i+1,j-1) R(i-1,j+1)/B(i+1,j-1) ...
           G(i-1,j+1)/R(i+1,j-1) G(i-1,j+1)/G(i+1,j-1) G(i-1,j+1)/B(i+1,j-1) B(i-1,j+1)/R(i+1,j-1) ...
           B(i-1,j+1)/G(i+1,j-1) B(i-1,j+1)/B(i+1,j-1)];
        % Rho de la muestra del supuesto borde de forma Diagonal del material B respecto al A
       rhoD22 = [R(i+1,j-1)/R(i-1,j+1) R(i+1,j-1)/G(i-1,j+1) R(i+1,j-1)/B(i-1,j+1) ...
           G(i+1,j-1)/R(i-1,j+1) G(i+1,j-1)/G(i-1,j+1) G(i+1,j-1)/B(i-1,j+1) B(i+1,j-1)/R(i-1,j+1) ...
           B(i+1,j-1)/G(i-1,j+1) B(i+1,j-1)/B(i-1,j+1)];
            
       % Si se cumplen las condiciones de tolerancia, el pixel ubicado en (i,j) es un borde
            if(max(abs(rhoH1-RHO))<Ep) 
                borde(i,j) = 0;
            end
            if(max(abs(rhoH2-RHO))<Ep)
                borde(i,j) = 0;
            end            
            if(max(abs(rhoV1-RHO))<Ep)
                borde(i,j) = 0;
            end
            if(max(abs(rhoV2-RHO))<Ep)
                borde(i,j) = 0;
            end            
            if(max(abs(rhoD11-RHO))<Ep)
                borde(i,j) = 0;
            end
            if(max(abs(rhoD12-RHO))<Ep)
                borde(i,j) = 0;
            end
            if(max(abs(rhoD21-RHO))<Ep)
                borde(i,j) = 0;
            end
             if(max(abs(rhoD22-RHO))<Ep)
                borde(i,j) = 0;
            end
   end
end
% Muestra la imagen
toc
imshow(borde)