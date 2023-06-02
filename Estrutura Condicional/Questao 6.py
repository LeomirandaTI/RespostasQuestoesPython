peso = float(input("Digite o peso (em kg): "))
altura = float(input("Digite a altura (em metros): "))

while altura > 3:
    print("Altura inválida. Altura informada em centimetros!")
    altura = float(input("Digite a altura (em metros): "))

imc = peso / (altura ** 2)

if imc < 20:
    situacao = "Abaixo do peso"
elif imc >= 20 and imc < 25:
    situacao = "Peso normal"
elif imc >= 25 and imc < 30:
    situacao = "Sobrepeso"
elif imc >= 30 and imc < 40:
    situacao = "Obeso"
else:
    situacao = "Obeso mórbido"

print("IMC:", imc)
print("Situação do peso:", situacao)