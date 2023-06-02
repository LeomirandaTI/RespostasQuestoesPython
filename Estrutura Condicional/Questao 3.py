while True:
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))

        media = (nota1 + nota2 + nota3) / 3

        if media >= 0 and media < 3:
            mensagem = "REPROVADO"
        elif media >= 3 and media < 7:
            mensagem = "em RECUPERAÇÃO"
        elif media >= 7 and media <= 10:
            mensagem = "APROVADO"
        else:
            mensagem = "Média inválida"

        print("MÉDIA:", media)
        print("infelizmente voçê está", mensagem)
        break
    except ValueError:
        print("Erro: Informe apenas números para a sua nota.")