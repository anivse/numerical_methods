%A=rand(10);
format long;
A=hilb(10);
x_ex=ones(10,1);
B=A*x_ex;
x=A\B;
error_rel=norm(x-x_ex)/norm(x_ex);
delB=0.01*rand(10,1);
x2=A\(B+delB);
err=norm(x-x2)/norm(x);
er=norm(delB)/norm(B);
c=cond(A);
%Матрица с нужным числом обусловленности

D=diag([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
[Q,R]=qr(rand(10));
A=Q*D*Q';
%Задание часть1
%Размерность матрицы фиксирована
%Выбрать числа cond 
%Найти точное решение
%Решить своим методом
%Относительная погрешность (числ-точное)/(точное)
%Построить график погрешность от числа обусловленности

%Задание часть 2
%Число обусловленности фиксировано, матрциа А фиксирована
%Меняется В 
%Задать изменение 
%Численное решение
%Влияние озмещения В на решение
%Влияние относительной погрешности возмущения на погрешность решения 

%тестовый пример

A=[1 2 3; 3 1 1; 2 3 1];
b=[8; 3; 5];

X=A\b;

H=[10 20 30 40 50 60 70 80 90 100];
X=ones(15,1);
for i=[10 50 100 500 1000 5000 10000 50000 100000 500000]
    D=diag([1,1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,i]);
    [Q,R]=qr(rand(15));
    A=Q*D*Q';
    b=A*X;
    writematrix(A,'A.txt','WriteMode','append','Delimiter','tab');
    writematrix(b,'b.txt','WriteMode','append','Delimiter','tab');
end


format long;
fileID=fopen('C:\Users\Acer\array1.txt','r');
formatSpec = '%f';
allX=fscanf(fileID,formatSpec);
fclose(fileID);

normX=norm(X);

N=15;
cols = floor(length(allX)/N);
XXX = reshape(allX(1:N*cols), [N,cols]);

H=[10 50 100 500 1000 5000 10000 50000 100000 500000];

for i=1:10
    rel_error(i)=abs(norm(XXX(:,i)-X)/norm(X));
end

loglog(H,rel_error);
title('Зависимость относительной погрешности от числа обусловленности');
xlabel('Число обусловленности');
ylabel('Относительная погрешность');







D=diag([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 100]);
[Q,R]=qr(rand(15));
A1=Q*D*Q';
writematrix(A1,'A2.txt','WriteMode','append','Delimiter','tab');

 b01=ones(15,1);
 x01=A1\b01;
 i=1;
for j= 1 : 0.001 : 2
    b=ones(15,1)*j;
    writematrix(b,'b2.txt','WriteMode','append','Delimiter','tab');
    error_b1(i)=norm(b-b01)/norm(b01);
    i=i+1;
end

format long;
fileID=fopen('C:\Users\Acer\array.txt','r');
formatSpec = '%f';
allX1=fscanf(fileID,formatSpec);
fclose(fileID);

N=15;
cols = floor(length(allX1)/N);
XXX1 = reshape(allX1(1:N*cols), [N,cols]);

for i=1:1001
    error_x1(i)=abs(norm(XXX1(:,i))-norm(x01)/norm(x01));
end

D=diag([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 1000000000]);
[Q,R]=qr(rand(15));
A2=Q*D*Q';
writematrix(A2,'A3.txt','WriteMode','append','Delimiter','tab');

 b02=ones(15,1);
 x02=A2\b02;
 i=1;
for j= 1 : 0.001 : 2
    b=ones(15,1)*j;
    writematrix(b,'b3.txt','WriteMode','append','Delimiter','tab');
    error_b2(i)=norm(b-b02)/norm(b02);
    i=i+1;
end

format long;
fileID=fopen('C:\Users\Acer\array1.txt','r');
formatSpec = '%f';
allX2=fscanf(fileID,formatSpec);
fclose(fileID);

N=15;
cols = floor(length(allX2)/N);
XXX2 = reshape(allX2(1:N*cols), [N,cols]);

for i=1:1001
    error_x2(i)=abs(norm(XXX2(:,i))-norm(x02)/norm(x02));
end

plot(error_b1,error_x1);
hold on;
plot(error_b2,error_x2);

title('Зависимость относительной погрешности решения от относительной погрешности возмущения');
xlabel('Относительная погрешность возмущения');
ylabel('Относительная погрешность решения');

legend({'Cond=1000000000','Cond=100'});


loglog(error_b1,error_x1);
hold on;
loglog(error_b2,error_x2);

title('Зависимость относительной погрешности решения от относительной погрешности возмущения');
xlabel('Относительная погрешность возмущения');
ylabel('Относительная погрешность решения');

legend({'Cond=1000000000','Cond=100'});


