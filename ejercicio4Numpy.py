import numpy as np

#creo una matriz de calificaciones de 3 estudiantes en 4 materias
calificaciones = np.array([[8.5, 7.0, 9.0, 8.0], # Carlos
                           [6.0, 7.5, 8.0, 7.0], # Ana
                           [9.0, 8.5, 9.5, 9.0]  # Luis
])

print("promedio por estudiante:", calificaciones.mean(axis=1)) #promedio por estudiante
print("promedio por materia:", calificaciones.mean(axis=0)) #promedio por materia