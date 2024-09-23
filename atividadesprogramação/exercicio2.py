#2 - Sabendo que a fórmula para calcular o peso ideal é:
#Para mulheres: (62.1 * altura) – 44.7;
#Para homens: (72.2 * altura) – 58;
#Faça um programa que recebe o sexo e a altura de uma pessoa e informe o peso ideal

genero = input("Digite seu gênero (M para masculino e F para feminino):").lower()
while genero != "m" and genero != "f":
    print("Tente novamente.")
    genero = input("Digite seu gênero (M para masculino e F para feminino):").lower()
    
h = float(input("Digite sua altura:"))
if genero == "f":
    print("Seu peso ideal é:", (62.1 * h) - 44.7)
else:
    print("Seu peso ideal é:", (72.2 * h) - 58)
