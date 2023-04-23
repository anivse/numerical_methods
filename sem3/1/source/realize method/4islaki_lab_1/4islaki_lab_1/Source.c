#include <stdio.h>
#include <math.h>
#include"assert.h"
#pragma warning (disable:4996)
double AlgFunc(double x) {
    return x * x * x * x + x * x * x - x * x - 15;
}

double TranFunc(double x) {
    return exp(x)+x+1;
}

double dAlgFunc(double x) {
    return 4 * x * x * x + 3 * x * x - 2 * x;
}

double dTranFunc(double x) {
    return exp(x) + 1;
}
void BisectionMethod(double(*func)(double), double left, double right, char const* filename) {
    double EPS = 1e-12;
    FILE* file=fopen(filename, "a");
    assert(func(left) * func(right) < 0);
    while (EPS <= 1e-1) {
        double a = left, b = right;
        double c = (b + a) / 2;
        int n = 0;
        while ((fabs(b - a)) > 2*EPS) {
            if ((func(a) * func(c)) < 0) {
                b = c;
            }
            else {
                a = c;
            }
            c = (a + b) / 2;
        //   printf("%.16lf ", c);
            n++;
            //printf("%i ", n);
        }
      double  x = c;
    /*  printf("%i ", n);*/
      printf("%.16lf ", x);
     // fprintf(stdout,"%i ", n);
        EPS = EPS / 0.1; 
    }
      fclose(file);
}

void SecantMethod(double(*func)(double), double right, char const* filename, double(*dfunc)(double)) {
   double EPS = 1e-12;
   FILE* file = fopen(filename, "a");
   while (EPS <= 1e-1) {
       double x0 = right, x1 = x0 - (func(x0) / dfunc(x0)), x2;
       // printf("%.16lf ", x1);
       int n = 0;
       while ((func(x1 - EPS) * func(x1 + EPS)) >= 0) {
           x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0));
           n++;
           x0 = x1;
           x1 = x2;
          // printf("%.20lf ", x1);
          //printf("%i ", n);
       }
    //printf("%i \n", n);
     printf("%.20lf ", x1);
   // fprintf(stdout,"%i ", n);
    // fprintf(file,"\n");
       EPS /= 0.1;
   }
    fclose(file);
}

int main() {
    //for (double i = 5;i >= 2;i=i-0.1) {
    //   // printf("%lf ", i);
    //     BisectionMethod(AlgFunc, 0, i, "doc.txt");
    //}
//BisectionMethod(AlgFunc, 0, 5, "doc.txt");
  //  BisectionMethod(TranFunc, -1.5, -1, "doc.txt");
    //for (double i = 2;i >= -1;i = i - 0.1) {
    //   // printf("%lf ", i);
    //    BisectionMethod(TranFunc, -1.5, i, "doc.txt");
    //}
    //for (double i = 5;i >= 2;i = i - 0.1) {
    // //   printf("%lf ", i);
    //    SecantMethod(AlgFunc, i, "doc.txt",dAlgFunc);
    //}
   //SecantMethod(AlgFunc,5,"doc.txt",dAlgFunc);
    //for (double i = 2;i >= -1;i = i - 0.1) {
    //  //  printf("%lf ", i);
    //    SecantMethod(TranFunc, i, "doc.txt",dTranFunc);
    //}
  SecantMethod(TranFunc, -1, "doc.txt",dTranFunc);
}