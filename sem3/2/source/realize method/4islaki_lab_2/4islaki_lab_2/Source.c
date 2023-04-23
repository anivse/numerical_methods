#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<windows.h>
#define N 100 

#pragma warning(disable:4996)


//long double** ArrayRead(FILE* file, int line, int column)
//{
//
//	long double** arr;
//	arr = (long double**)malloc(sizeof(long double*) * N);
//	for (int j = 0;j < column;j++)
//	{
//		arr[j] = (long double*)malloc(sizeof(long double) * N);
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
//	arr = (long double*)malloc(sizeof(long double) * N);
//	for (int i = 0;i < size;i++)
//	{
//		fscanf(file, "%lf", &arr[i]);
//		//printf("%.14lf \n", arr[i]);
//	}
//	return arr;
//}
//
//void RotationMethod(long double** A,long double* b)
//{
//	long double c, s;
//	/*FILE* f = fopen("array1.txt", "a");*/
//
//	FILE* f = fopen("rotationresult.txt", "a");
//
//	int k = 0;
//	long double X[N];
//	for (int i = 0;i < N - 1;i++)
//	{
//		for (int j = i + 1;j < N;j++)
//		{
//			c = A[i][k] / sqrt(A[i][k] * A[i][k] + A[j][k] * A[j][k]);
//			s = A[j][k] / sqrt(A[i][k] * A[i][k] + A[j][k] * A[j][k]);
//			for (int m = k;m < N;m++)
//			{
//				long double a1 = c * A[i][m] + s * A[j][m];
//				long double a2= c * A[j][m] - s * A[i][m];
//				A[i][m] = a1;
//				A[j][m] = a2;
//			}
//			
//			long double b1 = c * b[i] + s * b[j];
//			long double b2 = c * b[j] - s * b[i];
//			b[i] = b1;
//			b[j] = b2;
//		}
//		k++;
//	}
//	for (int i = N - 1;i >= 0;i--)
//	{
//		long double tmp = b[i];
//		for (int j = N - 1;j > i;j--)
//		{
//			tmp  -= A[i][j] * X[j];
//		}
//		X[i] = tmp / A[i][i];
//		fprintf(f,"%.16lf\n ", X[i]);
//	}
//	fprintf(f,"\n");
//	fclose(f);
//}

long double** ArrayRead(FILE* file, int line, int column)
{

	long double** arr;
	arr = (long double**)malloc(sizeof(long double*) * line);
	for (int j = 0;j < column;j++)
	{
		arr[j] = (long double*)malloc(sizeof(long double) * column);
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
	arr = (long double*)malloc(sizeof(long double) * size);
	for (int i = 0;i < size;i++)
	{
		fscanf(file, "%lf", &arr[i]);
		//printf("%.14lf \n", arr[i]);
	}
	return arr;
}

void RotationMethod(long double** A, long double* b,int size)
{
	long double c, s;
	/*FILE* f = fopen("array1.txt", "a");*/

	/*FILE* f = fopen("rotationresult.txt", "a");*/

	int k = 0;
	long double* X = (long double*)malloc(sizeof(long double) * size);
	for (int i = 0;i < size - 1;i++)
	{
		for (int j = i + 1;j < size;j++)
		{
			c = A[i][k] / sqrt(A[i][k] * A[i][k] + A[j][k] * A[j][k]);
			s = A[j][k] / sqrt(A[i][k] * A[i][k] + A[j][k] * A[j][k]);
			for (int m = k;m < size;m++)
			{
				long double a1 = c * A[i][m] + s * A[j][m];
				long double a2 = c * A[j][m] - s * A[i][m];
				A[i][m] = a1;
				A[j][m] = a2;
			}

			long double b1 = c * b[i] + s * b[j];
			long double b2 = c * b[j] - s * b[i];
			b[i] = b1;
			b[j] = b2;
		}
		k++;
	}
	for (int i = size - 1;i >= 0;i--)
	{
		long double tmp = b[i];
		for (int j = size - 1;j > i;j--)
		{
			tmp -= A[i][j] * X[j];
		}
		X[i] = tmp / A[i][i];
		//fprintf(f, "%.16lf\n ", X[i]);
	}
	/*fprintf(f, "\n");
	fclose(f);*/
	free(X);
}

int main()
{
	/*FILE* af = fopen("A.txt", "r");
	FILE* bf = fopen("b.txt", "r");
	for (int i = 0;i < 10;i++)
	{
		long double** A;
		long double* b;
		A = ArrayRead(af, N, N);
		b = ColumnRead(bf, N);
		RotationMethod(A, b);
		for (int i = 0;i < N;i++)
		{
			free(A[i]);
		}
		free(A);
		free(b);
		
	}
	fclose(af);
	fclose(bf);*/



	/*FILE* af = fopen("A3.txt", "r");
	FILE* bf = fopen("b3.txt", "r");
	long double** A;
	A = ArrayRead(af, N, N);
	if (A)
	{
		for (int i = 0;i <= 1000;i++)
		{
			long double* b;
			b = ColumnRead(bf, N);
			RotationMethod(A, b);
			free(b);

		}
		for (int i = 0;i < N;i++)
		{
			free(A[i]);
		}
	}
	free(A);
	fclose(af);
	fclose(bf);*/


	FILE* af = fopen("A.txt", "r");
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

		RotationMethod(A, b,size[i]);

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
	fclose(bf);

}

