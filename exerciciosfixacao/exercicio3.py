"""3o) Fazer um programa que leia um número inteiro positivo e informe se o número lido é
múltiplo de 4 e 8."""

num=int(input("Digite um número inteiro positivo: "))
while num<0:
    num=int(input("Digite um número inteiro positivo: "))
    
if num%4==0 and num%8==0:
    print("O número é múltiplo de 4 e 8.")
else:
    print("O número não é múltiplo de 4 e 8.")