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

def calculadora_completa():
  print("Calculadora Simple (Suma, Resta, Multiplicación, División)")
  try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    opcion = input("¿Sumar, Restar, Multiplicar o Dividir? (s/r/m/d): ")
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