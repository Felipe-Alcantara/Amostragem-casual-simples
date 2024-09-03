import random

print("Primeiro, vamos ver a amostragem proporcional estratificada")

print(" ")

print("Quando o experimento estatístico deve escolhe elementos de uma população estratificada (particionada), deve-se garantir que a representatividade proporcional de cada estrato componha a amostra.")

print(" ")

Populacao_1 = int(input("Digite o valor dos elementos no primeiro estrato: "))
Populacao_2 = int(input("Digite o valor dos elementos no segundo estrato: "))
Total = Populacao_1 + Populacao_2

print(" ")

print("A população total de elementos é de: {}".format(Total))

print(" ")

Porcentagem = float(input("Digite a porcentagem que retirará da amostra: "))

print(" ")

print("Devemos então dividir os estratos e aplicar amostragem casual simples em cada estrato para selecionar os elementos da amostra, garantindo, assim aleatoriedade e justiça na composição da amostra.")

print(" ")

Proporcao_1 = (Populacao_1 / Total)
Proporcao_2 = (Populacao_2 / Total)
Total_da_Percent = int((Porcentagem / 100) * Total)  # Convertendo para inteiro

Amostra_1 = (Proporcao_1 * Total_da_Percent)
Amostra_2 = (Proporcao_2 * Total_da_Percent)

print("Amostra final")
print("População 1: {}".format((round(Amostra_1))))
print("População 2: {}".format((round(Amostra_2))))

print(" ")

print("Agora, veremos a amostragem sistemática")

print(" ")

print("Geram-se sistemas que reduzem a quantidade de sorteios para escolher elementos para a composição da amostra")

print(" ")

print("Pode-se inserir os números de 0 a {} em uma urna e retirar, aleatoriamente, um número, chamado semente. Farão parte dessa amostra todos os números terminados pelo valor sorteado.".format(Total_da_Percent))

print("agora, vamos sortear uma semente para selecionar os elementos na amostra")

print(" ")

semente = random.randint(1, 9)  # Sorteando a semente entre 1 e 9
print("O numero sorteado é {}".format(semente))

print(" ")

# Gerando os números sorteados com base na semente e salto de 10
numeros_sorteados = list(range(semente, Total + 1, 10))

print(" ")

# Limitando o número de elementos sorteados ao valor de Total_da_Percent
numeros_sorteados = numeros_sorteados[:Total_da_Percent]

print("Os numeros sorteados a partir da semente são: {}".format(numeros_sorteados))