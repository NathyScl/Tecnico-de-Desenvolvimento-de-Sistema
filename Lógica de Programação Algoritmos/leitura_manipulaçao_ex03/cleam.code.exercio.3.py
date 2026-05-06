notas = []
for i in range(4):
        notas.append(int(input(f"Digite a {i+1}ª nota: ")))

        media = sum(notas)/len(notas)
        print("A média é: ", media)