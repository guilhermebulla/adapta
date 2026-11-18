# Claymorphism (Mobile)

- id: `claymorphism-mobile`  ·  tipo: Mobile  ·  status: supplemental
- pai: `claymorphism`  ·  complexidade: High
- era: Consumer/Education  ·  frameworks: react-native/react-native-reanimated/expo
- light/dark: supported / supported  ·  perf: cost:high/drivers:animation,large-images  ·  a11y: risk:conditional/requires:contrast-text-4.5,keyboard,visible-focus,reduced-moti…

## Best for
Children education apps, teen social products, crypto gamification, creative tools, brand mascot-led apps

## Não usar para
Serious enterprise, high-density data, editorial reading apps, fintech trust signals

## Cores primárias
Vivid Violet #7C3AED, Hot Pink #DB2777

## Cores secundárias
Canvas #F4F1FA, Soft Charcoal #332F3A, Emerald #10B981, Amber #F59E0B, Lavender-Gray #635F69

## Efeitos & animação
Multi-layer shadow stacks (nested View) to simulate clay depth, LinearGradient #A78BFA→#7C3AED buttons, borderRadius 40–50 outer / 32 cards / 20 buttons, Reanimated spring squish (scale 0.92 on press), BlurView glass-clay hybrid cards, floating blobs with slow ±20px drift, Haptics Light on every press

## Tokens
```css
--bg: #F4F1FA, --card-bg: rgba(255,255,255,0.7), --text: #332F3A, --muted: #635F69, --accent: #7C3AED, --accent2: #DB2777, --success: #10B981, --warning: #F59E0B, --radius-outer: 50px, --radius-card: 32px, --radius-button: 20px, --font-heading: Nunito Black, --font-body: DM Sans
```

## Checklist
Background uses #F4F1FA (no pure white), 
- Multi-layer clay shadow stack applied, 
- Cards use blurred glass-clay hybrid, 
- Buttons squish to scale 0.92 on press, 
- Spring physics on all interactions, 
- Nunito Black for headings, 
- Background blobs drifting, 
- Haptics on every press, 
- Nested border radius (card 32, inner 24), 
- Bento layout with hero span

## Prompt de referência
Design a Claymorphism (Mobile) mobile interface using claymorphism, clay, 3d, soft, bubbly, candy, playful, rounded. Prioritize clear hierarchy, safe areas, touch targets, visible focus, and reduced-motion alternatives.

