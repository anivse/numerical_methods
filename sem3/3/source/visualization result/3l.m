size = 15;
X=ones(15,1);

format long;

    for i=1:size
      for j=1:size
        if i == j
          A(i, j) =  100*rand();
        elseif i < j
          A(i, j) =  rand()*0.0000001;
        else
          A(i, j) =  rand()*0.0000001 ;
        end
      end
    end
  
h=[1 0.5 0.1 0.05 0.01 0.005 0.001 0.0005 0.0001 0.00005 0.00001];
    
    for l=1:11
        for i=1:size
            for j=1:size
                if i==j
                    A0(i,j)=A(i,j)*h(l);
                else 
                    A0(i,j)=A(i,j);
                end
            end
        end
        
        d(l)=det(A0);
        b0=A0*X;
        writematrix(A0,'A0.txt','WriteMode','append','Delimiter','tab');
        writematrix(b0,'b0.txt','WriteMode','append','Delimiter','tab');
    end
    
    for k=1:1000
       for i=1:size
      for j=1:size
        if i == j
          A(i, j) =  rand();
        else
          A(i, j) =   rand() * 0.00001;
        end
      end
    end
        
        dt(k)=det(A);
        b=A*X;
        writematrix(A,'A.txt','WriteMode','append','Delimiter','tab');
        writematrix(b,'b.txt','WriteMode','append','Delimiter','tab');
    end
    
fileID=fopen('C:\Users\Acer\Documents\4islaki\лаба 3\result2.txt','r');
formatSpec = '%f';
it=fscanf(fileID,formatSpec);
fclose(fileID);
 
ii=it';      

loglog(d,ii,'o','MarkerFaceColor',[0 0.447 0.741]);

title('Зависимость количества итераций от определителя матрицы коэффициентов');
xlabel('Определитель матрицы коэффициентов');
ylabel('Количество итераций');

format long;
fileID=fopen('C:\Users\Acer\Documents\4islaki\лаба 3\result3.txt','r');
formatSpec = '%f';
allX=fscanf(fileID,formatSpec);
fclose(fileID);

normX=norm(X);

N=15;
cols = floor(length(allX)/N);
XXX = reshape(allX(1:N*cols), [N,cols]);

for i=1:11
    rel_error(i)=abs(norm(XXX(:,i)-X)/norm(X));
end

loglog(d,rel_error);
title('Зависимость относительной погрешности от определителя матрицы');
xlabel('Определитель');
ylabel('Относительная погрешность');



fileID=fopen('C:\Users\Acer\Documents\4islaki\лаба 3\result1.txt','r');
formatSpec = '%f';
iterations=fscanf(fileID,formatSpec);
fclose(fileID);
 
iter=iterations';      

semilogx(dt,iter,'o','MarkerFaceColor',[0 0.447 0.741]);

title('Зависимость количества итераций от определителя матрицы коэффициентов');
xlabel('Определитель матрицы коэффициентов');
ylabel('Количество итераций');