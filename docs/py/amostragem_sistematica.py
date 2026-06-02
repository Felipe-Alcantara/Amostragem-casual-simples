"""Camada de apresentação (DOM) da Amostragem Sistemática na versão web.

A regra de negócio vem de :mod:`amostragem` (mesmo módulo da CLI). Este
arquivo só lê os inputs, chama a função pura e renderiza o resultado.
"""

from browser import document, html

from amostragem import amostra_sistematica


def calcular_sistematica(ev):
    try:
        populacao = int(document["populacao_sist"].value)
        amostra_desejada = int(document["amostra_sist"].value)
    except ValueError:
        mostrar_erro_sist("Por favor, preencha todos os campos com valores válidos!")
        return

    try:
        r = amostra_sistematica(populacao, amostra_desejada)
    except ValueError as e:
        mostrar_erro_sist(str(e))
        return

    intervalo = r["intervalo"]
    intervalo_int = r["intervalo_int"]
    semente = r["semente"]
    elementos = r["elementos"]

    resultado_div = document["resultado_sist"]
    resultado_div.clear()
    resultado_div.class_name = "result-box show"
    resultado_div <= html.H3("✅ RESULTADO")

    info_box = html.DIV(Class="result-item")
    info_box <= html.P(f"🎯 População total: {populacao:,} elementos".replace(',', '.'))
    info_box <= html.P(f"📊 Amostra desejada: {amostra_desejada:,} elementos".replace(',', '.'))
    info_box <= html.P(f"📏 Intervalo (salto): {intervalo:.2f} ≈ {intervalo_int}")
    info_box <= html.P(html.STRONG(f"🎲 Semente sorteada: {semente}"))
    resultado_div <= info_box

    calc_box = html.DIV(Class="calculation")
    calc_box <= html.P(html.STRONG("💡 PROCEDIMENTO:"))
    calc_box <= html.P(f"1. Dividimos {populacao} por {amostra_desejada} = {intervalo:.2f}")
    calc_box <= html.P(f"2. Sorteamos a semente entre 1 e {intervalo_int}: resultado = {semente}")
    calc_box <= html.P(f"3. A partir de {semente}, saltamos de {intervalo_int} em {intervalo_int}")
    resultado_div <= calc_box

    sample_box = html.DIV(Class="sample-list")
    sample_box <= html.P(html.STRONG("✅ ELEMENTOS SELECIONADOS:"))
    sample_box <= html.P(f"🎲 Semente sorteada: {semente}")
    sample_box <= html.BR()
    if len(elementos) <= 30:
        sample_box <= html.P(f"Amostra completa: {elementos}", Class="mono")
    else:
        sample_box <= html.P(f"Primeiros 15: {elementos[:15]}", Class="mono")
        sample_box <= html.P("...")
        sample_box <= html.P(f"Últimos 15: {elementos[-15:]}", Class="mono")
    sample_box <= html.BR()
    sample_box <= html.P(html.STRONG(f"📊 Total de elementos na amostra: {len(elementos)}"))
    resultado_div <= sample_box


def mostrar_erro_sist(mensagem):
    resultado_div = document["resultado_sist"]
    resultado_div.clear()
    resultado_div.class_name = "result-box show"
    resultado_div <= html.P(f"❌ {mensagem}", Class="error-msg")


document["calcular_sist"].bind("click", calcular_sistematica)
