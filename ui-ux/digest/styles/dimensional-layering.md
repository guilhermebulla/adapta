# Dimensional Layering

- id: `dimensional-layering`  ·  tipo: General  ·  status: active
- pai: ``  ·  complexidade: Medium
- era: 2020s Modern  ·  frameworks: tailwind/mui/chakra
- light/dark: supported / supported  ·  perf: cost:low/drivers:none  ·  a11y: risk:high/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Dashboards, card layouts, modals, navigation, product showcases, SaaS interfaces

## Não usar para
Print-style layouts, simple blogs, low-end devices, flat design requirements

## Cores primárias
Neutral base (#FFFFFF, #F5F5F5, #E0E0E0) + brand accent for elevated elements

## Cores secundárias
Shadow variations (sm/md/lg/xl), elevation colors, highlight colors for top layers

## Efeitos & animação
z-index stacking, box-shadow elevation (4 levels), transform: translateZ(), backdrop-filter, parallax

## Tokens
```css
--elevation-1: 0 1px 3px rgba(0,0,0,0.1), --elevation-2: 0 4px 6px rgba(0,0,0,0.1), --elevation-3: 0 10px 20px rgba(0,0,0,0.1), --elevation-4: 0 20px 40px rgba(0,0,0,0.15), --blur-amount: 8px
```

## Checklist
Layers clearly defined, 
- Shadows show depth, 
- Overlaps intentional, 
- Hierarchy clear, 
- Performance optimized, 
- Mobile depth maintained

## Prompt de referência
Design with dimensional layering. Use: z-index depth (multiple layers), overlapping cards, elevation shadows (4 levels), floating elements, parallax depth, backdrop blur for hierarchy, spatial UI feel.

