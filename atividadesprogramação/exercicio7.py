l1=int(input("Coloque o valor do primeiro lado:"))
l2=int(input("Coloque o valor do segundo lado:"))
l3=int(input("Coloque o valor do terceiro lado:"))

if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    print(" É um triângulo")

    if l1==l2==l3:
        print("Triângulo equilátero")
    elif l1==l2 or l1==l3 or l2==l3:
        print("Triângulo isósceles")
    else:  
        print("Triângulo escaleno")
else:
    print("Não é um triângulo")


