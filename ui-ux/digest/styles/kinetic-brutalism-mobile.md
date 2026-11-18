# Kinetic Brutalism (Mobile)

- id: `kinetic-brutalism-mobile`  ·  tipo: Mobile  ·  status: supplemental
- pai: `brutalism`  ·  complexidade: High
- era: 2020s Mobile Brutalism  ·  frameworks: react-native/expo/react-native-reanimated/nativewind
- light/dark: supported / conditional  ·  perf: cost:low/drivers:none  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Immersive storytelling apps, brand flagship mobile, music/culture platforms, sports apps, underground zines, limited-edition product drops, performance dashboards

## Não usar para
Calm informational apps, healthcare, finance contexts needing trust, children's, any context where aggressive typography feels inappropriate

## Cores primárias
Acid Yellow #DFE104, Rich Black #09090B

## Cores secundárias
Off-white #FAFAFA, Dark Gray #27272A, Zinc #A1A1AA, Border Zinc #3F3F46

## Efeitos & animação
Infinite marquee (Reanimated, Linear easing, 5s loop, hard clip), hero parallax (scale 1.0→1.3 + fade), sticky section header push, card flood inversion on press (bg→#DFE104, text→#000000), haptic Medium on every press, scroll-triggered interpolate transforms, 0px radius, 2px borders, 100ms color transitions

## Tokens
```css
--bg: #09090B, --fg: #FAFAFA, --muted: #27272A, --muted-fg: #A1A1AA, --accent: #DFE104, --accent-fg: #000000, --border: #3F3F46, --radius: 0px, --border-width: 2px, --shadow: none, --marquee-speed: 5000ms, --press-duration: 100ms, --font: Space Grotesk or Inter
```

## Checklist
Infinite marquee rows (Reanimated, no fade edges), 
- Hero parallax scroll (scale+opacity Interpolate), 
- All display text uppercase, 
- 0px border-radius, 
- 2px borders, 
- Acid yellow card flood on press, 
- Haptic Medium on every interaction, 
- Font scale helper (windowWidth/375*size), 
- Safe area for massive headers, 
- Reduced motion stops marquees

## Prompt de referência
Design a Kinetic Brutalism (Mobile) mobile interface using kinetic, brutalism, motion, marquee, acid yellow, uppercase, oversized, aggressive typography. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.

