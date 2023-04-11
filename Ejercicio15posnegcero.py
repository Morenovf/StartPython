# 15. Crea un algoritmo que determine si un número es positivo, negativo o cero.
def principal():
    print("Introduzca un número:")
    numero = input()
    numero = float(numero)
    if numero > 0:
        print("El número introducido es positivo")
    elif numero < 0:
        print("El número introducido es negativo")
    else:
        print("El número introducido es cero")