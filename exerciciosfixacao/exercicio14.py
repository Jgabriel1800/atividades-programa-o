"""14 – Uma loja virtual lhe contratou para desenvolver o sistema de pagamento. Foi explicado
que existem três formas de pagamento. São elas:
Pix – desconto de 11,11%
Dinheiro – valor normal do produto
Cartão – acréscimo de 3 reais no valor final
Faça um programa que leia o valor do produto e informe o preço final."""

valor_produto = float(input("Digite o valor do produto: "))
pagamento = input("Digite a forma de pagamento (1-Pix, 2-Dinheiro ou 3-Cartão): ")

while pagamento != "1" and pagamento != "2" and pagamento != "3":
    print("Forma de pagamento inválida.Tente novamente")
    pagamento = input("Digite a forma de pagamento (1-Pix, 2-Dinheiro ou 3-Cartão): ")

if pagamento == "1":
    valor_final = valor_produto - ((valor_produto/100)*11.11)
    print("O valor final do produto é R$", valor_final)
elif pagamento == "2":
    valor_final = valor_produto
    print("O valor final do produto é R$", valor_final)
else:
    valor_final = valor_produto + 3
    print("O valor final do produto é R$", valor_final)
