from browser import document, html
import random

def calcular_estratificada(ev):
    """Calcula a amostragem proporcional estratificada"""
    try:
        # Obter valores dos inputs
        estrato1 = int(document["estrato1"].value)
        estrato2 = int(document["estrato2"].value)
        porcentagem = float(document["porcentagem_estrat"].value)
        
        # Validações
        if estrato1 <= 0 or estrato2 <= 0:
            mostrar_erro_estrat("Os estratos devem ser maiores que zero!")
            return
        
        if porcentagem <= 0 or porcentagem > 100:
            mostrar_erro_estrat("A porcentagem deve estar entre 0 e 100!")
            return
        
        # Cálculos
        total_populacao = estrato1 + estrato2
        
        proporcao1 = estrato1 / total_populacao
        proporcao2 = estrato2 / total_populacao
        
        total_amostra = int((porcentagem / 100) * total_populacao)
        
        amostra1 = int(round(proporcao1 * total_amostra))
        amostra2 = int(round(proporcao2 * total_amostra))
        
        # Ajuste para garantir que a soma seja exata
        amostra_total_calculada = amostra1 + amostra2
        if amostra_total_calculada != total_amostra and total_amostra > 0:
            diferenca = total_amostra - amostra_total_calculada
            if proporcao1 > proporcao2:
                amostra1 += diferenca
            else:
                amostra2 += diferenca
        
        # Montar resultado
        resultado_div = document["resultado_estrat"]
        resultado_div.clear()
        resultado_div.class_name = "result-box show"
        
        # Título
        resultado_div <= html.H3("✅ RESULTADO")
        
        # Informações da população
        info_box = html.DIV(Class="result-item")
        info_box <= html.P(html.STRONG("📊 POPULAÇÃO:"))
        info_box <= html.P(f"Estrato 1: {estrato1:,} elementos".replace(',', '.'))
        info_box <= html.P(f"Estrato 2: {estrato2:,} elementos".replace(',', '.'))
        info_box <= html.P(f"Total: {total_populacao:,} elementos".replace(',', '.'))
        info_box <= html.P(f"Porcentagem da amostra: {porcentagem}%")
        resultado_div <= info_box
        
        # Cálculo das proporções
        calc_box = html.DIV(Class="calculation")
        calc_box <= html.P(html.STRONG("💡 CÁLCULO DAS PROPORÇÕES:"))
        calc_box <= html.P(f"Estrato 1: {estrato1}/{total_populacao} = {proporcao1:.2%}")
        calc_box <= html.P(f"Estrato 2: {estrato2}/{total_populacao} = {proporcao2:.2%}")
        calc_box <= html.P(f"Total da amostra: {porcentagem}% de {total_populacao} = {total_amostra} elementos")
        resultado_div <= calc_box
        
        # Distribuição da amostra
        sample_box = html.DIV(Class="sample-list")
        sample_box <= html.P(html.STRONG("✅ DISTRIBUIÇÃO DA AMOSTRA:"))
        sample_box <= html.P(f"Estrato 1: {proporcao1:.2%} × {total_amostra} = {amostra1} elementos")
        sample_box <= html.P(f"Estrato 2: {proporcao2:.2%} × {total_amostra} = {amostra2} elementos")
        sample_box <= html.P(html.STRONG(f"📊 Total: {amostra1 + amostra2} elementos"))
        resultado_div <= sample_box
        
        # Demonstração com amostragem sistemática
        if total_amostra > 0 and total_amostra <= total_populacao:
            demo_box = html.DIV(Class="calculation")
            demo_box <= html.P(html.STRONG("🎲 DEMONSTRAÇÃO - AMOSTRAGEM SISTEMÁTICA:"))
            
            # Sortear semente
            semente = random.randint(1, 9)
            numeros_sorteados = list(range(semente, total_populacao + 1, 10))
            numeros_sorteados = numeros_sorteados[:total_amostra]
            
            demo_box <= html.P(f"Semente sorteada: {semente}")
            demo_box <= html.P(f"Elementos terminados em {semente}:")
            
            if len(numeros_sorteados) > 15:
                elementos_str = f"[{numeros_sorteados[0]}, {numeros_sorteados[1]}, {numeros_sorteados[2]}, ..., {numeros_sorteados[-2]}, {numeros_sorteados[-1]}]"
                demo_box <= html.P(elementos_str)
            else:
                demo_box <= html.P(str(numeros_sorteados))
            
            demo_box <= html.P(f"Total: {len(numeros_sorteados)} elementos")
            resultado_div <= demo_box
        
        # Procedimento
        proc_box = html.DIV(Class="sample-list")
        proc_box <= html.P(html.STRONG("📝 PROCEDIMENTO:"))
        proc_box <= html.P(
            "Devemos aplicar amostragem casual simples em cada estrato " +
            "para selecionar os elementos da amostra, garantindo assim " +
            "aleatoriedade e representatividade proporcional de cada grupo."
        )
        resultado_div <= proc_box
        
    except ValueError:
        mostrar_erro_estrat("Por favor, preencha todos os campos com valores válidos!")
    except Exception as e:
        mostrar_erro_estrat(f"Erro ao calcular: {str(e)}")

def mostrar_erro_estrat(mensagem):
    """Mostra mensagem de erro"""
    resultado_div = document["resultado_estrat"]
    resultado_div.clear()
    resultado_div.class_name = "result-box show"
    resultado_div <= html.P(f"❌ {mensagem}", style={"color": "#ef4444", "font-weight": "bold"})

# Vincular evento ao botão
document["calcular_estrat"].bind("click", calcular_estratificada)
