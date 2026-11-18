# Liquid Glass

- id: `liquid-glass`  ·  tipo: Platform/Material  ·  status: active
- pai: ``  ·  complexidade: High
- era: Apple platforms, 2025  ·  frameworks: swiftui/uikit/appkit
- light/dark: supported / supported  ·  perf: cost:moderate/drivers:animation,blur  ·  a11y: risk:conditional/requires:contrast-text-4.5,keyboard,visible-focus,reduced-moti…

## Best for
Apple-platform navigation, controls, and system-aligned app chrome

## Não usar para
content layers, dense reading surfaces, or custom effects without accessibility fallbacks

## Cores primárias
Adaptive translucent material derived from surrounding content; use color judiciously

## Cores secundárias
Semantic content and system tint colors; preserve legibility and hierarchy

## Efeitos & animação
Lensing and refraction, adaptive translucency, and fluid morph transitions aligned to Apple platform behavior

## Tokens
```css
--material-role: navigation-controls, --translucency: adaptive, --tint: semantic, --reduced-transparency-fallback: opaque, --motion: platform-aligned
```

## Checklist
Use for navigation and controls, 
- Keep content on a separate layer, 
- Apply color judiciously, 
- Test reduced transparency, 
- Test reduced motion, 
- Verify text and control contrast

## Prompt de referência
Apply Apple Liquid Glass sparingly to navigation and controls. Use dynamic translucent material, lensing, and fluid transitions while keeping content clear. Respect reduced transparency and reduced motion settings.

