import random
fase = 1  
while True:  
    print(f"\nFase {fase}: Escolha uma resposta (A, B, C, D, E)")
    
    resposta_correta = random.choice(['A', 'B', 'C', 'D', 'E'])
    resposta_jogador = input("Digite sua resposta: ").upper()  
    if resposta_jogador == resposta_correta:
        print("Resposta correta! Você avançou para a próxima fase.")
        fase += 1  
        
        if fase > 5:
            print("Parabéns! Você venceu o jogo.")
            break 
    else:
        print("Resposta incorreta!Você começou novamente na fase 1.A resposta correta era: ", resposta_correta)
        fase = 1  
