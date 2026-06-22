---
name: Luminous Ether
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf2'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fb'
  on-surface: '#111c2d'
  on-surface-variant: '#494454'
  inverse-surface: '#263143'
  inverse-on-surface: '#ecf1ff'
  outline: '#7b7486'
  outline-variant: '#cbc3d7'
  surface-tint: '#6d3bd7'
  primary: '#6b38d4'
  on-primary: '#ffffff'
  primary-container: '#8455ef'
  on-primary-container: '#fffbff'
  inverse-primary: '#d0bcff'
  secondary: '#006591'
  on-secondary: '#ffffff'
  secondary-container: '#39b8fd'
  on-secondary-container: '#004666'
  tertiary: '#a63047'
  on-tertiary: '#ffffff'
  tertiary-container: '#c6495e'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e9ddff'
  primary-fixed-dim: '#d0bcff'
  on-primary-fixed: '#23005c'
  on-primary-fixed-variant: '#5516be'
  secondary-fixed: '#c9e6ff'
  secondary-fixed-dim: '#89ceff'
  on-secondary-fixed: '#001e2f'
  on-secondary-fixed-variant: '#004c6e'
  tertiary-fixed: '#ffdadc'
  tertiary-fixed-dim: '#ffb2b9'
  on-tertiary-fixed: '#400010'
  on-tertiary-fixed-variant: '#891933'
  background: '#f9f9ff'
  on-background: '#111c2d'
  surface-variant: '#d8e3fb'
typography:
  display:
    fontFamily: Sora
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Sora
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Sora
    fontSize: 28px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Sora
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
---

## Brand & Style

The design system shifts from heavy, metallic tones to a weightless, atmospheric experience. It targets high-end productivity, wellness, or creative platforms that prioritize mental clarity and focus. The aesthetic is defined by "Luminous Glassmorphism"—a blend of high-end minimalism and ethereal translucency.

By leveraging light-refracting surfaces and soft gradients, the UI should evoke a sense of openness and calm. The emotional response is one of breezy sophistication, removing visual friction through high white-space ratios and delicate depth cues.

## Colors

The palette is anchored in a "Soft Lavender to Sky Blue" spectrum, primarily used for interactive elements and brand accents. 

- **Primary Gradient:** A linear blend from Soft Lavender (#8B5CF6) to Sky Blue (#0EA5E9) at a 135-degree angle.
- **Surface:** The foundation is crisp White (#FFFFFF) and Slate-50 (#F8FAFC). Dark surfaces are strictly prohibited.
- **Accents:** Pastel Coral (#FB7185) and Mint (#34D399) are used sparingly for status indicators and subtle highlights to maintain the airy feel.
- **Typography:** Dark Grey (#1E293B) provides a high-contrast anchor, ensuring AAA accessibility against light backgrounds.

## Typography

This design system utilizes **Sora** for headlines to provide a geometric, modern character, while **Inter** is used for body copy to ensure maximum legibility and a systematic feel.

To maintain the "airy" aesthetic, headline weights are kept lighter (300-500) than traditional systems. Increase tracking slightly on display text to allow the characters to breathe. All body text should utilize a generous line height (1.5x+) to prevent visual density.

## Layout & Spacing

The layout philosophy centers on a **Fluid Grid** with exaggerated margins. Content should never feel cramped; if in doubt, increase the white space.

- **Desktop:** 12-column grid, 64px outer margins, 24px gutters.
- **Tablet:** 8-column grid, 32px outer margins, 20px gutters.
- **Mobile:** 4-column grid, 16px outer margins, 16px gutters.

Spacing follows a linear 8px scale. Vertical rhythm should prioritize large "XL" gaps between major sections to emphasize the airy design narrative.

## Elevation & Depth

Depth is achieved through **Glassmorphism** rather than traditional heavy shadows. Surfaces use high-transparency fills and background blurs.

- **Surface Treatment:** White backgrounds at 70-80% opacity with a `backdrop-filter: blur(20px)`.
- **Borders:** "Hairline" borders are required on all glass elements. Use a 1px solid border at 40% opacity of the primary color or a light grey.
- **Shadows:** Use only "Ambient Shadows"—extremely diffused, low-opacity (5-10%) shadows with a large spread and a slight blue tint (#0EA5E9) to mimic light passing through glass.

## Shapes

The shape language is "Rounded" to complement the soft gradient aesthetic. 

- Standard elements (buttons, inputs) use a **0.5rem (8px)** radius.
- Large containers and cards use **1rem (16px)** to **1.5rem (24px)** for a friendly, approachable structure. 
- Interactive feedback states should utilize rounded shapes to avoid any "sharp" or aggressive visual metaphors.

## Components

- **Buttons:** Primary buttons use the Lavender-to-Sky gradient with white text. Secondary buttons are "Ghost" style with the hairline border and a subtle 5% primary color fill on hover.
- **Cards:** Use the Glassmorphism specification (blur + hairline border). Avoid internal dividers; use white space to separate content chunks within the card.
- **Inputs:** Fields should be #F8FAFC with a 1px border that glows into a Sky Blue gradient on focus. Label text should be small, uppercase, and slightly tracked out.
- **Chips:** Highly rounded (pill-shaped), using light pastel fills (Mint/Coral) with 10% opacity and matching colored text.
- **Lists:** Use generous padding (16px vertical) between list items. Use subtle 1px lines at 5% opacity for separation, or purely rely on spacing.
- **Progress Indicators:** Use the primary gradient for active states, with a soft grey #F1F5F9 for the track.