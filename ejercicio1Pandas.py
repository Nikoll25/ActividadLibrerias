import pandas as pd

inventario = {
"producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
"precio": [45000, 30000, 89000, 8000, 150000],
"stock": [20, 5, 12, 40, 3],
}
#5. Explorar el inventario
df = pd.DataFrame(inventario)
print(df)
print("Primeras filas:")
print(df.head(3))

print("Forma del DataFrame:")
print(df.shape)

print("Nombres de las columnas:")
print(df.columns)

print("Estadísticas rápidas:")
print(df.describe())

#6. Productos por reponer
productos_reponer = df[df["stock"] < 10]
print("Productos por reponer:")
print(productos_reponer)

# 7. Valor del inventario
df["valor_inventario"] = df["precio"] * df["stock"]

df["reponer"] = df["stock"] < 10

print("Inventario actualizado:")
print(df)

import pandas as pd

inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3],
}

# 5. Explorar el inventario
df = pd.DataFrame(inventario)

print("Primeras filas:")
print(df.head(3))

print("Forma del DataFrame:")
print(df.shape)

print("Nombres de las columnas:")
print(df.columns)

print("Estadísticas rápidas:")
print(df.describe())

# 6. Productos por reponer
productos_reponer = df[df["stock"] < 10]

print("Productos por reponer:")
print(productos_reponer)

# 7. Valor del inventario
df["valor_inventario"] = df["precio"] * df["stock"]

df["reponer"] = df["stock"] < 10

print("Inventario actualizado:")
print(df)

# 8. Ordenar y resumir
inventario_ordenado = df.sort_values(by="precio", ascending=False)

print("Inventario del producto más caro al más barato:")
print(inventario_ordenado)

print("Precio promedio:")
print(df["precio"].mean())

# 9. Guardar y leer el archivo CSV
df.to_csv("inventario.csv", index=False)

df_leido = pd.read_csv("inventario.csv")

print("Datos leídos desde el archivo:")
print(df_leido)
