from soluciones.salario_semanal import leerdatos, calcularSalario, mostrarSalario
from soluciones.expresion_raiz import leerDatos, calcularX, mostrarResultado
from soluciones.factorial import leerN, calcularFactorial, mostrarFactorial


def main():
    while True:
        print("\nMENÚ DE OPCIONES")
        print("1. Calcular salario semanal")
        print("2. Calcular expresión con raíz")
        print("3. Calcular aproximación de factorial")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            horas, pago = leerdatos()
            salario = calcularSalario(horas, pago)
            mostrarSalario(salario)

        elif opcion == "2":
            a, b, c = leerDatos()
            x = calcularX(a, b, c)
            mostrarResultado(x)

        elif opcion == "3":
            n = leerN()
            n_factorial = calcularFactorial(n)
            mostrarFactorial(n_factorial)

        elif opcion == "4":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()