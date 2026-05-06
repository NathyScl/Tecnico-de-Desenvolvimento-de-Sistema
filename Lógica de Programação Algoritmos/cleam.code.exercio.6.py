#Primeira forma
for i in range(6,0,-1):
    for j in range(i):
        print("*", end="")
    print()

    #Segunda forma
    print("\n \n")
    for i in range(6,0,-1):
        print("*"*i)