# Exemplo 2: perguntar o nome do produto, a quantidade em estoque e o preço

nome = input("Informe o nome do produto: ")
quantidade = int(input("Digite a quantidade deste produto no estoque: "))
preco = float(input("Digite o preço deste produto: "))
print("Nome do produto: " + nome)
print(f"Quantidade disponível: {quantidade}")
print(f"Preço por unidade: {preco}")

# Se o estoque de produto estiver abaixo de 50, exiba a frase "Estoque do {produto} está muito baixo. Temos apenas
# {quantidade} unidade(s). Providencie mais!"
if(quantidade < 50):
    print(f"Estoque do {nome} está muito baixo. Temos apenas {quantidade} unidade(s). Providencie mais!")

#Calcule o valor do produto com imposto que é o seu valor bruto mais 10% (imposto)
precoComImposto = preco * 1.1
print(f"Preço total (com imposto): {precoComImposto}")