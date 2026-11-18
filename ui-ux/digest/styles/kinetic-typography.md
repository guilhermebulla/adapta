# Kinetic Typography

- id: `kinetic-typography`  ·  tipo: General  ·  status: active
- pai: ``  ·  complexidade: High
- era: 2020s Modern  ·  frameworks: gsap/framer-motion
- light/dark: supported / supported  ·  perf: cost:moderate/drivers:animation,blur  ·  a11y: risk:high/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Hero sections, marketing sites, video platforms, storytelling, creative portfolios, landing pages

## Não usar para
Long-form content, accessibility-critical, data interfaces, forms, elderly users

## Cores primárias
Flexible - high contrast recommended, bold colors for emphasis, animation-friendly palette

## Cores secundárias
Accent colors for emphasis, transition colors, gradient text fills

## Efeitos & animação
@keyframes text animation, typing effect, background-clip: text, GSAP ScrollTrigger, split text

## Tokens
```css
--text-animation-duration: 1s, --letter-delay: 0.05s, --typing-speed: 100ms, --gradient-text: linear-gradient(90deg, #color1, #color2), --morph-duration: 0.5s
```

## Checklist
Text animations smooth, 
- Prefers-reduced-motion respected, 
- Fallback for no-JS, 
- Mobile performance ok, 
- Typing effect timed, 
- Scroll triggers work

## Prompt de referência
Design with kinetic typography. Use: animated text, scroll-triggered reveals, typing effects, letter-by-letter animations, morphing text, gradient text fills, oversized hero text, text as the main visual element.

