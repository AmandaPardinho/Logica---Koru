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

# Comprar produtos
compras = []
continuarComprando = True

while(continuarComprando == True):
    print("Qual produto você quer comprar? Sendo: ")
    num = 0
    for produto in produtos:
        print(f"{num}: {produto['nome']}")
        num = num + 1

    codigo = int(input("Digite a opção desejada: "))

    print(f"Produto escolhido: {produtos[codigo]['nome']}, preço: {produtos[codigo]['preco']}")

    quantidadeDesejada = int(input(f"Quantos {produtos[codigo]['nome']} você quer comprar?"))

    compra = {
        "codigo": codigo,
        "quantidadeDesejada": quantidadeDesejada
    }
    compras.append(compra)

    # Dar baixa no estoque
    produtos[codigo]["quantidade"] = produtos[codigo]["quantidade"] - quantidadeDesejada
    continuarComprando = False

print(produtos)

# Total da compra
codigo = compras[0]['codigo']
total = compras[0]['quantidadeDesejada'] * produtos[codigo]['preco']
print(total)
