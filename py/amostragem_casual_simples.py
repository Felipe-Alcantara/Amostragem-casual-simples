from browser import document, html
import random

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
        
        if elementos_na_amostra == 0:
            mostrar_erro_casual("A amostra calculada é zero! Aumente a porcentagem.")
            return
        
        # REALIZAR O SORTEIO REAL
        # Criar lista da população (1 até população)
        populacao_lista = list(range(1, populacao + 1))
        
        # Sortear elementos aleatoriamente SEM REPETIÇÃO
        elementos_sorteados = random.sample(populacao_lista, elementos_na_amostra)
        elementos_sorteados.sort()  # Ordenar para melhor visualização
        
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
        
        # SORTEIO REALIZADO
        sorteio_box = html.DIV(Class="sample-list")
        sorteio_box <= html.P(html.STRONG("🎲 SORTEIO REALIZADO:"))
        sorteio_box <= html.P(f"Os {elementos_na_amostra} elementos foram sorteados aleatoriamente da população:")
        sorteio_box <= html.BR()
        
        # Mostrar elementos sorteados (limitar visualização se for muito grande)
        if elementos_na_amostra <= 50:
            sorteio_box <= html.P(f"Elementos sorteados: {elementos_sorteados}", style={"font-family": "monospace"})
        else:
            # Mostrar apenas primeiros e últimos
            primeiros_10 = elementos_sorteados[:10]
            ultimos_10 = elementos_sorteados[-10:]
            sorteio_box <= html.P(
                f"Primeiros 10: {primeiros_10}",
                style={"font-family": "monospace"}
            )
            sorteio_box <= html.P(
                f"Últimos 10: {ultimos_10}",
                style={"font-family": "monospace"}
            )
            sorteio_box <= html.P(f"(Total de {elementos_na_amostra} elementos sorteados)")
        
        resultado_div <= sorteio_box
        
        # Procedimento
        proc_box = html.DIV(Class="calculation")
        proc_box <= html.P(html.STRONG("📝 PROCEDIMENTO REALIZADO:"))
        proc_box <= html.P("1️⃣ Criamos uma população numerada de 1 até " + f"{populacao:,}".replace(',', '.'))
        proc_box <= html.P(f"2️⃣ Sorteamos aleatoriamente {elementos_na_amostra} elementos SEM repetição")
        proc_box <= html.P("3️⃣ Cada elemento teve a mesma probabilidade de ser selecionado")
        proc_box <= html.P(f"4️⃣ Probabilidade de seleção: {porcentagem}% ou {porcentagem/100:.4f}")
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
