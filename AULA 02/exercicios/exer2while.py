num = int(input("Digite um número par: "))
while num % 2 != 0:
    print("Número inválido. Tente novamente.")
    num = int(input("Digite um número par: "))
print(f"Obrigado! Você digitou o número par {num}.")