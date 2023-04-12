# 19. Dada una lista de números enteros, crea un algoritmo que elimine los números duplicados de la lista.
def principal():
    num = "a"
    lista = list()
    while len(num)>0:
        print("Introduzca un nuevo número entero. Enter para terminar.")
        num = input()
        try:
            num = int(num)
        except:
            if num != "":
                print("Entrada inválida")
                continue
        num = str(num)
        if len(num)>0:
            if num not in lista:
                lista.append(num)
    print(lista)
