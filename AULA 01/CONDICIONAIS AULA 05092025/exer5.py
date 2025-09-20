Desconto = 10
produto = 5.99

input("Bem vindo a Chico Store")

quantidade = int(input("Digite a quantidade desejada: "))

if quantidade > 10:
    print(f"Você ganhou {Desconto}% de desconto, valor total: R${(produto * quantidade) * (1 - Desconto / 100):.2f}")


else:
    print(f"Você não ganhou desconto")


