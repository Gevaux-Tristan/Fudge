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
Preset card · filter chip · **editor preset strip** (VSCO-style row of 56px thumbnails, each previewing the look on the user's own photo; active = `--accent` border) · custom slider (track + polarity fill + thumb; bipolar sliders show a signed value, magnitude sliders like Intensité/Grain/Vignettage/Estompé show none) · segmented control · FAB (fav / import / camera) · bottom-sheet/side-drawer editor · toast. Every interactive element has default / hover / focus-visible / active; `--accent` focus ring (`:focus-visible`).

## Capture
No custom viewfinder — the camera FAB opens the **native OS camera** via `<input type="file" accept="image/*" capture="environment">` (best quality, native aspect, correct orientation). Import uses the same pattern without `capture`. The captured/imported photo opens straight into the editor.

## Crop
"Recadrer" overlays the preview with a draggable/resizable box (corner handles + move), a rule-of-thirds grid, an outside dim, and a ratio chip row (Libre · Original · 1:1 · 4:5 · 5:4 · 3:2 · 2:3 · 16:9 · 9:16) with apply/cancel. The crop is stored normalized to the image and applied in `renderRecipe` (`opts.crop` source-rect) so preview + export match. White stroke/handles on the photo; selected ratio = white-filled chip.

## Motion
150–340ms, ease-out curves. Editor slides in (sheet on mobile, drawer ≥880px). Preview re-renders on `requestAnimationFrame`. Full `prefers-reduced-motion: reduce` fallback (transitions/animations collapsed).

## Layout
Mobile-first. Gallery: `repeat(auto-fill, minmax(158/190px, 1fr))`. Editor: full-screen sheet on mobile, 520px right drawer ≥880px. Safe-area insets respected.
