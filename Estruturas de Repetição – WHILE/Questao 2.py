idade = int(input("Informe a idade (ou Informe uma idade negativa para fazer continuar com o programa): "))
total_pessoas = 0
acima_50 = 0
abaixo_40 = 0
soma_idades = 0

while idade >= 0:
    total_pessoas += 1
    soma_idades += idade

    if idade > 50:
        acima_50 += 1
    elif idade < 40:
        abaixo_40 += 1

    idade = int(input("Informe a idade (ou Informe uma idade negativa para fazer continuar com o programa): "))

if total_pessoas > 0:
    media_idades = soma_idades / total_pessoas
    percentual_abaixo_40 = (abaixo_40 / total_pessoas) * 100

    print("Pessoas acima de 50 anos:", acima_50)
    print("Média de idade das pessoas:", media_idades)
    print("Percentual de pessoas com idade abaixo de 40 anos: {:.2f}%".format(percentual_abaixo_40))
else:
    print("Nenhuma idade foi informada.")
