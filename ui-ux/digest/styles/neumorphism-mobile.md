# Neumorphism (Mobile)

- id: `neumorphism-mobile`  ·  tipo: Mobile  ·  status: supplemental
- pai: `neumorphism`  ·  complexidade: Medium
- era: Tools/Lifestyle  ·  frameworks: react-native/react-native-shadow-2/react-native-reanimated
- light/dark: supported / not-recommended  ·  perf: cost:low/drivers:none  ·  a11y: risk:conditional/requires:contrast-text-4.5,keyboard,visible-focus,reduced-moti…

## Best for
Minimal hardware controls, smart home apps, aesthetic utility tools, health monitors, brand showcase pages

## Não usar para
High-density data, bright multi-color apps, apps needing strong visual hierarchy via color, dark-mode-only products

## Cores primárias
Accent Violet #6C63FF, Clay Base #E0E5EC

## Cores secundárias
Text Dark #3D4852, Text Muted #6B7280, Shadow Light rgba(255,255,255,0.6), Shadow Dark rgba(163,177,198,0.7), Inset Background #D1D9E6

## Efeitos & animação
Full-screen #E0E5EC base, dual-layer shadow via nested View (light top-left + dark bottom-right), extruded convex resting state, inset concave pressed/input state, Reanimated scale 0.97 on press, shadow opacity interpolates 1→0.4 on press, Haptics Light on every interaction, 8pt grid, no blur shadows (no shadowRadius blend), nested depth (extruded card contains inset icon slot)

## Tokens
```css
--bg: #E0E5EC, --text: #3D4852, --muted: #6B7280, --accent: #6C63FF, --shadow-light: rgba(255,255,255,0.6), --shadow-dark: rgba(163,177,198,0.7), --inset-bg: #D1D9E6, --radius-card: 32px, --radius-button: 16px, --font: Plus Jakarta Sans or System
```

## Checklist
Single #E0E5EC base applied across all screens, 
- Dual shadow (light+dark) implemented via nested View, 
- Extruded resting state on cards/buttons, 
- Inset concave state on inputs, 
- Scale 0.97 press + shadow opacity interpolation, 
- Haptics Light on all presses, 
- No black shadows or white backgrounds, 
- Nested depth pattern (extruded→inset), 
- Accent #6C63FF on active/focus only, 
- 8pt grid spacing

## Prompt de referência
Design a Neumorphism (Mobile) mobile interface using neumorphism, soft ui, dual shadow, extruded, inset, clay surface, monochromatic, cool grey. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.

