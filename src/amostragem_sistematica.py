import random

print("=" * 70)
print("          AMOSTRAGEM SISTEMÁTICA          ".center(70))
print("=" * 70)
print()

print("📌 DEFINIÇÃO:")
print("   Geram-se sistemas que reduzem a quantidade de sorteios para")
print("   escolher elementos para a composição da amostra.")
print("   O método utiliza uma 'semente' sorteada e um intervalo fixo (salto).")
print()
print("-" * 70)
print()

# Entrada de dados
populacao = int(input("📊 Digite o valor da sua população: "))
amostra = int(input("📈 Digite o tamanho da amostra desejada: "))
print()

# Cálculo do intervalo (salto)
intervalo = populacao / amostra

print("=" * 70)
print("                    CÁLCULOS                    ".center(70))
print("=" * 70)
print()
print(f"✅ População: {populacao}")
print(f"✅ Amostra desejada: {amostra}")
print(f"✅ Intervalo (salto): {intervalo:.2f} ≈ {int(intervalo)}")
print()
print("-" * 70)
print()
print("💡 PROCEDIMENTO:")
print(f"   1. Dividimos {populacao} por {amostra} = {intervalo:.2f}")
print(f"   2. Sorteamos um valor inicial (semente) entre 1 e {int(intervalo)}")
print(f"   3. A partir da semente, saltamos de {int(intervalo)} em {int(intervalo)}")
print("      até completar a amostra")
print()

# Sorteio da semente
valor_sorteado = random.randint(1, int(intervalo))

# Geração dos números sorteados
numeros_sorteados = list(range(valor_sorteado, populacao + 1, int(intervalo)))

print("=" * 70)
print("                    RESULTADO                    ".center(70))
print("=" * 70)
print()
print(f"🎲 Semente sorteada: {valor_sorteado}")
print()
print(f"✅ Elementos selecionados para a amostra:")
print(f"   {numeros_sorteados}")
print()
print(f"📊 Total de elementos na amostra: {len(numeros_sorteados)}")
print()
print("=" * 70)