%% Entrenamiento

clc; clear all;
RGB(:,:,:,1) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\foto1.png');
RGB(:,:,:,2) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\foto2.png');
RGB(:,:,:,3) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\foto3.png');
RGB(:,:,:,4) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\foto4.png');
RGB(:,:,:,5) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\foto5.png');
RGB(:,:,:,6) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\foto6.png');
RGB(:,:,:,7) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\foto7.png');
RGB(:,:,:,8) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\foto8.png');
RGB(:,:,:,9) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\foto9.png');
RGB(:,:,:,10) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\foto10.png');
RGB(:,:,:,11) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\foto11.png');
RGB(:,:,:,12) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\foto12.png');
RGB(:,:,:,13) = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\foto13.png');
%load('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\mascara.mat','-mat','mascara');
% figure(); imshow(RGB)
for s = 1:13
mascara = roipoly(RGB(:,:,:,s));
lunar = zeros(480,640);
piel = zeros(480,640);
for k = 1:3
    contL = 0;
    contP = 0;
 for i = 1:480
    for j = 1:640 
        if(mascara(i,j)==1)
        lunar(i,j,k) = RGB(i,j,k,s);
        piel(i,j,k) = 0;
        contL = contL + 1;
        else
        lunar(i,j,k) = 0;
        piel(i,j,k) = RGB(i,j,k,s);
        contP = contP +1;
        end
    end
 end
end

lunarR = lunar(:,:,1);
lunarG = lunar(:,:,2);
lunarB = lunar(:,:,3);

pielR = piel(:,:,1);
pielG = piel(:,:,2);
pielB = piel(:,:,3);

Ar = sum(sum(lunar(:,:,1)))/contL;
Ag = sum(sum(lunar(:,:,2)))/contL;
Ab = sum(sum(lunar(:,:,3)))/contL;

Br = sum(sum(piel(:,:,1)))/contP; 
Bg = sum(sum(piel(:,:,2)))/contP;
Bb = sum(sum(piel(:,:,3)))/contP;

rho(s,:) = [Ar/Br Ar/Bg Ar/Bb Ag/Br Ag/Bg Ag/Bb Ab/Br Ab/Bg Ab/Bb];
end


RHO = sum(rho)/s;

%% Detector de borde 

borde = 255*ones(480,640);
imagen = imread('C:\Users\Nano\Weas UdeC\Procesamiento digital de imagenes\Lab 3\foto4.png');
R = double(imagen(:,:,1));
G = double(imagen(:,:,2));
B = double(imagen(:,:,3));

Ep = 0.5;
for i=2:479
   for j=2:639
       rhoH = [R(i+1,j)/R(i-1,j) R(i+1,j)/G(i-1,j) R(i+1,j)/B(i-1,j) ...
           G(i+1,j)/R(i-1,j) G(i+1,j)/G(i-1,j) G(i+1,j)/B(i+1,j) B(i-1,j)/R(i+1,j)...
           B(i+1,j)/G(i-1,j) B(i+1,j)/B(i-1,j)];
       
       rhoV = [R(i,j+1)/R(i,j-1) R(i,j+1)/G(i,j-1) R(i,j+1)/B(i,j-1) ...
           G(i,j+1)/R(i,j-1) G(i,j+1)/G(i,j-1) G(i,j+1)/B(i,j-1) B(i,j+1)/R(i,j-1) ...
           B(i,j+1)/G(i,j-1) B(i,j+1)/B(i,j-1)];
       
       rhoD1 = [R(i-1,j-1)/R(i+1,j+1) R(i-1,j-1)/G(i+1,j+1) R(i-1,j-1)/B(i+1,j+1) ...
           G(i-1,j-1)/R(i+1,j+1) G(i-1,j-1)/G(i+1,j+1) G(i-1,j-1)/B(i+1,j+1) B(i-1,j-1)/R(i+1,j+1) ...
           B(i-1,j-1)/G(i+1,j+1) B(i-1,j-1)/B(i+1,j+1)];
       
       rhoD2 = [R(i-1,j+1)/R(i+1,j-1) R(i-1,j+1)/G(i+1,j-1) R(i-1,j+1)/B(i+1,j-1) ...
           G(i-1,j+1)/R(i+1,j-1) G(i-1,j+1)/G(i+1,j-1) G(i-1,j+1)/B(i+1,j-1) B(i-1,j+1)/R(i+1,j-1) ...
           B(i-1,j+1)/G(i+1,j-1) B(i-1,j+1)/B(i+1,j-1)];
            
            if(max(abs(rhoH-RHO))<Ep)
                borde(i,j) = 0;
            end
            
            if(max(abs(rhoV-RHO))<Ep)
                borde(i,j) = 0;
            end
            
            if(max(abs(rhoD1-RHO))<Ep)
                borde(i,j) = 0;
            end
            if(max(abs(rhoD2-RHO))<Ep)
                borde(i,j) = 0;
            end
   end
end

imshow(borde)


       
       