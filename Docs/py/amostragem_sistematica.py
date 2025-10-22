from browser import document, html
import random

def calcular_sistematica(ev):
    """Calcula a amostragem sistemática"""
    try:
        # Obter valores dos inputs
        populacao = int(document["populacao_sist"].value)
        amostra_desejada = int(document["amostra_sist"].value)
        
        # Validações
        if populacao <= 0:
            mostrar_erro_sist("A população deve ser maior que zero!")
            return
        
        if amostra_desejada <= 0:
            mostrar_erro_sist("O tamanho da amostra deve ser maior que zero!")
            return
        
        if amostra_desejada > populacao:
            mostrar_erro_sist("A amostra não pode ser maior que a população!")
            return
        
        # Cálculo do intervalo
        intervalo = populacao / amostra_desejada
        intervalo_int = int(intervalo)
        
        # Sorteio da semente
        semente = random.randint(1, intervalo_int)
        
        # Geração dos elementos da amostra
        elementos_selecionados = list(range(semente, populacao + 1, intervalo_int))
        
        # Limitar ao tamanho desejado (caso necessário)
        elementos_selecionados = elementos_selecionados[:amostra_desejada]
        
        # Montar resultado
        resultado_div = document["resultado_sist"]
        resultado_div.clear()
        resultado_div.class_name = "result-box show"
        
        # Título
        resultado_div <= html.H3("✅ RESULTADO")
        
        # Informações principais
        info_box = html.DIV(Class="result-item")
        info_box <= html.P(f"🎯 População total: {populacao:,} elementos".replace(',', '.'))
        info_box <= html.P(f"📊 Amostra desejada: {amostra_desejada:,} elementos".replace(',', '.'))
        info_box <= html.P(f"📏 Intervalo (salto): {intervalo:.2f} ≈ {intervalo_int}")
        info_box <= html.P(html.STRONG(f"🎲 Semente sorteada: {semente}"))
        resultado_div <= info_box
        
        # Cálculo detalhado
        calc_box = html.DIV(Class="calculation")
        calc_box <= html.P(html.STRONG("💡 PROCEDIMENTO:"))
        calc_box <= html.P(f"1. Dividimos {populacao} por {amostra_desejada} = {intervalo:.2f}")
        calc_box <= html.P(f"2. Sorteamos a semente entre 1 e {intervalo_int}: resultado = {semente}")
        calc_box <= html.P(f"3. A partir de {semente}, saltamos de {intervalo_int} em {intervalo_int}")
        resultado_div <= calc_box
        
        # Elementos selecionados
        sample_box = html.DIV(Class="sample-list")
        sample_box <= html.P(html.STRONG("✅ ELEMENTOS SELECIONADOS:"))
        
        # Formatar a lista de elementos
        elementos_str = str(elementos_selecionados)
        if len(elementos_selecionados) > 20:
            # Se for muito grande, mostrar apenas início e fim
            primeiros = elementos_selecionados[:10]
            ultimos = elementos_selecionados[-10:]
            elementos_str = f"{primeiros[0]}, {primeiros[1]}, {primeiros[2]}, ..., {ultimos[-3]}, {ultimos[-2]}, {ultimos[-1]}"
            sample_box <= html.P(f"[{elementos_str}]")
            sample_box <= html.P(f"(Mostrando início e fim da lista)")
        else:
            sample_box <= html.P(elementos_str)
        
        sample_box <= html.P(html.STRONG(f"📊 Total de elementos na amostra: {len(elementos_selecionados)}"))
        resultado_div <= sample_box
        
    except ValueError:
        mostrar_erro_sist("Por favor, preencha todos os campos com valores válidos!")
    except Exception as e:
        mostrar_erro_sist(f"Erro ao calcular: {str(e)}")

def mostrar_erro_sist(mensagem):
    """Mostra mensagem de erro"""
    resultado_div = document["resultado_sist"]
    resultado_div.clear()
    resultado_div.class_name = "result-box show"
    resultado_div <= html.P(f"❌ {mensagem}", style={"color": "#ef4444", "font-weight": "bold"})

# Vincular evento ao botão
document["calcular_sist"].bind("click", calcular_sistematica)
