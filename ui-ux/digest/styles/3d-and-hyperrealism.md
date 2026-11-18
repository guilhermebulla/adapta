# 3D & Hyperrealism

- id: `3d-and-hyperrealism`  ·  tipo: General  ·  status: active
- pai: ``  ·  complexidade: High
- era: 2020s Modern  ·  frameworks: threejs/react-three-fiber/custom
- light/dark: conditional / conditional  ·  perf: cost:high/drivers:animation,large-images  ·  a11y: risk:high/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Gaming, product showcase, immersive experiences, high-end e-commerce, architectural viz, VR/AR

## Não usar para
Low-end mobile, performance-limited, critical accessibility, data tables/forms

## Cores primárias
Deep Navy #001F3F, Forest Green #228B22, Burgundy #800020, Gold #FFD700, Silver #C0C0C0

## Cores secundárias
Complex gradients (5-10 stops), realistic lighting, shadow variations (20-40% darker)

## Efeitos & animação
WebGL/Three.js 3D, realistic shadows (layers), physics lighting, parallax (3-5 layers), smooth 3D (300-400ms)

## Tokens
```css
--perspective: 1000px, --parallax-layers: 5, --lighting-intensity: realistic, --shadow-depth: 20-40%, --animation-duration: 300-400ms
```

## Checklist
WebGL/Three.js integrated, 
- 3D models loaded, 
- Parallax 3-5 layers, 
- Realistic lighting verified, 
- Complex shadows rendered, 
- Physics animation smooth 300-400ms

## Prompt de referência
Build an immersive 3D interface using realistic textures, 3D models (Three.js/Babylon.js), complex shadows, realistic lighting, parallax scrolling (3-5 layers), physics-based motion. Include skeuomorphic elements with tactile detail.

