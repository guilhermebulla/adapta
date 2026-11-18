#!/usr/bin/env python3
"""Gera ui-ux/digest/ a partir de ui-ux/raw/. Sem IA, sem rede.
Uso:  python3 ui-ux/digest/build_digest.py
"""
import csv, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent   # ui-ux/
RAW, OUT = ROOT / "raw", ROOT / "digest"
LIMIT = 30_000

def rows(name):
    p = RAW / name
    if not p.exists():
        print(f"AVISO: {name} ausente — pulando"); return []
    with p.open(encoding="utf-8", newline="") as f:
        return [{k: (v or "") for k, v in r.items() if k} for r in csv.DictReader(f)]

def c(v, n=110):
    v = re.sub(r"\s+", " ", (v or "").replace("|", "/")).strip()
    return v if len(v) <= n else v[:n - 1].rstrip() + "…"

def write(name, lines):
    p = OUT / name
    p.parent.mkdir(parents=True, exist_ok=True)
    body = "\n".join(lines) + "\n"
    p.write_text(body, encoding="utf-8")
    kb = len(body.encode()) / 1024
    print(f"{name:32} {kb:6.1f} KB  {'OK' if kb * 1024 < LIMIT else '>>> EXCEDE 30KB'}")

def table(headers, body):
    return ["| " + " | ".join(headers) + " |",
            "|" + "---|" * len(headers)] + \
           ["| " + " | ".join(r) + " |" for r in body]

# ---------- styles ----------
st = rows("styles.csv")
def sid(r):
    s = c(r.get("Style ID"), 60) or re.sub(r"[^a-z0-9]+", "-", r.get("Style Category", "").lower()).strip("-")
    return s

idx = ["# Estilos — índice (1 linha por estilo)", "",
       "Fonte: raw/styles.csv. Carregue `styles/<style-id>.md` só depois de escolher.", ""]
idx += table(["id", "estilo", "tipo", "complexidade", "best for", "status"],
             [[f"`{sid(r)}`", c(r.get("Style Category"), 40), c(r.get("Type"), 12),
               c(r.get("Complexity"), 10), c(r.get("Best For"), 70), c(r.get("Status"), 12)]
              for r in st])
write("styles-index.md", idx)

for r in st:
    d = [f"# {c(r.get('Style Category'), 80)}", "",
         f"- id: `{sid(r)}`  ·  tipo: {c(r.get('Type'), 20)}  ·  status: {c(r.get('Status'), 20)}",
         f"- pai: `{c(r.get('Parent Style ID'), 40)}`  ·  complexidade: {c(r.get('Complexity'), 20)}",
         f"- era: {c(r.get('Era/Origin'), 30)}  ·  frameworks: {c(r.get('Framework Compatibility'), 60)}",
         f"- light/dark: {c(r.get('Light Mode ✓'), 15)} / {c(r.get('Dark Mode ✓'), 15)}"
         f"  ·  perf: {c(r.get('Performance'), 40)}  ·  a11y: {c(r.get('Accessibility'), 80)}"]
    for label, key in (("Best for", "Best For"), ("Não usar para", "Do Not Use For"),
                       ("Cores primárias", "Primary Colors"), ("Cores secundárias", "Secondary Colors"),
                       ("Efeitos & animação", "Effects & Animation")):
        d += ["", f"## {label}", c(r.get(key), 600) or "—"]
    d += ["", "## Tokens", "```css", (r.get("Design System Variables") or "/* TODO: definir */"), "```",
          "", "## Checklist", (r.get("Implementation Checklist") or "—").replace("☐ ", "\n- ").lstrip("\n- "),
          "", "## Prompt de referência", c(r.get("AI Prompt Keywords"), 700) or "—", ""]
    write(f"styles/{sid(r)}.md", d)

# ---------- colors-by-product ----------
pr, co = rows("products.csv"), rows("colors.csv")
cmap = {c(r.get("Product Type")).lower(): r for r in co}
hexcols = ["Primary", "Secondary", "Accent", "Background", "Foreground", "Border"]
filled = sum(1 for r in co for k in hexcols if c(r.get(k)))
if filled == 0:
    print("AVISO: colors.csv sem hex nas colunas de cor — digest sai com paleta textual apenas.")
body = []
for r in pr:
    m = cmap.get(c(r.get("Product Type")).lower(), {})
    body.append([c(r.get("Product Type"), 42),
                 c(r.get("Primary Style Recommendation"), 55),
                 c(r.get("Color Palette Focus"), 95),
                 " · ".join(f"{k} {c(m.get(k), 12)}" for k in hexcols if c(m.get(k))) or "—",
                 c(m.get("Notes"), 90)])
write("colors-by-product.md",
      ["# Cor por tipo de produto", "",
       "Fonte: raw/products.csv (Color Palette Focus) + raw/colors.csv (hex e Notes).", ""]
      + table(["produto", "estilo primário", "foco de paleta", "hex", "nota"], body))

# ---------- tipografia ----------
ty = rows("typography.csv")
write("typography-pairs.md",
      ["# Pares tipográficos", "", "Fonte: raw/typography.csv.", ""]
      + table(["no", "nome", "categoria", "heading", "body", "melhor para"],
              [[c(r.get("No"), 4), c(r.get("Font Pairing Name"), 40), c(r.get("Category"), 30),
                c(r.get("Heading Font"), 28), c(r.get("Body Font"), 28),
                c(r.get("Best For"), 85)] for r in ty]))

# ---------- landing ----------
ld = rows("landing.csv")
write("landing-structures.md",
      ["# Estruturas de landing", "", "Fonte: raw/landing.csv.", ""]
      + table(["id", "padrão", "ordem das seções", "CTA"],
              [[f"`{c(r.get('Pattern ID'), 40)}`", c(r.get("Pattern Name"), 45),
                c(r.get("Section Order"), 150), c(r.get("Primary CTA Placement"), 60)] for r in ld]))

# ---------- ux rules + app patterns ----------
def rules(inp, out, title):
    rs = rows(inp)
    cats = sorted({c(r.get("Category"), 40) for r in rs})
    lines = [f"# {title}", "", f"Fonte: raw/{inp}.", ""]
    for cat in cats:
        lines += [f"## {cat}", ""]
        lines += table(["issue", "severidade", "fazer", "não fazer"],
                       [[c(r.get("Issue"), 45), c(r.get("Severity"), 12),
                         c(r.get("Do"), 105), c(r.get("Don't"), 105)]
                        for r in rs if c(r.get("Category"), 40) == cat])
        lines.append("")
    write(out, lines)
rules("ux-guidelines.csv", "ux-rules.md", "Regras de UX e acessibilidade")
rules("app-interface.csv", "app-patterns.md", "Padrões de interface mobile")

# ---------- charts ----------
ch = rows("charts.csv")
write("charts.md",
      ["# Gráficos por tipo de dado", "", "Fonte: raw/charts.csv.", ""]
      + table(["dado", "gráfico", "alternativas", "quando NÃO usar"],
              [[c(r.get("Data Type"), 45), c(r.get("Best Chart Type"), 45),
                c(r.get("Secondary Options"), 55), c(r.get("When NOT to Use"), 130)] for r in ch]))

# ---------- motion ----------
mo = rows("motion.csv")
write("motion.md",
      ["# Movimento e transição", "", "Fonte: raw/motion.csv.", ""]
      + table(["categoria", "tier", "gatilho", "duração", "easing"],
              [[c(r.get("Category"), 40), c(r.get("Intensity Tier"), 20),
                c(r.get("Trigger"), 35), c(r.get("Duration"), 25), c(r.get("Easing"), 25)] for r in mo]))

print("\nPronto. Revise: styles-index.md (89 linhas), colors-by-product.md (194), "
      "ux-rules.md (130), app-patterns.md (32).")