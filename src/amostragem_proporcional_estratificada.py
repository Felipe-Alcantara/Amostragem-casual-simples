import random

print("=" * 70)
print("     AMOSTRAGEM PROPORCIONAL ESTRATIFICADA     ".center(70))
print("=" * 70)
print()

print("📌 DEFINIÇÃO:")
print("   Quando o experimento estatístico deve escolher elementos de uma")
print("   população estratificada (particionada), deve-se garantir que a")
print("   representatividade proporcional de cada estrato componha a amostra.")
print()
print("-" * 70)
print()

# Entrada de dados - Estratos
print("📊 DADOS DOS ESTRATOS:")
print()
populacao_1 = int(input("   Estrato 1 - Número de elementos: "))
populacao_2 = int(input("   Estrato 2 - Número de elementos: "))
total = populacao_1 + populacao_2

print()
print(f"   ✅ População total: {total} elementos")
print()
print("-" * 70)
print()

# Entrada da porcentagem
porcentagem = float(input("📈 Digite a porcentagem que retirará da amostra (%): "))
print()

print("=" * 70)
print("                    CÁLCULOS                    ".center(70))
print("=" * 70)
print()

# Cálculos das proporções
proporcao_1 = (populacao_1 / total)
proporcao_2 = (populacao_2 / total)
total_da_amostra = int((porcentagem / 100) * total)

amostra_1 = int(round(proporcao_1 * total_da_amostra))
amostra_2 = int(round(proporcao_2 * total_da_amostra))

print(f"Estrato 1:")
print(f"   • Proporção: {proporcao_1:.2%} ({populacao_1}/{total})")
print(f"   • Elementos na amostra: {amostra_1}")
print()
print(f"Estrato 2:")
print(f"   • Proporção: {proporcao_2:.2%} ({populacao_2}/{total})")
print(f"   • Elementos na amostra: {amostra_2}")
print()
print(f"Total da amostra: {amostra_1 + amostra_2} elementos ({porcentagem}% de {total})")
print()
print("-" * 70)
print()
print("💡 PROCEDIMENTO:")
print("   Devemos dividir os estratos e aplicar amostragem casual simples")
print("   em cada estrato para selecionar os elementos da amostra,")
print("   garantindo assim aleatoriedade e justiça na composição.")
print()

print("=" * 70)
print("          DEMONSTRAÇÃO: AMOSTRAGEM SISTEMÁTICA          ".center(70))
print("=" * 70)
print()

print("📌 MÉTODO ALTERNATIVO:")
print("   Podemos utilizar amostragem sistemática para selecionar elementos.")
print(f"   Inserimos números de 1 a {total} e sorteamos uma 'semente'.")
print("   Farão parte da amostra todos os números terminados pelo valor sorteado.")
print()
print("-" * 70)
print()

print("🎲 Sorteando semente...")
semente = random.randint(1, 9)
print()
print(f"   Semente sorteada: {semente}")
print()

# Gerando os números sorteados com base na semente e salto de 10
numeros_sorteados = list(range(semente, total + 1, 10))

# Limitando o número de elementos sorteados
numeros_sorteados = numeros_sorteados[:total_da_amostra]

print("=" * 70)
print("                    RESULTADO FINAL                    ".center(70))
print("=" * 70)
print()
print("📊 AMOSTRA PROPORCIONAL ESTRATIFICADA:")
print(f"   • Estrato 1: {amostra_1} elementos")
print(f"   • Estrato 2: {amostra_2} elementos")
print(f"   • Total: {amostra_1 + amostra_2} elementos")
print()
print("-" * 70)
print()
print("📊 DEMONSTRAÇÃO - AMOSTRAGEM SISTEMÁTICA:")
print(f"   Elementos selecionados (terminados em {semente}):")
print(f"   {numeros_sorteados}")
print()
print(f"   Total de elementos: {len(numeros_sorteados)}")
print()
print("=" * 70)