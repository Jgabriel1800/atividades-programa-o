"""12 - O jogo da vida é um jogo de tabuleiro no qual os jogadores sorteiam a profissão que
seguirão durante toda a partida. Cada profissão tem um salário específico que será entregue
ao jogador cada vez que chegar o dia do pagamento. Contudo, existe a cobrança de imposto
e muitas vezes o jogador receberá o salário pela metade. Neste jogo, o jogador escolherá um
dos dois caminhos possíveis para concluir a partida. No caminho A receberá o pagamento 30
vezes, mas dos 30 dez serão pagos pela metade. Já o caminho B receberá o pagamento 25
vezes, mas dos 25 cinco serão pagos pela metade. Considerando que não existem mais
despesas ou lucros durante o restante do jogo, informe o montante final do jogador.
OBS: O sistema receberá como dado de entrada a profissão sorteada pelo jogador. De acordo
com a tabela abaixo:"""
import random
nomejogador = input("Digite o nome do jogador: ")
Salario_medico=50
Salario_jornalista=24
Salario_advogado=50
Salario_professor=24
Salario_fisico=30
Salario_comerciante=12
Salario_estudante=16
profissao=random.choice(["Médico","Jornalista","Advogado","Professor","Físico","Comerciante","Estudante"])
print("Profissão sorteada: ",profissao)

salario = 0
escolha_caminho=int(input("Digite 1 para escolher o caminho A e 2 para escolher o caminho B: "))
if escolha_caminho == 1:
    if profissao=="Médico":
        salario = (Salario_medico*20) + ((Salario_medico/2)*10)
        print("O jogador",nomejogador,"receberá",salario,"reais.")
    elif profissao=="Jornalista":
        salario = (Salario_jornalista*20) + ((Salario_jornalista/2)*10)
        print("O jogador",nomejogador,"receberá",salario,"reais.")
    elif profissao=="Advogado":
        salario = (Salario_advogado*20) + ((Salario_advogado/2)*10)
        print("O jogador",nomejogador,"receberá",salario,"reais.")
    elif profissao=="Professor":
        salario = (Salario_professor*20) + ((Salario_professor/2)*10)
        print("O jogador",nomejogador,"receberá",salario,"reais.")
    elif profissao=="Físico":
        salario = (Salario_fisico*20) + ((Salario_fisico/2)*10)
        print("O jogador",nomejogador,"receberá",salario,"reais.")
    elif profissao=="Comerciante":
        salario = (Salario_comerciante*20) + ((Salario_comerciante/2)*10)
        print("O jogador",nomejogador,"receberá",salario,"reais.")
    elif profissao=="Estudante":
        salario = (Salario_estudante*20) + ((Salario_estudante/2)*10)
        print("O jogador",nomejogador,"receberá",salario,"reais.")
elif escolha_caminho == 2:
    if profissao=="Médico":
        salario = (Salario_medico*20) + ((Salario_medico/2)*5)
        print("O jogador",nomejogador,"receberá",salario,"reais.")
    elif profissao=="Jornalista":
        salario = (Salario_jornalista*20) + ((Salario_jornalista/2)*5)
        print("O jogador",nomejogador,"receberá",salario,"reais.")
    elif profissao=="Advogado":
        salario = (Salario_advogado*20) + ((Salario_advogado/2)*5)
        print("O jogador",nomejogador,"receberá",salario,"reais.")
    elif profissao=="Professor":
        salario = (Salario_professor*20) + ((Salario_professor/2)*5)
        print("O jogador",nomejogador,"receberá",salario,"reais.")
    elif profissao=="Físico":
        salario = (Salario_fisico*20) + ((Salario_fisico/2)*5)
        print("O jogador",nomejogador,"receberá",salario,"reais.")
    elif profissao=="Comerciante":
        salario = (Salario_comerciante*20) + ((Salario_comerciante/2)*5)
        print("O jogador",nomejogador,"receberá",salario,"reais.")
    elif profissao=="Estudante":
        salario = (Salario_estudante*20) + ((Salario_estudante/2)*5)
        print("O jogador",nomejogador,"receberá",salario,"reais.")