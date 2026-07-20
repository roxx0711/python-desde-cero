# Ejercicios de práctica: Iterando distintos tipos de datos

## Problema 1: Recorrer una palabra
Desarrolla un programa que recorra una palabra letra por letra e imprima cada carácter en una línea diferente.

```python
palabra = "python"
for letra in palabra:
    print(letra)
```

**Explicación:**
- `palabra = "python"` → guarda el string en una variable.
- `for letra in palabra:` → un string es iterable, así que el for va tomando cada carácter uno por uno y lo asigna a `letra`.
- `print(letra)` → imprime el carácter actual, y como está dentro del for, se repite en cada vuelta (una letra por línea).

---

## Problema 2: Contar vocales
Recorre una cadena de texto y muestra cuántas vocales contiene.

```python
texto = "Programacion en Python"
vocales = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vocales:
        contador += 1

print("Cantidad de vocales:", contador)
```

**Explicación:**
- `vocales = "aeiouAEIOU"` → string con todas las vocales (mayúsculas y minúsculas) para comparar.
- `contador = 0` → variable acumuladora, arranca en 0.
- `for letra in texto:` → recorre cada carácter del texto.
- `if letra in vocales:` → pregunta si esa letra está dentro del string `vocales`.
- `contador += 1` → si es vocal, suma 1 al contador (equivale a `contador = contador + 1`).
- `print(...)` → al terminar el for, muestra el total acumulado.

---

## Problema 3: Mostrar nombres
Dada una lista de nombres, muestra cada nombre en una línea distinta.

```python
nombres = ["Ana", "Luis", "Marta", "Pedro"]

for nombre in nombres:
    print(nombre)
```

**Explicación:**
- `nombres = [...]` → lista con los nombres.
- `for nombre in nombres:` → recorre la lista elemento por elemento.
- `print(nombre)` → imprime el nombre actual en cada iteración.

---

## Problema 4: Sumar números
Recorre una lista de números y calcula la suma total de todos sus elementos.

```python
numeros = [10, 5, 8, 20, 3]
suma = 0

for numero in numeros:
    suma += numero

print("La suma total es:", suma)
```

**Explicación:**
- `suma = 0` → acumulador inicial.
- `for numero in numeros:` → recorre cada número de la lista.
- `suma += numero` → va sumando cada número al acumulador.
- `print(...)` → muestra el resultado final después del for.

---

## Problema 5: Encontrar el número mayor
Recorre una lista de números e identifica cuál es el número más grande.

```python
numeros = [10, 45, 3, 67, 22]
mayor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

print("El número mayor es:", mayor)
```

**Explicación:**
- `mayor = numeros[0]` → se asume que el primer elemento es el mayor, como punto de partida.
- `for numero in numeros:` → recorre toda la lista.
- `if numero > mayor:` → compara el número actual con el mayor guardado hasta el momento.
- `mayor = numero` → si el actual es más grande, se actualiza la variable `mayor`.
- Al final, `mayor` contiene el número más grande de la lista.

---

## Problema 6: Contar números pares
Recorre una lista de números e indica cuántos de ellos son pares.

```python
numeros = [3, 8, 12, 7, 5, 20]
contador = 0

for numero in numeros:
    if numero % 2 == 0:
        contador += 1

print("Cantidad de números pares:", contador)
```

**Explicación:**
- `numero % 2 == 0` → el operador `%` devuelve el resto de la división. Si el resto al dividir por 2 es 0, el número es par.
- El resto de la lógica es igual al problema 2: se recorre, se pregunta la condición, y si se cumple se suma 1 al contador.

---

## Problema 7: Mostrar una tupla
Dada una tupla con los meses del año, muestra cada mes en una línea distinta.

```python
meses = ("Enero", "Febrero", "Marzo", "Abril")

for mes in meses:
    print(mes)
```

**Explicación:**
- `meses = (...)` → los paréntesis definen una tupla (parecida a una lista, pero inmutable, no se puede modificar después de creada).
- `for mes in meses:` → las tuplas también son iterables, así que se recorren igual que una lista.
- `print(mes)` → muestra cada mes en su propia línea.

---

## Problema 8: Recorrer un conjunto
Dado un conjunto de colores, muestra cada color en pantalla.

```python
colores = {"rojo", "verde", "azul"}

for color in colores:
    print(color)
```

**Explicación:**
- `colores = {...}` → las llaves sin `:` definen un **set** (conjunto), que no permite elementos repetidos y **no tiene un orden garantizado**.
- `for color in colores:` → recorre cada elemento del conjunto.
- Nota: como el set no tiene orden, el orden en que se imprimen los colores puede variar de una ejecución a otra.

---

## Problema 9: Mostrar claves y valores de un diccionario
Dado un diccionario con información de un estudiante (nombre, edad y carrera), recorre el diccionario mostrando cada clave junto con su valor correspondiente.

```python
estudiante = {
    "nombre": "Alfonso",
    "edad": 22,
    "carrera": "Analista Programador"
}

for clave, valor in estudiante.items():
    print(clave, ":", valor)
```

**Explicación:**
- `estudiante = {...}` → diccionario con pares clave-valor.
- `.items()` → método que devuelve cada par (clave, valor) del diccionario, para poder recorrerlos juntos.
- `for clave, valor in estudiante.items():` → en cada vuelta, `clave` toma el nombre del campo (ej. "nombre") y `valor` toma su contenido (ej. "Alfonso").
- `print(clave, ":", valor)` → imprime ambos datos juntos, separados por ":".

---

## Problema 10: Contar una letra específica
Recorre una palabra e indica cuántas veces aparece una letra ingresada por el usuario.

```python
palabra = "programacion"
letra_buscada = input("Ingresa una letra a buscar: ")
contador = 0

for letra in palabra:
    if letra == letra_buscada:
        contador += 1

print(f"La letra '{letra_buscada}' aparece {contador} veces")
```

**Explicación:**
- `input(...)` → pide al usuario que escriba una letra y la guarda como texto en `letra_buscada`.
- `for letra in palabra:` → recorre la palabra letra por letra.
- `if letra == letra_buscada:` → compara si la letra actual es igual a la que buscó el usuario.
- `contador += 1` → si coincide, suma 1.
- `f"...{...}..."` → es un f-string, permite insertar el valor de variables directamente dentro del texto.

