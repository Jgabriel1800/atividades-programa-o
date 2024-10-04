"""Sabendo-se que a distância entre Recife e Petrolina é de 712Km e que existem postos de
pedágio nas cidades de Caruaru e Arcoverde. Faça um programa que informe o valor pago
em pedágio por um viajante que saiu de Recife com destino a uma das cidades citadas."""

pedagio_arcoverde=50
pedagio_caruaru=25

print("para onde deseja ir?")
print("1-Caruaru")
print("2-Arcoverde")
print("3-Petrolina")

local=int(input("Digite o local desejado: "))

if local==1:
    valor_pago=pedagio_caruaru
    print("O valor para do pedagio para Caruaru é de: ", valor_pago)

elif local==2:
    valor_pago=pedagio_caruaru+pedagio_arcoverde
    print("O valor para do pedagio para Arcoverde é de: ", valor_pago)

elif local==3:
    valor_pago=pedagio_arcoverde+pedagio_caruaru
    print("O valor para do pedagio para Petrolina é de: ", valor_pago)