# Lista de produtos
produtos = []

# Usuário vai digitar três produtos de sua escolha, informndo nome, quantidade e preço
numerador = 1
while(numerador <= 3):
    nome = input(f"Informe o nome do {numerador}o. produto: ")
    quantidade = int(input(f"Digite a quantidade do {numerador}o. produto: "))
    preco = float(input(f"Digite o preço do {numerador}o. produto: "))
    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco
    }
    produtos.append(produto)
    numerador = numerador + 1

print(produtos)

# Como saber o preço do 3o. produto?
print(produtos[2]['preco'])

# Como saber o nome do 1o. produto?
print(produtos[0]['nome'])

# Somar todos os produtos em estoque
# Calcular o preço de todos os produtos somados
totalEstoque = 0
totalPreco = 0
for produto in produtos:
    totalEstoque = totalEstoque + produto['quantidade']
    totalPreco = totalPreco + produto['preco']

print(f"Total de produtos em estoque: {totalEstoque}")
print(f"Preço total dos produtos em estoque: {totalPreco}")