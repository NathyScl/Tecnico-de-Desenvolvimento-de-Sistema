ladoA = int(input("Digite o lado A: "))
ladoB = int(input("Digite o lado B: "))
ladoC = int(input("Digite o lado C: "))

if((LadoA+ladoB)>ladoC and (ladoA+ladoC)>LadoB and (ladoB+ladoC)>ladoA):
    if(ladoA == ladoB and ladoB == ladoC and ladoC == ladoA):
    print("Esquilatero")
elif(ladoA != ladoB and ladoB != ladoC and ladoC != ladoA):
    print("Esaleno")
else:
    print("Isósceles")
else:
    print("O triângulo não existe!")
