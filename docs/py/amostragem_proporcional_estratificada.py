"""Camada de apresentação (DOM) da Amostragem Estratificada na versão web.

O cálculo das proporções e tamanhos de cada estrato vem de :mod:`amostragem`
(mesmo módulo da CLI). Os sorteios ilustrativos por estrato e a demonstração
sistemática são apenas apresentação e usam ``random`` diretamente aqui.
"""

import random

from browser import document, html

from amostragem import amostra_estratificada


def calcular_estratificada(ev):
    try:
        estrato1 = int(document["estrato1"].value)
        estrato2 = int(document["estrato2"].value)
        porcentagem = float(document["porcentagem_estrat"].value)
    except ValueError:
        mostrar_erro_estrat("Por favor, preencha todos os campos com valores válidos!")
        return

    try:
        r = amostra_estratificada(estrato1, estrato2, porcentagem)
    except ValueError as e:
        mostrar_erro_estrat(str(e))
        return

    total_populacao = r["total"]
    proporcao1 = r["proporcao_1"]
    proporcao2 = r["proporcao_2"]
    amostra1 = r["amostra_1"]
    amostra2 = r["amostra_2"]
    total_amostra = int((porcentagem / 100) * total_populacao)

    # Ajuste de arredondamento para a soma bater com o total da amostra.
    if (amostra1 + amostra2) != total_amostra and total_amostra > 0:
        diferenca = total_amostra - (amostra1 + amostra2)
        if proporcao1 > proporcao2:
            amostra1 += diferenca
        else:
            amostra2 += diferenca

    resultado_div = document["resultado_estrat"]
    resultado_div.clear()
    resultado_div.class_name = "result-box show"
    resultado_div <= html.H3("✅ RESULTADO")

    info_box = html.DIV(Class="result-item")
    info_box <= html.P(html.STRONG("📊 POPULAÇÃO:"))
    info_box <= html.P(f"Estrato 1: {estrato1:,} elementos".replace(',', '.'))
    info_box <= html.P(f"Estrato 2: {estrato2:,} elementos".replace(',', '.'))
    info_box <= html.P(f"Total: {total_populacao:,} elementos".replace(',', '.'))
    info_box <= html.P(f"Porcentagem da amostra: {porcentagem}%")
    resultado_div <= info_box

    calc_box = html.DIV(Class="calculation")
    calc_box <= html.P(html.STRONG("💡 CÁLCULO DAS PROPORÇÕES:"))
    calc_box <= html.P(f"Estrato 1: {estrato1}/{total_populacao} = {proporcao1:.2%}")
    calc_box <= html.P(f"Estrato 2: {estrato2}/{total_populacao} = {proporcao2:.2%}")
    calc_box <= html.P(f"Total da amostra: {porcentagem}% de {total_populacao} = {total_amostra} elementos")
    resultado_div <= calc_box

    sample_box = html.DIV(Class="sample-list")
    sample_box <= html.P(html.STRONG("✅ DISTRIBUIÇÃO DA AMOSTRA:"))
    sample_box <= html.P(f"Estrato 1: {proporcao1:.2%} × {total_amostra} = {amostra1} elementos")
    sample_box <= html.P(f"Estrato 2: {proporcao2:.2%} × {total_amostra} = {amostra2} elementos")
    sample_box <= html.P(html.STRONG(f"📊 Total: {amostra1 + amostra2} elementos"))
    resultado_div <= sample_box

    sorteios_box = html.DIV(Class="sample-list")
    sorteios_box <= html.P(html.STRONG("🎲 SORTEIOS REALIZADOS:"))
    sorteios_box <= html.BR()
    _renderizar_sorteio(sorteios_box, "Estrato 1", amostra1, estrato1)
    _renderizar_sorteio(sorteios_box, "Estrato 2", amostra2, estrato2)
    resultado_div <= sorteios_box

    proc_box = html.DIV(Class="sample-list")
    proc_box <= html.P(html.STRONG("📝 PROCEDIMENTO:"))
    proc_box <= html.P(
        "Aplicamos amostragem casual simples em cada estrato para selecionar "
        "os elementos da amostra, garantindo aleatoriedade e representatividade "
        "proporcional de cada grupo."
    )
    resultado_div <= proc_box


def _renderizar_sorteio(container, rotulo, quantidade, tamanho_estrato):
    """Sorteia e renderiza os elementos de um estrato (camada de apresentação)."""
    if quantidade <= 0 or quantidade > tamanho_estrato:
        return
    sorteados = random.sample(range(1, tamanho_estrato + 1), quantidade)
    sorteados.sort()
    container <= html.P(html.STRONG(f"📍 {rotulo} - Sorteio de {quantidade} elementos:"))
    if quantidade <= 20:
        container <= html.P(f"  {sorteados}", Class="mono")
    else:
        container <= html.P(f"  Primeiros 10: {sorteados[:10]}", Class="mono")
        container <= html.P(f"  Últimos 10: {sorteados[-10:]}", Class="mono")
    container <= html.BR()


def mostrar_erro_estrat(mensagem):
    resultado_div = document["resultado_estrat"]
    resultado_div.clear()
    resultado_div.class_name = "result-box show"
    resultado_div <= html.P(f"❌ {mensagem}", Class="error-msg")


document["calcular_estrat"].bind("click", calcular_estratificada)
