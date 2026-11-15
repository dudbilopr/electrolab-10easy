# ElectroLab10.easy — Bilingual Electromagnetism Virtual Laboratory Suite (`M1`–`M12`)

<!-- ZENODO_BADGE_PLACEHOLDER -->
[![CI](https://github.com/dudbilopr/electrolab-10easy/actions/workflows/ci.yml/badge.svg)](https://github.com/dudbilopr/electrolab-10easy/actions/workflows/ci.yml)
[![Live Portal](https://img.shields.io/badge/GitHub%20Pages-Live%20Portal-0b8ca8?logo=github)](https://dudbilopr.github.io/electrolab-10easy/)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/Simulators-CC%20BY--NC--SA%204.0-b3246b.svg)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0001--7239--3497-a6ce39?logo=orcid)](https://orcid.org/0000-0001-7239-3497)

**ElectroLab10.easy** is the unified, versioned, and citable Zenodo archive of **62 interactive HTML5 Electromagnetism simulators** (**31 in Spanish** + **31 in English**) spanning university Modules **M1 through M12** — authored by **Dudbil Olvasada Pabón Riaño** (`10.Easy` / `physics.10easy`).

- **Live Bilingual Portal:** <https://dudbilopr.github.io/electrolab-10easy/>
- **Physical Validation Matrix (`L1`–`L4`):** [`VALIDATION_MATRIX.md`](VALIDATION_MATRIX.md)
- **Versioned Roadmap:** [`CHANGELOG.md`](CHANGELOG.md)

---

## Why Archive This Precedent on Zenodo?

1. **Timestamped Intellectual Precedent:** Establishes a permanent open DOI (`v1.0.0`) for all 62 HTML5 virtual laboratories created for bilingual (`ES` / `EN`) university Electromagnetism instruction.
2. **Continuous Versioning Under One Concept DOI:** Future refinements (`v1.1.0` English i18n polish, `v1.2.0` numerical physics validation against analytical invariants, `v2.0.0` lab benchmarks & verified co-authors) receive immutable Version DOIs while keeping the **Concept DOI** unchanged.
3. **Clear Authorship & Commercial Governance:** Simulators and portal UI carry `CC BY-NC-SA 4.0` (`10.Easy` non-commercial share-alike protection); verification scripts in `tests/` are licensed under `Apache-2.0`. Collaborators and students can be cleanly credited in `CITATION.cff` and `.zenodo.json` in later tagged releases once their modules pass verification.

---

## Module Coverage (`M1`–`M12` · 31 Paired ES/EN Laboratories)

| Module | Topic | Pairs | Spanish (`simulators/es/`) | English (`simulators/en/`) |
| :--- | :--- | :---: | :--- | :--- |
| **M1** | Coulomb's Law & Point Charges | 3 | `Sim_M1_Cargas`, `Sim_M1_Coulomb_Basico`, `Sim_M1_Coulomb_Pro` | `Sim_M1_Charges`, `Sim_M1_Coulomb_Basic`, `Sim_M1_Coulomb_Pro` |
| **M2** | Continuous Distributions & Field Lines | 9 | `Sim_M2_Anillo`, `Arco`, `Campo_Vectorial`, `Cilindro`, `Disco`, `Semicirculo`, `Tablero_Distribuciones`, `Tablero_Lineas`, `Varilla` | `Sim_M2_Ring`, `Arc`, `Vector_Field`, `Cylinder`, `Disk`, `Semicircle`, `Board_Distributions`, `Board_Lines`, `Rod` |
| **M3** | Electric Flux & Gauss's Law | 2 | `Sim_M3_Flujo`, `Sim_M3_Tabla_Gauss` | `Sim_M3_Flux`, `Sim_M3_Gauss_Table` |
| **M4** | Electric Potential & Equipotentials | 2 | `Sim_M4_Equipotenciales`, `Sim_M4_Potencial_3D` | `Sim_M4_Equipotentials`, `Sim_M4_Potential_3D` |
| **M5** | Capacitance & Dielectrics | 1 | `Sim_M5_Capacitancia` | `Sim_M5_Capacitance` |
| **M6** | DC Circuits & Resistivity | 2 | `Sim_M6_CircuitoDC`, `Sim_M6_Resistividad` | `Sim_M6_DC_Circuit`, `Sim_M6_Resistivity` |
| **M7** | Lorentz Force & Cyclotron | 1 | `Sim_M7_Lorentz` | `Sim_M7_Lorentz` |
| **M8** | Biot–Savart Law | 2 | `Sim_M8_BiotSavart_Anillo`, `Sim_M8_BiotSavart_Hilo` | `Sim_M8_Biot_Savart_Ring`, `Sim_M8_Biot_Savart_Wire` |
| **M9** | Ampère's Law & Solenoid | 2 | `Sim_M9_Solenoide`, `Sim_M9_Tabla_Ampere` | `Sim_M9_Solenoid`, `Sim_M9_Ampere_Table` |
| **M10** | Magnetic Flux & Faraday Induction | 2 | `Sim_M10_FEM_Movimiento`, `Sim_M10_FlujoMagnetico` | `Sim_M10_Motional_EMF`, `Sim_M10_Magnetic_Flux` |
| **M11** | Maxwell's Equations & EM Waves | 2 | `Sim_M11_EcuacionesMaxwell`, `Sim_M11_OndaEM` | `Sim_M11_Maxwell_Equations`, `Sim_M11_EM_Wave` |
| **M12** | LC Oscillations, Phasors & RLC | 3 | `Sim_M12_Fasores`, `Sim_M12_OsciladorLC`, `Sim_M12_RLC` | `Sim_M12_Phasors`, `Sim_M12_LC_Oscillator`, `Sim_M12_RLC` |

---

## Validation & Update Roadmap (`L1`–`L4`)

- **L1 — Structural & Portal CI (`v1.0.0`, Active):** Automated `pytest` verifies exact `31 ES + 31 EN` counts, 1-to-1 module pairing, balanced `<script>` tags, non-empty `<title>`, zero broken local relative paths, and 100% wiring in `index.html` & `VALIDATION_MATRIX.md`.
- **L2 — i18n Audit & Plasma Harmonization (`v1.1.0`):** Polish legacy English labels/titles and unify `brand-10easy` Plasma footers and favicons across all 62 HTML files.
- **L3 — Analytical Physics Invariant Tests (`v1.2.0`):** Headless/numerical verification of conservation laws and asymptotic limits defined in [`VALIDATION_MATRIX.md`](VALIDATION_MATRIX.md).
- **L4 — In-Canvas Self-Verification & Experimental Benchmarks (`v2.0.0`):** Embedded verification HUD badges + classroom lab comparison datasets.

---

## Running Local Verification

```powershell
pytest tests -v
```

---

## Related `10.Easy` Open-Science Ecosystem

| Repository | Focus | License | Zenodo Concept DOI |
| :--- | :--- | :--- | :--- |
| [**`holom-core`**](https://github.com/dudbilopr/holom-core) | Off-axis Digital Holography Core Library (`HoloM` Engine) | `Apache-2.0` | [`10.5281/zenodo.24255654`](https://doi.org/10.5281/zenodo.24255654) |
| [**`hololab-10easy`**](https://github.com/dudbilopr/hololab-10easy) | Interactive Digital Holography & Interferometry Virtual Lab | `CC BY-NC-SA 4.0` | [`10.5281/zenodo.24255658`](https://doi.org/10.5281/zenodo.24255658) |
| [**`muellerlab-10easy`**](https://github.com/dudbilopr/muellerlab-10easy) | Portable ESP32-C6 Dual-Mode Mueller Polarimeter & Twin | `Apache-2.0` / `CC BY-NC-SA 4.0` | [`10.5281/zenodo.24256277`](https://doi.org/10.5281/zenodo.24256277) |

---

## Citation

See [`CITATION.cff`](CITATION.cff). Author: **Dudbil Olvasada Pabón Riaño** ([ORCID 0000-0001-7239-3497](https://orcid.org/0000-0001-7239-3497)), **10.Easy**.
