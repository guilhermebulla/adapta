# Executive Dashboard

- id: `executive-dashboard`  ·  tipo: BI/Analytics  ·  status: supplemental
- pai: `data-dense-dashboard`  ·  complexidade: Medium
- era: 2020s Modern  ·  frameworks: recharts/chartjs/d3
- light/dark: supported / supported  ·  perf: cost:low/drivers:none  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
C-suite dashboards, business summary reports, decision-maker dashboards, strategic planning views

## Não usar para
Detailed analyst dashboards, technical deep-dives, operational monitoring

## Cores primárias
Brand colors, professional palette (blue/grey/white), accent for KPIs, red for alerts/concerns

## Cores secundárias
KPI highlight colors: positive (green), negative (red), neutral (grey), trend arrow colors

## Efeitos & animação
KPI value animations (count-up), trend arrow direction animations, metric card hover lift, alert pulse effect

## Tokens
```css
--kpi-font-size: 48px, --sparkline-height: 32px, --status-green: #22C55E, --status-yellow: #F59E0B, --status-red: #EF4444, --card-min-width: 280px
```

## Checklist
KPIs 4-6 maximum, 
- Trends visible, 
- Status colors clear, 
- One-page view, 
- Mobile simplified, 
- Print-friendly layout

## Prompt de referência
Design an executive dashboard. Use: large KPI cards (4-6 max), trend sparklines, high-level summary only, clean layout with white space, traffic light indicators (red/yellow/green), at-a-glance insights, minimal detail.

