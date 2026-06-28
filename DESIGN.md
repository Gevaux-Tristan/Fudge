# Design

Single-file webapp (`index.html`). Dark, photographic, monochrome (black / white / grey). Geist (Google Fonts).

## Theme
Monochrome, restrained. The photo previews carry all the colour; the chrome is black/white/grey. The "accent" is white (the brightest neutral), used for active/primary states only.

## Color (tokens in `:root`)
- Surfaces: `--bg #000` · `--bg2 #0c0c0c` · `--panel #151515` · `--panel2 #1e1e1e`
- Lines: `--line #2a2a2a` · `--line2 #3a3a3a`
- Text: `--txt #f4f4f4` · `--txt2 #a6a6a6` · `--txt3 #6c6c6c`
- Accent (white): `--accent #ffffff` · `--accent2 #e6e6e6` — the brightest neutral, used for active / primary only.
- Ink on accent (black on white): `--ink #0a0a0a`
- Slider polarity: `--pos #f0f0f0` (positive) · `--neg #8a8a8a` (negative)

Rules: accent (white) = actions, current selection, state only (never decoration). Text on accent = `--ink`. No grey text on coloured backgrounds.

## Typography
Geist (fallback Helvetica Neue, Arial). Fixed px scale (product register): 17 (h1) · 16 (h2) · 15 (body/input) · 14 (slider value, foot buttons) · 13 (labels, chips, controls) · 12 (compact controls, raw) · 11 (sub, eyebrow, count) · 10 (badges). Numbers use `font-variant-numeric: tabular-nums`.

## Radius scale
- `--r-lg 16px` cards / sheets
- `--r-md 11px` inputs, buttons, panels, controls
- `--r-sm 7px` badges, inner segments, logo
- pill `999px` (filter chips), circles `50%` (fav, fab)

## Components
Preset card · filter chip · base-pick button · custom slider (track + polarity fill + thumb) · segmented control · FAB · bottom-sheet/side-drawer editor · toast. Every interactive element has default / hover / focus-visible / active; `--accent` focus ring (`:focus-visible`).

## Motion
150–340ms, ease-out curves. Editor slides in (sheet on mobile, drawer ≥880px). Preview re-renders on `requestAnimationFrame`. Full `prefers-reduced-motion: reduce` fallback (transitions/animations collapsed).

## Layout
Mobile-first. Gallery: `repeat(auto-fill, minmax(158/190px, 1fr))`. Editor: full-screen sheet on mobile, 520px right drawer ≥880px. Safe-area insets respected.
