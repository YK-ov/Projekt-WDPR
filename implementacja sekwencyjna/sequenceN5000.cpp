
#include <iostream>
#include <ctime>
#include <omp.h>

using namespace std;


void swapElement(float* firstNum, float* secondNum){
        float temp = *firstNum;
        *firstNum = *secondNum;
        *secondNum = temp;
}

void bubbleSort(float* arr, int size){
        for (int i = 0; i < size - 1; i++){
                for (int j = 0; j < size - i - 1; j++){
                        if (arr[j] > arr[j+1]){
                                swapElement(&arr[j], &arr[j+1]);
                        }
                }

        }
}

void fillWithRandomNumbers(float* arr, int size){
        for (int i = 0; i < size; i++){
                arr[i] = static_cast <float> (rand()) / static_cast <float> (size);
        }
}


int main(){
        int size = 5000;
        float* arr = new float[size];

        fillWithRandomNumbers(arr, size);

        double start = omp_get_wtime();

        bubbleSort(arr, size);

        double end = omp_get_wtime();

        cout << "Time: " << (end - start) / 60 << " min\n";

        delete[] arr;

        return 0;
}
