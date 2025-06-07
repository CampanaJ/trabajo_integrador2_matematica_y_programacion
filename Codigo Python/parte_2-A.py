# Parte 2: Operaciones con DNIs

def obtener_conjunto_digitos(dni):
    return set(dni)

def contar_frecuencias(dni):
    frecuencias = {}
    for digito in dni:
        if digito in frecuencias:
            frecuencias[digito] += 1
        else:
            frecuencias[digito] = 1
    return frecuencias

def suma_digitos(dni):
    return sum(int(d) for d in dni)

# Ingreso de DNIs (reales o ficticios)
dni1 = input("Ingrese el DNI del primer integrante: ")  # ejemplo: 39151194
dni2 = input("Ingrese el DNI del segundo integrante: ")  # ejemplo: 42692226

# Generación de conjuntos de dígitos únicos
conjunto_A = obtener_conjunto_digitos(dni1)
conjunto_B = obtener_conjunto_digitos(dni2)

print(f"\nConjunto A = {conjunto_A}")
print(f"Conjunto B = {conjunto_B}")

# Operaciones entre conjuntos
union = conjunto_A.union(conjunto_B)
interseccion = conjunto_A.intersection(conjunto_B)
diferencia_AB = conjunto_A.difference(conjunto_B)
diferencia_BA = conjunto_B.difference(conjunto_A)
diferencia_simetrica = conjunto_A.symmetric_difference(conjunto_B)

print(f"\nUnión (A ∪ B) = {union}")
print(f"Intersección (A ∩ B) = {interseccion}")
print(f"Diferencia (A - B) = {diferencia_AB}")
print(f"Diferencia (B - A) = {diferencia_BA}")
print(f"Diferencia simétrica (A Δ B) = {diferencia_simetrica}")

# Frecuencia de cada dígito
frecuencias_A = contar_frecuencias(dni1)
frecuencias_B = contar_frecuencias(dni2)

print("\nFrecuencias en DNI 1:")
for digito, cantidad in frecuencias_A.items():
    print(f"Dígito {digito}: {cantidad} vez/veces")

print("\nFrecuencias en DNI 2:")
for digito, cantidad in frecuencias_B.items():
    print(f"Dígito {digito}: {cantidad} vez/veces")

# Suma total de dígitos
suma_A = suma_digitos(dni1)
suma_B = suma_digitos(dni2)

print(f"\nSuma de los dígitos del DNI 1: {suma_A}")
print(f"Suma de los dígitos del DNI 2: {suma_B}")

# Evaluación de condiciones lógicas

# Condición: Dígito compartido
digito_comun = conjunto_A.intersection(conjunto_B)
if digito_comun:
    print(f"\nDígito compartido entre todos los conjuntos: {digito_comun}")

# Condición: Diversidad numérica alta
if len(conjunto_A) > 6:
    print("Conjunto A tiene alta diversidad numérica.")
if len(conjunto_B) > 6:
    print("Conjunto B tiene alta diversidad numérica.")

# Condición: Resultado de expresiones lógicas del papel
print(f"\nDígitos en A y no en B: {diferencia_AB}")
print(f"Dígitos en A o en B, pero no en ambos: {diferencia_simetrica}")