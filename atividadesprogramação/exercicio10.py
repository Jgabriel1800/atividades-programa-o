#10 – Faça um programa que leia dois números e informe o menor número.
n1=float(input("Insira um número:"))
n2=float(input("Insira outro número:"))

if n1>n2:
    print("O menor número é:",n2)

elif n1<n2:
    print("O menor número é:",n1)

else:
    print("Os números são iguais.")