
#!/bin/bash -l
#SBATCH -N 1
#SBATCH --exclusive
#SBATCH -o sequenceOutputN5000.txt

echo "Uruchamiam program sekwencyjny 20 razy, rozmiar tablicy = 5000"

for i in {1..20}
do
        echo "Wynik iteracji $i:"
        ./sequence
done
