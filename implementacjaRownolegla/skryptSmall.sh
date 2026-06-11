#!/bin/bash -l
#SBATCH -N 1
#SBATCH --exclusive
#SBATCH -o plik_wyjsciowySmall.txt

echo "Rozpoczecie testow skalowalnosci OpenMP..."
echo "=========================================="


for threads in 1 2 4 8 12 16 20 24
do
    echo "Uruchamianie dla liczby watkow: $threads"

    export OMP_NUM_THREADS=$threads

    ./programSmall_omp
 
    echo "------------------------------------------"
done

echo "Wszystkie testy zostaly zakonczone."
