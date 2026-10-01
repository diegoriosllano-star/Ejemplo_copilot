'''
Planteamiento del problema:
Calcular el valor de x utilizando la expresión:

x = sqrt(b - a^2) / c

Los valores de a, b y c deberán ser introducidos por el usuario.
'''

# PROBLEMA: calcular el valor de x mediante una expresión con raíz cuadrada

# ENTRADAS:
# a
# b
# c

# SALIDA:
# x

# ALGORITMO
# 1. Leer el valor de a
# 2. Leer el valor de b
# 3. Leer el valor de c
# 4. Calcular b - a^2
# 5. Calcular la raíz cuadrada del resultado anterior
# 6. Dividir el resultado entre c
# 7. Mostrar el valor de x


# CONTRATO DE FUNCIONES

# leerDatos()
# Entrada: ninguna
# Salida: a, b, c
# Responsabilidad: pedir al usuario los valores de a, b y c
# No debe: realizar cálculos ni mostrar el resultado final


# calcularX(a, b, c)
# Entrada: a, b, c
# Salida: x
# Responsabilidad: calcular x utilizando sqrt(b - a^2) / c
# No debe: pedir datos al usuario ni mostrar resultados


# mostrarResultado(x)
# Entrada: x
# Salida: ninguna
# Responsabilidad: mostrar el valor calculado de x
# No debe: pedir datos ni realizar cálculos


# CASOS DE PRUEBA

# Caso 1
# Entrada: a = 2, b = 20, c = 5
# Resultado esperado: x = 0.8

def leerDatos():
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    return a, b, c

def calcularX(a, b, c):
    import math
    x = math.sqrt(b - a**2) / c
    return x

def mostrarResultado(x):
    print(f"El valor de x es: {x}")
    