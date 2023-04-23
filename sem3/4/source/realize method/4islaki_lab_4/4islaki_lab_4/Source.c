#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#pragma warning(disable:4996)

#define eps 10e-12

#define N 15

double** ArrayRead(FILE* file, int line, int column)
{
	double** arr;
	arr = (double**)malloc(sizeof(double*) * line);
	if (!arr)
		return NULL;
	for (int j = 0;j < column;j++)
	{
		arr[j] = (double*)malloc(sizeof(double) * column);
		if (!arr[j])
			return NULL;
		for (int i = 0;i < line;i++)
		{
			fscanf(file, "%lf", &arr[j][i]);
		}
	}
	return arr;
}

double* ColumnRead(FILE* file, int size)
{
	double* arr;
	arr = (double*)malloc(sizeof(double) * size);
	if (!arr)
		return NULL;
	for (int i = 0;i < size;i++)
	{
		fscanf(file, "%lf", &arr[i]);
		//printf("%.14lf \n", arr[i]);
	}
	return arr;
}

double* Multiplication(double** matrix, double* vector, int size)
{
	double* result = (double*)malloc(sizeof(double) * size);

	for (int i = 0; i < size; i++)
	{
		result[i] = 0;
		for (int j = 0; j < size; j++)
		{
				result[i] += matrix[i][j] * vector[j];
		}
	}
	return result;
}

double ScalarProduct(double* X, double* Y, int size)
{
	double product = 0;
	for (int i = 0;i < size;i++)
	{
		product += X[i] * Y[i];
	}
	return product;
}

double* OneVector(int size)
{
	double* vector = (double*)malloc(sizeof(double) * size);

	for (int i = 0;i < size;i++)
	{
		vector[i] = 1;
	}
	return vector;
}

double* MultVectorByNumber(double* vector, double number, int size)
{
	double* result = (double*)malloc(sizeof(double) * size);

	for (int i = 0;i < size;i++)
	{
		result[i] = number * vector[i];
	}
	return result;
}

double* SubstractionVector(double* X, double* Y, int size)
{
	double* result = (double*)malloc(sizeof(double) * size);

	for (int i = 0;i < size;i++)
	{
		result[i] = X[i] - Y[i];
		//printf("%lf\n", result[i]);
	}
	//printf("\n");
	return result;
}

void EqColumn(double* A, double* B, int size)
{
	for (int i = 0; i < size;i++)
	{
		A[i] = B[i];
	}
}

double Norm2(double* vector, int size)
{
	double sum = 0;
	for (int i = 0;i < size;i++)
	{
		sum += vector[i] * vector[i];
	}
	return sqrt(sum);
}

double NormInf(double* vector, int size)
{
	double normmax = 0, norm;
	for (int i = 0;i < size;i++)
	{
		norm = 0;
		norm = fabs(vector[i]);
		if (norm > normmax)
			normmax = norm;
	}
	return normmax;
}



void Print(double* vect, int size)
{
	for (int i = 0;i < size;i++)
	{
		printf("%.16lf\n", vect[i]);
	}
	printf("\n");
}

double* PowerMethod1Eigen(double** matrix, int size)
{
	double* X0 = OneVector(size), * X = OneVector(size), * XX = OneVector(size);
	double eigen = 0, eigenlast = 0, apostAssesment = 0, norm;
	double* eigenvector = OneVector(size);
	int k = 1;
	do
	{
		eigenlast = eigen;
		free(X);
		free(XX);
		XX = Multiplication(matrix, X0, size);
		norm = NormInf(XX, size);
		X = MultVectorByNumber(XX, 1 / norm, size);
		eigen = norm;
		//printf("%.16lf\n", eigen);
		EqColumn(eigenvector, X, size);
		EqColumn(X0, X, size);
		k++;
		//printf("\n\n%i///\n\n ", k);
		apostAssesment = Norm2(SubstractionVector(Multiplication(matrix, eigenvector, size), MultVectorByNumber(eigenvector, eigen, size), size), size) / Norm2(eigenvector, size);
		//printf("%.16lf\n", apostAssesment);
	//} while (eps < fabs(eigenlast - eigen));
	} while (eps < apostAssesment);
	free(X);
	free(XX);
	return eigenvector;
}

void PowerMethod2Eigen(double** matrix, double* eigen1vector, int size)
{
    /* double ep = 10e-12;
	while (ep <= 10e-1)
	{*/
		double* X = OneVector(size);
		double gamma = ScalarProduct(X, eigen1vector, size) / ScalarProduct(eigen1vector, eigen1vector, size);
		double* gammaMultE1Vect = MultVectorByNumber(eigen1vector, gamma, size);
		double* Y0 = SubstractionVector(X, gammaMultE1Vect, size);
		double* YY = OneVector(size);
		double* Y = OneVector(size);
		double eigen = 0, eigenlast = 0, norm, apostAssesment = 0;
		double* eigen2vector = OneVector(size);
		int k = 0;
		do
		{
			free(YY);
			free(Y);
			eigenlast = eigen;
			gamma = ScalarProduct(Y0, eigen1vector, size) / ScalarProduct(eigen1vector, eigen1vector, size);
			gammaMultE1Vect = MultVectorByNumber(eigen1vector, gamma, size);
			YY = SubstractionVector(Y0, gammaMultE1Vect, size);
			YY = Multiplication(matrix, YY, size);
			norm = NormInf(YY,size);
			Y = MultVectorByNumber(YY, 1 / norm, size);
			eigen = norm;
			//printf("%.16lf\n", eigen);
			EqColumn(eigen2vector, Y, size);
			EqColumn(Y0, Y, size);
			k++;
			apostAssesment = Norm2(SubstractionVector(Multiplication(matrix, eigen2vector, size), MultVectorByNumber(eigen2vector, eigen, size), size), size) / Norm2(eigen2vector, size);
		} while (eps < apostAssesment);
	    //} while (eps < fabs(eigenlast - eigen));
		//printf("%.16lf ", eigen);
		printf("%i, ", k);
		free(Y);
		free(X);
		free(gammaMultE1Vect);
		free(eigen2vector);
		/*ep *= 10;
	}*/

	//return eigen2vector;
}


int main()
{


	FILE* af = fopen("f.txt", "r");

	for (int i = 0;i < 81;i++)
	{
		double** matrix = ArrayRead(af, N, N);
		double* e1vect = PowerMethod1Eigen(matrix, N);
		PowerMethod2Eigen(matrix, e1vect, N);
		free(matrix);
		free(e1vect);
		//printf("\n");
	}

	fclose(af);

}