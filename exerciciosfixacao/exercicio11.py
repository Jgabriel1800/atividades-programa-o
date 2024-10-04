"""11 - Um menino chamado Francisco mora no estado de São Paulo, em um sítio nas cercanias
da Vila Abobrinha, no interior do estado. Essa região é de difícil acesso e não existe transporte
escolar e nem energia elétrica. Todos os dias acorda com o cantar do velho galo Altaliba que
não “falha” em cantar ao raiar do sol. Gasta 50 min para caminhar uma légua e meia até
chegar à única escola da região. Por conta da distância, Francisco, filho do Nhô Bento,
sempre chega atrasado à sala de aula. A professora pergunta o motivo e ele explica que saiu
apressado e não deu tempo de calçar a botina que ajudaria a caminhar mais rápido. Chico
fala que quando sai de botina consegue chegar à escola em 40 min e quando vem montando
no Teobaldo esse tempo diminui para 30 min. Dona Marocas, que é a professora da escola,
retruca dizendo que em dias quentes ele para no riacho e por conta disso o tempo para chegar à
escola aumenta em 40 min. Já quando sai sem café da manhã entra no pomar do Nhô Lau,
aumentando em 20 min o tempo para chegar à escola por conta das goiabas que come.
Quando se encontra com Rosinha, aí não tem jeito. Atrasa 10 min por cada troca de ptialina
realizada. O Chico toma a fala já chateado e diz que chega 30 min mais rápido quando é
surpreendido pela onça. Agora é com você. Qual o tempo gasto por Chico para chegar à
escola no dia 07/06/2021."""

import random


tempo_sem_botina = 50
tempo_com_botina = 40
tempo_telbaldo = 30
aumento_riacho = 40
aumento_pomar = 20
aumento_rosinha = 10  
tempo_onca = 30  


com_botina = random.choice([True, False])
parou_no_riacho = random.choice([True , False])
comeu_goiabas = random.choice([True ,False])
encontrou_rosinha = random.choice([True , False])  
surpreendido_onca = random.choice([True , False])  


tempo_total = tempo_com_botina if com_botina else tempo_sem_botina
if parou_no_riacho:
    tempo_total += aumento_riacho
if comeu_goiabas:
    tempo_total += aumento_pomar
if encontrou_rosinha:
    tempo_total += aumento_rosinha


if surpreendido_onca:
    tempo_total -= tempo_onca

# Resultado
print("Com botina: ",com_botina)
print("Parou no riacho:", parou_no_riacho)
print("Comeu goiabas: ",comeu_goiabas)
print("Encontrou Rosinha: ", encontrou_rosinha)
print("Surpreendido pela onça: ",surpreendido_onca)
print("O tempo gasto por Chico para chegar à escola no dia 07/06/2021 é de", tempo_total, "minutos.")
