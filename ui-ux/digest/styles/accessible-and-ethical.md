# Accessible & Ethical

- id: `accessible-and-ethical`  ·  tipo: General  ·  status: active
- pai: ``  ·  complexidade: Low
- era: Universal  ·  frameworks: css
- light/dark: supported / supported  ·  perf: cost:low/drivers:none  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Government, healthcare, education, inclusive products, large audience, legal compliance, public

## Não usar para
None - accessibility universal

## Cores primárias
Measured high-contrast pairs (4.5:1 normal-text baseline; 7:1 enhanced target), simple primary, clear secondary, high luminosity (7:1+)

## Cores secundárias
Symbol-based colors (not color-only), supporting patterns, inclusive combinations

## Efeitos & animação
Clear focus rings (3-4px), ARIA labels, skip links, responsive design, reduced motion, 44x44px touch targets

## Tokens
```css
--contrast-ratio: 7:1, --font-size-min: 16px, --focus-ring: 3-4px, --touch-target: 44x44px, --wcag-target: enhanced, --keyboard-accessible: true, --sr-test-required: true
```

## Checklist
complete-page conformance tested against the chosen target, 
- 7:1+ contrast checked, 
- Keyboard navigation tested, 
- Screen reader tested, 
- Focus visible 3-4px, 
- Semantic HTML used, 
- Touch targets 44x44px

## Prompt de referência
Design toward enhanced accessibility criteria; verify complete-page conformance. Include: high contrast (7:1+), large text (16px+), keyboard navigation, screen reader compatibility, focus states visible (3-4px ring), semantic HTML, ARIA labels, skip links, reduced motion support (prefers-reduced-motion), 44x44px touch targets.

