import math

def main():
    #escribe tu código abajo de esta línea
    print("Este programa calcula el área de un triángulo")
    print("==============================================")

    print("Dame el lado a:")
    a = float(input())

    print("Dame el lado b:")
    b = float(input())

    print("Dame el lado c:")
    c= float(input())

    s=(a+b+c)/2
    area=math.sqrt(s*(s-a)*(s-b)*(s-c))

    print(f"El área del triángulo es: {area:.4f}")

if __name__=='__main__':
    main()
