#15 – Fazer um programa que leia a idade de uma pessoa e informe se a mesma já poderá tirar a
#habilitação e o título de eleitor, apenas o título de eleitor ou nenhum dos dois.

idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você já pode tirar a habilitação e o título de eleitor")

elif idade >= 16:
    print("Você já pode tirar o título de eleitor")

else:
    print("Você não pode tirar a habilitação e nem o título")
