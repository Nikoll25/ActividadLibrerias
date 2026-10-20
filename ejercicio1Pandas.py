import pandas as pd

# se crea un inventario con los productos, sus precios y las cantidades disponibles
inventario = {
"producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
"precio": [45000, 30000, 89000, 8000, 150000],
"stock": [20, 5, 12, 40, 3],
}
#5. Explorar el inventario

# se convierte el inventario en un dataframe para organizar los datos en una tabla
df = pd.DataFrame(inventario)
print(df)

# se muestran las primeras tres filas del dataframe
print("Primeras filas:")
print(df.head(3))

#muestro la forma del dataframe
print("Forma del DataFrame:")
print(df.shape)

# muestro los nombres de las columnas del dataframe
print("Nombres de las columnas:")
print(df.columns)

# muestro estadísticas rápidas del dataframe
print("Estadísticas rápidas:")
print(df.describe())

#6. Productos por reponer

#Se filtra y muestra solo los productos con stock menor a 10.
productos_reponer = df[df["stock"] < 10]
print("Productos por reponer:")
print(productos_reponer)

# 7. Valor del inventario

#Agrego una columna valor_inventario (precio * stock)
df["valor_inventario"] = df["precio"] * df["stock"]

# Agrego una columna "reponer" que sea True si el stock es menor a 10
df["reponer"] = df["stock"] < 10

#Muestro el DataFrame resultante.
print("Inventario actualizado:")
print(df)

# 8. Ordenar y resumir

#ordeno el inventario del producto más caro al más barato con sort_values
inventario_ordenado = df.sort_values(by="precio", ascending=False)

print("Inventario del producto más caro al más barato:")
print(inventario_ordenado)

#calculo el promedio de los precios de los productos con mean
print("Precio promedio:")
print(df["precio"].mean())

# 9. Guardar y leer el archivo CSV

#Guardo el DataFrame en un archivo CSV llamado "inventario.csv" sin incluir el índice
df.to_csv("inventario.csv", index=False)

#leo el archivo CSV con pd.read_csv y lo muestro 
df_leido = pd.read_csv("inventario.csv")

print("Datos leídos desde el archivo:")
print(df_leido)
