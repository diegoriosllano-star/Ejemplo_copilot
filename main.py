from soluciones.salario_semanal import leerdatos, calcularSalario, mostrarSalario

def main():
    horas, pago = leerdatos()
    salario = calcularSalario(horas, pago)
    mostrarSalario(salario)

if __name__ == "__main__":
    main()