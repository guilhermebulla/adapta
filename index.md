# ui-ux — índice de roteamento

Base de conhecimento de design system para consumo por LLMs/skills.
Corpus original: nextlevelbuilder/ui-ux-pro-max-skill (MIT, Next Level Builder).
Digerido e mantido neste repositório. Ver NOTICE.md para atribuição.

## Estrutura
- `digest/` — arquivos curados e resumidos (ESTE é o material de trabalho)
- `digest/styles/` — 1 arquivo .md por estilo completo (tokens CSS, checklist, anti-uso)
- `raw/` — corpus original completo. NÃO baixe nada daqui, exceto consulta pontual de hex.

## FATOS SOBRE OS DADOS
- Os códigos hex das cores EXISTEM no corpus (ex.: #2563EB, #0F172A, ~194 linhas em raw/colors.csv).
  Se algum arquivo ou resumo alegar que os hex estão ausentes, essa alegação está DESATUALIZADA — ignore.
- Alguns valores de borda usam rgba() em vez de hex — normalize para token CSS antes de usar.
- Se um hex parecer malformado (ex.: comprimento incorreto), não o repare por conta própria:
  declare a dúvida ao usuário ou peça o trecho de raw/ correspondente.

## Mapa dos arquivos (digest/)
### Índices (leia primeiro, são baratos)
| arquivo | conteúdo | quando chamar |
| `styles-index.md` | 1 linha por estilo: id, nome, tipo, complexidade, "best for" | sempre que a decisão envolver estética/estilo |
| `colors-by-product.md` | tipo de produto → foco de paleta + nota | quando o produto já foi identificado |

### Conteúdo por tarefa
| arquivo | conteúdo | quando chamar |
| `landing-structures.md` | estruturas de landing page | página de conversão/venda |
| `app-patterns.md` | padrões de interface de app | telas de aplicativo/dashboard |
| `charts.md` | boas práticas de gráficos | visualização de dados |
| `motion.md` | diretrizes de animação e movimento | microinterações, transições |
| `typography-pairs.md` | pares tipográficos | escolha de fontes |
| `ux-rules.md` | regras de usabilidade por categoria | revisão de UX (leia por categoria, não inteiro) |
| `styles/<style-id>.md` | 1 estilo completo | SÓ depois de escolher o estilo em `styles-index.md` |
| `build_digest.py` | script que gerou o digest | manutenção do repo, não consumo |

## Regras de leitura
1. Comece por este arquivo. Ele diz o que existe e quando chamar cada arquivo.
2. Nunca baixe nada de `raw/`. Nunca baixe a pasta `styles/` inteira.
3. Máximo 4 arquivos do digest por consulta. Máximo 1 detalhe de estilo por consulta.
4. `styles/<id>.md` só depois da escolha registrada em `styles-index.md`.
5. Arquivo já lido nesta conversa não é relido.
6. Fetch vazio, truncado ou 404 → use o que já está em contexto; sem isso, peça ao usuário
   para colar o trecho. NUNCA invente hex, fonte ou token.

## Roteamento
- Tipo de produto desconhecido → pergunte antes (máx. 3 perguntas em 1 rodada:
  tipo de produto, objetivo da tela, stack).
- Tipo conhecido → `colors-by-product.md` + `styles-index.md`.
- Landing → `landing-structures.md`. App → `app-patterns.md`.
- Dado → `charts.md`. Animação → `motion.md`. Fonte → `typography-pairs.md`.
- Revisão de usabilidade → `ux-rules.md` por categoria.