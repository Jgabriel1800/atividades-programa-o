"""10o) Salto Ornamental é um esporte individual que consiste em saltar de uma plataforma
elevada, fixa ou não (trampolin), em direção a uma piscina, realizando uma série de
movimentos acrobáticos e estéticos. Um dos critérios para vencer a competição é espirar a
menor quantidade de água no processo de mergulho. Três mergulhadores foram para a final.
Utilize seu conhecimento adquirido na disciplina para criar um meio de identificar o vencedor.
OBS: Só poderá utilizar o que foi visto em sala de aula"""

import random
mergulhador1=input("Digite o nome do primeiro mergulhador: ")
mergulhador2=input("Digite o nome do segundo mergulhador: ")
mergulhador3=input("Digite o nome do terceiro mergulhador: ")

nota1=random.randint(0,10)
nota2=random.randint(0,10)
nota3=random.randint(0,10)

print("A nota do atleta",mergulhador1,"foi:",nota1)
print("A nota do atleta",mergulhador2,"foi:",nota2)
print("A nota do atleta",mergulhador3,"foi:",nota3)

if nota1>nota2 and nota1>nota3:
    print("O vencedor foi:",mergulhador1)
elif nota2>nota1 and nota2>nota3:
    print("O vencedor foi:",mergulhador2)
elif nota3>nota1 and nota3>nota2:
    print("O vencedor foi:",mergulhador3)
else:
    print("Houve empate")
