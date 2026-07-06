# ⚙️ Funciones en Python

Las **funciones** son bloques de código reutilizables que realizan una tarea específica. Su principal objetivo es **evitar repetir código**, haciendo que los programas sean más organizados, fáciles de leer y sencillos de mantener.

En lugar de escribir el mismo conjunto de instrucciones varias veces, una función permite escribirlas una sola vez y ejecutarlas cada vez que sea necesario.

---

## 📌 ¿Por qué se llaman funciones?

El término **función** proviene de las matemáticas, donde una función recibe uno o varios valores de entrada, realiza un proceso y devuelve un resultado.

Python adopta este mismo concepto:

**Entrada → Proceso → Salida**

Por ejemplo:

- Recibe dos números.
- Los suma.
- Devuelve el resultado.

---

## 🎯 ¿Para qué sirven?

Las funciones permiten:

- ✅ Reutilizar código.
- ✅ Evitar escribir las mismas instrucciones varias veces.
- ✅ Dividir un programa grande en partes más pequeñas.
- ✅ Facilitar la lectura y comprensión del código.
- ✅ Hacer más sencillo el mantenimiento del programa.

---

## 📝 Sintaxis básica

```python
def nombre_funcion(parametros):
    # Código de la función
    return resultado
```

### Partes de una función

- **`def`** → Palabra reservada que indica que se va a crear una función.
- **`nombre_funcion`** → Nombre que identifica a la función.
- **`(parámetros)`** → Datos que la función recibe para trabajar (opcional).
- **`:`** → Indica el inicio del bloque de código.
- **`return`** → Devuelve un resultado al lugar donde fue llamada la función (opcional).

---

## 💻 Ejemplo

```python
def sumar(a, b):
    return a + b

resultado = sumar(10, 5)

print("La suma es:", resultado)
```

### Explicación paso a paso

```python
def sumar(a, b):
```

- **`def`** crea una nueva función.
- **`sumar`** es el nombre de la función.
- **`a`** y **`b`** son los **parámetros**, es decir, los datos que recibirá la función.

---

```python
return a + b
```

- **`return`** devuelve el resultado de la suma.
- Cuando la función termina, ese valor regresa al lugar donde fue llamada.

---

```python
resultado = sumar(10, 5)
```

Aquí ocurre lo siguiente:

- Se llama a la función **`sumar()`**.
- Se envían los valores **10** y **5**.
- Esos valores se almacenan en los parámetros **a** y **b**.
- La función realiza la suma.
- Devuelve **15**.
- Ese resultado se guarda en la variable **resultado**.

---

```python
print("La suma es:", resultado)
```

Finalmente, **`print()`** muestra el resultado en la consola.

**Salida:**

```python
La suma es: 15
```

---

# 📌 Parámetros y argumentos

Aunque muchas personas los usan como sinónimos, tienen una pequeña diferencia.

### Parámetros

Son las variables que aparecen al definir la función.

```python
def saludar(nombre):
    print("Hola", nombre)
```

Aquí, **`nombre`** es un **parámetro**.

---

### Argumentos

Son los valores reales que se envían cuando se llama a la función.

```python
saludar("Alfonso")
```

Aquí, **`"Alfonso"`** es un **argumento**.

---

# 💡 Ejemplo práctico

```python
def multiplicar(numero1, numero2):
    return numero1 * numero2

resultado = multiplicar(8, 4)

print(resultado)
```

**Salida:**

```python
32
```

En este ejemplo:

- La función recibe dos números.
- Los multiplica.
- Devuelve el resultado.
- Finalmente, se imprime en pantalla.

---

## ⭐ En resumen

Las funciones son una de las herramientas más importantes de Python, ya que permiten organizar el código, reutilizar instrucciones y desarrollar programas más limpios, claros y fáciles de mantener.



🏠 [Inicio](../../../README.md)
