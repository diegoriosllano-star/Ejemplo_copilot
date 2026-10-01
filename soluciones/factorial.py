'''
Planteamiento del problema:
Calcular una aproximación de n! utilizando la expresión:

n! ≈ sqrt(2*pi) * e^(-n) * n^(n + 1/2)

El valor de n deberá ser introducido por el usuario.
'''

# PROBLEMA: calcular una aproximación del factorial de n

# ENTRADA:
# n

# SALIDA:
# n_factorial

# ALGORITMO
# 1. Leer el valor de n
# 2. Calcular sqrt(2*pi)
# 3. Calcular e elevado a -n
# 4. Calcular n elevado a (n + 1/2)
# 5. Multiplicar los tres resultados anteriores
# 6. Guardar el resultado en n_factorial
# 7. Mostrar el resultado


# CONTRATO DE FUNCIONES

# leerN()
# Entrada: ninguna
# Salida: n
# Responsabilidad: pedir al usuario el valor de n
# No debe: realizar cálculos ni mostrar el resultado final


# calcularFactorial(n)
# Entrada: n
# Salida: n_factorial
# Responsabilidad: calcular la aproximación de n! usando la fórmula indicada
# No debe: pedir datos al usuario ni mostrar resultados


# mostrarFactorial(n_factorial)
# Entrada: n_factorial
# Salida: ninguna
# Responsabilidad: mostrar el resultado aproximado del factorial
# No debe: pedir datos ni realizar cálculos


# CASOS DE PRUEBA

# Caso 1
# Entrada: n = 5
# Resultado esperado: n_factorial ≈ 118.019168

def leerN():
    n = int(input("Ingrese el valor de n: "))
    return n

def calcularFactorial(n):
    import math
    n_factorial = math.sqrt(2 * math.pi) * math.exp(-n) * (n ** (n + 0.5))
    return n_factorial

def mostrarFactorial(n_factorial):
    print(f"La aproximación de n! es: {n_factorial}")
    