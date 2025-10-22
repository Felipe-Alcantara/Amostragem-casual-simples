from browser import document, html

def calcular_casual_simples(ev):
    """Calcula a amostragem casual simples"""
    try:
        # Obter valores dos inputs
        populacao = int(document["populacao_casual"].value)
        porcentagem = float(document["porcentagem_casual"].value)
        
        # Validações
        if populacao <= 0:
            mostrar_erro_casual("A população deve ser maior que zero!")
            return
        
        if porcentagem <= 0 or porcentagem > 100:
            mostrar_erro_casual("A porcentagem deve estar entre 0 e 100!")
            return
        
        # Cálculo
        elementos_na_amostra = int((populacao * porcentagem) / 100)
        
        # Montar resultado
        resultado_div = document["resultado_casual"]
        resultado_div.clear()
        resultado_div.class_name = "result-box show"
        
        # Título
        resultado_div <= html.H3("✅ RESULTADO")
        
        # Informações principais
        info_box = html.DIV(Class="result-item")
        info_box <= html.P(f"🎯 População total: {populacao:,} elementos".replace(',', '.'))
        info_box <= html.P(f"📊 Porcentagem da amostra: {porcentagem}%")
        info_box <= html.P(html.STRONG(f"📈 Tamanho da amostra: {elementos_na_amostra:,} elementos".replace(',', '.')))
        resultado_div <= info_box
        
        # Cálculo detalhado
        calc_box = html.DIV(Class="calculation")
        calc_box <= html.P(html.STRONG("💡 CÁLCULO:"))
        calc_box <= html.P(f"Amostra = (População × Porcentagem) / 100")
        calc_box <= html.P(f"Amostra = ({populacao} × {porcentagem}) / 100 = {elementos_na_amostra}")
        resultado_div <= calc_box
        
        # Procedimento
        proc_box = html.DIV(Class="sample-list")
        proc_box <= html.P(html.STRONG("🎲 PROCEDIMENTO:"))
        proc_box <= html.P(
            f"Para realizar esta amostragem, insira os {populacao:,} elementos ".replace(',', '.') +
            f"em uma urna e retire, aleatoriamente, {elementos_na_amostra:,} elementos.".replace(',', '.')
        )
        proc_box <= html.P("Cada elemento tem a mesma probabilidade de ser selecionado!")
        resultado_div <= proc_box
        
    except ValueError:
        mostrar_erro_casual("Por favor, preencha todos os campos com valores válidos!")
    except Exception as e:
        mostrar_erro_casual(f"Erro ao calcular: {str(e)}")

def mostrar_erro_casual(mensagem):
    """Mostra mensagem de erro"""
    resultado_div = document["resultado_casual"]
    resultado_div.clear()
    resultado_div.class_name = "result-box show"
    resultado_div <= html.P(f"❌ {mensagem}", style={"color": "#ef4444", "font-weight": "bold"})

# Vincular evento ao botão
document["calcular_casual"].bind("click", calcular_casual_simples)
