# Regras de UX e acessibilidade

Fonte: raw/ux-guidelines.csv.

## AI Interaction

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Disclaimer | High | Clearly label AI generated content | Present AI as human |
| Streaming | Medium | Stream text response token by token | Show loading spinner for 10s+ |
| Feedback Loop | Low | Thumps up/down or 'Regenerate' | Static output only |

## Accessibility

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Color Contrast | High | Minimum 4.5:1 ratio for normal text | Low contrast text |
| Color Only | High | Use icons/text in addition to color | Red/green only for error/success |
| Alt Text | High | Descriptive alt text for meaningful images | Empty or missing alt attributes |
| Heading Hierarchy | Medium | Use sequential heading levels h1-h6 | Skip heading levels or misuse for styling |
| ARIA Labels | High | Add aria-label for icon-only buttons | Icon buttons without labels |
| Keyboard Navigation | High | Keep tab order aligned with visual order and test every action without a pointer | Keyboard traps or illogical tab order |
| Screen Reader | Medium | Use semantic HTML and ARIA properly | Div soup with no semantics |
| Form Labels | High | Use label with for attribute or wrap input | Placeholder-only inputs |
| Error Messages | High | Use aria-live or role=alert for errors | Visual-only error indication |
| Skip Links | Medium | Provide skip to main content link | No skip link on nav-heavy pages |
| Motion Sensitivity | High | Honor prefers-reduced-motion and present the final readable state without parallax or scroll-jacking | Force scroll effects |
| Focus Not Obscured (Minimum) | High | Offset sticky UI with scroll-padding and dismiss or move persistent overlays | Let headers footers banners or chat widgets fully cover focus |
| Focus Not Obscured (Enhanced) | Medium | Keep the entire focused component unobscured by author-created content | Present this enhanced AAA criterion as an AA requirement or allow persistent UI to hide any part of focus |
| Focus Appearance | Medium | Use an indicator at least as large as a 2 CSS px perimeter with 3:1 state contrast | Present this enhanced AAA criterion as an AA requirement or use a thin low-contrast outline |
| Dragging Movements | High | Add buttons menus or tap-to-move controls and retain keyboard operation | Make dragging the only way to reorder resize or select |
| Target Size (Minimum) | High | Use at least 24 by 24 CSS px or verify spacing equivalent inline user-agent or essential exceptions | Assume native 44pt or 48dp guidance defines web conformance |
| Consistent Help | Medium | Keep contact self-help and automated help in consistent locations | Move help controls to different locations on each page |
| Text Reflow and Spacing | Critical | Use fluid sizes content-driven height and unitless line height | Clip text in fixed-width or fixed-height boxes |
| Compact Control Semantics | Critical | Prefer a button and expose pressed or selected state that matches the visible label | Use a clickable div or reveal the only action on hover |
| Contextual Live Badge Updates | High | Use one appropriate atomic status message such as 3 items in cart | Announce a bare number or make every badge a competing live region |

## Animation

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Excessive Motion | High | Animate 1-2 key elements per view maximum | Animate everything that moves |
| Duration Timing | Medium | Use shared motion tokens and test that feedback stays responsive | Present 150-300ms or any cutoff as a universal requirement |
| Reduced Motion | High | Check prefers-reduced-motion media query | Ignore accessibility motion settings |
| Loading States | High | Use skeleton screens or spinners | Leave UI frozen with no feedback |
| Hover vs Tap | High | Use click/tap for primary interactions | Rely only on hover for important actions |
| Continuous Animation | Medium | Use for loading indicators only | Use for decorative elements |
| Transform Performance | Medium | Use transform and opacity for animations | Animate width/height/top/left properties |
| Easing Functions | Low | Use deceleration when arriving acceleration when leaving and linear for constant-rate progress | Reject linear easing even for steady rotation or progress |
| Auto-Rotating Content Controls | High | Provide previous next and play/pause; stop on focus or hover and when reduced motion is requested | Auto-advance slides without a stop control |
| Cancellable State Transitions | High | Cancel or replace prior motion; set the final semantic state directly and handle cancellation cleanup | Depend on animationend or transitionend for required state correctness |

## Content

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Truncation | Medium | Truncate with ellipsis and expand option | Overflow or broken layout |
| Date Formatting | Low | Use relative or locale-aware dates | Ambiguous date formats |
| Number Formatting | Low | Use thousand separators or abbreviations | Long unformatted numbers |
| Placeholder Content | Low | Use realistic sample data | Lorem ipsum everywhere |
| Essential Text Truncation | Critical | Wrap stack resize or provide a visible full-detail path | Clamp essential meaning only to make cards uniform |
| Compact Label Semantics | High | Choose static or interactive markup from the label's meaning and ownership | Make every pill clickable or encode status with color alone |
| Compact Label Overflow | High | Bound only unpredictable values; use nowrap with a shrinkable label; expose full text to keyboard pointe… | Let one compact label wrap to a second line or use a hover-only tooltip |

## Data Entry

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Bulk Actions | Low | Allow multi-select and bulk edit | Single row actions only |

## Feedback

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Loading Indicators | High | Follow platform and component guidance; preserve layout focus and accessible busy status | Apply one timing threshold to every operation or leave long waits unexplained |
| Empty States | Medium | Show helpful message and action | Blank empty screens |
| Error Recovery | Medium | Provide clear next steps | Error without recovery path |
| Progress Indicators | Medium | Step indicators or progress bar | No indication of progress |
| Toast Notifications | Medium | Auto-dismiss after 3-5 seconds | Toasts that never disappear |
| Confirmation Messages | Medium | Brief success message | Silent success |

## Forms

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Input Labels | High | Always show label above or beside input | Placeholder as only label |
| Error Placement | High | Show a specific error below the input and reference it with aria-describedby | Show only a top-level error without identifying each invalid field |
| Inline Validation | Medium | Validate on blur for most fields | Validate only on submit |
| Input Types | Medium | Use email tel number url etc | Text input for everything |
| Autofill Support | Medium | Use autocomplete attribute properly | Block or ignore autofill |
| Required Indicators | Medium | Use asterisk or (required) text | No indication of required fields |
| Password Visibility | Medium | Toggle to show/hide password | No visibility toggle |
| Submit Feedback | High | Show loading then success/error state | No feedback after submit |
| Input Affordance | Medium | Use distinct input styling | Inputs that look like plain text |
| Mobile Keyboards | Medium | Use inputmode attribute | Default keyboard for all inputs |
| Redundant Entry | Medium | Auto-populate prior values or let users select previously entered information | Ask users to retype the same address or account data without necessity |
| IME Composition Enter | High | Cancel the default action of handled Enter before guarding isComposing or legacy keyCode 229; preserve S… | Send or clear text on every Enter keydown or submit from compositionend |

## Forms / Accessibility

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Focusable Error Summary | High | Place it at the top of the form; move focus to its heading or container after failed submit; link each i… | Replace inline errors with a visual-only summary or move focus on every blur |

## Interaction

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Focus States | High | Use a visible focus ring on every interactive control, including modal controls | Remove focus outline without replacement |
| Hover States | Medium | Change cursor and add subtle visual change | No hover feedback on clickable elements |
| Active States | Medium | Add pressed/active state visual change | No feedback during interaction |
| Disabled States | Medium | Reduce opacity and change cursor | Confuse disabled with normal state |
| Loading Buttons | High | Disable button and show loading state | Allow multiple clicks during processing |
| Error Feedback | High | Show clear error messages near problem | Silent failures with no feedback |
| Success Feedback | Medium | Show success message or visual change | No confirmation of completed action |
| Confirmation Dialogs | High | Confirm before delete/irreversible actions | Delete without confirmation |

## Layout

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Z-Index Management | High | Define z-index scale system (10 20 30 50) | Use arbitrary large z-index values |
| Overflow Hidden | Medium | Test all content fits within containers | Blindly apply overflow-hidden |
| Fixed Positioning | Medium | Account for safe areas and other fixed elements | Stack multiple fixed elements carelessly |
| Stacking Context | Medium | Understand what creates new stacking context | Expect z-index to work across contexts |
| Content Jumping | High | Reserve appropriate space or keep async states in a stable content-driven container | Insert compact text or media without a layout strategy |
| Viewport Units | Medium | Use dvh or account for mobile browser chrome | Use 100vh for full-screen mobile layouts |
| Container Width | Medium | Limit max-width for text content (65-75ch) | Let text span full viewport width |
| Long Token Wrapping | High | Use overflow-wrap anywhere and let flex or grid text children shrink | Apply word-break break-all to all prose |
| Chip Collection Reflow | High | Wrap the collection or use an operable +n disclosure for hidden overflow values | Force all chips into one clipped row or hide overflow values |

## Maps

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Map Attribution Visible | Critical | Keep the map library attribution control visible on load; it may collapse after interaction to an (i) bu… | Disable the attribution control, hide it behind a click on load, or hide the logo or credits with CSS |
| Map Text Alternative | Critical | Label the map container as a region, add a short text summary of the map's key insight, and offer a feat… | Leave the map as an unlabeled canvas or a div with no text equivalent |
| Map Keyboard and Non-Drag Navigation | High | Keep the map keyboard handler on (arrow keys pan, +/- zoom), make markers focusable with Enter opening d… | Disable map keyboard handling or make dragging the only way to pan, swipe a compare view or scrub a map… |
| Map Symbology Not Color Alone | High | Pair color with an icon, shape, pattern or label per category; use colorblind-safe map schemes such as C… | Encode alert versus normal or map categories only with red and green fills or circle colors |
| Normalized Choropleth Map | High | Fill regions by rates, densities or percentages (per capita, per km2, share of total); show raw totals a… | Fill choropleth regions by raw totals such as case counts or population |
| Perceptual Map Color Ramps | High | Use single-hue sequential or perceptually uniform ramps (Viridis, ColorBrewer sequential) and diverging… | Use rainbow or jet ramps, which add false boundaries and uneven lightness, or saturated data colors on a… |
| Safe Map Popup Content | High | Render feature attribute values as text through DOM text nodes with setDOMContent or setText; use setHTM… | Interpolate feature properties into strings passed to setHTML, Leaflet bindPopup or innerHTML |
| Cluster Dense Map Points | Medium | Cluster points at low zoom with a count label, set clusterMaxZoom, and zoom into a cluster on click or E… | Draw tens of thousands of individual or DOM markers at every zoom level |
| Large Geodata as Vector Tiles | Medium | Serve large map datasets as vector tiles (MVT or PMTiles) and keep GeoJSON slim: drop unused properties,… | Load a multi-megabyte GeoJSON file with every attribute into the browser |
| Map Camera Reduced Motion | Medium | Keep MapLibre and Mapbox camera moves non-essential so the library skips them under prefers-reduced-moti… | Mark decorative flights essential: true or start a requestAnimationFrame camera loop regardless of the m… |

## Navigation

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Smooth Scroll | High | Use scroll-behavior: smooth on html element | Jump directly without transition |
| Sticky Navigation | Medium | Add padding-top to body equal to nav height | Let nav overlap first section content |
| Active State | Medium | Highlight active nav item with color/underline | No visual feedback on current location |
| Back Button | High | Preserve navigation history properly | Break browser/app back button behavior |
| Deep Linking | Medium | Update URL on state/view changes | Static URLs for dynamic content |
| Breadcrumbs | Low | Use for sites with 3+ levels of depth | Use for flat single-level sites |

## Onboarding

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| User Freedom | Medium | Provide Skip and Back buttons | Force linear unskippable tour |

## Performance

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Image Optimization | High | Use appropriate size and format (WebP) | Unoptimized full-size images |
| Lazy Loading | Medium | Lazy load below-fold images and content | Load everything upfront |
| Code Splitting | Medium | Split code by route/feature | Single large bundle |
| Caching | Medium | Set appropriate cache headers | No caching strategy |
| Font Loading | Medium | Use font-display swap or optional | Invisible text during font load |
| Third Party Scripts | Medium | Load non-critical scripts async/defer | Synchronous third-party scripts |
| Bundle Size | Medium | Monitor and minimize bundle size | Ignore bundle size growth |
| Render Blocking | Medium | Inline critical CSS defer non-critical | Large blocking CSS files |

## Responsive

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Mobile First | Medium | Start with mobile styles then add breakpoints | Desktop-first causing mobile issues |
| Breakpoint Testing | Medium | Test at 320 375 414 768 1024 1440 | Only test on your device |
| Touch Friendly | High | Increase touch targets on mobile | Same tiny buttons on mobile |
| Readable Font Size | High | Minimum 16px body text on mobile | Tiny text on mobile |
| Viewport Meta | High | Use width=device-width initial-scale=1 | Missing or incorrect viewport |
| Horizontal Scroll | High | Ensure content fits viewport width | Content wider than viewport |
| Image Scaling | Medium | Use max-width: 100% on images | Fixed width images overflow |
| Table Handling | Medium | Use horizontal scroll or card layout | Wide tables breaking layout |

## Search

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Autocomplete | Medium | Show predictions as user types | Require full type and enter |
| No Results | Medium | Show 'No results' with suggestions | Blank screen or '0 results' |

## Security / Accessibility

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Accessible Authentication (Minimum) | Critical | Allow password managers and paste; offer passkeys OAuth or another non-cognitive method | Block paste or require manual OTP transcription with no alternative |

## Spatial UI

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Gaze Hover | High | Scale/highlight element on look | Static element until pinch |
| Depth Layering | Medium | Use glass material and z-offset | Flat opaque panels blocking view |

## Sustainability

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Auto-Play Video | Medium | Prefer click-to-play; provide pause and captions; stop off-screen and honor reduced motion | Auto-play high-resolution loops without pause or captions |
| Asset Weight | Medium | Compress and lazy load 3D models | Load 50MB textures |

## Touch

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Touch Target Size | High | Use 44pt on iOS and 48dp on Android; for web use the separate WCAG Target Size rule | Treat one unit or minimum as universal across platforms |
| Touch Spacing | Medium | Minimum 8px gap between touch targets | Tightly packed clickable elements |
| Gesture Conflicts | Medium | Avoid horizontal swipe on main content | Override system gestures |
| Tap Delay | Medium | Use touch-action CSS or fastclick | Default mobile tap handling |
| Pull to Refresh | Low | Disable where not needed | Enable by default everywhere |
| Haptic Feedback | Low | Use for confirmations and important actions | Overuse vibration feedback |

## Typography

| issue | severidade | fazer | não fazer |
|---|---|---|---|
| Line Height | Medium | Use 1.5-1.75 for body text | Cramped or excessive line height |
| Line Length | Medium | Limit to 65-75 characters per line | Full-width text on large screens |
| Font Size Scale | Medium | Use consistent modular scale | Random font sizes |
| Font Loading | Medium | Reserve space with fallback font | Layout shift when fonts load |
| Contrast Readability | High | Use darker text on light backgrounds | Gray text on gray background |
| Heading Clarity | Medium | Clear size/weight difference | Headings similar to body text |
| Heading Line Balance | Medium | Bound the measure and test natural-wrap fallback across widths fonts and locales | Promise an exact final line or insert blanket nonbreaking spaces or hardcoded br tags |

