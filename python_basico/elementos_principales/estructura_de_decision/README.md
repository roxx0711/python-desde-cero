# Estructura de decisión

Son instrucciones que permite que un programa tome decisiones evaluando una o varias condiciones. Dependiendo de si la condición es verdadera o falsa, el programa ejecutara un bloque de codigo u otro. Estas estructuera hacen que los programas sean dinamicos y acapaces de responder a diferentes siuaciones 

## Principales estructuras de decisión son:
>if

>if...else

>if...elif...else


### Ejemplo de if
edad = 18

if edad >= 18:
    print("Eres mayor de edad")


### Ejemplo de if...else
edad = 16

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")


### Ejemplo de if...elif...else
nota = 85

if nota >= 90:
    print("Excelente")
elif nota >= 70:
    print("Aprobado")
else:
    print("Reprobado")