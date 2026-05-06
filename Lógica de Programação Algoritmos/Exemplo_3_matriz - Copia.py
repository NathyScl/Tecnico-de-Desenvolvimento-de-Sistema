linhas = int(input("Quantidade de linhas (i):"))
colunas = int(input("Quantidade de colunas (j):"))
matriz = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input(f"M[{i}][{j}] = ")))
    matriz.append(linha)

print("Matriz preenchia: ")
for linha in matriz:
    print(linha)