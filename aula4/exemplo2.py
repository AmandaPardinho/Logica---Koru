# Exemplo 2: perguntar o nome do produto, a quantidade em estoque e o preço

nome = input("Informe o nome do produto: ")
quantidade = int(input("Digite a quantidade deste produto no estoque: "))
preco = float(input("Digite o preço deste produto: "))
print("Nome do produto: " + nome)
print(f"Quantidade disponível: {quantidade}")
print(f"Preço por unidade: {preco}")

# Se o estoque de produto estiver abaixo de 50, exiba a frase "Estoque do {produto} está muito baixo. Providencie mais!"
if(quantidade < 50):
    print(f"Estoque do {nome} está muito baixo. Temos apenas {quantidade} unidades. Providencie mais!")
