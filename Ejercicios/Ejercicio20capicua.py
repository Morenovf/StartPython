# 20. Crea un algoritmo que determine si un número es capicúa o no.
def principal():
    x = 0
    i = 0
    while x == 0:
        print("Introduzca un número entero:")
        num = input()
        if num.isdigit() and len(num)<=1:
            print("El número no es capicúa")
            break
        try:
            num = int(num)
            x = 1
        except:
            print("Entrada incorrecta")
            continue
    num = str(num)
    while i < len(num):
        if num[i]==num[-i-1]:
            i += 1
            continue
        else:
            print("El número no es capicúa")
            break
    if i == len(num) and len(num)>1:
        print("El número es capicúa")