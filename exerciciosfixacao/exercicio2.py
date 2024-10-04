"""2 - No antigo Egito existiram intermináveis conflitos. Sendo uma civilização rica na agricultura
e com forte exército, o Egito encontrava-se na mira de conquistadores. Quase todos repelidos
perante o forte poder do exército egípcio. A maior ameaça do reino era a própria política
interna. Era uma país governado pelo Faraó, figura que acreditavam ser um deus na terra.
Abaixo do Faraó existia o vizir. Esse era responsável pela administração do reino e respondia
apenas ao Faraó. Muitos consideravam o vizir como o feiticeiro do reino. Historiadores acreditam
que os faraós mais famosos foram Hatshepsut, Tutmés III, Ramsés II, Amenhotep III, Tutancâmon
e Cleópatra. Só que esses ficam em segundo plano diante do poder do faraó Yami. Esse era
querido pelo povo e poderoso no combate. O único que rivalizava com o poder do faraó Yami era
o seu vizir conhecido como Kaiba. Um homem focado em conquistar o trono do faraó. Profecias
afirmavam que se existisse guerra entre os apoiados de Yami e os de Kaiba as consequências
seriam desastrosas. O Egito chegaria ao fim. Objetivando a preservação do povo egípcio, foram
criadas estratégias para que os dois pudessem descobrir o vencedor da disputa, mas sem prejuízo
para o povo. Assim, nasceu um jogo de cartas conhecido como mostro de duelo. Por ser um
protótipo cada duelista teria apenas duas cartas. O faraó utilizou uma carta conhecida como Mago
Negro e outra que invocava um ser com o poder dos raios. Já o vizir utilizou uma carta que
invocava um dragão e outra que invocava um gênio mágico. Sabendo que a primeira disputa foi
entre o Mago e o gênio e a segunda entre o dragão e o ser elétrico da escuridão. Faça um
programa que determine o nível de poder de cada carta e o vencedor do duelo.
PS: Nenhuma carta tem poder inferior a 1000 ou superior a 4000."""

ataque_mago_negro= 2500
defesa_mago_negro= 2100
poder_mago_negro= (2500+2100)/2
print("O nivel de poder do mago negro: ", poder_mago_negro)

ataque_dragao=3000
defesa_dragao=2500
poder_dragao=(3000+2500)/2
print("O nivel de poder do dragão: ", poder_dragao)
ataque_raio=2500
defesa_raio=1200
poder_raio=(2500+1200)/2
print("O nivel de poder do raio: ", poder_raio)

ataque_genio=1800
defesa_genio=1000
poder_genio=(1800+1000)/2
print("O nivel de poder do genio: ", poder_genio)

duelo_vencido_yami=0
duelo_vencido_kaiba=0

if(poder_mago_negro>poder_genio):
    duelo_vencido_yami+=1
    print("Yami venceu o primeiro duelo")
else:
    duelo_vencido_kaiba+=1
    print("Kaiba venceu o primeiro duelo")

if(poder_raio>poder_dragao):
    duelo_vencido_yami+=1
    print("Yami venceu o segundo duelo")
else:
    duelo_vencido_kaiba+=1
    print("Kaiba venceu o segundo duelo")





