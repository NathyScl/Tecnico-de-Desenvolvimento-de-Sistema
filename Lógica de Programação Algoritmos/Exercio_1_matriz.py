matriz1 = []
matriz2 = []
matriz_soma = []


#PREENCHER MATRIZ (REPETIR SEMPRE QUE PREENCHER MATRIZ)
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Matriz1{i}][{j}] = ")))
    matriz1.append(linha)

#PREENCHER MATRIZ (REPETIR SEMPRE QUE PREENCHER MATRIZ)
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input(f"Matriz2[{i}][{j}] = ")))
    matriz2.append(linha)

#PREENCHER MATRIZ (REPETIR SEMPRE QUE PREENCHER MATRIZ)
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(matriz1[{i}][{j}]+matriz2[{i}][{j}])
    matriz_soma.append(linha)

#PREENCHER MATRIZ (REPETIR SEMPRE QUE PREENCHER MATRIZ)
    print("Matriz Soma: ")
    for linha in matriz_soma:
        print(linha)
