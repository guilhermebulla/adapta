# Neo Brutalism (Mobile)

- id: `neo-brutalism-mobile`  ·  tipo: Mobile  ·  status: supplemental
- pai: `neubrutalism`  ·  complexidade: High
- era: 2020s Neo-Brutalism  ·  frameworks: react-native/expo/nativewind
- light/dark: supported / not-recommended  ·  perf: cost:moderate/drivers:animation,blur  ·  a11y: risk:conditional/requires:contrast-text-4.5,keyboard,visible-focus,reduced-moti…

## Best for
Creative tools, collab platforms, Gen Z marketing & e-commerce, portfolio sites, sticker-book style content apps

## Não usar para
Serious enterprise apps, conservative industries, sober fintech, accessibility-first contexts (must tune contrast)

## Cores primárias
Cream #FFFDF5, Hot Red #FF6B6B, Vivid Yellow #FFD93D

## Cores secundárias
Soft Violet #C4B5FD, Pure Black #000000, White #FFFFFF

## Efeitos & animação
Thick 4px black borders on all major elements, hard offset shadows (4–8px, no blur), mechanical press: translateX/Y equal to shadow offset, slightly rotated cards/badges (-2deg/2deg), high-saturation color blocking, spring/linear animations only

## Tokens
```css
--bg: #FFFDF5, --ink: #000000, --accent-primary: #FF6B6B, --accent-secondary: #FFD93D, --accent-muted: #C4B5FD, --white: #FFFFFF, --border-primary: 4px solid #000000, --shadow-offset-small: 4px, --shadow-offset-medium: 8px, --radius: 0px, --radius-pill: 999px, --font: Space Grotesk
```

## Checklist
4px borders on major elements, 
- Hard offset shadow implemented via extra View, 
- Mechanical press hides shadow, 
- Cream canvas background, 
- Pop-art color palette used, 
- Cards/badges slightly rotated, 
- No gradients or soft shadows, 
- Only bold/black type weights, 
- Badges slapped with absolute positioning, 
- Anti-patterns (no subtle gray, no blur) avoided

## Prompt de referência
Design a Neo Brutalism (Mobile) mobile interface using neo brutalism, pop art, stickers, thick borders, cream background, hot red, vivid yellow, soft violet. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.

