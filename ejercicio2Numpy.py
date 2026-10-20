import numpy as np

ventas = np.array([120000, 95000, 150000, 80000, 200000, 175000, 110000])
print("Ventas originales:", ventas)
print("Ventas con aumento del 10%:", ventas * 1.1)
print("Total de la semana:", ventas.sum())
print("Total de la semana con aumento:", (ventas * 1.1).sum())