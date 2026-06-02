"""CLI da Amostragem Sistemática.

Responsável apenas por entrada/saída no terminal; a regra de negócio
(cálculo do intervalo, sorteio da semente e geração) vive em :mod:`amostragem`.
"""

from amostragem import amostra_sistematica


def ler_inteiro(mensagem):
    """Lê um inteiro do usuário, repetindo até receber valor válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("⚠️  Digite um número inteiro válido.")


def main():
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

    populacao = ler_inteiro("📊 Digite o valor da sua população: ")
    amostra = ler_inteiro("📈 Digite o tamanho da amostra desejada: ")
    print()

    try:
        r = amostra_sistematica(populacao, amostra)
    except ValueError as e:
        print(f"❌ {e}")
        return

    print("=" * 70)
    print("                    CÁLCULOS                    ".center(70))
    print("=" * 70)
    print()
    print(f"✅ População: {r['populacao']}")
    print(f"✅ Amostra desejada: {r['amostra_desejada']}")
    print(f"✅ Intervalo (salto): {r['intervalo']:.2f} ≈ {r['intervalo_int']}")
    print()
    print("-" * 70)
    print()
    print("💡 PROCEDIMENTO:")
    print(f"   1. Dividimos {r['populacao']} por {r['amostra_desejada']} = {r['intervalo']:.2f}")
    print(f"   2. Sorteamos a semente entre 1 e {r['intervalo_int']}: resultado = {r['semente']}")
    print(f"   3. A partir de {r['semente']}, saltamos de {r['intervalo_int']} em {r['intervalo_int']}")
    print()
    print("=" * 70)
    print("                    RESULTADO                    ".center(70))
    print("=" * 70)
    print()
    print(f"🎲 Semente sorteada: {r['semente']}")
    print()
    print("✅ Elementos selecionados para a amostra:")
    print(f"   {r['elementos']}")
    print()
    print(f"📊 Total de elementos na amostra: {len(r['elementos'])}")
    print()
    print("=" * 70)


if __name__ == "__main__":
    main()
