# 19. Dada una lista de números enteros, crea un algoritmo que elimine los números duplicados de la lista.
num = "a"
lista = list()
while len(num)>0:
    print("Introduzca un nuevo número entero:")
    num = input()
    if len(num)>0:
        if num not in lista:
            lista.append(num)
print(lista)
