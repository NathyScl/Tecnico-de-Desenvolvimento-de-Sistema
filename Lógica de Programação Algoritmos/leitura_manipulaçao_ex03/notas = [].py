notas = []

for i in range(4):
    # Tentar solicitar as notas
    try:
        nota = float(input(f"Digite a (i+1)ª nota: "))

        if(nota < 0 or nota > 10):
            print("Nota inválida, insira um valor entre 0 e 10!") 
            exit()
        else:
            notas.append(nota)
     #Se tiver algum erro (excessão) de valor, retorno uma mensagem
    except ValueError:
        print("Erro: insire um número valido!")

#se a pessoa apenas digitou texto
if not nota:
    print("Error: Nenhuma nota foi inserida!")
else:
    media = sum(notas)/len(notas)

    if(media >= 7):
        print(f"Média = {media} - aprovado!")
    elif(media >= 5):
          print(f"Média = {media} - recuperação:")
    else:
          print(f"Média = {media} - Reprovação") 