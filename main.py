import os
#from Varios import principal

import Ejercicio1DNI
import Ejercicio2Salarios
import Ejercicio3vuelos
import Ejercicio4Radio
import Ejercicio5MayorMenor
import Ejercicio6Celsius
import Ejercicio7Par
import Ejercicio8Bisiesto
import Ejercicio9Palindroma
import Ejercicio10Alfabeticamente
import Ejercicio11algoritmo
import Ejercicio12primo
import Ejercicio13cubo
import Ejercicio14sumapares
import Ejercicio15posnegcero
import Ejercicio16media
import Ejercicio17aleatorio
import Ejercicio18anagrama
import Ejercicio19sinduplicados
import Ejercicio20capicua

while True:
    os.system("cls") #Limpia la pantalla en la consola
    print("Bienvenidos")
    print("Menu principal")
    print("1-Calcular DNI")
    print("2-Calcular Salario Neto Español")
    print("3-Determinar ruta para llegar por avion")
    print("4-Calcular radio del círculo")
    (...)

    print("8-Año bisiesto")
    print("10-Ordenar una cadena")
    print("20-Determinar números capicuas")

    print("0 -Salir")

    opcion = input("Seleccione una opción:")

    if opcion == "1":
        Ejercicio1DNI.principal()
    elif opcion == "2":
        Ejercicio2Salario.principal()
    elif opcion == "3":
        Ejercicio3vuelos.principal()
    elif opcion == "4":
        Ejercicio4Radio.principal() 
    elif opcion == "5":
        Ejercicio5MayorMenor.principal() 
    elif opcion == "6":
        Ejercicio6Celsius.principal() 
    elif opcion == "7":
        Ejercicio7Par.principal()
    elif opcion == "8":
        Ejercicio8Bisiesto.principal()     
    elif opcion == "9":
        Ejercicio9Palindroma.principal() 
    elif opcion == "10":
        Ejercicio10Alfabeticamente.principal() 
    elif opcion == "11":
        Ejercicio11algoritmo.principal() 
    elif opcion == "12":
        Ejercicio12primo.principal() 
    elif opcion == "13":
        Ejercicio13cubo.principal() 
    elif opcion == "14":
        Ejercicio14sumapares.principal() 
    elif opcion == "15":
        Ejercicio15posnegcero.principal()
    elif opcion == "16":
        Ejercicio16media.principal() 
    elif opcion == "17":
        Ejercicio17aleatorio.principal()
    elif opcion == "18":
        Ejercicio18anagrama.principal()
    elif opcion == "19":
        Ejercicio19sinduplicados.principal()       
    elif opcion == "20":
        Ejercicio20capicua.principal()     

    elif opcion == "0":
        print("Un placer atenderle. Chao!")
        break

    continuar=input("Presione enter para continuar...")
