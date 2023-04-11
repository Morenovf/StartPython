try:
    celsius = float(input("Introduzca los grados celsius: "))
    
    fahrenheit = (celsius*1.8) + 32
    
    print(f"{celsius} grados celsius son {fahrenheit} grados fahrenheit")
    
except:
    print("Error, introduce un dato correcto")