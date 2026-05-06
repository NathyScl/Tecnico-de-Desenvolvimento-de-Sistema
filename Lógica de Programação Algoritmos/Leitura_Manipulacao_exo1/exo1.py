# importa as bibliotecas
import pandas as pd
import os

dados = {
    "Nome": [],
    "Disciplina": [],
    "Nota": []
}

deseja_continuar = ""

while(deseja_continuar != "n"): 
    print("\n Digite os dados: ")
    nome = input("Nome: ")
    disciplina = int(input("Disciplina: "))
    nota = input("Nota: ")

    dados["Nome"].append(nome)
    dados["Disciplina"].append(disciplina)
    dados["Nota"].append(nota)

    deseja_continuar = input("Deseja continuar? (s\n)").strip().lower()
    #strip() -> tirar espaços em branco
    #lower() -> transformar em minúsculo

    df = pd.DataFrame(dados)
    print(df)

#definir o caminho pnde será salvo o aequivo
os.chdir("C:\\Users\\48838150800\\Documents\\Leitura_Manipulacao_exo1\\")

df.to_csv("dados.txt", sep="\t", index=False)
print(" Dados salvos em 'Dados.txt'!")

#Leitura dos arquivos
try:
    df_lido = pd.read_csv("dados.txt", sep="\t")
    print(df_lido)
except FileNotFoundError:
    print("\n Arquivo não encontrado!")