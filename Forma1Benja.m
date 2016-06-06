im(:,:,:,1)=imread('foto1.png');
im(:,:,:,2)=imread('foto2.png');
im(:,:,:,3)=imread('foto3.png');
im(:,:,:,4)=imread('foto4.png');
im(:,:,:,5)=imread('foto5.png');
im(:,:,:,6)=imread('foto6.png');
im(:,:,:,7)=imread('foto7.png');
im(:,:,:,8)=imread('foto8.png');
im(:,:,:,9)=imread('foto9.png');
 
for s=1:9 
R = im(:,:,1);
G = im(:,:,2);
B=  im(:,:,3);

ir1=zeros(480,640);ir2=zeros(480,640);ir3=zeros(480,640);
ib1=zeros(480,640);ib2=zeros(480,640);ib3=zeros(480,640);
ig1=zeros(480,640);ig2=zeros(480,640);ig3=zeros(480,640);
    for i = 1:480
    for k=1:480
      for j= 1:640
         ir1(i,j)=R(i,k).\R(i,j);
         ir2(i,j)=R(i,k).\G(i,j);
         ir3(i,j)=R(i,k).\B(i,j);
         ib1(i,j)=B(i,k).\R(i,j);
         ib2(i,j)=B(i,k).\G(i,j);
         ib3(i,j)=B(i,k).\B(i,j);
         ig1(i,j)=G(i,k).\R(i,j);
         ig2(i,j)=G(i,k).\G(i,j);
         ig3(i,j)=G(i,j).\B(i,j);
        end
    end
    end
   
% mascara y imagenes
lunar1=zeros(480,640);lunar2=zeros(480,640);lunar3=zeros(480,640);lunar4=zeros(480,640);lunar5=zeros(480,640);lunar6=zeros(480,640);lunar7=zeros(480,640);lunar8=zeros(480,640);lunar9=zeros(480,640);
piel1=zeros(480,640);piel2=zeros(480,640);piel3=zeros(480,640);piel4=zeros(480,640);piel5=zeros(480,640);piel6=zeros(480,640);piel7=zeros(480,640);piel8=zeros(480,640);piel9=zeros(480,640); 

for k = 1:3
   
    contL1=0;contL2=0;contL3=0;contL4=0;contL5=0;contL6=0;contL7=0;contL8=0;contL9=0;
    contP1=0;contP2=0;contP3=0;contP4=0;contP5=0;contP6=0;contP7=0;contP8=0;contP9=0;
  for i = 1:480
    for j =1:640 
         if(ir1(i,j)==1)
         piel1(i,j,k)=0; lunar1(i,j,k) = im(i,j,k);contL1=contL1 +1;
         else
         lunar1(i,j,k) = 0;piel1(i,j,k)=im(i,j,k); contP1=contP1 +1;
         end
         if(ir2(i,j)==1)
         piel2(i,j,k)=0;lunar2(i,j,k) = im(i,j,k);contL2=contL2 +1;
         else
         lunar2(i,j,k) = 0;piel2(i,j,k) = im(i,j,k); contP2=contP2 +1;
         end    
         if(ir3(i,j)==1)
         piel3(i,j,k)=0; lunar3(i,j,k) = im(i,j,k);contL3=contL3 +1;
         else
         lunar3(i,j,k) = 0; piel3(i,j,k) = im(i,j,k);contP3=contP3 +1;
         end    
         if(ib1(i,j)==1)
         piel4(i,j,k)=0;lunar4(i,j,k) = im(i,j,k);contL4=contL4 +1;  
         else
         lunar4(i,j,k) = 0;  piel4(i,j,k) = im(i,j,k); contP4=contP4 +1;     
         end  
         if(ib2(i,j)==1)
         piel5(i,j,k)=0; lunar5(i,j,k) = im(i,j,k);contL5=contL5 +1;
         else
         lunar5(i,j,k) = 0;piel5(i,j,k) = im(i,j,k); contP5=contP5 +1;     
         end    
         if(ib3(i,j)==1)
         piel6(i,j,k)=0;lunar6(i,j,k) = im(i,j,k);contL6=contL6 +1;
         else
         lunar6(i,j,k) = 0; piel6(i,j,k) = im(i,j,k); contP6=contP6 +1;     
         end     
         if(ig1(i,j)==1)
         piel7(i,j,k)=0;lunar7(i,j,k) = im(i,j,k);contL7=contL7 +1;
         else
         lunar7(i,j,k) = 0; piel7(i,j,k) = im(i,j,k); contP7=contP7 +1; 
         end
         if(ig2(i,j)==1)
         piel8(i,j,k)=0;lunar8(i,j,k) = im(i,j,k);contL8=contL8 +1;
         else
             lunar8(i,j,k) = 0; piel8(i,j,k) = im(i,j,k); contP8=contP8 +1;
         end     
         if(ig3(i,j)==1)
         piel9(i,j,k)=0;lunar9(i,j,k) = im(i,j,k);contL9=contL9 +1;
         else
         lunar9(i,j,k) = 0; piel9(i,j,k) = im(i,j,k); contP9=contP9 +1;
         end
        end
    end
 end

 
lunarR1 = lunar1(:,:,1);lunarR2 = lunar2(:,:,1);lunarR3=lunar3(:,:,1);lunarR4 = lunar4(:,:,1);lunarR5 = lunar5(:,:,1);lunarR6=lunar6(:,:,1);lunarR7 = lunar7(:,:,1);lunarR8 = lunar8(:,:,1);lunarR9 = lunar9(:,:,1);          
lunarG1 = lunar1(:,:,2);lunarG2 = lunar2(:,:,2);lunarG3=lunar3(:,:,2);lunarG4 = lunar4(:,:,2);lunarG5 = lunar5(:,:,2);lunarG6=lunar6(:,:,2);lunarG7 = lunar7(:,:,2);lunarG8 = lunar8(:,:,2);lunarG9 = lunar9(:,:,2);      
lunarB1 = lunar1(:,:,3);lunarB2 = lunar2(:,:,3);lunarB3=lunar3(:,:,3);lunarB4 = lunar4(:,:,3);lunarB5 = lunar5(:,:,3);lunarB6=lunar6(:,:,3);lunarB7 = lunar7(:,:,3);lunarB8 = lunar8(:,:,3);lunarB9 = lunar9(:,:,3);      

pielR1 = piel1(:,:,1);pielR2 = piel2(:,:,1);pielR3=piel3(:,:,1);pielR4 = piel4(:,:,1);pielR5 = piel5(:,:,1);pielR6=piel6(:,:,1);pielR7 = piel7(:,:,1);pielR8 = piel8(:,:,1);pielR9 = piel9(:,:,1);          
pielG1 = piel1(:,:,2);pielG2 = piel2(:,:,2);pielG3=piel3(:,:,2);pielG4 = piel4(:,:,2);pielG5 = piel5(:,:,2);pielG6=piel6(:,:,2);pielG7 = piel7(:,:,2);pielG8 = piel8(:,:,2);pielG9 = piel9(:,:,2);      
pielB1 = piel1(:,:,3);pielB2 = piel2(:,:,3);pielB3=piel3(:,:,3);pielB4 = piel4(:,:,3);pielB5 = piel5(:,:,3);pielB6=piel6(:,:,3);pielB7 = piel7(:,:,3);pielB8 = piel8(:,:,3);pielB9 = piel9(:,:,3);  

Ar1 = sum(sum(lunar1(:,:,1)))/contL1;Ar2 = sum(sum(lunar2(:,:,1)))/contL2;Ar3 = sum(sum(lunar3(:,:,1)))/contL3;Ar4 = sum(sum(lunar4(:,:,1)))/contL4;Ar5 = sum(sum(lunar5(:,:,1)))/contL5;Ar6 = sum(sum(lunar6(:,:,1)))/contL6;Ar7 = sum(sum(lunar7(:,:,1)))/contL7;Ar8 = sum(sum(lunar8(:,:,1)))/contL8;Ar9 = sum(sum(lunar9(:,:,1)))/contL9;
Ag1 = sum(sum(lunar1(:,:,2)))/contL1;Ag2 = sum(sum(lunar2(:,:,2)))/contL2;Ag3 = sum(sum(lunar3(:,:,2)))/contL3;Ag4 = sum(sum(lunar4(:,:,2)))/contL4;Ag5 = sum(sum(lunar5(:,:,2)))/contL5;Ag6 = sum(sum(lunar6(:,:,2)))/contL6;Ag7 = sum(sum(lunar7(:,:,2)))/contL7;Ag8 = sum(sum(lunar8(:,:,2)))/contL8;Ag9 = sum(sum(lunar9(:,:,2)))/contL9;
Ab1 = sum(sum(lunar1(:,:,3)))/contL1;Ab2 = sum(sum(lunar2(:,:,3)))/contL2;Ab3 = sum(sum(lunar3(:,:,3)))/contL3;Ab4 = sum(sum(lunar4(:,:,3)))/contL4;Ab5 = sum(sum(lunar5(:,:,3)))/contL5;Ab6 = sum(sum(lunar6(:,:,3)))/contL6;Ab7 = sum(sum(lunar7(:,:,3)))/contL7;Ab8 = sum(sum(lunar8(:,:,3)))/contL8;Ab9 = sum(sum(lunar9(:,:,3)))/contL9;

Br1 = sum(sum(piel1(:,:,1)))/contP1;Br2= sum(sum(piel2(:,:,1)))/contP2;Br3 = sum(sum(piel3(:,:,1)))/contP3;Br4 = sum(sum(piel4(:,:,1)))/contP4;Br5 = sum(sum(piel5(:,:,1)))/contP5;Br6 = sum(sum(piel6(:,:,1)))/contP6;Br7 = sum(sum(piel7(:,:,1)))/contP7;Br8 = sum(sum(piel8(:,:,1)))/contP8;Br9 = sum(sum(piel9(:,:,1)))/contP9;
Bg1 = sum(sum(piel1(:,:,2)))/contP1;Bg2 = sum(sum(piel2(:,:,2)))/contP2;Bg3 = sum(sum(piel3(:,:,2)))/contP3;Bg4 = sum(sum(piel4(:,:,2)))/contP4;Bg5 = sum(sum(piel5(:,:,2)))/contP5;Bg6 = sum(sum(piel6(:,:,2)))/contP6;Bg7 = sum(sum(piel7(:,:,2)))/contP7;Bg8 = sum(sum(piel8(:,:,2)))/contP8;Bg9 = sum(sum(piel9(:,:,2)))/contP9;
Bb1 = sum(sum(piel1(:,:,3)))/contP1;Bb2 = sum(sum(piel2(:,:,3)))/contP2;Bb3 = sum(sum(piel3(:,:,3)))/contP3;Bb4 = sum(sum(piel4(:,:,3)))/contP4;Bb5 = sum(sum(piel5(:,:,3)))/contP5;Bb6 = sum(sum(piel6(:,:,3)))/contP6;Bb7 = sum(sum(piel7(:,:,3)))/contP7;Bb8 = sum(sum(piel8(:,:,3)))/contP8;Bb9 = sum(sum(piel9(:,:,3)))/contP9;

rho=zeros(9,9);
 
rho(1,1)=Ar1/Br1;rho(1,4)=Ag1/Br1;rho(1,7)=Ab1/Br1;
rho(1,2)=Ar1/Bg1;rho(1,5)=Ag1/Bg1;rho(1,8)=Ab1/Bg1;
rho(1,3)=Ar1/Bb1;rho(1,6)=Ag1/Bb1;rho(1,9)=Ab1/Bb1;

rho(2,1)=Ar2/Br2;rho(2,4)=Ag2/Br2;rho(2,7)=Ab2/Br2;
rho(2,2)=Ar2/Bg2;rho(2,5)=Ag2/Bg2;rho(2,8)=Ab2/Bg2;
rho(2,3)=Ar2/Bb2;rho(2,6)=Ag2/Bb2;rho(2,9)=Ab2/Bb2;

rho(3,1)=Ar3/Br3;rho(3,4)=Ag3/Br3;rho(3,7)=Ab3/Br3;
rho(3,2)=Ar3/Bg3;rho(3,5)=Ag3/Bg3;rho(3,8)=Ab3/Bg3;
rho(3,3)=Ar3/Bb3;rho(3,6)=Ag3/Bb3;rho(3,9)=Ab3/Bb3;

rho(4,1)=Ar4/Br4;rho(4,4)=Ag4/Br4;rho(4,7)=Ab4/Br4;
rho(4,2)=Ar4/Bg4;rho(4,5)=Ag4/Bg4;rho(4,8)=Ab4/Bg4;
rho(4,3)=Ar4/Bb4;rho(4,6)=Ag4/Bb4;rho(4,9)=Ab4/Bb4;

rho(5,1)=Ar5/Br5;rho(5,4)=Ag5/Br5;rho(5,7)=Ab5/Br5;
rho(5,2)=Ar5/Bg5;rho(5,5)=Ag5/Bg5;rho(5,8)=Ab5/Bg5;
rho(5,3)=Ar5/Bb5;rho(5,6)=Ag5/Bb5;rho(5,9)=Ab5/Bb5;

rho(6,1)=Ar6/Br6;rho(6,4)=Ag6/Br6;rho(6,7)=Ab6/Br6;
rho(6,2)=Ar6/Bg6;rho(6,5)=Ag6/Bg6;rho(6,8)=Ab6/Bg6;
rho(6,3)=Ar6/Bb6;rho(6,6)=Ag6/Bb6;rho(6,9)=Ab6/Bb6;

rho(7,1)=Ar7/Br7;rho(7,4)=Ag7/Br7;rho(7,7)=Ab7/Br7;
rho(7,2)=Ar7/Bg7;rho(7,5)=Ag7/Bg7;rho(7,8)=Ab7/Bg7;
rho(7,3)=Ar7/Bb7;rho(7,6)=Ag7/Bb7;rho(7,9)=Ab7/Bb7;

rho(8,1)=Ar8/Br8;rho(8,4)=Ag8/Br8;rho(8,7)=Ab8/Br8;
rho(8,2)=Ar8/Bg8;rho(8,5)=Ag8/Bg8;rho(8,8)=Ab8/Bg8;
rho(8,3)=Ar8/Bb8;rho(8,6)=Ag8/Bb8;rho(8,9)=Ab8/Bb8;

rho(9,1)=Ar9/Br9;rho(9,4)=Ag9/Br9;rho(9,7)=Ab9/Br9;
rho(9,2)=Ar9/Bg9;rho(9,5)=Ag9/Bg9;rho(9,8)=Ab9/Bg9;
rho(9,3)=Ar9/Bb9;rho(9,6)=Ag9/Bb9;rho(9,9)=Ab9/Bb9;

A=sum(rho)/9;
RHO(s,:)=A;
end



%%
rhos
RHO = sum(rhos)/s




%%
%%
%%
%%
%%
%%
