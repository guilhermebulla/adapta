# Motion-Driven

- id: `motion-driven`  ·  tipo: General  ·  status: active
- pai: ``  ·  complexidade: High
- era: 2020s Modern  ·  frameworks: gsap/framer-motion
- light/dark: supported / supported  ·  perf: cost:low/drivers:none  ·  a11y: risk:conditional/requires:contrast-text-4.5,keyboard,visible-focus,reduced-moti…

## Best for
Portfolio sites, storytelling platforms, interactive experiences, entertainment apps, creative, SaaS

## Não usar para
Data dashboards, critical accessibility, low-power devices, content-heavy, motion-sensitive

## Cores primárias
Bold colors emphasize movement, high contrast animated, dynamic gradients, accent action colors

## Cores secundárias
Transitional states, success (Green #22C55E), error (Red #EF4444), neutral feedback

## Efeitos & animação
Scroll anim (Intersection Observer), hover (300-400ms), entrance, parallax (3-5 layers), page transitions

## Tokens
```css
--animation-duration: 300-400ms, --parallax-layers: 5, --scroll-behavior: smooth, --gpu-accelerated: true, --entrance-animation: true, --page-transition: smooth
```

## Checklist
Scroll animations active, 
- Parallax 3-5 layers, 
- Entrance animations smooth, 
- Page transitions fluid, 
- GPU accelerated, 
- Prefers-reduced-motion respected

## Prompt de referência
Build an animation-heavy interface with scroll-triggered animations, microinteractions, parallax scrolling (3-5 layers), smooth transitions (300-400ms), entrance animations, page transitions. Use Intersection Observer for scroll effects, transform for performance, GPU acceleration.

