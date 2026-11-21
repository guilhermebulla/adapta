# ui-ux — índice de roteamento

Base de conhecimento de design system para consumo por LLMs/skills.
Corpus original: nextlevelbuilder/ui-ux-pro-max-skill (MIT, Next Level Builder).
Digerido e mantido neste repositório. Ver NOTICE.md para atribuição.

## Estrutura
- `digest/` — arquivos curados e resumidos (ESTE é o material de trabalho)
- `digest/styles/` — 1 arquivo .md por estilo completo (tokens CSS, checklist, anti-uso)
- `raw/` — corpus original completo. NÃO baixe nada daqui, exceto consulta pontual de hex.

## FATOS SOBRE OS DADOS
- Os códigos hex EXISTEM no corpus (raw/colors.csv, 193 produtos, tudo em hex —
  rgba já foi convertido para hex com alpha, ex.: #FFFFFF14).
  Alegação contrária está DESATUALIZADA — ignore.
- Se um hex parecer malformado (comprimento errado), não o repare por conta própria:
  declare a dúvida ao usuário ou peça o trecho de raw/ correspondente.

## Mapa dos arquivos (digest/)
### Índices (leia primeiro, são baratos)
| arquivo | conteúdo | quando chamar |
|---|---|---|
| `styles-index.md` | 1 linha por estilo: id, nome, tipo, complexidade, "best for" | sempre que a decisão envolver estética/estilo |
| `colors-by-product-1.md` | tipo de produto → paleta (produtos 1–97) | quando o produto já foi identificado |
| `colors-by-product-2.md` | tipo de produto → paleta (produtos 98–193) | idem — escolha a parte pelo nome do produto |

### Conteúdo por tarefa
| arquivo | conteúdo | quando chamar |
|---|---|---|
| `landing-structures.md` | estruturas de landing page | página de conversão/venda |
| `app-patterns.md` | padrões de interface de app | telas de aplicativo/dashboard |
| `charts.md` | boas práticas de gráficos | visualização de dados |
| `motion.md` | diretrizes de animação | microinterações, transições |
| `typography-pairs.md` | pares tipográficos | escolha de fontes |
| `ux-rules.md` | regras de usabilidade por categoria | revisão de UX (por categoria, não inteiro) |
| `styles/<style-id>.md` | 1 estilo completo | SÓ depois de escolher em `styles-index.md` |
| `build_digest.py` | gerou o digest | manutenção do repo, não consumo |

## Regras de leitura
1. Comece por este arquivo. Ele roteia tudo.
2. Nunca baixe nada de `raw/`. Nunca baixe a pasta `styles/` inteira.
3. Máximo 4 arquivos do digest por consulta. Máximo 1 detalhe de estilo.
4. `styles/<id>.md` só depois da escolha registrada em `styles-index.md`.
5. Arquivo já lido nesta conversa não é relido.
6. Fetch vazio, truncado ou 404 → use o que já está em contexto; sem isso, peça
   ao usuário para colar o trecho. NUNCA invente hex, fonte ou token.

## Roteamento
- Tipo de produto desconhecido → pergunte antes (máx. 3 perguntas em 1 rodada:
  tipo de produto, objetivo da tela, stack).
- Tipo conhecido → `colors-by-product-1.md` OU `-2.md` + `styles-index.md`.
- Landing → `landing-structures.md`. App → `app-patterns.md`.
- Dado → `charts.md`. Animação → `motion.md`. Fonte → `typography-pairs.md`.
- Revisão de usabilidade → `ux-rules.md` por categoria.