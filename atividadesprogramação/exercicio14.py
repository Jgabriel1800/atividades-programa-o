#Contudo, o Lobo não sabia que as
#concessionárias brasileiras entregam o veículo praticamente sem combustível. Sendo assim,
#parou no primeiro posto para abastecer, mas achou complicado sabe qual combustível seria
#mais econômico utilizar: gasolina ou etanol? Você poderia ajudar? Informe qual combustível
#será mais econômico.

#O Lobo percorreu 500 km com 30 litros de gasolina. O preço do litro da gasolina é R$ 4,50 e o
# do etanol é R$ 3,20. a moto do Lobo tem um tanque de 50 litros.

#OBS: Considere que a moto do Lobo tem um tanque de 50 litros e que o preço do litro da gasolina é R$ 4,50 e o do etanol é R$ 3,20.



consumogasolina = 500 / 30


consumoetanol = 500 / 30


precogasolina = consumogasolina * 4.5


precoetanol = consumoetanol * 3.2


if precogasolina < precoetanol:
    print('A gasolina é mais econômica')
else:    
    print('O etanol é mais econômico')

