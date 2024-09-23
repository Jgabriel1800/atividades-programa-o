#11 – Fazer um programa que leia um valor monetário em real e informe o mesmo valor em dólar e Euro.
valordolar=5.54
valoreuro=6.15
valor=float(input("Insira sua quantia de dinheiro em reais:"))
escolha=input("Escolha a moeda que deseja converter (dolar ou euro):").lower()
while escolha != "dolar" and escolha!= "euro":
    print("Tente novamente.")
    escolha=input("Escolha a moeda que deseja converter (dolar ou euro):").lower()

if escolha =="dolar":
    valor= valor/valordolar
    print("O seu valor convertido em dolar será igual a:",valor)

else:
    valor=valor/valoreuro

    print("O seu valor convertido em euro será igual a:",valor)


