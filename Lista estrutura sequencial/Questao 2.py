while True:
    AnoNascimento = input("Informe o ano do seu nascimento: ")
    AnoAtual = input("Informe o ano atual: ")

    if not AnoNascimento.isdigit() or not AnoAtual.isdigit():
        print("Ano de nascimento ou ano atual inválido. Informe apenas números.")
    else:
        IdadePessoa = int(AnoAtual) - int(AnoNascimento)
        Idade2050 = 2050 - int(AnoNascimento)
        print(f"A) A sua idade atual é {IdadePessoa}")
        print(f"B) A sua idade em 2050 será {Idade2050}")
        break