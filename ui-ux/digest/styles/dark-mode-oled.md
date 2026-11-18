# Dark Mode (OLED)

- id: `dark-mode-oled`  ·  tipo: General  ·  status: active
- pai: ``  ·  complexidade: Low
- era: 2020s Modern  ·  frameworks: tailwind/mui/chakra
- light/dark: not-recommended / supported  ·  perf: cost:low/drivers:none  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Night-mode apps, coding platforms, entertainment, eye-strain prevention, OLED devices, low-light

## Não usar para
Print-first content, high-brightness outdoor, color-accuracy-critical

## Cores primárias
Deep Black #000000, Dark Grey #121212, Midnight Blue #0A0E27

## Cores secundárias
Vibrant accents: Neon Green #39FF14, Electric Blue #0080FF, Gold #FFD700, Plasma Purple #BF00FF

## Efeitos & animação
Minimal glow (text-shadow: 0 0 10px), dark-to-light transitions, low white emission, high readability, visible focus

## Tokens
```css
--bg-black: #000000, --bg-dark-grey: #121212, --text-primary: #FFFFFF, --accent-neon: neon colors, --glow-effect: minimal, --oled-optimized: true
```

## Checklist
Deep black #000000 or #121212, 
- Vibrant neon accents used, 
- Text contrast 7:1+, 
- Minimal glow effects, 
- OLED power optimization, 
- No white (#FFFFFF) background

## Prompt de referência
Create an OLED-optimized dark interface with deep black (#000000), dark grey (#121212), midnight blue accents. Use minimal glow effects, vibrant neon accents (green, blue, gold, purple), high contrast text. Optimize for eye comfort and OLED power saving.

