import csv
with open("produtos_exemplo.csv", newline = '\n') as csvfile:
    leitor = csv.reader(csvfile, delimiter = ',') # delimiter => mostra como os atributos são separados no arquivo
    next(leitor) # next => retira o cabeçalho

    #for linha in leitor:
     #   print(linha)
      # print(linha[0])

 # Usando dicionário para ler o arquivo
    produtos = []
    for linha in leitor:
        produto = {
            "codigo": int(linha[0]),
            "nome": linha[1],
            "preco": float(linha[2])
        }
        produtos.append(produto)
print(produtos)