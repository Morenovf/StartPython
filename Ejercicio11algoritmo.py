# 11. Crea un algoritmo que calcule el factorial de un número entero.
def principal():
    print("Introduzca un número entero:")
    numero = input()
    numero = int(numero)
    i = 1
    factorial=1
    while i <=numero:
        factorial *=  i
        i += 1
    print("El factorial de", numero, "es", factorial)