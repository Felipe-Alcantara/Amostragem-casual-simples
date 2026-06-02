"""CLI da Amostragem Casual Simples (ACS).

Responsável apenas por entrada/saída no terminal; a regra de negócio
(cálculo e sorteio) vive em :mod:`amostragem`.
"""

from amostragem import amostra_casual_simples


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
    print("          AMOSTRAGEM CASUAL SIMPLES (ACS)          ".center(70))
    print("=" * 70)
    print()
    print("📌 DEFINIÇÃO:")
    print("   Nesse tipo de amostragem, cada elemento da amostra é escolhido")
    print("   por sorteio individual a partir da população.")
    print("   Normalmente utilizamos uma porcentagem da população total.")
    print()
    print("-" * 70)
    print()

    populacao = ler_inteiro("📊 Digite a quantidade de elementos na sua população: ")
    porcentagem = ler_float("📈 Digite a porcentagem que retirará da amostra (%): ")
    print()

    try:
        r = amostra_casual_simples(populacao, porcentagem)
    except ValueError as e:
        print(f"❌ {e}")
        return

    print("=" * 70)
    print("                    RESULTADO                    ".center(70))
    print("=" * 70)
    print()
    print(f"✅ População total: {r['populacao']} elementos")
    print(f"✅ Porcentagem da amostra: {r['porcentagem']}%")
    print(f"✅ Tamanho da amostra: {r['tamanho_amostra']} elementos")
    print()
    print("-" * 70)
    print()
    print("🎲 SORTEIO REALIZADO (sem repetição):")
    print(f"   {r['elementos']}")
    print()
    print("💡 PROCEDIMENTO:")
    print(f"   Cada um dos {r['populacao']} elementos teve a mesma probabilidade")
    print(f"   de ser selecionado para compor a amostra de {r['tamanho_amostra']}.")
    print()
    print("=" * 70)


if __name__ == "__main__":
    main()
