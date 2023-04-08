import csv
with open("produtos_exemplo.csv", newline = '\n') as csvfile:
    leitor = csv.reader(csvfile, delimiter = ',')
    next(leitor)

    for linha in leitor:
        print(linha)
        print(linha[0])