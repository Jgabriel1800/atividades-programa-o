
import random

def competidor(atleta):
    valor1 = random.randint(1, 100)
    valor2 = random.randint(1, 100)
    valor3 = random.randint(1, 100)

    print(f"O atleta",atleta, "fez",valor1, "metros.")
    print(f"O atleta" ,atleta, "fez", valor2, "metros.")
    print(f"O atleta" ,atleta, "fez",valor3, "metros.")

    
    if (valor1 % 2 == 0 and valor2 % 2 != 0) or (valor1 % 2 != 0 and valor2 % 2 == 0):
        print("O atleta não queimou a largada.")
        return valor3
    else:
        print("O atleta queimou a largada.")
        return 0


atleta1 = input("Coloque o nome do primeiro atleta: ")
atleta2 = input("Coloque o nome do segundo atleta: ")


resultadoatleta1 = competidor(atleta1)
resultadoatleta2 = competidor(atleta2)


if resultadoatleta1 ==0 and resultadoatleta2 == 0:
    print("Ambos os atletas queimaram a largada. ")
elif resultadoatleta1 == 0:
    print("O atleta ",atleta2, "venceu a competição", atleta1, "queimou a largada.")
elif resultadoatleta2 == 0:
    print("O atleta" ,atleta1, "venceu a competição", atleta2, "queimou a largada.")
else:
    if resultadoatleta1 > resultadoatleta2:
        print("O atleta" ,atleta1, "venceu a competição.")
    elif resultadoatleta1 < resultadoatleta2:
        print("O atleta" ,atleta2, "venceu a competição.")
    else:
        print("Os atletas empataram.")
