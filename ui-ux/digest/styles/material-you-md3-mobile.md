# Material 3 Expressive (Mobile)

- id: `material-you-md3-mobile`  ·  tipo: Mobile  ·  status: active
- pai: ``  ·  complexidade: Medium
- era: Google Material Design 3  ·  frameworks: material-3/jetpack-compose/android-views/flutter
- light/dark: supported / supported  ·  perf: cost:moderate/drivers:animation,blur  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Android, Wear OS, and Pixel-aligned products using Material 3 components

## Não usar para
Ultra-minimal brutalist brands, terminal/hacker aesthetics, monochrome editorial apps

## Cores primárias
Primary Violet #6750A4, Secondary Container #E8DEF8, Tertiary #7D5260

## Cores secundárias
Surface #FFFBFE, On Surface #1C1B1F, Surface Container #F3EDF7, Outline #79747E

## Efeitos & animação
Tonal elevation (overlay colors instead of strong shadows), pill-shaped buttons and chips (borderRadius 999), emphasized easing Easing.bezier(0.2,0,0,1), state layers (pressed overlays 10–15% opacity), Reanimated-filled label float for inputs, HapticFeedback on FAB/toggles

## Tokens
```css
--md3-bg: #FFFBFE, --md3-on-surface: #1C1B1F, --md3-primary: #6750A4, --md3-on-primary: #FFFFFF, --md3-secondary-container: #E8DEF8, --md3-on-secondary-container: #1D192B, --md3-tertiary: #7D5260, --md3-surface-container: #F3EDF7, --md3-outline: #79747E, --radius-pill: 999px, --easing-emphasized: cubic-bezier(0.2,0,0,1)
```

## Checklist
MD3 color tokens applied (background/surface/container), 
- All CTAs are pill-shaped, 
- State-layer overlays instead of opacity 0.5 hacks, 
- Emphasized easing used for all animations, 
- Floating label inputs implemented, 
- FAB uses tertiary color with correct elevation, 
- Safe areas respected for organic shapes, 
- No pure white background, 
- No harsh box-shadows (ambient only)

## Prompt de referência
Design a Material 3 Expressive mobile interface with vibrant semantic color, contrasting shapes, flexible typography, adaptive components, spring motion, and reduced-motion alternatives.

