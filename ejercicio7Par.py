def principal():
    #Entrada
    num = input("Introduce un numero: ")
    valido = False
    par = True

    #Proceso
    while valido == False:
        if num.isdigit():
            num = int(num)
            valido = True
            if num % 2 == 0:
                par = True
                #print(str(num) + " es numero par")
            else:
                par = False
            #print(str(num) + " es numero impar")
        else:
            num = input("Introduce un numero correcto: ")

    #Salida
    print("El numero es par", par)

