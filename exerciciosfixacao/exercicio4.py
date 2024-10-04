"""4o) Bart é o filho mais velho de uma família com 5 integrantes. Conforme apresentamos na
figura.Certo dia foi solicitado que Bart fosse a pastelaria do krusty, pois hoje seria o dia do pastel.
Chegando à pastelaria Bart viu o seguinte menu. Sabendo-se que cada membro da família come apenas um pastel, informe o valor gasto por
Bart."""
custo_carne=12.5
custo_queijo=10.0
custo_frango=11.11

carne=0
queijo=0
frango=0
for i in range(5):
    sabor=int(input("Digite o sabor do pastel(1=carne,2=queijo,3=frango): "))
    while sabor !=1 and sabor !=2 and sabor !=3:
        print("Sabor inválido")
        sabor=int(input("Digite o sabor do pastel(1=carne,2=queijo,3=frango): "))

    if sabor==1:
        carne+=1
    elif sabor==2:
        queijo+=1
    else:
        frango+=1


valor=carne*12.5 + queijo*10.0 + frango*11.11
print("quantidade pasteis de carne: ", carne)
print("quantidade pasteis de queijo: ", queijo)
print("quantidade pasteis de frango: ", frango)

print("O valor total gasto foi igual à: ", valor)
