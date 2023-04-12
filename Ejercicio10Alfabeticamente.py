def principal():
    getInputUser = ""
    listaName = []

    def startProgram(getInputUser):
        #global getInputUser
        
        while getInputUser == "":
            getInputUser = input("Introduce nombres: ")
            listaName.append(getInputUser)
            finish=input("¿Desea finalizar el programa? s/n: ")
            if finish== "s":
                listaName.sort()
                print(listaName)
            else:
                getInputUser = ""

    startProgram(getInputUser)
<<<<<<< HEAD:ejercicio10Alfabeticamente.py
    
    #Cambios
=======
>>>>>>> cae8088f6189167fc80b2a1118926214a7b2739d:Ejercicio10Alfabeticamente.py
