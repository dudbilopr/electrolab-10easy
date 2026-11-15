# Changelog & Release Roadmap

All notable releases of **ElectroLab10.easy** are documented here and archived chronologically on Zenodo under a single persistent **Concept DOI** so classroom links and citations stay stable while updates accumulate.

## [1.0.0] - 2026-11-15 — Precedent Baseline Release (L1 Verified)
### Added
- Archived **62 standalone HTML5 Electromagnetism virtual laboratories**: 31 Spanish (`simulators/es/`) and 31 paired English (`simulators/en/`) modules covering `M1` through `M12`.
- Built unified bilingual portal [`index.html`](index.html) using the `10.Easy` Plasma design language (`#b3246b` / `#0b8ca8`), with module filters (`M1`–`M12`), live search, ES/EN switcher, and transparent validation-status panel.
- Added automated structural & link-integrity verification suite ([`tests/test_simulators.py`](tests/test_simulators.py)) and GitHub Actions CI + GitHub Pages workflows.
- Established `VALIDATION_MATRIX.md` defining physical invariants (`L1`–`L4`), dual-license governance (`CC BY-NC-SA 4.0` for simulators/UI, `Apache-2.0` for test tooling), `CITATION.cff`, and `.zenodo.json`.

---

## Planned Roadmap (Subsequent Zenodo Version DOIs)

### [1.1.0] — Bilingual i18n Audit & Plasma UI Harmonization (`L2`)
- Fix residual escaped apostrophes (`\'`) and mixed Spanish/English labels inside legacy `simulators/en/` titles and tooltips.
- Standardize inline Plasma SVG favicons, responsive canvas scaling, and `#credits` attribution footers across all 62 HTML files.
- Verify zero browser console warnings across desktop and mobile viewports.

### [1.2.0] — Analytical & Numerical Physics Verification Suite (`L3`)
- Implement headless solver cross-checks in `tests/` validating `M1`–`M12` equations (Gauss flux invariance, Biot-Savart asymptotic limits, cyclotron energy conservation, Poynting vector ratio $E/B = c$, RLC resonance $Q$ factor).
- Publish automated per-module pass/tolerance reports linked from the portal badge.

### [2.0.0] — Interactive Self-Verification HUD & Lab Benchmarks (`L4`)
- Embed live in-canvas `Física verificada` self-check pills inside priority `M1`–`M12` simulators alongside reproducible classroom/laboratory benchmark datasets.
- Incorporate verified contributor credits (`CITATION.cff` / `.zenodo.json`) for completed co-authored modules.
