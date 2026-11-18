# Cyberpunk Mobile HUD

- id: `cyberpunk-mobile-hud`  ·  tipo: Mobile  ·  status: supplemental
- pai: `hud-sci-fi-fui`  ·  complexidade: High
- era: Cyber-Noir  ·  frameworks: react-native/custom/expo
- light/dark: not-recommended / supported  ·  perf: cost:high/drivers:animation,large-images  ·  a11y: risk:conditional/requires:contrast-text-4.5,keyboard,visible-focus,reduced-moti…

## Best for
Gaming dashboards, crypto/cyberpunk apps, sci-fi companion tools, hacker OS skins, data-heavy monitoring HUDs

## Não usar para
Serious enterprise, health/finance requiring calm trust, minimal editorial apps

## Cores primárias
Void #0A0A0F, Card #12121A

## Cores secundárias
Neon Green #00FF88, Neon Magenta #FF00FF, Cyber Cyan #00D4FF, Neutral Text #E0E0E0, Alert Red #FF3366, Border #2A2A3A

## Efeitos & animação
Deep void background with neon radiance, chamfered 45° corners via SVG/Skia, scanline overlay, CRT flicker opacity oscillation, glitch animations (translateX ±2), neon pulses around buttons, HUD corner brackets, terminal prompt text inputs, heavy use of blurView holographic panels

## Tokens
```css
--bg: #0A0A0F, --card: #12121A, --fg: #E0E0E0, --muted: #1C1C2E, --accent: #00FF88, --accent2: #FF00FF, --accent3: #00D4FF, --border: #2A2A3A, --destructive: #FF3366, --radius: 0px, --font-heading: Orbitron, --font-body: JetBrains Mono
```

## Checklist
Chamfered corners used instead of radius, 
- Scanline & CRT flicker implemented, 
- Orbitron + JetBrains Mono typography, 
- Neon glow shadows on primary buttons, 
- Glitch animation on active states, 
- Prompt-style inputs with custom cursor, 
- HUD corner brackets implemented, 
- Safe-area system status bar styled, 
- Reduced motion disables glitch/flicker, 
- Icons configured with Lucide accent color

## Prompt de referência
Design a Cyberpunk Mobile HUD mobile interface using cyberpunk, neon, glitch, chamfered, orbitron, jetbrains, scanlines, crt. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.

