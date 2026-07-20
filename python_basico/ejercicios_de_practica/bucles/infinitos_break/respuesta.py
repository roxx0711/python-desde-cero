# ============================================================
# EJERCICIOS DE PRÁCTICA:
# while True, break y continue
# ============================================================


# ============================================================
# PROBLEMA 1: CONTRASEÑA CORRECTA
# ============================================================

print("\n--- PROBLEMA 1: CONTRASEÑA CORRECTA ---")

clave_correcta = "python123"

while True:
    clave = input("Ingresa la contraseña: ")

    if clave == clave_correcta:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta, intenta de nuevo.")


# ============================================================
# PROBLEMA 2: NÚMERO POSITIVO
# ============================================================

print("\n--- PROBLEMA 2: NÚMERO POSITIVO ---")

while True:
    numero = float(input("Ingresa un número: "))

    if numero > 0:
        print("Número positivo ingresado. Fin del programa.")
        break
    else:
        print("Ese número no es positivo, intenta otra vez.")


# ============================================================
# PROBLEMA 3: EDAD VÁLIDA
# ============================================================

print("\n--- PROBLEMA 3: EDAD VÁLIDA ---")

while True:
    edad = int(input("Ingresa tu edad: "))

    if edad < 1 or edad > 120:
        print("Edad inválida, debe estar entre 1 y 120.")
        continue

    print("Edad válida:", edad)
    break


# ============================================================
# PROBLEMA 4: MENÚ DE SALIDA
# ============================================================

print("\n--- PROBLEMA 4: MENÚ DE SALIDA ---")

while True:
    print("\n1. Continuar")
    print("2. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "2":
        print("Saliendo del programa...")
        break
    else:
        print("Continuando...")


# ============================================================
# PROBLEMA 5: NOMBRE OBLIGATORIO
# ============================================================

print("\n--- PROBLEMA 5: NOMBRE OBLIGATORIO ---")

while True:
    nombre = input("Ingresa tu nombre: ")

    if nombre == "":
        print("El nombre no puede estar vacío, intenta de nuevo.")
        continue

    print("Hola,", nombre)
    break


# ============================================================
# PROBLEMA 6: NÚMERO PAR
# ============================================================

print("\n--- PROBLEMA 6: NÚMERO PAR ---")

while True:
    numero = int(input("Ingresa un número entero: "))

    if numero % 2 == 0:
        print("Número par ingresado. Fin del programa.")
        break
    else:
        print("El número es impar, intenta otra vez.")


# ============================================================
# PROBLEMA 7: ADIVINAR UN NÚMERO
# ============================================================

print("\n--- PROBLEMA 7: ADIVINAR UN NÚMERO ---")

numero_secreto = 7

while True:
    intento = int(input("Adivina el número secreto: "))

    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número.")
        break
    else:
        print("Incorrecto, intenta de nuevo.")


# ============================================================
# PROBLEMA 8: CONFIRMACIÓN
# ============================================================

print("\n--- PROBLEMA 8: CONFIRMACIÓN ---")

while True:
    respuesta = input("¿Desea continuar? (S/N): ").upper()

    if respuesta == "S":
        print("Continuando...")
        continue

    elif respuesta == "N":
        print("Fin del programa.")
        break

    else:
        print("Respuesta inválida, intenta de nuevo.")


# ============================================================
# PROBLEMA 9: MÚLTIPLO DE 5
# ============================================================

print("\n--- PROBLEMA 9: MÚLTIPLO DE 5 ---")

while True:
    numero = int(input("Ingresa un número: "))

    if numero % 5 == 0:
        print("Es múltiplo de 5. Fin del programa.")
        break
    else:
        print("No es múltiplo de 5, intenta otra vez.")


# ============================================================
# PROBLEMA 10: NOTA APROBATORIA
# ============================================================

print("\n--- PROBLEMA 10: NOTA APROBATORIA ---")

while True:
    nota = float(input("Ingresa una nota: "))

    if nota >= 4.0:
        print("Nota aprobatoria. Fin del programa.")
        break
    else:
        print("Nota insuficiente, intenta con otra.")


# ============================================================
# PROBLEMA 11: CORREO ELECTRÓNICO
# ============================================================

print("\n--- PROBLEMA 11: CORREO ELECTRÓNICO ---")

while True:
    correo = input("Ingresa tu correo electrónico: ")

    if "@" in correo:
        print("Correo válido:", correo)
        break
    else:
        print("Correo inválido, debe contener '@'.")


# ============================================================
# FIN DEL PROGRAMA
# ============================================================

print("\n===================================")
print("TODOS LOS EJERCICIOS HAN TERMINADO")
print("===================================")