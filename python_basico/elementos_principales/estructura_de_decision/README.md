# 🔀 Estructuras de decisión

Las **estructuras de decisión** son instrucciones que permiten que un programa **tome decisiones** evaluando una o varias condiciones.

Dependiendo de si una condición es **verdadera (`True`)** o **falsa (`False`)**, el programa ejecutará un bloque de código diferente.

Gracias a ellas, los programas pueden adaptarse a distintas situaciones y responder de forma dinámica según los datos que reciben.

---

## 🤔 ¿Por qué existen?

En la vida cotidiana tomamos decisiones constantemente.

Por ejemplo:

- Si está lloviendo, llevo paraguas.
- Si tengo hambre, como.
- Si termino mi tarea, puedo descansar.

En programación ocurre exactamente lo mismo. Un programa necesita decidir qué hacer según las condiciones que se presenten.

---

## 📌 Principales estructuras de decisión

- `if`
- `if...else`
- `if...elif...else`

---

# ✅ `if`

La palabra **`if`** significa **"si"** en inglés.

Se utiliza para ejecutar un bloque de código **solo si una condición es verdadera**.

Si la condición es falsa, simplemente no ejecuta ese bloque y continúa con el resto del programa.

### Sintaxis

```python
if condicion:
    # Código a ejecutar
```

### Ejemplo

```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
```

### Explicación

- Se crea la variable **edad** con el valor `18`.
- Python evalúa la condición `edad >= 18`.
- Como la condición es **True**, ejecuta el `print()`.

**Salida:**

```python
Eres mayor de edad
```

---

# 🔄 `if...else`

La palabra **`else`** significa **"si no"** o **"de lo contrario"**.

Se utiliza cuando queremos ejecutar un bloque de código si la condición es verdadera y otro diferente si es falsa.

### Sintaxis

```python
if condicion:
    # Código si la condición es verdadera
else:
    # Código si la condición es falsa
```

### Ejemplo

```python
edad = 16

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

### Explicación

- Python verifica si `16 >= 18`.
- La condición es **False**.
- Entonces ejecuta el bloque que está dentro de `else`.

**Salida:**

```python
Eres menor de edad
```

---

# 🔀 `if...elif...else`

La palabra **`elif`** significa **"else if"**, es decir, **"si no, entonces si..."**.

Se utiliza cuando existen **varias condiciones** posibles y el programa debe comprobarlas una por una hasta encontrar una que sea verdadera.

Si ninguna condición se cumple, se ejecuta el bloque `else`.

### Sintaxis

```python
if condicion1:
    # Código
elif condicion2:
    # Código
else:
    # Código
```

### Ejemplo

```python
nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")
```

### Explicación

Python evalúa las condiciones en orden:

1. ¿La nota es mayor o igual a **90**? ❌ No.
2. ¿La nota es mayor o igual a **70**? ✅ Sí.
3. Como encontró una condición verdadera, imprime **"Aprobado"** y deja de evaluar las demás.

**Salida:**

```python
Aprobado
```

---

# 📊 Comparación de las estructuras de decisión

| Estructura | ¿Cuándo se utiliza? |
|------------|---------------------|
| `if` | Cuando solo se necesita comprobar una condición. |
| `if...else` | Cuando existen dos posibles resultados: verdadero o falso. |
| `if...elif...else` | Cuando hay varias condiciones y diferentes resultados posibles. |

---

## 💡 Ejemplo práctico

```python
temperatura = 28

if temperatura >= 30:
    print("Hace mucho calor")
elif temperatura >= 20:
    print("El clima es agradable")
else:
    print("Hace frío")
```

**Salida:**

```python
El clima es agradable
```
