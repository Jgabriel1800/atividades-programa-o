import random
carga_maxima=800

valorcarga=random.randint(0,1000)

if valorcarga>carga_maxima:
    print("A carga foi igual a:",valorcarga)
    print("Ocorreu a viagem")

else:
    print("A carga foi igual a:",valorcarga)
    print("A viagem não ocorreu")