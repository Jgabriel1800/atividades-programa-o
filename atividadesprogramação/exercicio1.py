#1 - Fazer um programa que leia dois números inteiros. Armazene os números lindos nas
#variáveis num1 e num2. Se número o número armazenado na variável num2 for par, exiba a
#soma dos números lidos, se não, exiba a multiplicação.

n1=int(input("Digite o seu primeiro número:"))
n2=int(input("Digite o seu segundo número:"))
if n2%2==0:
    print("A soma dos valores será igual a:", n1+n2)
else:
    print("A multiplicação dos valores será igual a:", n1*n2)
