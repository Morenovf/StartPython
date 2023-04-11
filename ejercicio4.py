def principal():
    import math

    radio = float(input("Introduce el radio del circulo: "))
    areaCirculo = radio ** 2 * math.pi
    perimetroCirculo = radio * 2 * math.pi

    print(f"El area del circulo es {areaCirculo} y el perimetro es {perimetroCirculo}")