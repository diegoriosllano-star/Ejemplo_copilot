'''
Planteamiento del problema:
Calcula el salario semanal de 
un trabajador. Las horas 
mayores a 40 se pagan al 
doble
'''

# PROBLEMA: calcular salario semanal
# ENTRADAS: horas_trabajadas, pago_por_hora
# SALIDA: salario_semanal
# ALGORITMO
# 1. Leer horas trabajadas
# 2. Leer pago por hora
# 3. Si horas <= 40:
#       salario = horas * pago
# 4. Si no:
#       extra = horas - 40
#       salario = (40 * pago) + (extra * pago * 2)
# 5. Mostrar salario

#contrato de funciones 
#leerdatos()
#Entrada: ninguna
#Salida: horas y pago
#Responsabilidad: pedir datos al usuario

#calcularSalario(horas, pago)
#Entrada: horas, pago
#Salida: salario 
#Responsabilidad:calcular, no imprimir

#mostrarSalario(salario)
#Entrada: salario
#Salida: ninguna
#Responsabilidad:mostrar resultado

#casos de prueba
# Caso 1: 45 horas a $10
#entrada: horas=45, pago=10
#salida: salario=450    

#Caso 2: 40 horas a $10
#entrada: horas=40, pago=10 
#salida: salario=400

#caso 3: 50 horas a $12
#entrada: horas=50, pago=12
#salida: salario=720

# Restricciones:
# - no imprimir dentro de la funcion de calcularSalario
# - devolver el resultado
# - no usar bibliotecas externas
# - no realices llamadas a funciones dentro de este archivo


def leerdatos():
    horas = float(input("Ingrese las horas trabajadas: "))
    pago = float(input("Ingrese el pago por hora: "))
    return horas, pago


def calcularSalario(horas, pago):
    if horas <= 40:
        salario = horas * pago
    else:
        extra = horas - 40
        salario = (40 * pago) + (extra * pago * 2)
    return salario


def mostrarSalario(salario):
    print(f"El salario semanal es: {salario}")