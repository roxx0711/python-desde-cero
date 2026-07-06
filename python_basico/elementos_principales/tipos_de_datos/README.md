# 📊 Tipos de datos en Python

Los **tipos de datos** son una característica fundamental de Python, ya que permiten clasificar la información que se almacena en una variable. Cada tipo de dato representa una forma diferente de guardar información, como números, texto o valores lógicos, y define qué operaciones pueden realizarse con ella.

Gracias a los tipos de datos, Python puede interpretar correctamente el contenido de una variable y evitar errores al ejecutar un programa.

---

## 🔢 `int` (Integer)

El nombre **´int´** proviene de la palabra inglesa **Integer**, que significa **número entero**.

Se utiliza para representar números que **no tienen parte decimal**, ya sean positivos, negativos o cero.

### ¿Cuándo se utiliza?
- Contadores.
- Edad de una persona.
- Cantidad de objetos.
- Identificadores numéricos.

### Ejemplo

```python
edad = 20
cantidad = 150
temperatura = -5
```

---

## 🔹 `float` (Floating Point)

El nombre **`float`** proviene de **Floating Point Number** (número de punto flotante).

Se llama así porque el punto decimal puede "flotar", permitiendo representar números con decimales.

### ¿Cuándo se utiliza?
- Altura.
- Peso.
- Precios.
- Promedios.
- Mediciones.

### Ejemplo

```python
precio = 19.99
pi = 3.1416
altura = 1.75
```

---

## 📝 `str` (String)

El nombre **`str`** proviene de **String**, que significa **cadena de caracteres**.

Se utiliza para almacenar texto. Una cadena puede contener letras, números, símbolos y espacios.

Siempre debe escribirse entre comillas simples (`' '`) o dobles (`" "`).

### ¿Cuándo se utiliza?
- Nombres.
- Direcciones.
- Correos electrónicos.
- Mensajes.
- Contraseñas.

### Ejemplo

```python
nombre = "Alfonso"
mensaje = "Bienvenido al sistema"
```

---

## ✅ `bool` (Boolean)

El nombre **`bool`** proviene de **Boolean**, en honor al matemático **George Boole**, creador del álgebra booleana.

Solo puede almacenar dos valores:

- `True` → Verdadero
- `False` → Falso

Se utiliza principalmente para tomar decisiones dentro del programa.

### ¿Cuándo se utiliza?
- Verificar si un usuario inició sesión.
- Saber si un dato existe.
- Validar condiciones.

### Ejemplo

```python
es_mayor = True
tiene_permiso = False
```

---

## 📋 `list` (Lista)

El nombre **`list`** significa simplemente **lista**.

Es una colección **ordenada y modificable** de elementos.

Puede almacenar diferentes tipos de datos al mismo tiempo.

### Características

- ✅ Ordenada.
- ✅ Permite elementos repetidos.
- ✅ Se puede modificar (agregar, eliminar o cambiar elementos).

### ¿Cuándo se utiliza?

- Lista de alumnos.
- Productos.
- Notas.
- Tareas.

### Ejemplo

```python
frutas = ["Manzana", "Pera", "Naranja"]

frutas.append("Uva")
```

---

## 📦 `tuple` (Tupla)

El nombre **`tuple`** significa **tupla**.

Es muy parecida a una lista, pero tiene una diferencia importante:

**No puede modificarse una vez creada.**

### Características

- ✅ Ordenada.
- ✅ Permite repetidos.
- ❌ No se puede modificar.

### ¿Cuándo se utiliza?

Cuando los datos nunca deben cambiar.

Por ejemplo:

- Coordenadas.
- Fechas.
- Configuraciones.

### Ejemplo

```python
coordenadas = (10, 25)

# coordenadas[0] = 15 ❌ Produce error
```

---

## 🎯 `set` (Conjunto)

El nombre **`set`** significa **conjunto**, igual que en matemáticas.

Almacena elementos **únicos**, por lo que elimina automáticamente los repetidos.

### Características

- ❌ No mantiene un orden específico.
- ❌ No admite elementos repetidos.
- ✅ Muy rápido para buscar datos.

### ¿Cuándo se utiliza?

- Eliminar duplicados.
- Comparar grupos de datos.
- Verificar si un elemento existe.

### Ejemplo

```python
numeros = {1, 2, 3, 3, 2, 1}

print(numeros)
# {1, 2, 3}
```

---

## 📚 `dict` (Dictionary)

El nombre **`dict`** proviene de **Dictionary** (diccionario).

Guarda la información mediante **pares clave : valor**.

Es similar a un diccionario real, donde una palabra (clave) tiene una definición (valor).

### Características

- Cada clave debe ser única.
- Los valores pueden repetirse.
- Permite acceder rápidamente a la información.

### ¿Cuándo se utiliza?

- Información de usuarios.
- Configuraciones.
- Bases de datos simples.
- Datos organizados.

### Ejemplo

```python
persona = {
    "nombre": "Ana",
    "edad": 20,
    "ciudad": "Santiago"
}

print(persona["nombre"])
```

---

# 📌 Resumen de los tipos de datos

| Tipo | Significado | ¿Qué almacena? | Ejemplo |
|------|-------------|----------------|----------|
| `int` | Integer | Números enteros | `25` |
| `float` | Floating Point | Números decimales | `3.14` |
| `str` | String | Texto | `"Hola"` |
| `bool` | Boolean | Verdadero o Falso | `True` |
| `list` | Lista | Colección modificable | `[1,2,3]` |
| `tuple` | Tupla | Colección no modificable | `(1,2,3)` |
| `set` | Conjunto | Elementos únicos | `{1,2,3}` |
| `dict` | Dictionary | Clave - Valor | `{"nombre":"Ana"}` |

---

# 🏷️ Reforzamiento de tipado de datos (Type Hints)

Python es un lenguaje de **tipado dinámico**, lo que significa que normalmente **no es obligatorio indicar el tipo de una variable**, ya que Python lo detecta automáticamente.

Sin embargo, desde **Python 3.5** existe una característica llamada **Type Hints** o **anotaciones de tipos**, que permite indicar qué tipo de dato se espera en una variable, parámetro o valor de retorno de una función.

> **Importante:** estas anotaciones **no obligan** a Python a cumplir el tipo durante la ejecución. Su objetivo es hacer el código más claro, facilitar el mantenimiento y ayudar a herramientas como VS Code, PyCharm o analizadores estáticos a detectar posibles errores antes de ejecutar el programa.

---

## 📍 Tipado en variables

Se puede indicar el tipo esperado usando `:`.

```python
nombre: str = "Alfonso"
edad: int = 20
altura: float = 1.75
activo: bool = True
```

Esto facilita que cualquier persona entienda qué tipo de dato debería contener cada variable.

---

## 📍 Tipado en funciones

También se pueden especificar los tipos de los parámetros y el tipo que devuelve una función.

```python
def sumar(a: int, b: int) -> int:
    resultado: int = a + b
    return resultado
```

### ¿Qué significa?

- `a: int` → el parámetro `a` debe ser un entero.
- `b: int` → el parámetro `b` debe ser un entero.
- `-> int` → la función devolverá un número entero.
- `resultado: int` → la variable `resultado` debería contener un entero.

---

## ✅ Ventajas del tipado

- 📖 Hace el código más fácil de leer.
- 🤝 Facilita el trabajo en equipo.
- 🐞 Ayuda a detectar errores antes de ejecutar el programa.
- 🛠️ Mejora el autocompletado y las sugerencias del editor.
- 📚 Sirve como documentación del código.

---

## 💡 Ejemplo completo

```python
nombre: str = "Alfonso"
edad: int = 20

def sumar(arg1: int, arg2: int) -> int:
    resultado: int = arg1 + arg2
    return resultado

total = sumar(10, 15)

print(nombre)
print(edad)
print(total)
```
