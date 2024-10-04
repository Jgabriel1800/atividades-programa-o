Jogador1 = input("Nome do jogador 1: ")
Jogador2 = input("Nome do jogador 2: ")

while True:  
    print("Escolha 1 para Pedra, 2 para Papel e 3 para Tesoura")

    escolha1 = int(input(f"{Jogador1}, escolha: "))
    while escolha1!= 1 and escolha1!= 2 and escolha1!= 3:
        print("Escolha inválida! Tente novamente.")
        escolha1 = int(input("escolha novamente: "))

    escolha2 = int(input(f"{Jogador2}, escolha: "))
    while escolha2!= 1 and escolha2!= 2 and escolha2!= 3:
        print("Escolha inválida! Tente novamente.")
        escolha2 = int(input("escolha novamente: "))

    if escolha1 == escolha2:
        print("Empate!")
    elif (escolha1 == 1 and escolha2 == 3) or (escolha1 == 2 and escolha2 == 1) or (escolha1 == 3 and escolha2 == 2):
        print(f"{Jogador1} venceu!")
    else:
        print(f"{Jogador2} venceu!")

    jogar_novamente = input("\nDesejam jogar novamente? (s/n): ").lower()
    if jogar_novamente != 's':
        print("Obrigado por jogar!")
        break
