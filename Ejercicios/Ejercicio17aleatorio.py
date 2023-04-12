# 17. Crea un algoritmo que genere un número aleatorio entre 1 y 100, y le pida al usuario adivinarlo. El algoritmo deberá indicar si el número introducido es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto.
def principal():
    import random
    x = 0
    y = 0
    nalea = random.randint(1,100)
    while y == 0:
        print("Inroduce un nuevo número entero entre el 1 y el 100")
        numero = input()
        try:
            numero = int(numero)
            y = 1
        except:
            print("Entrada inválida.")
            continue
    while x == 0:
        if numero > nalea:
            print("El número introducido es mayor")
            y = 0
            while y == 0:
                print("Inroduce un nuevo número entero entre el 1 y el 100")
                numero = input()
                try:
                    numero = int(numero)
                    y = 1
                except:
                    print("Entrada inválida.")
                    continue
        elif numero < nalea:
            print("El número introducido es menor")
            y = 0
            while y == 0:
                print("Inroduce un nuevo número entero entre el 1 y el 100")
                numero = input()
                try:
                    numero = int(numero)
                    y = 1
                except:
                    print("Entrada inválida.")
                    continue
        else:
            x = 1
            print("¡Felicidades!, Has acertado el número")
