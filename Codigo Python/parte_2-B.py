from datetime import datetime
from itertools import product

# Función para determinar si un año es bisiesto
def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

# Ingreso de años de nacimiento (ejemplo ficticio si se repiten)
anios_nacimiento = []
cantidad_integrantes = int(input("Ingrese la cantidad de integrantes del grupo: "))

for i in range(cantidad_integrantes):
    anio = int(input(f"Ingrese el año de nacimiento del integrante {i + 1}: "))
    anios_nacimiento.append(anio)

# Contar pares e impares
pares = 0
impares = 0
for anio in anios_nacimiento:
    if anio % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nCantidad que nacieron en años pares: {pares}")
print(f"Cantidad que nacieron en años impares: {impares}")

# Verificar si todos nacieron después del 2000
if all(anio > 2000 for anio in anios_nacimiento):
    print("Grupo Z")

# Verificar si alguno nació en año bisiesto
if any(es_bisiesto(anio) for anio in anios_nacimiento):
    print("Tenemos un año especial")

# Calcular edades actuales
anio_actual = datetime.now().year
edades = [anio_actual - anio for anio in anios_nacimiento]

# Producto cartesiano entre años y edades
producto_cartesiano = list(product(anios_nacimiento, edades))

print("\nProducto cartesiano entre años de nacimiento y edades actuales:")
for par in producto_cartesiano:
    print(par)
