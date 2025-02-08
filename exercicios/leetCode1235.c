#include <stdio.h>
#include <stdlib.h>
# define swap(a,b) {int t; t = a; a = b; b = t;}

void merge(int *endTime, int *startTime, int *profit, int l, int m, int r)
{
    int tamanho = r - l + 1;
    int *endTimeAux = malloc(tamanho * (sizeof(int)));
    int *startAux = malloc(tamanho * (sizeof(int)));
    int *profitAux = malloc(tamanho * (sizeof(int)));

    if(endTimeAux)
    {   
        int subVetorEsq = l; // inicio do sub-vetor a esquerda
        int subVetorDireita = m + 1;  // inicio do sub-vetor a direita

        int i = 0;
        while(subVetorDireita <= r && subVetorEsq <= m)
        {
            // se o elemento da esquerda for menor que o da direita entao coloca o da esquerda
            if(endTime[subVetorDireita] < endTime[subVetorEsq]) 
            {
                endTimeAux[i] = endTime[subVetorDireita];
                startAux[i] = startTime[subVetorDireita];
                profitAux[i] = profit[subVetorDireita];
                i++;
                subVetorDireita++;
            }
            else
            {
                endTimeAux[i] = endTime[subVetorEsq];
                startAux[i] = startTime[subVetorEsq];
                profitAux[i] = profit[subVetorEsq];
                i++;
                subVetorEsq++;
            }
        }

        while(subVetorEsq <= m)
        {
            endTimeAux[i] = endTime[subVetorEsq];
            startAux[i] = startTime[subVetorEsq];
            profitAux[i] = profit[subVetorEsq];
            i++;
            subVetorEsq++;
        }

        while(subVetorDireita <= r)
        {
            endTimeAux[i] = endTime[subVetorDireita];
            startAux[i] = startTime[subVetorDireita];
            profitAux[i] = profit[subVetorDireita];
            i++;
            subVetorDireita++;
        }

        i = 0;
        while(i < tamanho)
        {   
            endTime[l] =  endTimeAux[i];
            startTime[l] = startAux[i];
            profit[l] = profitAux[i];
            l++;
            i++;
        }
        free(endTimeAux);
        free(startAux);
        free(profitAux);
    }
}

void mergeSort(int *endTime, int * startTime, int *profit, int l, int r)
{
    if(l < r)
    {
        int m = (l + r)/2;
        mergeSort(endTime,startTime, profit, l, m);
        mergeSort(endTime,startTime, profit, m + 1, r);
        merge(endTime,startTime, profit, l, m, r);
    }
}


int find(int *endTime, int begin, int startTime)
{
    for(int i = begin; i >= 0; i--)
    {
        if(endTime[i] <= startTime) return i+1;
    }
    return -2;
}

int optimize(int *endTime, int *startTime, int* profit, int vetorSize)
{
    int *job = malloc(sizeof(int) * (vetorSize + 1));
    int aux;
    job[0] = 0, job[1] = profit[0];

    for(int i = 2; i <= vetorSize; i++)
    {
        aux = find(endTime, i - 1, startTime[i - 1]);
        if(aux == -1)
        {
            job[i] = (profit[i - 1] > job[i - 1]) ? profit[i - 1] : job[i-1]; 
        }
        else
        {
            job[i] = (profit[i - 1] + job[aux] > job[i - 1]) ? profit[i - 1] + job[aux] : job[i-1]; 
        }
    }

    int result = job[vetorSize];
    free(job);

    return result;

}

int jobScheduling (int* startTime, int startTimeSize, int* endTime, int endTimeSize, int* profit, int profitSize) 
{
    mergeSort(endTime, startTime, profit,0, endTimeSize - 1);

    return optimize(endTime,startTime,profit,profitSize);
}

int main ()
{

    int startTime[] = {1,2,3,3};
    int endtime[] = {3,4,5,6};
    int profit[] = {50,10,40,70};
    int teste = jobScheduling(startTime,4,endtime,4,profit,4);
    printf("%d",teste);
    return 0;
}