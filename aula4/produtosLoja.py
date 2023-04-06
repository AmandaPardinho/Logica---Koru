#Usuário digita o valor de três produtos
precos = []

numerador = 1
while(numerador <= 3):
    precos.append(float(input(f"Digite o preço do {numerador}o. produto: ")))
    numerador = numerador + 1

print(precos)
print(" ")

#Percorrer a lista de preços de produtos
for preco in precos:
    print(preco)
print(" ")

#Calculando o preço total
total = 0
for preco in precos:
    total = total + preco

print(total)
print(total/len(precos))