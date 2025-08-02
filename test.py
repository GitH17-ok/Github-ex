import time
import numpy as np
import matplotlib.pyplot as plt

# --- Konfiguration ---
MATRIX_SIZE = 2000  # Größe der Matrizen. Erhöhen Sie dies für anspruchsvollere Berechnungen.
# Hinweis: Bei sehr großen Werten kann es zu Speichermangel kommen.

# --- Teil 1: Rechenintensive Aufgabe (NumPy Matrixmultiplikation) ---
print(f"Starte rechenintensive Aufgabe mit Matrizen der Größe {MATRIX_SIZE}x{MATRIX_SIZE}...")
start_compute_time = time.time()

# Zwei große Zufallsmatrizen erstellen
matrix_a = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)
matrix_b = np.random.rand(MATRIX_SIZE, MATRIX_SIZE)

# Matrixmultiplikation durchführen
result_matrix = np.dot(matrix_a, matrix_b)

end_compute_time = time.time()
compute_time = end_compute_time - start_compute_time
print(f"Rechenintensive Aufgabe abgeschlossen in: {compute_time:.4f} Sekunden")

# --- Teil 2: Plotten mit Matplotlib ---
print("Starte Plot-Erstellung mit Matplotlib...")
start_plot_time = time.time()

# Eine einfache Visualisierung des Ergebnisses erstellen
# Wir nehmen hier nur einen kleinen Teil der Ergebnis-Matrix, um den Plot nicht zu überladen
plt.figure(figsize=(10, 6))
plt.imshow(result_matrix[:50, :50], cmap='viridis') # Zeigt die ersten 50x50 Elemente
plt.colorbar(label='Wert')
plt.title(f'Ergebnis der Matrixmultiplikation ({MATRIX_SIZE}x{MATRIX_SIZE})')
plt.xlabel('Spalte')
plt.ylabel('Zeile')
plt.axis('off') # Achsen ausblenden, da es nur ein repräsentativer Plot ist

# Plot speichern (oder anzeigen, wenn im Notebook ausgeführt)
# Im Colab/Codespaces Notebook wird es direkt angezeigt
# Wenn Sie es speichern möchten:
# plt.savefig('matrix_result_plot.png', dpi=300)

end_plot_time = time.time()
plot_time = end_plot_time - start_plot_time
print(f"Plot-Erstellung abgeschlossen in: {plot_time:.4f} Sekunden")

# --- Gesamtzeit ---
total_time = compute_time + plot_time
print(f"\nGesamtzeit für Berechnung und Plot: {total_time:.4f} Sekunden")

# Überprüfen Sie optional die Form und einige Werte der Ergebnis-Matrix
# print(f"Shape der Ergebnis-Matrix: {result_matrix.shape}")
# print(f"Erste 5x5 Elemente der Ergebnis-Matrix:\n{result_matrix[:5, :5]}")
plt.show()