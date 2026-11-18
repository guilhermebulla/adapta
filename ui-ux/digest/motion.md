# Movimento e transição

Fonte: raw/motion.csv.

| categoria | tier | gatilho | duração | easing |
|---|---|---|---|---|
| Hover Micro-interaction | Subtle | hover | 150-200ms | power1.out |
| Hover Micro-interaction | Standard | hover | 200-300ms | power2.out |
| Hover Micro-interaction | Complex | hover + mousemove | 300-500ms | elastic.out(1,0.4) |
| Scroll Reveal | Subtle | scroll (viewport enter) | 300-400ms | power1.out |
| Scroll Reveal | Standard | scroll (viewport enter) | 400-600ms | power2.out |
| Scroll Reveal | Complex | scroll (continuous scrub) | tied to scroll position | none (scrub-driven) |
| Stagger List | Subtle | load or scroll | 250-350ms | power1.out |
| Stagger List | Standard | load or scroll | 300-450ms | back.out(1.4) |
| Stagger List | Complex | load or scroll | 400-700ms | expo.out |
| Page Transition | Subtle | route change | 200-300ms | power1.inOut |
| Page Transition | Standard | route change | 400-600ms | power2.inOut |
| Page Transition | Complex | route change | 500-800ms | expo.inOut |
| Parallax Scroll | Subtle | scroll (continuous) | tied to scroll position | linear (scrub) |
| Parallax Scroll | Standard | scroll (continuous) | tied to scroll position | linear (scrub) |
| Loading / Skeleton | Subtle | on mount / async wait | 1200-1600ms loop | sine.inOut |
| Loading / Skeleton | Standard | on mount / async wait | 800-1200ms loop | power1.inOut |
| Carousel / Auto-Rotation | Standard | timer / focus / hover / visibility | user-controlled or stopp… | none |
