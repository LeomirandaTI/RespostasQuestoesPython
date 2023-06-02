while True:
    numero = float(input("Digite um número positivo: "))

    if numero < 0:
        print("O número digitado não é positivo.")
    else:
        quadrado = numero ** 2
        cubo = numero ** 3
        raiz_quadrada = numero ** 0.5
        raiz_cubica = numero ** (1/3)

        print("O número ao quadrado é:", quadrado)
        print("O número ao cubo é:", cubo)
        print("A raiz quadrada do número é:", raiz_quadrada)
        print("A raiz cúbica do número é:", raiz_cubica)
        break