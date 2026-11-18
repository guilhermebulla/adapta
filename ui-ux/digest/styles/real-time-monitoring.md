# Real-Time Monitoring

- id: `real-time-monitoring`  ·  tipo: BI/Analytics  ·  status: supplemental
- pai: `data-dense-dashboard`  ·  complexidade: Medium
- era: 2020s Modern  ·  frameworks: recharts/chartjs/d3
- light/dark: supported / supported  ·  perf: cost:low/drivers:none  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
System monitoring dashboards, DevOps dashboards, real-time analytics, stock market dashboards, live event tracking

## Não usar para
Historical analysis, long-term trend reports, archived data dashboards

## Cores primárias
Alert colors: critical (red #FF0000), warning (orange #FFA500), normal (green #22C55E), updating (blue animation)

## Cores secundárias
Status indicator colors, chart line colors varying by metric, streaming data highlight colors

## Efeitos & animação
Real-time chart animations, alert pulse/glow, status indicator blink animation, smooth data stream updates, loading effect

## Tokens
```css
--pulse-animation: pulse 2s infinite, --alert-z-index: 1000, --live-indicator: #22C55E, --critical-color: #DC2626, --update-interval: 5s, --toast-duration: 5s
```

## Checklist
Live updates working, 
- Alert sounds optional, 
- Connection status shown, 
- Auto-refresh indicated, 
- Critical alerts prominent, 
- Offline fallback

## Prompt de referência
Design a real-time monitoring dashboard. Use: live status indicators (pulsing), streaming charts, alert notifications, connection status, auto-refresh indicators, critical alerts prominent, system health overview.

