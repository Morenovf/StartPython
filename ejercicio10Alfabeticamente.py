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
    
    #Cambios