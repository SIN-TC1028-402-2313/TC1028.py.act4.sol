import math

def main():
    #escribe tu código abajo de esta línea
    print("Este programa calcula el área y volumen de una esfera")
    print("=====================================================")

    print("Dame el radio de la esfera: ")
    radio = float(input())

    area=4*math.pi*radio**2
    volumen=4/3*math.pi*radio**3

    print(f"El área de la esfera es: {area:.2f}")
    print(f"El volumen de la esfera es: {volumen:.2f}")

if __name__=='__main__':
    main()
