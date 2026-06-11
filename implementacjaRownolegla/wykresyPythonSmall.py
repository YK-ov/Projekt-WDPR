import matplotlib.pyplot as plt

# Dane z pliku plik_wyjsciowySmall.txt
threads = [1, 2, 4, 8, 12, 16, 20, 24]
times_min = [0.00197025, 0.00109906, 0.000648035, 0.000462811, 0.000395174, 0.000477587, 0.000520228, 0.000499007]

# Konwersja na sekundy w celu uzyskania czytelnych wartości na osi Y
times_sec = [t * 60 for t in times_min]

# Obliczenie przyspieszenia (Speedup)
t1 = times_sec[0]
speedup = [t1 / tp for tp in times_sec]

# Konfiguracja globalna stylu dla eleganckiego wyglądu
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['text.color'] = '#2c3e50'
plt.rcParams['axes.labelcolor'] = '#2c3e50'
plt.rcParams['xtick.color'] = '#34495e'
plt.rcParams['ytick.color'] = '#34495e'

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6.5))
fig.suptitle('Analiza skalowalności OpenMP (Typ danych: float) - Mały zbiór', fontsize=16, fontweight='bold', y=0.98)

# --- WYKRES 1: Czas wykonania (w sekundach) ---
ax1.plot(threads, times_sec, marker='o', markersize=8, markerfacecolor='#ffffff',
         markeredgewidth=2, color='#d35400', linewidth=2.5, label='Czas zmierzony')

ax1.set_title('Czas wykonania w zależności od liczby wątków', fontsize=12, fontweight='semibold', pad=12)
ax1.set_xlabel('Liczba wątków (p)', fontsize=11, labelpad=8)
ax1.set_ylabel('Czas wykonania [s]', fontsize=11, labelpad=8)
ax1.set_xticks(threads)

# Estetyka osi i siatki
ax1.grid(True, linestyle=':', alpha=0.6, color='#b0bec5')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_color('#cfd8dc')
ax1.spines['bottom'].set_color('#cfd8dc')
ax1.legend(frameon=True, facecolor='#ffffff', edgecolor='#eceff1', loc='upper right')

# --- WYKRES 2: Przyspieszenie ---
ax2.plot(threads, speedup, marker='s', markersize=7, markerfacecolor='#ffffff',
         markeredgewidth=2, color='#6a1b9a', linewidth=2.5, label='Przyspieszenie empiryczne $S(p)$')
ax2.plot(threads, threads, linestyle='--', color='#c62828', alpha=0.8, linewidth=1.8, label='Przyspieszenie idealne')

ax2.set_title('Przyspieszenie algorytmu vs Teoretyczne maksimum', fontsize=12, fontweight='semibold', pad=12)
ax2.set_xlabel('Liczba wątków (p)', fontsize=11, labelpad=8)
ax2.set_ylabel('Przyspieszenie $S(p) = T_1 / T_p$', fontsize=11, labelpad=8)
ax2.set_xticks(threads)

# Estetyka osi i siatki
ax2.grid(True, linestyle=':', alpha=0.6, color='#b0bec5')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_color('#cfd8dc')
ax2.spines['bottom'].set_color('#cfd8dc')
ax2.legend(frameon=True, facecolor='#ffffff', edgecolor='#eceff1', loc='upper left')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('skalowalnosc_openmp_small_elegant.png', dpi=300, bbox_inches='tight')
plt.show()
