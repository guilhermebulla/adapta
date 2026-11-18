# Inclusive Design

- id: `inclusive-design`  ·  tipo: General  ·  status: active
- pai: ``  ·  complexidade: Low
- era: Universal  ·  frameworks: css
- light/dark: supported / supported  ·  perf: cost:low/drivers:none  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Public services, education, healthcare, finance, government, accessible consumer, inclusive

## Não usar para
None - accessibility universal

## Cores primárias
Measured contrast pairs targeting 7:1 for normal text, avoid red-green only, symbol-based indicators, high contrast primary

## Cores secundárias
Supporting patterns (stripes, dots, hatch), symbols, combinations, clear non-color indicators

## Efeitos & animação
Haptic feedback (vibration), voice guidance, focus indicators (4px+ ring), motion options, alt content, semantic

## Tokens
```css
--contrast-ratio: 7:1, --font-size: 16px+, --keyboard-accessible: true, --sr-test-required: true, --wcag-target: enhanced, --color-symbols: true, --haptic: enabled
```

## Checklist
complete-page conformance tested against the chosen target, 
- 7:1+ contrast all text, 
- Keyboard accessible (Tab/Enter), 
- Screen reader tested, 
- Focus visible 3-4px, 
- No color-only indicators, 
- Haptic fallback

## Prompt de referência
Design for universal accessibility: high contrast (7:1+), large text (16px+), keyboard-only navigation, screen reader optimization, enhanced accessibility criteria with complete-page verification, symbol-based color indicators (not color-only), haptic feedback, voice interaction support, reduced motion options.

