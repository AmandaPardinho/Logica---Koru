# Calcular 4 ao cubo
print(4*4*4)
print(pow(4, 3))

# Declarar a função soma(), que recebe dois números inteiros e retorna a soma entre eles
    # def => definition => usada para declarar uma função
def soma(num1, num2):
    total = num1 + num2
    return total

soma1 = soma(5, 4)
print(soma1)

soma2 = soma(15, -5)
print(soma2)

total1 = soma(soma(5, 6), soma(8, 2))
soma3 = soma(total1, 20)
print(soma3)

# Criar uma função que calcula o fatorial de um determinado número
def fatorial(numero):
    total2 = 1
    i = numero
    while(i >= 1):
        total2 = total2 * i
        i -= 1
    return total2

print(fatorial(5))