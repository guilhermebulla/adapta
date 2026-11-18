# Spatial UI (VisionOS)

- id: `spatial-ui-visionos`  ·  tipo: General  ·  status: active
- pai: ``  ·  complexidade: High
- era: 2024 Spatial Era  ·  frameworks: swiftui/custom
- light/dark: supported / supported  ·  perf: cost:moderate/drivers:animation,blur  ·  a11y: risk:conditional/requires:contrast-text-4.5,keyboard,visible-focus,reduced-moti…

## Best for
Spatial computing apps, VR/AR interfaces, immersive media, futuristic dashboards

## Não usar para
Text-heavy documents, high-contrast requirements, non-3D capable devices

## Cores primárias
Frosted Glass #FFFFFF (15-30% opacity), System White

## Cores secundárias
Vibrant system colors for active states, deep shadows for depth

## Efeitos & animação
Parallax depth, dynamic lighting response, gaze-hover effects, smooth scale on focus

## Tokens
```css
--glass-bg: rgba(255,255,255,0.2), --glass-blur: 40px, --glass-saturate: 180%, --window-radius: 24px, --depth-shadow: 0 8px 32px rgba(0,0,0,0.1), --focus-scale: 1.02
```

## Checklist
Glass effect visible, 
- Depth layers clear, 
- Hover states defined, 
- Colors vibrant on active, 
- Floating feel achieved, 
- Contrast maintained

## Prompt de referência
Design a VisionOS-style spatial interface. Use: frosted glass panels, depth layers, translucent backgrounds (15-30% opacity), vibrant colors for active states, gaze-hover effects, floating windows, immersive feel.

