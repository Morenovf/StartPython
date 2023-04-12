import os
import sys
#from Varios import principal

from Ejercicios import Ejercicio1DNI
from Ejercicios import Ejercicio2Salario
from Ejercicios import Ejercicio3vuelos
from Ejercicios import Ejercicio4Radio
from Ejercicios import Ejercicio5MayorMenor
from Ejercicios import Ejercicio6Celsius
from Ejercicios import Ejercicio7Par
from Ejercicios import Ejercicio8Bisiesto
from Ejercicios import Ejercicio9Palindroma
from Ejercicios import Ejercicio10Alfabeticamente
from Ejercicios import Ejercicio11algoritmo
from Ejercicios import Ejercicio12primo
from Ejercicios import Ejercicio13cubo
from Ejercicios import Ejercicio14sumapares
from Ejercicios import Ejercicio15posnegcero
from Ejercicios import Ejercicio16media
from Ejercicios import Ejercicio17aleatorio
from Ejercicios import Ejercicio18anagrama
from Ejercicios import Ejercicio19sinduplicados
from Ejercicios import Ejercicio20capicua

while True:
    if sys.platform.startswith("linux"):
        # linux
        os.system('clear') 
    elif sys.platform == "darwin":
        # MAX OS X
        os.system('clear') 
    elif os.name == "nt":
        #Windows, Cigwyin, etc. (32/64-bit)
        os.system('cls') 
    # os.system("cls") #Limpia la pantalla en la consola
    # os.system("clear") #Limpia pantalla consola MAC y Linux
    
    print("Bienvenidos")
    print("Menu principal")

    print("1-Calcular letra DNI español")
    print("2-Calcular Salario Neto Español")
    print("3-Determinar ruta para llegar por avion")
    print("4-Calcular çarea y perímetro de un círculo dado su radio")
    print("5-Calcular numero mayor y menor")
    print("6-Convertir grados Celsius a Fahrenheit")
    print("7-Determinar numero par o impar")
    print("8-Determinar si un año es bisiesto")
    print("9-Determinar si una cadena de texto es un palíndromo")
    print("10-Ordenar lista de nombres")
    print("11-Calcular Salario Neto Español")
    print("12-Determinar si un número es primo")
    print("13-Calcular área y volumen de un cubo dado su lado")
    print("14-Calcular suma de todos los numeros pares de una lista")
    print("15-Determinar si un número es positivo, negativo o cero")
    print("16-Calcular la media de a lista")
    print("17-Generar numero aleatorio entre 1 y 100 y pedir al usuario adivinarlo.")
    print("18-Determinar si cadena de texto es anagrama de otra cadena")
    print("19-Eliminar numeros duplicados de una lista")
    print("20-Determinar números capicuas")

    print("0-Salir")

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
