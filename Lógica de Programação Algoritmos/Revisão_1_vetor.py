saltos = []

for i in range(7):
    saltos.append(int(input("Digite o valor do salto")))

# Todos os saltos ma ordem em que foram realizados
print(saltos)

# Maior
maior = saltos[0]

for salto in saltos:
    if(salto > maior):
        maior = salto

print("O maior salto é: ", maior)

# Menor
menor = saltos[0]

for salto in saltos:
    if(salto < menor):
        menor = salto

print("O maior salto é: ", menor)

# Média sem maior e menor
soma = 0

for salto in saltos:
    if(Saltos !=maior and salto != menor):
        soma = soma = + salto
media = soma / 5
print("A média sem maior e menor é: ", media)

# Média geral
soma = 0

for salto in saltos:
    soma = soma + salto
media_geral = soma / 7
print("A média geral é: ",media_geral)