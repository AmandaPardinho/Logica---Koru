i = 1

while(i <= 10):
    print(i)
    i = i + 1
print("")

i = 10

while(i >= 1):
    print(i)
    i = i - 1
print("")

numero = int(input("Digite um número de 1 até 10: "))
while(numero < 1) or (numero > 10):
    print("Número inválido! Digite um número de 1 até 10")
    numero = int(input("Digite um número de 1 até 10: "))