"""8o) Em 1994 aconteceu a primeira final de copa do mundo que foi decidida nos pênaltis. Trinta
anos se passaram e cabe a você desenvolver um sistema que possa relembrar esse
momento. Seu sistema deve simular a disputa de pênaltis entre duas equipes. Para isso, siga
as orientações abaixo:Gere dois números inteiros aleatório entre 1 e 10.
 O primeiro número representa o batedor e o segundo o goleiro.
 Se número do batedor for maior que o número do goleiro o pênalti será convertido.
 Sabendo-se que cada equipe tem direito a 5 cobranças, informe o nome da equipe vencedora
ou se será necessário iniciar uma rodada de alternâncias."""

import random

equipe1 = 0
equipe2 = 0
penaltis = 5
for i in range(penaltis):
    batedorequipe1 = random.randint(1, 10)
    goleiroequipe2 = random.randint(1, 10)

    print(f"\nCobrança {i + 1}:")
    print(f"(Batedor): {batedorequipe1} vs  (Goleiro): {goleiroequipe2}")

    if batedorequipe1 > goleiroequipe2:
        equipe1 += 1
        print(f" converteu o pênalti!")
    else:
        print(f" perdeu o pênalti!")

   
    batedorequipe2 = random.randint(1, 10)
    goleiroequipe1 = random.randint(1, 10)

    print(f"(Batedor): {batedorequipe2} vs (Goleiro): {goleiroequipe1}")

    if batedorequipe2 > goleiroequipe1:
        equipe2 += 1
        print(f" converteu o pênalti!")
    else:
        print(f" perdeu o pênalti!")


print(f"\nResultado final:  {equipe1} x {equipe2} ")


if equipe1 > equipe2:
    print(f"Equipe 1 venceu!")
elif equipe2 > equipe1:
    print(f"Equipe 2 venceu!")
else:
    print("Empate! Iniciaremos a rodada de alternâncias.")

   
    while equipe1 == equipe2:
       
        batedorequipe1 = random.randint(1, 10)
        goleiroequipe2 = random.randint(1, 10)

        print(f"\nCobrança Alternada  (Batedor): {batedorequipe1} vs (Goleiro): {goleiroequipe2}")

        if batedorequipe1 > goleiroequipe2:
            equipe1 += 1
            print(f" converteu o pênalti!")
        else:
            print(f" perdeu o pênalti!")

        batedorequipe2 = random.randint(1, 10)
        goleiroequipe1 = random.randint(1, 10)

        print(f" (Batedor): {batedorequipe2} vs  (Goleiro): {goleiroequipe1}")

        if batedorequipe2 > goleiroequipe1:
            equipe2 += 1
            print(f" converteu o pênalti!")
        else:
            print(f" perdeu o pênalti!")
    print(f"\nResultado final:  {equipe1} x {equipe2} ")
    if equipe1 > equipe2:
        print(f"Equipe 1 venceu!")
    else:
        print(f"Equipe 2 venceu!")

