numeros = []
cont_pares = 0

for i in (10):
    num = int(input("Digite um número: "))
    numeros.append(num)
for numero in numeros:
    if(numero%2==0):
        cont_pares = cont_pares + 1
        print("A quantidade de número de pares são: ", cont_pares)