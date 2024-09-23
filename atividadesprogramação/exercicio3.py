precogasolina=0.75
distancia=295
litrosnecessariosvamp=distancia/11
litrosnecessariosmorcego=distancia/16

modelo=input(("Escolha um dos modelos(vampiro voador ou morcego preto):")).lower()
while modelo != "vampiro voador" and modelo != "morcego preto":
    print("Tente novamente.")
    modelo=input(("Escolha um dos modelos(vampiro voador ou morcego preto):")).lower()

if modelo == "vampiro voador":
    print("valor total a ser gasto",litrosnecessariosvamp*precogasolina+ 500)
else:
    print("valor total a ser gasto",litrosnecessariosmorcego*precogasolina+ 300) 