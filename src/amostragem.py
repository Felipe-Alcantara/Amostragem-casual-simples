"""Lógica pura das técnicas de amostragem probabilística.

Este módulo contém apenas regra de negócio: cálculo e sorteio.
Não faz entrada/saída (nem `input`/`print`, nem manipulação de DOM),
para que possa ser reutilizado pela versão CLI (`src/`) e pela versão
web em Brython (`docs/`), além de ser testável de forma isolada.
"""

import random


def amostra_casual_simples(populacao, porcentagem, rng=random):
    """Calcula e sorteia uma amostra casual simples (sem reposição).

    Cada elemento tem a mesma probabilidade de ser selecionado.

    Args:
        populacao: total de elementos da população (inteiro > 0).
        porcentagem: percentual da população a amostrar (0 < x <= 100).
        rng: fonte de aleatoriedade (default: módulo ``random``); facilita teste.

    Returns:
        dict com ``populacao``, ``porcentagem``, ``tamanho_amostra`` e
        ``elementos`` (lista ordenada dos elementos sorteados de 1..populacao).

    Raises:
        ValueError: se a população não for positiva, a porcentagem estiver
            fora de (0, 100] ou a amostra resultante for zero.
    """
    if populacao <= 0:
        raise ValueError("A população deve ser maior que zero.")
    if porcentagem <= 0 or porcentagem > 100:
        raise ValueError("A porcentagem deve estar entre 0 (exclusivo) e 100.")

    tamanho_amostra = int((populacao * porcentagem) / 100)
    if tamanho_amostra == 0:
        raise ValueError("A amostra calculada é zero. Aumente a porcentagem.")

    elementos = rng.sample(range(1, populacao + 1), tamanho_amostra)
    elementos.sort()

    return {
        "populacao": populacao,
        "porcentagem": porcentagem,
        "tamanho_amostra": tamanho_amostra,
        "elementos": elementos,
    }


def amostra_sistematica(populacao, amostra_desejada, rng=random):
    """Calcula e sorteia uma amostra sistemática.

    Usa uma 'semente' sorteada e um intervalo fixo (salto) para selecionar
    elementos, reduzindo a quantidade de sorteios.

    Args:
        populacao: total de elementos da população (inteiro > 0).
        amostra_desejada: tamanho da amostra (0 < x <= populacao).
        rng: fonte de aleatoriedade (default: módulo ``random``).

    Returns:
        dict com ``populacao``, ``amostra_desejada``, ``intervalo``,
        ``semente`` e ``elementos`` (lista dos elementos selecionados).

    Raises:
        ValueError: se a população não for positiva, a amostra não for
            positiva ou a amostra exceder a população.
    """
    if populacao <= 0:
        raise ValueError("A população deve ser maior que zero.")
    if amostra_desejada <= 0:
        raise ValueError("O tamanho da amostra deve ser maior que zero.")
    if amostra_desejada > populacao:
        raise ValueError("A amostra não pode ser maior que a população.")

    intervalo = populacao / amostra_desejada
    intervalo_int = int(intervalo)
    semente = rng.randint(1, intervalo_int)

    elementos = list(range(semente, populacao + 1, intervalo_int))
    elementos = elementos[:amostra_desejada]

    return {
        "populacao": populacao,
        "amostra_desejada": amostra_desejada,
        "intervalo": intervalo,
        "intervalo_int": intervalo_int,
        "semente": semente,
        "elementos": elementos,
    }


def amostra_estratificada(estrato_1, estrato_2, porcentagem):
    """Calcula a amostra proporcional estratificada de dois estratos.

    Garante representatividade proporcional de cada estrato na amostra final.

    Args:
        estrato_1: número de elementos do estrato 1 (inteiro > 0).
        estrato_2: número de elementos do estrato 2 (inteiro > 0).
        porcentagem: percentual da população total a amostrar (0 < x <= 100).

    Returns:
        dict com ``total``, ``porcentagem``, ``proporcao_1``, ``proporcao_2``,
        ``amostra_1``, ``amostra_2`` e ``total_amostra``.

    Raises:
        ValueError: se algum estrato não for positivo ou a porcentagem
            estiver fora de (0, 100].
    """
    if estrato_1 <= 0 or estrato_2 <= 0:
        raise ValueError("Cada estrato deve ter mais de zero elementos.")
    if porcentagem <= 0 or porcentagem > 100:
        raise ValueError("A porcentagem deve estar entre 0 (exclusivo) e 100.")

    total = estrato_1 + estrato_2
    proporcao_1 = estrato_1 / total
    proporcao_2 = estrato_2 / total
    total_amostra = int((porcentagem / 100) * total)

    amostra_1 = int(round(proporcao_1 * total_amostra))
    amostra_2 = int(round(proporcao_2 * total_amostra))

    return {
        "total": total,
        "porcentagem": porcentagem,
        "proporcao_1": proporcao_1,
        "proporcao_2": proporcao_2,
        "amostra_1": amostra_1,
        "amostra_2": amostra_2,
        "total_amostra": amostra_1 + amostra_2,
    }
