# ui-ux — índice de roteamento

Corpus vendorizado de nextlevelbuilder/ui-ux-pro-max-skill (MIT — ver NOTICE.md).
Base URL dos digests:
https://raw.githubusercontent.com/guilhermebulla/adapta/main/ui-ux/digest/

## Protocolo de leitura (obrigatório, nesta ordem)

1. NUNCA baixe nada de `raw/`. `raw/` é fonte de verdade, não material de runtime.
   Tamanho total ~470 KB: baixar isso queima o contexto e trunca.
2. Pergunte antes de buscar: (a) tipo de produto, (b) objetivo da tela/página,
   (c) stack. Cada resposta elimina um arquivo da fila.
3. Caminho: `index.md` → 1 índice (`styles-index.md` OU `colors-by-product.md`)
   → `styles/<style-id>.md` do estilo escolhido → no máximo 2 auxiliares.
4. Orçamento rígido por consulta: **≤ 4 arquivos**, **≤ 1 detalhe de estilo**.
5. Cache de conversa: arquivo já lido nesta conversa não é relido.
6. Degradação: fetch falhou, veio vazio ou truncou → responda com o que já está
   em contexto; se não houver, peça ao usuário para colar o trecho.
   NUNCA invente token, hex ou nome de fonte.

## Mapa dos arquivos

### Índices (leia primeiro, são baratos)

| arquivo | conteúdo | quando chamar |
|---|---|---|
| `styles-index.md` | 1 linha por estilo: id, nome, tipo, complexidade, "best for" | sempre que a decisão envolver estética/estilo |
| `colors-by-product.md` | tipo de produto → foco de paleta + nota | quando o produto já foi identificado |
| `styles/<style-id>.md` | 1 estilo completo (tokens CSS, checklist, anti-uso) | só depois de escolher o estilo |

### Auxiliares (máximo 2 por consulta)

| arquivo | linhas | chama quando |
|---|---|---|
| `typography-pairs.md` | 74 | precisa de par tipográfico concreto |
| `landing-structures.md` | 34 | é landing page / página de conversão |
| `app-patterns.md` | 32 | é app mobile / fluxo de tela |
| `ux-rules.md` | 130 | revisão de usabilidade ou acessibilidade |
| `charts.md` | 25 | há dado para visualizar |
| `motion.md` | 17 | há animação/transição em jogo |

## Schemas reais (para você saber o que cada digest pode responder)

**products.csv** — 194 registros, 10 colunas:
`No, Product Type, Keywords, Primary Style Recommendation, Secondary Styles,
Landing Page Pattern, Dashboard Style, Color Palette Focus, Key Considerations, rtl_level`
→ É o **ponto de entrada nº 1**. Um tipo de produto resolve estilo + landing + cor de uma vez.

**styles.csv** — ~89 registros, 30 colunas. As que importam:
`Style ID, Style Category, Type, Keywords, Primary Colors, Secondary Colors,
Effects & Animation, Best For, Do Not Use For, Complexity, AI Prompt Keywords,
CSS/Technical Keywords, Implementation Checklist, Design System Variables,
Status, Parent Style ID, Preferred Mode, rtl_level`
→ `Type` separa General / Mobile. `Status` = active | supplemental | deprecated.
`Parent Style ID` indica variante de um estilo pai — não trate como estilo novo.

**colors.csv** — 194 registros, 19 colunas:
`No, Product Type, Primary, On Primary, Secondary, On Secondary, Accent, On Accent,
Background, Foreground, Card, Card Foreground, Muted, Muted Foreground, Border,
Destructive, On Destructive, Ring, Notes`
→ ATENÇÃO: no commit atual as colunas de hex estão VAZIAS. Use `products.csv ›
Color Palette Focus` como fallback declarado, e diga ao usuário que a paleta
exata não está disponível na base.

**typography.csv** — 74 registros, 11 colunas:
`No, Font Pairing Name, Category, Heading Font, Body Font, Mood/Style Keywords,
Best For, Google Fonts URL, CSS Import, Tailwind Config, Notes`

**landing.csv** — 34 registros, 10 colunas:
`No, Pattern Name, Keywords, Section Order, Primary CTA Placement, Color Strategy,
Recommended Effects, Conversion Optimization, Pattern ID, Aliases`

**ux-guidelines.csv** e **app-interface.csv** — 130 e 32 registros, 10/11 colunas:
`No, Category, Issue, [Keywords], Platform, Description, Do, Don't,
Code Example Good, Code Example Bad, Severity`

**charts.csv** — 25 registros, 15 colunas:
`No, Data Type, Keywords, Best Chart Type, Secondary Options, When to Use,
When NOT to Use, Data Volume Threshold, Color Guidance, Accessibility Risk,
Accessibility Notes, A11y Fallback, Library Recommendation, Interactive Level`

**motion.csv** — 17 registros, 12 colunas:
`No, Category, Intensity Tier, Keywords, Trigger, Duration, Easing, GSAP Snippet,
Framework Notes, Do, Don't, Performance Notes`

**ui-reasoning.csv** — 194 registros, 12 colunas:
`No, UI_Category, Recommended_Pattern, Style_Priority, Color_Mood, Typography_Mood,
Key_Effects, Decision_Rules, Anti_Patterns, Severity, Reasoning, Confidence`
→ Único arquivo com `Anti_Patterns` e `Decision_Rules` explícitos. Use para justificar
uma escolha, nunca para descobrir o estilo (é mais caro que products.csv).

**icons.csv** — 105 registros. **stacks/*.csv** — 66 linhas (react).
→ Stacks apenas se o usuário já disse a stack. Não carregue as três.

## Árvore de decisão

1. Produto/tela desconhecido → pergunte o tipo de produto.
2. Tipo identificado → `colors-by-product.md` + `styles-index.md`.
3. Estilo escolhido → `styles/<style-id>.md` (1 arquivo, nunca dois).
4. É landing → +`landing-structures.md`.
5. É app → +`app-patterns.md`.
6. Tem gráfico → +`charts.md`.
7. Tem animação → +`motion.md`.
8. Precisa de fonte explícita → `typography-pairs.md`.

## Contrato de saída (sem isto a skill vira conversa)

Toda resposta termina em dois blocos, sem exceção:

1. **Tokens** — CSS custom properties prontas para colar:
   `--color-bg, --color-surface, --color-fg, --color-primary, --color-accent,
   --color-border, --font-display, --font-body, --radius, --space-*, --motion-*`
   Valor ausente na base = `/* TODO: definir */`, nunca um chute.
2. **Checklist de implementação** — 5 a 10 itens verificáveis, derivados do
   `Implementation Checklist` do estilo + `ux-rules` aplicáveis.

Se você não conseguiu ler `styles/<id>.md`, diga qual arquivo faltou e o que
você está assumindo. Não preencha o vazio em silêncio.