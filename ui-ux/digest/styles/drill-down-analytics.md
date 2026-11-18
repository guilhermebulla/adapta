# Drill-Down Analytics

- id: `drill-down-analytics`  ·  tipo: BI/Analytics  ·  status: supplemental
- pai: `data-dense-dashboard`  ·  complexidade: Medium
- era: 2020s Modern  ·  frameworks: recharts/chartjs/d3
- light/dark: supported / supported  ·  perf: cost:low/drivers:none  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Sales analytics, product analytics, funnel analysis, multi-dimensional data exploration, business intelligence

## Não usar para
Simple linear data, single-metric dashboards, streaming real-time dashboards

## Cores primárias
Primary brand, breadcrumb colors, drill-level indicator colors, hierarchy depth colors

## Cores secundárias
Drill-down path indicator colors, level-specific colors, highlight colors for selected level, transition colors

## Efeitos & animação
Drill-down expand animations, breadcrumb click transitions, smooth detail reveal, level change smooth, data reload animation

## Tokens
```css
--breadcrumb-separator: /, --expand-duration: 300ms, --level-indent: 24px, --back-button-size: 40px, --context-bar-height: 48px, --drill-transition: 300ms ease
```

## Checklist
Breadcrumbs clear, 
- Back navigation easy, 
- Expand animation smooth, 
- Context preserved, 
- Mobile drill works, 
- Deep links supported

## Prompt de referência
Design a drill-down analytics dashboard. Use: breadcrumb navigation, expandable sections, summary-to-detail flow, back button prominent, level indicators, context preservation, hierarchical data display.

