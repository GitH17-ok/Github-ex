import pandas as pd

import matplotlib.pyplot as plt

# Beispiel-Daten als DataFrame
data = {
    'Jahr': [2020, 2021, 2022, 2023],
    'Umsatz': [100, 150, 200, 250]
}
df = pd.DataFrame(data)

# Plot erstellen
plt.plot(df['Jahr'], df['Umsatz'], marker='o')
plt.title('Umsatzentwicklung')
plt.xlabel('Jahr')
plt.ylabel('Umsatz')
plt.grid(True)
plt.savefig("Copilot_Generated_Plot.png", dpi=300)  # Speichern des Plots
plt.show()