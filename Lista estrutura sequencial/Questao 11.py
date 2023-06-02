while True:
    try:
        total_eleitores = int(input("Digite o número total de eleitores: "))
        votos_candidato1 = int(input("Digite o número de votos do primeiro candidato: "))
        votos_candidato2 = int(input("Digite o número de votos do segundo candidato: "))

        
        if votos_candidato1 + votos_candidato2 > total_eleitores:
            print("Erro: O número de votos informado é maior do que o número total de eleitores.")
            continue
        else:
            votos_nulos = total_eleitores - votos_candidato1 - votos_candidato2

            percentual_candidato1 = (votos_candidato1 / total_eleitores) * 100
            percentual_candidato2 = (votos_candidato2 / total_eleitores) * 100
            percentual_nulos = (votos_nulos / total_eleitores) * 100

            print("Percentual de votos do primeiro candidato: {:.2f}%".format(percentual_candidato1))
            print("Percentual de votos do segundo candidato: {:.2f}%".format(percentual_candidato2))
            print("Percentual de votos nulos: {:.2f}%".format(percentual_nulos))
            
        break

    except ValueError:
        print("Erro: Informe apenas números para o número de eleitores e votos dos candidatos.")