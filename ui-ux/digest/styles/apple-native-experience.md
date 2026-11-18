# Apple Native Experience

- id: `apple-native-experience`  ·  tipo: Platform/System  ·  status: active
- pai: ``  ·  complexidade: Medium
- era: Apple Human Interface Guideli…  ·  frameworks: swiftui/uikit/appkit/react-native/custom
- light/dark: supported / supported  ·  perf: cost:moderate/drivers:animation  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion,seman…

## Best for
Native-feeling phone, tablet, and desktop apps, productivity tools, settings, forms, lists, media and utility products, responsive web apps adopting platform-aware behavior

## Não usar para
Liquid Glass as the defining visual treatment, visionOS spatial interfaces, decorative blur or gradients, dense dashboards needing unrelated platform conventions, or web layouts that must behave identically on every platform

## Cores primárias
Adaptive system backgrounds and grouped surfaces; semantic accent, label, separator, fill, and destructive colors; avoid hard-coded appearance assumptions

## Cores secundárias
Secondary and tertiary labels, grouped content surfaces, control fills, accessible accent states, light/dark semantic mapping

## Efeitos & animação
Content-first hierarchy, system typography roles, 8pt-aligned spacing, restrained borders and shadows, platform-appropriate corner radii, SF Symbols-style consistent icons, adaptive light/dark appearance, purposeful 150-300ms transitions, reduced-motion and reduced-transparency fallbacks

## Tokens
```css
--color-bg: semantic system background, --color-surface: grouped surface, --color-label-primary: semantic primary label, --color-label-secondary: semantic secondary label, --color-accent: platform accent, --color-separator: semantic separator, --font-body: system-ui, --space-unit: 4px, --radius-control: 10px, --touch-target: 44px, --motion-duration: 150-300ms, --focus-ring: 2px
```

## Checklist
Use semantic roles for navigation bars, tab bars, sidebars, toolbars, buttons, segmented controls, toggles, text/search fields, sheets, popovers, menus, alerts, lists, and grouped content; preserve safe areas; provide keyboard and screen-reader semantics; verify light/dark contrast; test phone, tablet, desktop, reduced motion, and reduced transparency

## Prompt de referência
Design an Apple Native Experience interface with system typography, semantic adaptive colors, platform-aware navigation, accessible controls, grouped lists, sheets, popovers, purposeful transitions, and responsive behavior across phone, tablet, desktop, and web. Do not require Liquid Glass, blur, or gradients.

