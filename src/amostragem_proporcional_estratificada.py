"""CLI da Amostragem Proporcional Estratificada.

Responsável apenas por entrada/saída no terminal; a regra de negócio
(proporções e tamanho de cada estrato na amostra) vive em :mod:`amostragem`.
"""

from amostragem import amostra_estratificada


def ler_inteiro(mensagem):
    """Lê um inteiro do usuário, repetindo até receber valor válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("⚠️  Digite um número inteiro válido.")


def ler_float(mensagem):
    """Lê um número real do usuário, repetindo até receber valor válido."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("⚠️  Digite um número válido.")


def main():
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

    print("📊 DADOS DOS ESTRATOS:")
    print()
    estrato_1 = ler_inteiro("   Estrato 1 - Número de elementos: ")
    estrato_2 = ler_inteiro("   Estrato 2 - Número de elementos: ")
    print()
    porcentagem = ler_float("📈 Digite a porcentagem que retirará da amostra (%): ")
    print()

    try:
        r = amostra_estratificada(estrato_1, estrato_2, porcentagem)
    except ValueError as e:
        print(f"❌ {e}")
        return

    print("=" * 70)
    print("                    CÁLCULOS                    ".center(70))
    print("=" * 70)
    print()
    print(f"   ✅ População total: {r['total']} elementos")
    print()
    print("Estrato 1:")
    print(f"   • Proporção: {r['proporcao_1']:.2%} ({estrato_1}/{r['total']})")
    print(f"   • Elementos na amostra: {r['amostra_1']}")
    print()
    print("Estrato 2:")
    print(f"   • Proporção: {r['proporcao_2']:.2%} ({estrato_2}/{r['total']})")
    print(f"   • Elementos na amostra: {r['amostra_2']}")
    print()
    print(f"Total da amostra: {r['total_amostra']} elementos "
          f"({r['porcentagem']}% de {r['total']})")
    print()
    print("-" * 70)
    print()
    print("💡 PROCEDIMENTO:")
    print("   Devemos dividir os estratos e aplicar amostragem casual simples")
    print("   em cada estrato para selecionar os elementos da amostra,")
    print("   garantindo assim aleatoriedade e justiça na composição.")
    print()
    print("=" * 70)


if __name__ == "__main__":
    main()
