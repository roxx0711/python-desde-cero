# ============================================================
# PROBLEMAS DE PRÁCTICA:
# RECURSIVIDAD Y CÁLCULO MATEMÁTICO BÁSICO
# ============================================================


# ============================================================
# PARTE 1: RECURSIVIDAD
# ============================================================


# ------------------------------------------------------------
# PROBLEMA 1: CONTAR DESDE UN NÚMERO HASTA CERO
# ------------------------------------------------------------

print("\n--- PROBLEMA 1: CUENTA REGRESIVA ---")

def cuenta_regresiva(numero):

    print(numero)

    if numero > 0:
        cuenta_regresiva(numero - 1)


numero = int(input("Ingresa un número: "))

cuenta_regresiva(numero)


# ------------------------------------------------------------
# PROBLEMA 2: SUMAR NÚMEROS PARES
# ------------------------------------------------------------

print("\n--- PROBLEMA 2: SUMAR NÚMEROS PARES ---")


def sumar_pares(numero, suma):

    if numero <= 0:
        print("La suma es:", suma)

    elif numero % 2 == 0:
        suma = suma + numero
        sumar_pares(numero - 1, suma)

    else:
        sumar_pares(numero - 1, suma)


numero = int(input("Ingresa un número: "))

sumar_pares(numero, 0)


# ------------------------------------------------------------
# PROBLEMA 3: MULTIPLICAR NÚMEROS HASTA N
# ------------------------------------------------------------

print("\n--- PROBLEMA 3: MULTIPLICAR NÚMEROS ---")

def multiplicar_hasta(numero):

    if numero == 1:
        return 1

    return numero * multiplicar_hasta(numero - 1)


numero = int(input("Ingresa un número: "))

resultado = multiplicar_hasta(numero)

print("El resultado de la multiplicación es:", resultado)


# ------------------------------------------------------------
# PROBLEMA 4: CONTAR NÚMEROS POSITIVOS
# ------------------------------------------------------------

print("\n--- PROBLEMA 4: CONTAR NÚMEROS POSITIVOS ---")

def contar_positivos(numero):

    if numero == 0:
        return 0

    return 1 + contar_positivos(numero - 1)


numero = int(input("Ingresa un número: "))

resultado = contar_positivos(numero)

print("Hay", resultado, "números positivos.")


# ------------------------------------------------------------
# PROBLEMA 5: SUMAR LOS DÍGITOS DE UN NÚMERO
# ------------------------------------------------------------

print("\n--- PROBLEMA 5: SUMAR LOS DÍGITOS ---")

def sumar_digitos(numero):

    if numero == 0:
        return 0

    return numero % 10 + sumar_digitos(numero // 10)


numero = int(input("Ingresa un número: "))

resultado = sumar_digitos(numero)

print("La suma de los dígitos es:", resultado)


# ============================================================
# PARTE 2: CÁLCULO MATEMÁTICO BÁSICO
# ============================================================


# ------------------------------------------------------------
# PROBLEMA 1: DOBLE Y TRIPLE
# ------------------------------------------------------------

print("\n--- CÁLCULO 1: DOBLE Y TRIPLE ---")

numero = float(input("Ingresa un número: "))

doble = numero * 2
triple = numero * 3

print("Doble:", doble)
print("Triple:", triple)


# ------------------------------------------------------------
# PROBLEMA 2: SUMA, RESTA Y MULTIPLICACIÓN
# ------------------------------------------------------------

print("\n--- CÁLCULO 2: OPERACIONES BÁSICAS ---")

numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)


# ------------------------------------------------------------
# PROBLEMA 3: ÁREA DE UN RECTÁNGULO
# ------------------------------------------------------------

print("\n--- CÁLCULO 3: ÁREA DE UN RECTÁNGULO ---")

base = float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))

area = base * altura

print("El área del rectángulo es:", area)


# ------------------------------------------------------------
# PROBLEMA 4: CELSIUS A FAHRENHEIT
# ------------------------------------------------------------

print("\n--- CÁLCULO 4: CELSIUS A FAHRENHEIT ---")

celsius = float(input("Ingresa los grados Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("La temperatura en Fahrenheit es:", fahrenheit)


# ------------------------------------------------------------
# PROBLEMA 5: DESCUENTO DE UN PRODUCTO
# ------------------------------------------------------------

print("\n--- CÁLCULO 5: DESCUENTO ---")

precio = float(input("Ingresa el precio del producto: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))

valor_descuento = precio * descuento / 100

precio_final = precio - valor_descuento

print("El precio final es:", precio_final)


# ============================================================
# FIN DEL PROGRAMA
# ============================================================

print("\n==============================================")
print("TODOS LOS EJERCICIOS HAN TERMINADO")
print("==============================================")