def principal():
    num1 = input("Escribe el primer numero: ")
    num2 = input("Escribe el segundo numero: ")
    num3 = input("Escribe el tercero numero: ")
    num4 = input("Escribe el cuarto numero: ")
    num5 = input("Escribe el quinto numero: ")

    arrayNum = [num1, num2, num3, num4, num5]

    valido = False

    while valido == False:
        for i in range(5):
            if arrayNum[i].isdigit():
                arrayNum[i] = int(arrayNum[i])
            else:
                arrayNum[i] = input(str(arrayNum[i]) + " no es un numero. Escribe un numero correcto: ")
        valido = True
    numeroMayor = arrayNum[0]
    numeroMenor = arrayNum[0]
    print("Tus numeros son: " + str(arrayNum))

    for i in range(len(arrayNum)):
        if numeroMayor <= arrayNum[i]:
            numeroMayor = arrayNum[i]

    print("El mayor numero de la lista es:  " + str(numeroMayor))

    for i in range(len(arrayNum)):
        if numeroMenor >= arrayNum[i]:
            numeroMenor = arrayNum[i]

    print("El menor numero de la lista es:  " + str(numeroMenor))