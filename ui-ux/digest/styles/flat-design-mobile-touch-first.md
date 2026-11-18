# Flat Design Mobile (Touch-First)

- id: `flat-design-mobile-touch-first`  ·  tipo: Mobile  ·  status: supplemental
- pai: `flat-design`  ·  complexidade: Low
- era: 2010s–2020s Flat Mobile  ·  frameworks: react-native/expo/nativewind/flutter/swiftui
- light/dark: supported / conditional  ·  perf: cost:low/drivers:none  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Cross-platform apps (iOS+Android parity), information-dense dashboards, system UI, brand illustration, onboarding flows, marketing pages, icon design

## Não usar para
Ultra-premium contexts needing depth/shadow, dark-mode-first products, contexts where flat design reads as unfinished or sterile

## Cores primárias
Blue #3B82F6, Emerald #10B981

## Cores secundárias
Background #FFFFFF, Surface #F3F4F6, Text #111827, Amber #F59E0B, Border #E5E7EB

## Efeitos & animação
Immediate press feedback (scale 0.97, no delay), color section blocking (full-width contrasting View), zero elevation/shadow, solid icon containers (colored squares/circles), geometric low-opacity shape overlays, bottom tabs solid fill (no floating)

## Tokens
```css
--bg: #FFFFFF, --surface: #F3F4F6, --fg: #111827, --primary: #3B82F6, --secondary: #10B981, --accent: #F59E0B, --border: #E5E7EB, --radius-sm: 6px, --radius-md: 12px, --radius-pill: 999px, --shadow: none, --elevation: 0, --touch-target: 48px, --spacing: 4 8 16 24 32 48
```

## Checklist
Zero elevation AND shadowOpacity on all elements, 
- Color-blocking sections (not borders), 
- All touch targets ≥ 48×48, 
- No gradients on flat elements, 
- Icons inside solid colored containers, 
- Pressable scale feedback, 
- Geometric shapes as bg decoration, 
- Bold flat bottom tabs (no floating), 
- Primary headlines much larger than body, 
- 4pt spacing system throughout

## Prompt de referência
Design a Flat Design Mobile (Touch-First) mobile interface using flat, 2D, no shadow, color blocking, geometric, bold, poster, icon. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.

