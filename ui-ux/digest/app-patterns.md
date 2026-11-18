# Padrões de interface mobile

Fonte: raw/app-interface.csv.

## Accessibility

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Icon Button Labels | Critical | Set accessibilityLabel or label prop on icon buttons | Icon buttons without accessible names |
| Form Control Labels | Critical | Pair Text label with input and set accessibilityLabel | Inputs with placeholder only |
| Role & Traits | High | Use accessibilityRole/button/link/checkbox etc. | Rely on generic views with no roles |
| Dynamic Updates | Medium | Use accessibilityLiveRegion or announceForAccessibility | Update text silently with no announcement |
| Decorative Icons | Medium | Mark decorative icons as not accessible | Have screen reader read every icon |
| Dragging Alternatives | High | Provide named Move up/down buttons or a position menu beside drag handles; route iOS and Android behavio… | Make drag, swipe, or a web-only pointer handler the only way to reorder native content |

## Animation

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Duration & Easing | Medium | Use ease-out for enter/ease-in for exit | Use long or linear animations for core UI |
| Respect Reduced Motion | Critical | Check reduceMotionEnabled and simplify animations | Ignore user motion preferences |
| Limited Continuous Motion | Medium | Use looping only where necessary | Keep decorative elements looping forever |

## Anti-Pattern

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| No Gesture-Only Actions | Critical | Provide visible buttons in addition to gestures | Rely on swipe/shake only with no UI affordance |

## Feedback

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Loading Indicators | High | Use ActivityIndicator or skeleton for >300ms operations | Leave button and screen frozen |
| Success Feedback | Medium | Show toast/checkmark or banner | Complete actions silently with no confirmation |
| Error Feedback | High | input-level error + summary banner | Only change border color with no explanation |

## Forms

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Inline Validation | Medium | Validate onBlur and onSubmit | Validate on every keystroke causing jank |
| Keyboard Type | Medium | Match email/tel/number/search types | Use default keyboard for all inputs |
| Auto Focus & Next | Low | Use onSubmitEditing to focus next input | Force users to tap each field manually |
| Password Visibility | Medium | Provide Show/Hide icon toggling secureTextEntry | Force users to type blind with no option |
| Authentication Reuse | Critical | Support password managers passkeys paste and prefilled confirmed values | Force users to retype credentials or the same data in one flow |

## Navigation

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Back Behavior | Critical | Use navigation.goBack and keep screen state | Reset stack or exit app unexpectedly |
| Bottom Tabs | Medium | Use 3–5 tabs and move extras to More/Settings | Overloaded tab bar with many icons |
| Modal Escape | High | Provide close button and swipe-down where platform expects | Trapping users in modal with no obvious exit |

## Performance

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Virtualize Long Lists | High | Use keyExtractor and initialNumToRender appropriately | Render hundreds of items with ScrollView |
| Image Size & Cache | Medium | Use Image component with proper resizeMode and caching | Load full-resolution images everywhere |
| Debounce High-Freq Events | Medium | Wrap handlers with debounce/throttle | Run heavy logic on every event |

## Safe Areas

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Safe Area Insets | High | Wrap screens in SafeAreaView or apply insets | Place tappable content under system bars |

## State

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Preserve Screen State | Medium | Keep components mounted or persist state | Reset list scroll and form inputs on every visit |

## Theming

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Light/Dark Contrast | High | Use semantic tokens and test both themes | Reuse light-theme grays directly in dark mode |

## Touch

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Touch Target Size | Critical | Select 44pt for iOS and 48dp for Android at runtime; evaluate web targets separately against WCAG 2.5.8… | Collapse iOS 44pt, Android 48dp, and web 24 CSS px into one cross-platform number |
| Touch Spacing | Medium | Keep at least 8dp spacing between touchables | Cluster many buttons with no gap |
| Gesture Conflicts | High | Reserve horizontal swipes for carousels | Full-screen custom swipe conflicting with back |

## Typography

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Base Font Size | High | Use platform fontScale and at least 14–16pt base | Render critical text below 12pt |
| Dynamic Type Support | High | Set allowFontScaling and test large text | Disable scaling on all text globally |

