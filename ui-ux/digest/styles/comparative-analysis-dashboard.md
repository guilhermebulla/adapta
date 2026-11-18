# Comparative Analysis Dashboard

- id: `comparative-analysis-dashboard`  ·  tipo: BI/Analytics  ·  status: supplemental
- pai: `data-dense-dashboard`  ·  complexidade: Medium
- era: 2020s Modern  ·  frameworks: recharts/chartjs/d3
- light/dark: supported / supported  ·  perf: cost:low/drivers:none  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Period-over-period reporting, A/B test dashboards, market comparison, competitive analysis, regional performance

## Não usar para
Single metric dashboards, future projections (use forecasting), real-time only (no historical)

## Cores primárias
Comparison colors: primary (blue), comparison (orange/purple), delta indicator (green/red)

## Cores secundárias
Winning metric color (green), losing metric color (red), neutral comparison (grey), benchmark colors

## Efeitos & animação
Comparison bar animations (grow to value), delta indicator animations (direction arrows), highlight on compare

## Tokens
```css
--positive-color: #22C55E, --negative-color: #EF4444, --neutral-color: #6B7280, --comparison-gap: 2rem, --arrow-size: 16px, --badge-padding: 4px 8px
```

## Checklist
Period selector works, 
- Deltas calculated, 
- Colors meaningful, 
- Benchmarks shown, 
- Mobile stacks properly, 
- Export comparison

## Prompt de referência
Design a comparison dashboard. Use: side-by-side metrics, period selectors (vs last month), delta indicators (+/-), benchmark lines, A/B comparison tables, winning/losing highlights, percentage change badges.

