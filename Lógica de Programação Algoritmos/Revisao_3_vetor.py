matriz = [
   [1,10,9,8,9],
   [2.10,10,10,10],
   [3,8,7.5,8,7],
   [4,5,5,5,5,]
]

soma = 0
for i in range (4):
    for j in range(5):
        soma = soma + matriz[i][j]

print("Soma Total = ", soma)