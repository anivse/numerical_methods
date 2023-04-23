#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <windows.h>
#define  eps  10e-15 ///< желаемая точность 

#define N 15

#pragma warning(disable:4996)
#pragma warning(disable:6031)

long double** ArrayRead(FILE* file, int line, int column)
{
    long double** arr;
	arr = (long double**)malloc(sizeof(long double*) * N);
	if (!arr)
		return NULL;
	for (int j = 0;j < column;j++)
	{
		arr[j] = (long double*)malloc(sizeof(long double) * N);
		if (!arr[j])
			return NULL;
		for (int i = 0;i < line;i++)
		{
			fscanf(file, "%lf", &arr[j][i]);
			//printf("%.14lf ", arr[j][i]);
		}
		//printf("\n");
	}
	return arr;
}

long double* ColumnRead(FILE* file, int size)
{
	long double* arr;
	arr = (long double*)malloc(sizeof(long double) * N);
	if (!arr)
		return NULL;
	for (int i = 0;i < size;i++)
	{
		fscanf(file, "%lf", &arr[i]);
		//printf("%.14lf \n", arr[i]);
	}
	return arr;
}


long double** CreatePrecondMatrix(long double** A)
{
	long double** C = (long double**)malloc(sizeof(long double*) * N);
	if (!C)
		return NULL;
	long double tmp;
	for (int i = 0;i < N;i++)
	{
		tmp = A[i][i];
		C[i] = (long double*)malloc(sizeof(long double) * N);

		if (!C[i])
			return NULL;

		for (int j = 0;j < N;j++)
		{
			if (i != j)
				C[i][j] = -A[i][j] / tmp;
			else
				C[i][j] = 0;
			//printf("%.16lf ",C[i][j]);
		}
		//printf("\n");
	}
	//printf("\n");
	return C;
}

long double NormMatrix(long double** matrix)
{
	long double normmax=0,norm2;
	for (int i = 0;i < N;i++)
	{
		norm2 = 0;
		for (int j = 0;j < N;j++)
		{
			norm2 += fabs(matrix[i][j]);
		}
		if (norm2 > normmax)
			normmax = norm2;
	}
	return normmax;
}


long double* ZeroApproximate(long double** A, long double* b)
{
	long double diag[N];

	long double* X = (long double*)malloc(sizeof(long double) * N);

	if (!X)
		return NULL;

	for (int i = 0;i < N;i++)
	{
		diag[i] = A[i][i];
	}

	//printf("\n\n");

	for (int j = 0;j < N;j++)
	{
		X[j] = b[j] / diag[j];
		//printf("%.16lf ",X[j]);
	}
	//printf("\n\n");
	return X;
}

void PrintResult(long double* X,FILE* f)
{
	for (int i = 0;i < N;i++)
	{
		fprintf(f, "%.20lf\n ", X[i]);
	}
	fprintf(f, "\n");
}

void Jacobi(long double **A, long double *b)
{

	//FILE* f = fopen("result1.txt", "a");
	/*FILE* f = fopen("result2.txt", "a");*/

	FILE* f = fopen("result3.txt", "a");

	long double* tempX = (long double*)malloc(sizeof(long double) * N);

	if (!tempX)
		return;

	long double norm; 
	long double* X = ZeroApproximate(A, b);
	long double** C = CreatePrecondMatrix(A);
	long double normC = NormMatrix(C);
	long double stopcond = (1 - normC) * eps / normC;
	//printf("%.16lf\n", normC);
	int count = 0;
	do {

		for (int i = 0; i < N; i++) {
			tempX[i] = b[i];
			for (int g = 0; g < N; g++) {
				if (i != g)
					tempX[i] -= A[i][g] * X[g];
			}
			tempX[i] /= A[i][i];
		}

		norm = fabs(X[0] - tempX[0]);

		for (int h = 0; h < N; h++) {
			if (fabs(X[h] - tempX[h]) > norm)
				norm = fabs(X[h] - tempX[h]);
			X[h] = tempX[h];
			//printf("%.16lf ", X[h]);
		}
		//printf("\n");
		count++;
	} while (norm>stopcond);

	
	PrintResult(X, f);

    //	fprintf(f,"%i\n", count);
    	printf("%i\n", count);

	free(C);
	free(tempX);
	free(X);
	fclose(f);

}


//long double** ArrayRead(FILE* file, int line, int column)
//{
//	long double** arr;
//	arr = (long double**)malloc(sizeof(long double*) * line);
//	if (!arr)
//		return NULL;
//	for (int j = 0;j < column;j++)
//	{
//		arr[j] = (long double*)malloc(sizeof(long double) * column);
//		if (!arr[j])
//			return NULL;
//		for (int i = 0;i < line;i++)
//		{
//			fscanf(file, "%lf", &arr[j][i]);
//			//printf("%.14lf ", arr[j][i]);
//		}
//		//printf("\n");
//	}
//	return arr;
//}
//
//long double* ColumnRead(FILE* file, int size)
//{
//	long double* arr;
//	arr = (long double*)malloc(sizeof(long double) * size);
//	if (!arr)
//		return NULL;
//	for (int i = 0;i < size;i++)
//	{
//		fscanf(file, "%lf", &arr[i]);
//		//printf("%.14lf \n", arr[i]);
//	}
//	return arr;
//}
//
//
//long double** CreatePrecondMatrix(long double** A, int size)
//{
//	long double** C = (long double**)malloc(sizeof(long double*) * size);
//	if (!C)
//		return NULL;
//	long double tmp;
//	for (int i = 0;i < size;i++)
//	{
//		tmp = A[i][i];
//		C[i] = (long double*)malloc(sizeof(long double) * size);
//
//		if (!C[i])
//			return NULL;
//
//		for (int j = 0;j < size;j++)
//		{
//			if (i != j)
//				C[i][j] = -A[i][j] / tmp;
//			else
//				C[i][j] = 0;
//			//printf("%.16lf ",C[i][j]);
//		}
//		//printf("\n");
//	}
//	//printf("\n");
//	return C;
//}
//
//long double NormMatrix(long double** matrix,int size)
//{
//	long double normmax = 0, norm2;
//	for (int i = 0;i < size;i++)
//	{
//		norm2 = 0;
//		for (int j = 0;j < size;j++)
//		{
//			norm2 += fabs(matrix[i][j]);
//		}
//		if (norm2 > normmax)
//			normmax = norm2;
//	}
//	return normmax;
//}
//
//
//long double* ZeroApproximate(long double** A, long double* b, int size)
//{
//	long double* diag=(long double*)malloc(sizeof(long double)*size);
//
//	long double* X = (long double*)malloc(sizeof(long double) * size);
//
//	if (!X)
//		return NULL;
//
//	for (int i = 0;i < size;i++)
//	{
//		diag[i] = A[i][i];
//	}
//
//	//printf("\n\n");
//
//	for (int j = 0;j < size;j++)
//	{
//		X[j] = b[j] / diag[j];
//		//printf("%.16lf ",X[j]);
//	}
//	//printf("\n\n");
//	return X;
//}
//
//void PrintResult(long double* X,FILE* f)
//{
//	for (int i = 0;i < N;i++)
//	{
//		fprintf(f, "%.16lf\n ", X[i]);
//	}
//	fprintf(f, "\n");
//}
//
//
//void Jacobi(long double** A, long double* b, int size)
//{
//
//	//FILE* f = fopen("result1.txt", "a");
//	/*FILE* f = fopen("result2.txt", "a");*/
//
//	FILE* f = fopen("jacobiresult.txt", "a");
//
//	long double* tempX = (long double*)malloc(sizeof(long double) * size);
//
//	if (!tempX)
//		return;
//
//	long double norm;
//	long double* X = ZeroApproximate(A, b,size);
//	long double** C = CreatePrecondMatrix(A,size);
//	long double normC = NormMatrix(C,size);
//	long double stopcond = (1 - normC) * eps / normC;
//	//printf("%.16lf\n", normC);
//	int count = 0;
//	do {
//
//		for (int i = 0; i < size; i++) {
//			tempX[i] = b[i];
//			for (int g = 0; g < size; g++) {
//				if (i != g)
//					tempX[i] -= A[i][g] * X[g];
//			}
//			tempX[i] /= A[i][i];
//		}
//
//		norm = fabs(X[0] - tempX[0]);
//
//		for (int h = 0; h < size; h++) {
//			if (fabs(X[h] - tempX[h]) > norm)
//				norm = fabs(X[h] - tempX[h]);
//			X[h] = tempX[h];
//			//printf("%.16lf ", X[h]);
//		}
//		//printf("\n");
//		count++;
//		/*} while (norm > stopcond);*/
//	} while (count < 5);
//
//
//	PrintResult(X, f);
//
//	//	fprintf(f,"%i\n", count);
//	//	printf("%i\n", count);
//
//	for (int m = 0;m < size;m++)
//	{
//		free(C[m]);
//	}
//
//	free(C);
//
//	free(tempX);
//	free(X);
//	fclose(f);
//
//}

int main()
{
	/*double A[3][3] = { {4,-1,1},{-1,3,-1},{1,-1,5} };
	double b[3] = { 4,1,5 };
	double X[3] = { 1,0.3333333,1 };
	Jacobi(A, b);*/

	/*FILE* af = fopen("A.txt", "r");
	FILE* bf = fopen("b.txt", "r");


	for (int i = 0;i < 1000;i++)
	{
		double** A = ArrayRead(af, N, N);
		double* b = ColumnRead(bf, N);
		Jacobi(A, b);

		free(b);

		for (int i = 0;i < N;i++)
		{
			free(A[i]);
		}

		free(A);
	}

	fclose(af);
	fclose(bf);*/


	FILE* af = fopen("A0.txt", "r");
	FILE* bf = fopen("b0.txt", "r");


	for (int i = 0;i < 11;i++)
	{
		double** A = ArrayRead(af, N, N);
		double* b = ColumnRead(bf, N);
		Jacobi(A, b);

		free(b);

		for (int k = 0;k < N;k++)
		{
			free(A[k]);
		}

		free(A);
	}

	fclose(af);
	fclose(bf);



	/*FILE* af = fopen("A.txt", "r");
	FILE* bf = fopen("b.txt", "r");

	int size[99];
	size[0] = 10;
	for (int k = 1;k < 99;k++)
	{
		size[k] = size[k - 1] + 5;
	}


	LARGE_INTEGER start, end, counter;
	double time;

	QueryPerformanceFrequency(&counter);

	for (int i = 0;i < 99;i++)
	{
		long double** A = ArrayRead(af, size[i], size[i]);
		long double* b = ColumnRead(bf, size[i]);

		QueryPerformanceCounter(&start);

		Jacobi(A, b, size[i]);

		QueryPerformanceCounter(&end);
		time = (double)((double)(end.QuadPart - start.QuadPart) / (double)counter.QuadPart);
		printf("%.10lf ", time);

		free(b);

		for (int j = 0;j < size[i];j++)
		{
			free(A[j]);
		}

		free(A);
	}

	fclose(af);
	fclose(bf);*/

}