fruta = "morango"
print(fruta)

#Iniciar o array frutas informando o nome das frutas selecionadas
frutas = ["laranja", "maçã", "banana"]

#Exibir o conteúdo do array frutas
print(frutas)

#Exibir o nome da segunda fruta armazenada no array frutas
print(frutas[1])

#Quantas frutas temos no array frutas?
quantidadeFrutas = len(frutas)
print(quantidadeFrutas)

#Função append()
frutas.append("abacate")
print(len(frutas))
print(frutas)

#Quero apagar a 4a. fruta (abacate)
frutas.pop(3)
print(len(frutas))
print(frutas)

#Adicionar româ à lista de frutas (adiciona ao final da lista)
frutas.append("romã")

#Remover banana da lista de frutas
frutas.remove("banana")
print(len(frutas))
print(frutas)