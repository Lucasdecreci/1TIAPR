#preciso criar uma lista com 3 strings e concatenar em uma unica string separada por virgula

lista_frutas = ["maçã", "banana", "laranja"]
frutas_concatenadas = ", ".join(lista_frutas)
print(frutas_concatenadas)  # Saída: maçã, banana, laranja
#o que faz o metodo join?
#o metodo join concatena os elementos de uma lista em uma unica string, separando-os pelo caractere especificado (neste caso, uma vírgula seguida de um espaço). 