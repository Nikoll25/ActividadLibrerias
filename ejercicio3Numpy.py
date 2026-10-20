#importo la libreria numpy
import numpy as np

#creo un array de temperaturas en grados Celsius
celsius = np.array([18, 22, 25, 19, 30])

print("celsius:", celsius)
#calculo la temperatura en grados Fahrenheit
print("fahrenheit:", celsius * 9/5 + 32)