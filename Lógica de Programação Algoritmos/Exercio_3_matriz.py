matriz = []


for i in range (4):
    linha = []
    for j in range(4):
        linha.append(int(input((f"Matriz[{i}][{j}]"))))
matriz.append(linha)

x = int(input("Digite um número para ser procurando: "))
contador = 0
for i in range(4):
    if(matriz[i][j] == x):
        print("X está na matriz")
        print("Posição i: ",i)
        print("Posição j: ",j)
        contador+=1
        if(contador == 0):
            print("X Não está na matriz")