# Sketch Hand-Drawn (Mobile)

- id: `sketch-hand-drawn-mobile`  ·  tipo: Mobile  ·  status: supplemental
- pai: `anti-polish-raw-aesthetic`  ·  complexidade: Medium
- era: Creative/Education  ·  frameworks: react-native/react-native-reanimated/expo
- light/dark: supported / supported  ·  perf: cost:low/drivers:none  ·  a11y: risk:low/requires:contrast-text-4.5,keyboard,visible-focus,reduced-motion

## Best for
Low-fidelity prototyping, creative brands, children/picturebook apps, education tools, journaling apps, gamified puzzles

## Não usar para
Enterprise dashboards, high-density data tables, fintech precision tools, medical or legal apps

## Cores primárias
Red Marker #FF4D4D, Pencil Black #2D2D2D

## Cores secundárias
Warm Paper #FDFBF7, Old Paper #E5E0D8, Blue Ballpoint #2D5DA1, Post-it Yellow #FFF9C4

## Efeitos & animação
Wobbly borderRadius (unique per corner: 15/25/20/10), borderWidth 2–3 solid/dashed, hard offset shadow via rear View (4px,4px) #2D2D2D, Kalam Bold headings, PatrickHand Regular body, slight rotation (-1deg/1deg) on cards, absolute SVG scribble overlays (arrows/tape/tacks), jiggle -2deg↔2deg on error, LayoutAnimation spring on layout changes, Haptics on press, paper texture repeating background

## Tokens
```css
--bg: #FDFBF7, --text: #2D2D2D, --accent-red: #FF4D4D, --accent-blue: #2D5DA1, --postit: #FFF9C4, --border-width: 3px, --shadow-offset: 4px 4px, --font-heading: Kalam Bold, --font-body: Patrick Hand, --rotation-card: -1deg to 1deg
```

## Checklist
Warm paper background texture applied, 
- Kalam Bold headings, 
- Wobbly corner radii on all cards, 
- Hard offset shadow View (not blur), 
- Cards slightly rotated, 
- Button press shifts to cover shadow, 
- SVG tape/tack decorations, 
- PatrickHand for inputs, 
- Jiggle error animation, 
- Minimum 48x48 touch targets

## Prompt de referência
Design a Sketch Hand-Drawn (Mobile) mobile interface using sketch, hand-drawn, handwriting, wobbly, imperfect, paper, kalam, organic. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.

