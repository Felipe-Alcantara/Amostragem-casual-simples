print("Nesse tipo de amostragem cada elemento da amostra é escolhido por sorteio individual a partir da população, normalmente uma porcentagem da população")


Populacao = int(input("Digite a quantidade de elementos na sua população: "))
Porcentagem = float(input("Digite a porcentagem que retirará da amostra: "))

ElementosNaAmostra = ((Populacao * Porcentagem)/100)
print("Terão {} elementos na sua amostra".format(ElementosNaAmostra))

print("Pode-se inserir os {} elementos em uma urna e retirar, aleatoriamente, {}.".format(Populacao, ElementosNaAmostra))