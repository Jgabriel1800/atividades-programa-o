"""1 - Certo Instituto Federal estava sofrendo com ataques de seres estranhos durante as noites
do final de semana. Depois de muitos sustos decidiu-se contratar especialistas para averiguar
o problema. Foram chamados os caças fantasmas, os irmãos winchester e Dr. Van Helsing.
Os caças fantasmas identificaram que o problema era uma invasão de boneco de machimelo
e que os feixes de prótons poderiam capturar todos, mas o custo seria de 350 reais por cada
boneco encontrado. Já os irmãos winchester falaram que o instituto foi construído em um
antigo cemitério e que os mortos estão levantando para estudar. A solução seria queimar
cada túmulo. No entanto, seriam gastos 120 reais com cada túmulo queimado. Por fim, Van
Helsing falou que era caso de vampiros que passavam a noite nos galhos das árvores
transformados em morcegos esperando sangue. A solução seria colocar alho em todas as
árvores que tenha morcego. O custo seria de 50 reais por cada árvores. Diante de tudo que
foi passado pedimos a uma aluna para vigiar o instituto durante uma noite. Essa menina, tinha
no seu cinto um sistema com três botões. O botão número 1 deveria se apertado se encontrar
boneco de machimelo, o botão de número 2 deveria ser apertado se encontrar algum túmulo,
o botão de número 3 deveria ser apertado quando encontrar um morcego. A menina passou
a noite vestida de branco e andando pelo instituto e pressionou o botão 4 vezes. Agora é com
você informe quanto a escola gastou durante a semana."""

custo_boneco=350
custo_tumulo=120
custo_arvore=50

botao1=0
botao2=0
botao3=0

for i in range(4):
    botao=int(input("Digite o botão pressionado: "))
    while botao != 1 and botao != 2 and botao != 3:
        print("Botão inválido.")
        botao=int(input("Digite o botão pressionado: "))
    if botao==1:
        botao1+=1
    elif botao==2:
        botao2+=1
    elif botao==3:
        botao3+=1
    else:
        print("Botão inválido.")

total=custo_boneco*botao1+custo_tumulo*botao2+custo_arvore*botao3

print(f"O instituto gastou {total} reais durante a semana.")
