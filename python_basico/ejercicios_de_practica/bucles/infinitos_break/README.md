# Ejercicios de práctica: `while True`, `break` y `continue`

## Problema 1: Contraseña correcta
Desarrolla un programa que solicite al usuario una contraseña.

```python
clave_correcta = "python123"

while True:
    clave = input("Ingresa la contraseña: ")
    if clave == clave_correcta:
        print("Contraseña correcta. Acceso concedido.")
        break
    else:
        print("Contraseña incorrecta, intenta de nuevo.")
```

**Explicación:**
- `while True:` → crea un bucle infinito, se repite para siempre a menos que algo lo detenga desde adentro.
- `input(...)` → pide la contraseña y la guarda en `clave`.
- `if clave == clave_correcta:` → compara lo ingresado con la contraseña real.
- `break` → corta el bucle inmediatamente, es lo que "detiene" el `while True`.
- `else:` → si no coincide, muestra el mensaje y el bucle vuelve a empezar (porque no hubo `break`).

---

## Problema 2: Número positivo
Solicita al usuario un número.

```python
while True:
    numero = float(input("Ingresa un número: "))
    if numero > 0:
        print("Número positivo ingresado. Fin del programa.")
        break
    else:
        print("Ese número no es positivo, intenta otra vez.")
```

**Explicación:**
- `float(input(...))` → convierte el texto ingresado a número decimal, para poder compararlo con `>`.
- `if numero > 0:` → si el número es mayor que cero, se cumple la condición de "positivo".
- `break` → termina el bucle apenas se cumple la condición.
- Si no se cumple, no hay `break`, así que el `while True` vuelve a pedir otro número.

---

## Problema 3: Edad válida
Solicita la edad del usuario.

```python
while True:
    edad = int(input("Ingresa tu edad: "))
    if edad < 1 or edad > 120:
        print("Edad inválida, debe estar entre 1 y 120.")
        continue
    print("Edad válida:", edad)
    break
```

**Explicación:**
- `int(input(...))` → convierte lo ingresado a número entero.
- `if edad < 1 or edad > 120:` → detecta si la edad está fuera del rango permitido.
- `continue` → salta directo a la siguiente vuelta del bucle, sin ejecutar el resto del código de abajo (es decir, se salta el `print` y el `break` de las últimas dos líneas).
- Si la edad sí es válida, el `continue` nunca se ejecuta, entonces el código sigue con el `print` y el `break`, terminando el programa.

---

## Problema 4: Menú de salida
Muestra continuamente el siguiente menú.

```python
while True:
    print("1. Continuar")
    print("2. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "2":
        print("Saliendo del programa...")
        break
    else:
        print("Continuando...")
```

**Explicación:**
- Las dos líneas de `print` muestran el menú cada vez que el bucle se repite.
- `input(...)` → guarda la opción elegida por el usuario.
- `if opcion == "2":` → si elige "Salir" (opción 2), se ejecuta el `break` y el programa termina.
- `else:` → cualquier otra opción (incluida la 1) hace que el bucle continúe y el menú se vuelva a mostrar.

---

## Problema 5: Nombre obligatorio
Solicita el nombre del usuario.

```python
while True:
    nombre = input("Ingresa tu nombre: ")
    if nombre == "":
        print("El nombre no puede estar vacío, intenta de nuevo.")
        continue
    print("Hola,", nombre)
    break
```

**Explicación:**
- `if nombre == "":` → un string vacío ("") significa que el usuario no escribió nada y solo presionó Enter.
- `continue` → si está vacío, salta al inicio del bucle y vuelve a pedir el nombre, sin llegar al `print` final.
- Si el nombre no está vacío, el `continue` se salta, se ejecuta el saludo y luego el `break` termina el programa.

---

## Problema 6: Número par
Solicita un número entero.

```python
while True:
    numero = int(input("Ingresa un número entero: "))
    if numero % 2 == 0:
        print("Número par ingresado. Fin del programa.")
        break
    else:
        print("El número es impar, intenta otra vez.")
```

**Explicación:**
- `numero % 2 == 0` → si el resto de dividir por 2 es 0, el número es par.
- `break` → se ejecuta solo cuando el número es par, terminando el bucle.
- Si es impar, el `else` muestra el mensaje y el bucle continúa pidiendo otro número.

---

## Problema 7: Adivinar un número
El programa tiene un número secreto.

```python
numero_secreto = 7

while True:
    intento = int(input("Adivina el número secreto: "))
    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número.")
        break
    else:
        print("Incorrecto, intenta de nuevo.")
```

**Explicación:**
- `numero_secreto = 7` → variable fija que guarda el número que el usuario debe adivinar.
- `intento = int(input(...))` → guarda el número que el usuario propone.
- `if intento == numero_secreto:` → compara el intento con el número secreto.
- `break` → corta el bucle únicamente cuando acierta; si falla, el bucle se repite indefinidamente.

---

## Problema 8: Confirmación
Pregunta al usuario si desea continuar.

```python
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
```

**Explicación:**
- `.upper()` → convierte la respuesta a mayúsculas, así "s" y "S" se tratan igual.
- `if respuesta == "S":` → si quiere continuar, el `continue` fuerza que el bucle vuelva a preguntar de inmediato.
- `elif respuesta == "N":` → si quiere salir, el `break` termina el programa.
- `else:` → cualquier otra respuesta (que no sea "S" ni "N") cae aquí, muestra el aviso, y como no hay `break` ni `continue` explícito, el bucle simplemente vuelve a empezar de forma natural.

---

## Problema 9: Múltiplo de 5
Solicita un número.

```python
while True:
    numero = int(input("Ingresa un número: "))
    if numero % 5 == 0:
        print("Es múltiplo de 5. Fin del programa.")
        break
    else:
        print("No es múltiplo de 5, intenta otra vez.")
```

**Explicación:**
- `numero % 5 == 0` → si el resto de dividir el número por 5 es 0, entonces es múltiplo de 5.
- `break` → detiene el bucle solo cuando se cumple esa condición.
- Si no es múltiplo, se muestra el mensaje y el `while True` vuelve a pedir otro número.

---

## Problema 10: Nota aprobatoria
Solicita una nota.

```python
while True:
    nota = float(input("Ingresa una nota: "))
    if nota >= 4.0:
        print("Nota aprobatoria. Fin del programa.")
        break
    else:
        print("Nota insuficiente, intenta con otra.")
```

**Explicación:**
- `float(input(...))` → permite ingresar notas con decimales, como 4.5 o 5.8.
- `if nota >= 4.0:` → verifica si la nota alcanza o supera el mínimo de aprobación.
- `break` → termina el programa apenas se ingresa una nota aprobatoria.
- Si la nota es menor a 4.0, el bucle sigue pidiendo otra.

---

## Problema 11: Correo electrónico
Solicita un correo electrónico.

```python
while True:
    correo = input("Ingresa tu correo electrónico: ")
    if "@" not in correo:
        print("Correo inválido, debe contener '@'.")
        continue
    print("Correo válido:", correo)
    break
```

**Explicación:**
- `if "@" not in correo:` → revisa si el carácter "@" NO está presente en el texto ingresado.
- `continue` → si falta el "@", se salta el resto del código y vuelve a pedir el correo desde el inicio del bucle.
- Si el correo sí contiene "@", el `continue` no se ejecuta, entonces sigue con el `print` de confirmación y el `break` que termina el programa.