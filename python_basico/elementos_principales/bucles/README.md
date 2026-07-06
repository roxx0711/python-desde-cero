🏠 [Volver al inicio](../../README.md)


# 🔄 ¿Qué son los bucles?

Los **bucles** (también llamados **ciclos** o **iteraciones**) son estructuras de control que permiten **repetir un bloque de código varias veces de forma automática**.

Su principal objetivo es evitar escribir el mismo código repetidamente. En lugar de copiar las mismas instrucciones una y otra vez, un bucle las ejecuta las veces que sean necesarias.

Un bucle puede repetirse:

- ✅ Un número determinado de veces.
- ✅ Hasta que se cumpla una condición.
- ✅ Recorriendo los elementos de una colección, como una lista o una cadena de texto.

---

## 🤔 ¿Por qué existen?

Imagina que quieres imprimir un mensaje **100 veces**.

Sin un bucle tendrías que escribir:

```python
print("Hola")
print("Hola")
print("Hola")
...
```

Con un bucle basta con unas pocas líneas:

```python
for i in range(100):
    print("Hola")
```

Esto hace que el código sea más corto, organizado y fácil de mantener.

---

# 📌 Tipos de bucles en Python

Python tiene dos tipos principales de bucles:

- `for`
- `while`

---

# 🔁 `for`

La palabra **`for`** significa **"para"** en inglés.

Se utiliza cuando **se conoce la cantidad de repeticiones** o cuando se desea recorrer todos los elementos de una colección, como una lista, una tupla, un conjunto, un diccionario o una cadena de texto.

## ¿Cuándo se utiliza?

- Recorrer listas.
- Leer una cadena de texto.
- Repetir una acción un número específico de veces.
- Procesar colecciones de datos.

### Sintaxis

```python
for variable in coleccion:
    # Código a repetir
```

---

## Ejemplo

```python
frutas = ["Manzana", "Banana", "Cereza"]

for fruta in frutas:
    print(fruta)
```

### Explicación

- Se crea una lista llamada **frutas**.
- El bucle **for** toma un elemento de la lista en cada repetición.
- Ese elemento se guarda en la variable **fruta**.
- Finalmente, se imprime en pantalla.

**Salida:**

```python
Manzana
Banana
Cereza
```

---

## Otro ejemplo usando `range()`

La función `range()` genera una secuencia de números.

```python
for numero in range(1, 6):
    print(numero)
```

**Salida:**

```python
1
2
3
4
5
```

---

# 🔄 `while`

La palabra **`while`** significa **"mientras"** en inglés.

Se utiliza cuando **no se conoce cuántas veces se repetirá el código**, ya que el bucle continuará ejecutándose mientras una condición sea verdadera (`True`).

Cuando la condición se vuelve falsa (`False`), el bucle termina automáticamente.

## ¿Cuándo se utiliza?

- Esperar una respuesta del usuario.
- Contadores.
- Menús interactivos.
- Juegos.
- Procesos que dependen de una condición.

### Sintaxis

```python
while condicion:
    # Código a repetir
```

---

## Ejemplo

```python
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
```

### Explicación

- Se crea la variable **contador** con el valor `1`.
- Python verifica si `contador <= 5`.
- Mientras la condición sea verdadera, imprime el número.
- Después aumenta el contador en uno con `contador += 1`.
- Cuando el contador llega a `6`, la condición deja de cumplirse y el bucle termina.

**Salida:**

```python
1
2
3
4
5
```

---

# 📊 Diferencias entre `for` y `while`

| `for` | `while` |
|-------|---------|
| Se utiliza cuando se conoce la cantidad de repeticiones o se recorre una colección. | Se utiliza cuando la cantidad de repeticiones depende de una condición. |
| Recorre automáticamente los elementos de una colección. | La condición debe actualizarse manualmente para evitar un ciclo infinito. |
| Es más sencillo para recorrer listas, cadenas o rangos. | Es más flexible cuando no se sabe cuándo terminará el proceso. |

---

## ⚠️ Cuidado con los bucles infinitos

Un **bucle infinito** ocurre cuando la condición de un `while` **nunca deja de ser verdadera**, por lo que el programa continúa ejecutándose sin detenerse.

### Ejemplo

```python
contador = 1

while contador > 0:
    print(contador)
```

En este caso, el valor de `contador` nunca cambia, por lo que la condición siempre será verdadera y el programa nunca terminará.

