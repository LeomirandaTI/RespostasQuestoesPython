while True:
    try:
        numero = int(input("Digite um número inteiro: "))

        soma = 0

        for i in range(1, numero + 1):
            soma += i
        
        print("A soma dos números inteiros entre 1 e", numero, "é:", soma)
        break
    except ValueError:
        print("Invalido! Nao foi informado um numero inteiro")
        continue