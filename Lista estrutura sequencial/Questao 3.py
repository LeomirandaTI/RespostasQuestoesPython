import math


a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))


delta = b**2 - 4*a*c


if delta < 0:
    print("A equação não possui raízes reais.")
else:
    
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)

    
    print("As raízes da equação são:")
    print("x1 =", x1)
    print("x2 =", x2)