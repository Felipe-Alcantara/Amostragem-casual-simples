# 📊 Técnicas de Amostragem em Python

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()


## Índice

- 🔎 [🌐 Versão Web — Demo online](#web)  ← Destaque (clique para abrir a demo)
- 📖 [Sobre o Projeto](#sobre-o-projeto)
- 🎯 [Objetivo](#objetivo)
- 🚀 [Para Que Serve?](#para-que-serve)
- 🛠️ [Técnicas Implementadas](#técnicas-implementadas)
- 💻 [Como Usar](#como-usar)
- 🧪 [Testes](#testes)
- 🤝 [Contribuindo](#contribuindo)


## 📖 Sobre o Projeto

Este projeto nasceu durante minhas aulas de **Estatística em setembro de 2024**, quando percebi a necessidade de ter ferramentas práticas para visualizar e compreender melhor os diferentes métodos de amostragem. Recentemente (outubro de 2025), redescobri este projeto esquecido no meu GitHub e decidi dar uma **repaginada completa**, melhorando o código, a organização e a apresentação visual dos scripts.

<a name="web"></a>
## 🌐 Versão Web — Demo online

Agora o projeto também está disponível como uma aplicação web interativa. A versão web roda a lógica Python diretamente no navegador via **Brython**, permitindo testar as mesmas técnicas sem instalar nada.

- Acesse a demo: https://felipe-alcantara.github.io/Amostragem-casual-simples/
- Sem instalação — roda no navegador (desktop e mobile)
- Mantém a lógica Python original (os módulos foram adaptados para Brython)
- Recursos: tema claro/escuro, interface responsiva, cálculos em tempo real e explicações didáticas

Como testar rapidamente:

1. Abrir a demo no link acima (recomendado).
2. Ou, localmente, sirva a pasta `docs/` via HTTP (o Brython precisa de HTTP para
   carregar os módulos Python):

```bash
python -m http.server 8000 --directory docs
# e depois acesse: http://localhost:8000/
```


### 🎯 Objetivo

Fornecer implementações práticas e didáticas de três principais técnicas de amostragem estatística:
- **Amostragem Casual Simples (ACS)**
- **Amostragem Sistemática**
- **Amostragem Proporcional Estratificada**

## 🚀 Para Que Serve?

Este projeto é útil para:

- 📚 **Estudantes de Estatística**: Visualizar na prática como funcionam diferentes técnicas de amostragem
- 💻 **Estudantes de Python**: Estudar lógica de programação com exemplos práticos e aplicados
- 🔬 **Pesquisadores**: Ter uma referência rápida para implementar métodos de amostragem
- 🎓 **Professores**: Usar como material didático em aulas de Estatística ou Programação
- 🧮 **Profissionais**: Calcular rapidamente tamanhos de amostras para pesquisas e estudos

## 📁 Estrutura do Projeto

```
Amostragem-casual-simples/
├── src/
│   ├── amostragem.py                              # Lógica pura (regra de negócio)
│   ├── amostragem_casual_simples.py              # CLI - Amostragem Casual Simples
│   ├── amostragem_sistematica.py                 # CLI - Amostragem Sistemática
│   └── amostragem_proporcional_estratificada.py  # CLI - Amostragem Estratificada
├── tests/
│   └── test_amostragem.py                        # Testes da lógica pura
├── docs/                                         # Versão web (GitHub Pages)
│   ├── index.html
│   ├── css/style.css
│   └── py/                                        # Apresentação Brython + cópia de amostragem.py
├── LICENSE
└── README.md
```

> A regra de negócio fica em `src/amostragem.py` e é reutilizada pela CLI e pela
> versão web, mantendo cálculo e apresentação separados.

## 🛠️ Técnicas Implementadas

### 1. 🎲 Amostragem Casual Simples (ACS)

A forma mais básica de amostragem, onde cada elemento da população tem a mesma probabilidade de ser selecionado.

**Características:**
- Sorteio individual de elementos
- Baseado em porcentagem da população
- Método mais simples e direto

**Uso:**
```bash
python src/amostragem_casual_simples.py
```

### 2. 🔢 Amostragem Sistemática

Método que utiliza uma "semente" sorteada e um intervalo fixo (salto) para selecionar elementos de forma sistemática.

**Características:**
- Reduz a quantidade de sorteios necessários
- Utiliza intervalo calculado (população/amostra)
- Eficiente para grandes populações

**Uso:**
```bash
python src/amostragem_sistematica.py
```

### 3. 📊 Amostragem Proporcional Estratificada

Técnica avançada para populações divididas em estratos, garantindo representatividade proporcional de cada grupo.

**Características:**
- Garante representatividade de subgrupos
- Calcula proporções automaticamente
- Inclui demonstração com amostragem sistemática

**Uso:**
```bash
python src/amostragem_proporcional_estratificada.py
```

## 💻 Como Usar

### Pré-requisitos

- Python 3.x instalado
- Nenhuma biblioteca externa necessária (usa apenas módulos padrão)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Felipe-Alcantara/Amostragem-casual-simples.git
```

2. Navegue até a pasta do projeto:
```bash
cd Amostragem-casual-simples
```

3. Execute o script desejado:
```bash
python src/amostragem_casual_simples.py
```

### Exemplos de Uso

#### Exemplo 1: Amostragem Casual Simples
```
População: 1000 elementos
Porcentagem: 10%
Resultado: 100 elementos na amostra
```

#### Exemplo 2: Amostragem Sistemática
```
População: 500 elementos
Amostra desejada: 50 elementos
Intervalo: 10
Semente sorteada: 3
Resultado: [3, 13, 23, 33, 43, ...]
```

#### Exemplo 3: Amostragem Estratificada
```
Estrato 1: 600 elementos (60%)
Estrato 2: 400 elementos (40%)
Porcentagem: 15%
Resultado: 
  - Estrato 1: 90 elementos
  - Estrato 2: 60 elementos
  - Total: 150 elementos
```

## 🎓 Conceitos Aprendidos

Ao estudar este projeto, você vai praticar:

### Python
- ✅ Entrada e saída de dados (`input()`, `print()`)
- ✅ Manipulação de variáveis e tipos de dados
- ✅ Operações matemáticas e cálculos
- ✅ Uso do módulo `random`
- ✅ List comprehension e `range()`
- ✅ Formatação de strings (f-strings)
- ✅ Estruturação e organização de código

### Estatística
- ✅ Conceitos de população e amostra
- ✅ Técnicas de amostragem probabilística
- ✅ Cálculo de proporções e percentuais
- ✅ Estratificação de populações
- ✅ Amostragem sistemática com intervalos

## 🧪 Testes

A lógica de cálculo e sorteio é coberta por testes com a biblioteca padrão
(`unittest`), sem dependências externas. Para rodar:

```bash
python -m unittest discover -s tests
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

1. Fazer um fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abrir um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👤 Autor

**Felipe Alcântara**

- GitHub: [@Felipe-Alcantara](https://github.com/Felipe-Alcantara)
---

<div align="center">

**⭐ Se este projeto foi útil para você, considere dar uma estrela!**

Feito com ❤️ e Python 🐍

</div>
