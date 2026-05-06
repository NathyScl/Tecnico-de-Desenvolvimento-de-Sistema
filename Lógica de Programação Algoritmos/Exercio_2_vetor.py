numeros = []
soma = 0
media = 0

for i in (6):
    num = int(input("Digite um número: "))
    numeros.append(num)

for numero in numeros:
    soma = soma + numero
media = soma/6
print("A média é: ", media)