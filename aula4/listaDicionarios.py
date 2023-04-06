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
