#Faça um programa que leia o tipo de figura geométrica (retângulo, triângulo ou círculo) e
#informe a área da mesma. Obs: Cada figura tem uma forma específica para calcular a área.


figura = input("Coloque o tipo de figura geométrica (retângulo, triângulo ou círculo):").lower()

while figura != "retângulo" and figura != "triângulo" and figura != "círculo":
    print("Tente novamente.")
    figura = input("Coloque o tipo de figura geométrica (retângulo, triângulo ou círculo):").lower()

if figura=="retângulo":
    altura= int(input("Insira valor da altura:"))
    base=int(input("Insira o valor da base:"))
    area=base*altura
    print("O valor da area será igual a:",area)

elif figura== "triângulo":
    altura=int(input("Insira o valor da altura:"))
    base=int(input("Insira valor da base:"))
    area=(base*altura)/2
    print("O valor da area será igual a:",area)

else:
    raio=int(input("Insira o valor do raio:"))
    area=3.14*(raio**2)
    print("O valor da area será igual a:",area)


