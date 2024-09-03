import random

print("Geram-se sistemas que reduzem a quantidade de sorteios para escolher elementos para a composição da amostra")

print(" ")

populacao = int(input("Digite o valor da sua população: "))
amostra = int(input("Digite a amostra da sua população: "))
divisao = (populacao / amostra)

print("Podemos dividir {} por {}. Acharemos {}, escolhemos aleatoriamente a semente a partir de um sorteio dos valores de 1 a {}, saltando de {} a {} escolhemos a amostra".format(populacao, amostra, divisao, divisao, divisao, divisao))

valor_sorteado = random.randint(1, divisao)

numeros_sorteados = list(range(valor_sorteado, populacao + 1, int(divisao)))

print("Suponha se seja sorteado o valor {}. Então a amostra seria: {}".format(valor_sorteado, numeros_sorteados))