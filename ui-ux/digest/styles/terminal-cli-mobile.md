# Terminal CLI (Mobile)

- id: `terminal-cli-mobile`  ·  tipo: Mobile  ·  status: supplemental
- pai: `hud-sci-fi-fui`  ·  complexidade: Medium
- era: Retro-Future 1980s–2020s  ·  frameworks: react-native/expo/nativewind
- light/dark: not-recommended / supported  ·  perf: cost:low/drivers:none  ·  a11y: risk:conditional/requires:contrast-text-4.5,keyboard,visible-focus,reduced-moti…

## Best for
Developer tools, Web3/blockchain apps, geek-culture apps, ARG games, sci-fi/noir gaming companions, hacker/security tools, creative studio portfolios

## Não usar para
Consumer products, health apps, anything requiring approachability or warmth, children's apps, standard enterprise contexts

## Cores primárias
Matrix Green #33FF00, OLED Black #050505

## Cores secundárias
Amber #FFB000, Muted Green #1A3D1A, Error Red #FF3333, Border Green #33FF00

## Efeitos & animação
Blinking cursor (500ms opacity loop), typewriter text reveal hook, scanline overlay (repeating lines 0.05 opacity), ASCII art headers, instant color inversion on press (bg-green text-black), haptic on every keystroke, boot sequence splash on launch

## Tokens
```css
--bg: #050505, --fg-primary: #33FF00, --fg-amber: #FFB000, --fg-muted: #1A3D1A, --fg-error: #FF3333, --border: #33FF00, --radius: 0px, --font: SpaceMono-Regular or JetBrains Mono, --font-sizes: 12 14 16 only, --blink-duration: 500ms, --scanline-opacity: 0.05
```

## Checklist
0px border-radius everywhere, 
- ASCII-style borders on cards, 
- Boot sequence on launch, 
- Blinking cursor component, 
- Typewriter hook for new content, 
- Scanline overlay (0.05 opacity), 
- Haptic on every button press, 
- Footer status bar component, 
- hitSlop on all bracketed buttons (44×44dp), 
- Reduced motion respected

## Prompt de referência
Design a Terminal CLI (Mobile) mobile interface using terminal, cli, matrix green, monospace, hacker, ascii, command line, developer. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.

