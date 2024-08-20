import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Sumar 2 números")
    print("2. Restar 2 números")
    print("3. Multiplicar 2 números")
    print("4. Dividir 2 números")
    print("5. Sumar N números")
    print("6. Salir")

def ejecutar_calculadora():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == '1':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", sumar.sumar(a, b))
        elif opcion == '2':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", resta.restar(a, b))
        elif opcion == '3':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            print("Resultado:", multiplicacion.multiplicar(a, b))
        elif opcion == '4':
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            try:
                print("Resultado:", dividir.dividir(a, b))
            except ValueError as e:
                print(e)
        elif opcion == '5':
            numeros = list(map(float, input("Ingrese los números separados por espacio: ").split()))
            print("Resultado:", suma_avanzada.suma_avanzada(*numeros))
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    ejecutar_calculadora()
