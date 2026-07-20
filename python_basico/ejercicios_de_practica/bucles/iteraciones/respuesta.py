# ============================================================
# EJERCICIOS DE PRÁCTICA:
# ITERANDO DISTINTOS TIPOS DE DATOS
# ============================================================


# ============================================================
# PROBLEMA 1: RECORRER UNA PALABRA
# ============================================================

print("\n--- PROBLEMA 1: RECORRER UNA PALABRA ---")

palabra = "python"

for letra in palabra:
    print(letra)


# ============================================================
# PROBLEMA 2: CONTAR VOCALES
# ============================================================

print("\n--- PROBLEMA 2: CONTAR VOCALES ---")

texto = "Programacion en Python"
vocales = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1

print("Cantidad de vocales:", contador)


# ============================================================
# PROBLEMA 3: MOSTRAR NOMBRES
# ============================================================

print("\n--- PROBLEMA 3: MOSTRAR NOMBRES ---")

nombres = ["Ana", "Luis", "Marta", "Pedro"]

for nombre in nombres:
    print(nombre)


# ============================================================
# PROBLEMA 4: SUMAR NÚMEROS
# ============================================================

print("\n--- PROBLEMA 4: SUMAR NÚMEROS ---")

numeros = [10, 5, 8, 20, 3]
suma = 0

for numero in numeros:
    suma += numero

print("La suma total es:", suma)


# ============================================================
# PROBLEMA 5: ENCONTRAR EL NÚMERO MAYOR
# ============================================================

print("\n--- PROBLEMA 5: ENCONTRAR EL NÚMERO MAYOR ---")

numeros = [10, 45, 3, 67, 22]
mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print("El número mayor es:", mayor)


# ============================================================
# PROBLEMA 6: CONTAR NÚMEROS PARES
# ============================================================

print("\n--- PROBLEMA 6: CONTAR NÚMEROS PARES ---")

numeros = [3, 8, 12, 7, 5, 20]
contador = 0

for numero in numeros:
    if numero % 2 == 0:
        contador += 1

print("Cantidad de números pares:", contador)


# ============================================================
# PROBLEMA 7: MOSTRAR UNA TUPLA
# ============================================================

print("\n--- PROBLEMA 7: MOSTRAR UNA TUPLA ---")

meses = ("Enero", "Febrero", "Marzo", "Abril")

for mes in meses:
    print(mes)


# ============================================================
# PROBLEMA 8: RECORRER UN CONJUNTO
# ============================================================

print("\n--- PROBLEMA 8: RECORRER UN CONJUNTO ---")

colores = {"rojo", "verde", "azul"}

for color in colores:
    print(color)


# ============================================================
# PROBLEMA 9: MOSTRAR CLAVES Y VALORES DE UN DICCIONARIO
# ============================================================

print("\n--- PROBLEMA 9: MOSTRAR CLAVES Y VALORES ---")

estudiante = {
    "nombre": "Alfonso",
    "edad": 22,
    "carrera": "Analista Programador"
}

for clave, valor in estudiante.items():
    print(clave, ":", valor)


# ============================================================
# PROBLEMA 10: CONTAR UNA LETRA ESPECÍFICA
# ============================================================

print("\n--- PROBLEMA 10: CONTAR UNA LETRA ---")

palabra = "programacion"
letra_buscada = input("Ingresa una letra a buscar: ")
contador = 0

for letra in palabra:
    if letra == letra_buscada:
        contador += 1

print(f"La letra '{letra_buscada}' aparece {contador} veces")


# ============================================================
# FIN DEL PROGRAMA
# ============================================================

print("\n==============================================")
print("TODOS LOS EJERCICIOS HAN TERMINADO")
print("==============================================")