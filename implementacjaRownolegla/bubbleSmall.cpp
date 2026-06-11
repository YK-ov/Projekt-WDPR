#include <iostream>
#include <vector>
#include <ctime>
#include <omp.h>
#include <algorithm>


void bubble_sort_parallel(std::vector<float>& arr) {
    int n = arr.size(); 

    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {
#pragma omp parallel for default(none) shared(arr, n)
            for (int j = 1; j < n; j += 2) {
                if (arr[j - 1] > arr[j]) {
                    double temp = arr[j - 1];
                    arr[j - 1] = arr[j];
                    arr[j] = temp;
                }
            }
        } else {
#pragma omp parallel for default(none) shared(arr, n)
            for (int j = 2; j < n; j += 2) {
                if (arr[j - 1] > arr[j]) {
                    double temp = arr[j - 1];
                    arr[j - 1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }
}

double random_fill(std::vector<float>,int size) {
        return static_cast<double>(rand()) / RAND_MAX * 100.0;
}

int main() {
    srand(time(NULL));

    std::vector<float> dane;
    int size = 3500;

    
    dane.reserve(dane.size() + size);

    for (int i = 0; i < size; i++) {
        dane.emplace_back(random_fill(dane, size));
    }

    double start = omp_get_wtime();
    bubble_sort_parallel(dane);
    double end = omp_get_wtime();

    std::cout << "Time: " << (end - start) / 60.0 << " min\n";
   

    return 0;
}
