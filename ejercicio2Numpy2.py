import numpy as np

ventas = np.array([120000, 95000, 150000, 80000, 200000, 175000, 110000])

# Aplicar un aumento del 10% a todas las ventas
ventas_aumentadas = ventas * 1.10

# Calcular el total de la semana
total = np.sum(ventas_aumentadas)

print("Ventas con aumento:", ventas_aumentadas)
print("Total de la semana:", total)
