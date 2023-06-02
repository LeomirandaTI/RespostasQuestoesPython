while True:
    try:
        numero1 = int(input("Digite o primeiro número inteiro: "))
        numero2 = int(input("Digite o segundo número inteiro: "))

        menor = min(numero1, numero2)
        maior = max(numero1, numero2)

        print("Números inteiros entre", menor, "e", maior, ":")

        for numero in range(menor + 1, maior):
            print(numero)
    except ValueError:
        print("Invalido! Nao foi informado um numero inteiro")