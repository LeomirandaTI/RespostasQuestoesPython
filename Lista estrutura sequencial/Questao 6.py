while True:
    valor_gasto = input("Digite o valor gasto pelo cliente: ")

    try:
        valor_gasto = float(valor_gasto)
        break
    except ValueError:
        print("Valor inválido. Digite apenas números.")

gorjeta = valor_gasto * 0.1
print("O valor da gorjeta a ser pago é:", gorjeta)