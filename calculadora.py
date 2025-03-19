import math

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    if num2 == 0:
        return "Error: División por cero"
    return num1 / num2

def raiz_cuadrada(num):
    if num < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo"
    return math.sqrt(num)

def calculadora_completa():
    print("Calculadora Simple (Suma, Resta, Multiplicación, División, Raíz Cuadrada)")
    try:
        opcion = input("¿Sumar, Restar, Multiplicar, Dividir o Raíz Cuadrada? (s/r/m/d/rc): ")
        
        if opcion.lower() == 'rc':
            num = float(input("Ingresa el número para calcular la raíz cuadrada: "))
            print("Resultado:", raiz_cuadrada(num))
        else:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            
            if opcion.lower() == 's':
                print("Resultado:", sumar(num1, num2))
            elif opcion.lower() == 'r':
                print("Resultado:", restar(num1, num2))
            elif opcion.lower() == 'm':
                print("Resultado:", multiplicar(num1, num2))
            elif opcion.lower() == 'd':
                print("Resultado:", dividir(num1, num2))
            else:
                print("Opción inválida.")
    except ValueError:
        print("Entrada inválida. Ingresa números válidos.")

calculadora_completa()