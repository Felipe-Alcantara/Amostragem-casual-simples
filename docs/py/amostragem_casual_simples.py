"""Camada de apresentação (DOM) da Amostragem Casual Simples na versão web.

A regra de negócio vem de :mod:`amostragem` (mesmo módulo da CLI). Este
arquivo só lê os inputs, chama a função pura e renderiza o resultado.
"""

from browser import document, html

from amostragem import amostra_casual_simples


def calcular_casual_simples(ev):
    try:
        populacao = int(document["populacao_casual"].value)
        porcentagem = float(document["porcentagem_casual"].value)
    except ValueError:
        mostrar_erro_casual("Por favor, preencha todos os campos com valores válidos!")
        return

    try:
        r = amostra_casual_simples(populacao, porcentagem)
    except ValueError as e:
        mostrar_erro_casual(str(e))
        return

    elementos = r["elementos"]
    tamanho = r["tamanho_amostra"]

    resultado_div = document["resultado_casual"]
    resultado_div.clear()
    resultado_div.class_name = "result-box show"
    resultado_div <= html.H3("✅ RESULTADO")

    info_box = html.DIV(Class="result-item")
    info_box <= html.P(f"🎯 População total: {populacao:,} elementos".replace(',', '.'))
    info_box <= html.P(f"📊 Porcentagem da amostra: {porcentagem}%")
    info_box <= html.P(html.STRONG(f"📈 Tamanho da amostra: {tamanho:,} elementos".replace(',', '.')))
    resultado_div <= info_box

    calc_box = html.DIV(Class="calculation")
    calc_box <= html.P(html.STRONG("💡 CÁLCULO:"))
    calc_box <= html.P("Amostra = (População × Porcentagem) / 100")
    calc_box <= html.P(f"Amostra = ({populacao} × {porcentagem}) / 100 = {tamanho}")
    resultado_div <= calc_box

    sorteio_box = html.DIV(Class="sample-list")
    sorteio_box <= html.P(html.STRONG("🎲 SORTEIO REALIZADO:"))
    sorteio_box <= html.P(f"Os {tamanho} elementos foram sorteados aleatoriamente da população:")
    sorteio_box <= html.BR()
    if tamanho <= 50:
        sorteio_box <= html.P(f"Elementos sorteados: {elementos}", Class="mono")
    else:
        sorteio_box <= html.P(f"Primeiros 10: {elementos[:10]}", Class="mono")
        sorteio_box <= html.P(f"Últimos 10: {elementos[-10:]}", Class="mono")
        sorteio_box <= html.P(f"(Total de {tamanho} elementos sorteados)")
    resultado_div <= sorteio_box

    proc_box = html.DIV(Class="calculation")
    proc_box <= html.P(html.STRONG("📝 PROCEDIMENTO REALIZADO:"))
    proc_box <= html.P("1️⃣ Criamos uma população numerada de 1 até " + f"{populacao:,}".replace(',', '.'))
    proc_box <= html.P(f"2️⃣ Sorteamos aleatoriamente {tamanho} elementos SEM repetição")
    proc_box <= html.P("3️⃣ Cada elemento teve a mesma probabilidade de ser selecionado")
    proc_box <= html.P(f"4️⃣ Probabilidade de seleção: {porcentagem}% ou {porcentagem/100:.4f}")
    resultado_div <= proc_box


def mostrar_erro_casual(mensagem):
    resultado_div = document["resultado_casual"]
    resultado_div.clear()
    resultado_div.class_name = "result-box show"
    resultado_div <= html.P(f"❌ {mensagem}", Class="error-msg")


document["calcular_casual"].bind("click", calcular_casual_simples)
