x = float(input("Digite o comprimento do lado X: "))
y = float(input("Digite o comprimento do lado Y: "))
z = float(input("Digite o comprimento do lado Z: "))

if x < y + z and y < x + z and z < x + y:
    print("Os valores formam um triângulo.")
else:
    print("Os valores não formam um triângulo.")
