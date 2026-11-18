# 3D Product Preview

- id: `3d-product-preview`  ·  tipo: General  ·  status: active
- pai: ``  ·  complexidade: High
- era: 2025+ E-commerce 3D  ·  frameworks: threejs/model-viewer/spline
- light/dark: conditional / conditional  ·  perf: cost:high/drivers:animation,large-images  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
E-commerce, furniture, fashion, automotive, electronics, jewelry, product configurators

## Não usar para
Content-heavy sites, blogs, dashboards, low-bandwidth, accessibility-critical

## Cores primárias
Product-dependent, neutral backgrounds: Soft Grey #E8E8E8, Pure White #FFFFFF

## Cores secundárias
Shadow gradients, reflection planes, environment lighting colors, accent highlights

## Efeitos & animação
Drag-to-rotate, pinch-to-zoom, spin animation, AR placement, material switching, smooth orbit controls

## Tokens
```css
--canvas-bg: #F5F5F5, --hotspot-color: #3B82F6, --loading-spinner: primary, --rotation-speed: 0.5, --zoom-min: 0.5, --zoom-max: 2
```

## Checklist
3D model loads fast, 
- Rotation smooth, 
- Zoom works (pinch/scroll), 
- AR button functional, 
- Colors switchable, 
- Mobile touch works

## Prompt de referência
Design a 3D product preview interface. Use: 360° rotation, drag-to-spin, pinch-to-zoom, AR preview button, material/color switcher, hotspot annotations, orbit controls, product configurator, smooth rendering.

