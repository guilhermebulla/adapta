# Predictive Analytics

- id: `predictive-analytics`  ·  tipo: BI/Analytics  ·  status: supplemental
- pai: `data-dense-dashboard`  ·  complexidade: Medium
- era: 2020s Modern  ·  frameworks: recharts/chartjs/d3
- light/dark: supported / supported  ·  perf: cost:low/drivers:none  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Forecasting dashboards, anomaly detection systems, trend prediction dashboards, AI-powered analytics, budget planning

## Não usar para
Historical-only dashboards, simple reporting, real-time operational dashboards

## Cores primárias
Forecast line color (distinct from actual), confidence interval shading, anomaly highlight (red alert), trend colors

## Cores secundárias
High confidence (dark color), low confidence (light color), anomaly colors (red/orange), normal trend (green/blue)

## Efeitos & animação
Forecast line animation on draw, confidence band fade-in, anomaly pulse alert, smoothing function animations

## Tokens
```css
--forecast-dash: 5 5, --confidence-opacity: 0.2, --anomaly-color: #F59E0B, --prediction-color: #8B5CF6, --scenario-toggle-width: 48px, --ai-accent: #6366F1
```

## Checklist
Forecast line distinct, 
- Confidence bands visible, 
- Anomalies highlighted, 
- Scenarios switchable, 
- Predictions dated, 
- Accuracy shown

## Prompt de referência
Design a predictive analytics dashboard. Use: forecast lines (dashed), confidence intervals (shaded bands), trend projections, anomaly highlights, scenario toggles, AI insight cards, probability indicators.

