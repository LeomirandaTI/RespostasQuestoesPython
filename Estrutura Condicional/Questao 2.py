nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Otimo! A media ficou {media} e o aluno foi aprovado.")
else:
    print(f"Que pena, a media ficou {media} e o aluno foi reprovado.")


