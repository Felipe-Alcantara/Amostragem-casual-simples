# IA.md — Contexto Operacional

> Contexto para quem mantém este projeto (humano ou IA). Registra arquitetura,
> decisões, verificações e pendências, conforme o `felixo-standards`
> (`core/GUIA_MINIMO_QUALIDADE.md`).

## Visão geral

Projeto educacional de três técnicas de amostragem probabilística:
casual simples, sistemática e proporcional estratificada. Existe em duas formas
que compartilham a mesma regra de negócio:

- **CLI** (`src/`): scripts Python de terminal (`input`/`print`).
- **Web** (`docs/`): mesma lógica rodando no navegador via Brython, publicada
  no GitHub Pages.

## Arquitetura

- `src/amostragem.py` — **única fonte da regra de negócio**. Funções puras
  (`amostra_casual_simples`, `amostra_sistematica`, `amostra_estratificada`),
  sem I/O, com validação de entrada e `ValueError` em mensagens claras. Aceita
  um `rng` injetável para testes determinísticos.
- `src/amostragem_*.py` — CLIs; só fazem entrada/saída e chamam a lógica pura.
- `docs/py/amostragem_*.py` — camada de apresentação web (DOM via Brython);
  importam `amostragem` e renderizam o resultado.
- `docs/py/amostragem.py` — **cópia** de `src/amostragem.py`, necessária porque o
  Brython carrega módulos por HTTP a partir de `docs/`. Mantida em sincronia com
  o original.
- `tests/test_amostragem.py` — testes da lógica pura (`unittest`, stdlib).

## Decisões relevantes

- **Separação cálculo × apresentação**: antes a regra estava duplicada e
  embutida na CLI e no DOM. Extraída para `src/amostragem.py` para reúso e
  testabilidade.
- **Versão web mantida e movida para `docs/`**: o commit `67c2aac` dizia ter
  removido a versão web, mas os arquivos seguiam na raiz. Decidiu-se manter a
  demo e colocá-la em `docs/` (padrão GitHub Pages que o README já esperava).
- **`docs/py/amostragem.py` é cópia, não link**: Brython não importa de fora do
  diretório servido. Ao alterar a regra de negócio, atualizar **os dois**
  arquivos. Próximo passo possível: script ou hook que copie automaticamente.
- **Imagem `docs/images/c598f7e8-...png`**: NÃO é órfã — é usada como textura de
  fundo em `docs/css/style.css` (modos claro e escuro). Tem ~2,3 MB; otimizar o
  peso é uma melhoria futura, mas remover quebraria o visual.

## Validação executada

- `python -m unittest discover -s tests` → 10 testes OK (cobre cálculo, sorteio
  sem repetição/ordenado, proporções e todos os caminhos de validação).
- Smoke test manual das 3 CLIs com entradas válidas e inválidas (população 0/
  negativa, porcentagem > 100, amostra > população) → mensagens de erro corretas.
- Versão web: sintaxe Python validada nos 4 módulos; `docs/` servido via
  `http.server` com index/CSS/`py/amostragem.py` respondendo 200.

## Riscos e pendências

- **Verificação manual da demo no navegador pendente**: não havia browser
  automatizado no ambiente. Confirmar que os três botões calculam e renderizam
  (especialmente a resolução do `import amostragem` pelo Brython com
  `pythonpath: ['py']`) abrindo `http://localhost:8000/` após
  `python -m http.server 8000 --directory docs`.
- **Sincronização de `amostragem.py`** entre `src/` e `docs/py/` é manual.
- **Peso da imagem de fundo** (~2,3 MB) pode ser otimizado.
