inicio = int(input("Digite o número inicio: "))
fim = int(input("Digite uo número fim: "))
soma = 0 

for i in range(inicio, fim+1):
    if (i%2 == 0):
     soma = soma + i
    
    print(soma)
     
    