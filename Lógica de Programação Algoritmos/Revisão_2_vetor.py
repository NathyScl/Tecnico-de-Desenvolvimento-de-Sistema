# Solicite um texto para o usuario
texto = input("Digita um texto qualquer: ")

# Exibir letra por letra do texto
# Para cada letra no texto
for letra in texto:
    print(letra)

# Contar quantidade de caracteres != ''
qtd_caracteres = 0

for letra in texto:
    if(letra != " "):
        qtd_caracteres+=1
print("A quantidade de caracteres é: ", qtd_caracteres)

# Contar as quantidades de volgais
vogais = "aeiouAEIOUáàãâÁÀÃÂéèêÉÈÊíìîóòôõÓÒÕÔúùûÚÙÛ"
qtd_vogais = 0

for vogal in volgais:
    for letra in texto:
        if(letra == vogal):
            qtd_vogais+=1
printO("A quantidade de vogais é: ", qtd_vogais)
""
# Palindromo
texto_invetido = reversed(texto)

for i in range(len(texto)-1,-1,-1):
    texto_invertido = texto_invetido + texto[i]

    if(texto == texto_invertido):
        print("É palíndromo!")
else:
    print("Não é palíndromo")