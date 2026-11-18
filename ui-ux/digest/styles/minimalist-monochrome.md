# Minimalist Monochrome

- id: `minimalist-monochrome`  ·  tipo: Mobile  ·  status: supplemental
- pai: `minimalism-and-swiss-style`  ·  complexidade: Medium
- era: 2020s Editorial Mobile  ·  frameworks: react-native/expo/swiftui/tailwind
- light/dark: supported / conditional  ·  perf: cost:low/drivers:none  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Luxury fashion e-commerce mobile, editorial publications, high-end portfolio apps, experimental/avant-garde brands, digital exhibitions

## Não usar para
Entertainment, colorful brands, friendly consumer apps, anything requiring visual warmth or gradient

## Cores primárias
Pure Black #000000, Pure White #FFFFFF

## Cores secundárias
Muted #F5F5F5, Dark Gray #525252, Border Light #E5E5E5

## Efeitos & animação
Instant inversion active state (tap → bg-black text-white, zero transition-none), no shadows (strictly 2D), full-bleed horizontal rules (4px black section dividers), subtle paper noise texture (opacity: 0.03), slide-in page transitions with hard edge

## Tokens
```css
--color-bg: #FFFFFF, --color-fg: #000000, --color-muted: #F5F5F5, --color-muted-fg: #525252, --color-border: #000000, --color-border-light: #E5E5E5, --radius: 0px, --shadow: none, --border-hairline: 1px solid #E5E5E5, --border-thin: 1px solid #000000, --border-thick: 2px solid #000000, --border-heavy: 4px solid #000000, --font-display: Playfair Display, --font-body: Source Serif 4, --font-mono: JetBrains Mono
```

## Checklist
0px border-radius on ALL elements, 
- No shadows anywhere, 
- Instant inversion on every tap (transition-none), 
- 4px black line separates hero from content, 
- Safe area respected (pt-safe pb-safe), 
- h-14 touch targets, 
- Sticky section headers with border-b, 
- Typography hero: word spans full screen width, 
- Paper noise texture on backgrounds, 
- Menu word-label instead of icon

## Prompt de referência
Design a Minimalist Monochrome mobile interface using monochrome, black white, editorial, austere, typographic, sharp, zero radius, high contrast. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.

