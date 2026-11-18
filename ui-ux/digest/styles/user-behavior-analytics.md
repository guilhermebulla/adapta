# User Behavior Analytics

- id: `user-behavior-analytics`  ·  tipo: BI/Analytics  ·  status: supplemental
- pai: `data-dense-dashboard`  ·  complexidade: Medium
- era: 2020s Modern  ·  frameworks: recharts/chartjs/d3
- light/dark: supported / supported  ·  perf: cost:low/drivers:none  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Conversion funnel analysis, user journey tracking, engagement analytics, cohort analysis, retention tracking

## Não usar para
Real-time operational metrics, technical system monitoring, financial transactions

## Cores primárias
Funnel stage colors: high engagement (green), drop-off (red), conversion (blue), user flow arrows (grey)

## Cores secundárias
Stage completion colors (success), abandonment colors (warning), engagement levels (gradient), cohort colors

## Efeitos & animação
Funnel animation (fill-down), flow diagram animations (connection draw), conversion pulse, engagement bar fill

## Tokens
```css
--funnel-width: 100%, --stage-colors: gradient, --flow-opacity: 0.6, --cohort-cell-size: 40px, --retention-line-color: #3B82F6, --engagement-scale: 5 levels
```

## Checklist
Funnel stages clear, 
- Flow diagram readable, 
- Conversions calculated, 
- Cohorts comparable, 
- Retention trends visible, 
- Privacy compliant

## Prompt de referência
Design a user behavior analytics dashboard. Use: funnel visualization, user flow diagrams (Sankey), conversion metrics, engagement heatmaps, cohort tables, retention curves, session replay indicators.

