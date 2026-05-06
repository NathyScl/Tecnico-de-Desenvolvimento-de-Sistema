valorCompra = float(input("Digite o valor da conta: "))
cupomDesconto = input("Possui cupom de desconto? ")

if(valorCompra >= 200 or cupomDesconto == "Sim"):
    print("Você ganhou um desconto de 15%!")
else:
    print("Você não tem dinheiro a desconto no momento!")