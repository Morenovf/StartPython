def principal():
    #Entrada
    año = int(input("Introduce el año para saber si es bisiesto: "))

    #Proceso
    if (año% 4 == 0) and (año%100 != 0):
        resultado = f"El año {año} es bisiesto"
    elif año%400 == 0:
        resultado = f"El año {año} es bisiesto"
    else:
        resultado = f"El año {año} no es bisiesto"
        
    #Salida
    print(resultado)
    
    #Cambios