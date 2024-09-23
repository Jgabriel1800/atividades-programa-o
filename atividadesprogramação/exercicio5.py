#Para uma eleição ser considerada válida é necessário que a soma dos votos de todos os
#candidatos seja superior a soma dos votos brancos e nulos. Na aldeia da folha, foi realizada a
#eleição do sexto Hokage. Nela os candidatos foram: Naruto Uzumaki, Sakura Haruno e Shin
#Aburame. Faça um programa que informe o vencedor da eleição se a mesma for considerada
#válida.

votosnaruto=int(input("Votos no naruto:"))
votossakura=int(input("Votos na sakura:"))
votosshin=int(input("Votos no shin:"))
votosbrancos=int(input("Votos brancos:"))
votosnulos=int(input("Votos nulos:"))

votosvalidos=int(votosnaruto)+int(votossakura)+int(votosshin)
votosinvalidos=int(votosbrancos)+int(votosnulos)

if votosinvalidos>votosvalidos:
    print("Eleição inválida")

else:
    if votosnaruto>votossakura and votosnaruto>votosshin:
        print("Naruto hokage")
    elif votossakura>votosnaruto and votossakura>votosshin:
        print("Sakura hokage")
    elif votosshin>votosnaruto and votosshin>votossakura:
        print("Shin hokage")

