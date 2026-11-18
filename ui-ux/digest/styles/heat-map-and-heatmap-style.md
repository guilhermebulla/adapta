# Heat Map & Heatmap Style

- id: `heat-map-and-heatmap-style`  ·  tipo: BI/Analytics  ·  status: supplemental
- pai: `data-dense-dashboard`  ·  complexidade: Medium
- era: 2020s Modern  ·  frameworks: recharts/chartjs/d3
- light/dark: supported / supported  ·  perf: cost:low/drivers:none  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Geographical analysis, performance matrices, correlation analysis, user behavior heatmaps, temperature/intensity data

## Não usar para
Linear data representation, categorical comparisons (use bar charts), small datasets

## Cores primárias
Gradient scale: Cool (blue #0080FF) to hot (red #FF0000), neutral middle (white/yellow)

## Cores secundárias
Support gradients: Light (cool blue) to dark (warm red), divergent for positive/negative data, monochromatic options

## Efeitos & animação
Color gradient transitions on data change, cell highlighting on hover, tooltip reveal on click, smooth color animation

## Tokens
```css
--heatmap-cool: #0080FF, --heatmap-neutral: #FFFFFF, --heatmap-hot: #FF0000, --cell-size: 24px, --legend-width: 200px, --tooltip-bg: rgba(0,0,0,0.9)
```

## Checklist
Color scale clear, 
- Legend visible, 
- Tooltips informative, 
- Colorblind alternatives, 
- Zoom/pan for geo, 
- Performance for large data

## Prompt de referência
Design a heatmap visualization. Use: color gradient scale (cool to hot), cell-based grid, intensity legend, hover tooltips, geographic or matrix layout, divergent color scheme for +/- values, accessible color alternatives.

