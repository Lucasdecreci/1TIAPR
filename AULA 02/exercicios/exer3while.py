import random
print("Bem-vindo ao jogo de adivinhação!")

tentativa = 3   
numero = random.randint(1, 10)

while tentativa > 0:
    palpite = int(input("Digite um número entre 1 e 10: "))
    if palpite == numero:
        print("Parabéns! Você adivinhou o número.")
        break
    else:
        tentativa -= 1
print(f"Errado! Você tem {tentativa} tentativas restantes.")