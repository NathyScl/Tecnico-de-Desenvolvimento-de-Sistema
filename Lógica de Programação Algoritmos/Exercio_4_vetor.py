vetor = []
invertido = [0,0,0,0,0]

for i in range (5):
    num = int(input("Digite um número: "))
    vetor.append(num)

for i in range(5):
    invertido[i] = vetor[4-i]

print(invertido)   