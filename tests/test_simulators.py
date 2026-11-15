import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SIM_ES = ROOT / "simulators" / "es"
SIM_EN = ROOT / "simulators" / "en"
INDEX_HTML = ROOT / "index.html"
MATRIX_MD = ROOT / "VALIDATION_MATRIX.md"

EXPECTED_MODULE_COUNTS = {
    "M1": 3,
    "M2": 9,
    "M3": 2,
    "M4": 2,
    "M5": 1,
    "M6": 2,
    "M7": 1,
    "M8": 2,
    "M9": 2,
    "M10": 2,
    "M11": 2,
    "M12": 3,
}

TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
ATTR_RE = re.compile(r"""(?:src|href)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
SCRIPT_OPEN_RE = re.compile(r"<script\b[^>]*>", re.IGNORECASE)
SCRIPT_CLOSE_RE = re.compile(r"</script>", re.IGNORECASE)


def _sim_files(folder: Path) -> list[Path]:
    return sorted(folder.glob("Sim_*.html"))


def test_simulator_counts():
    es = _sim_files(SIM_ES)
    en = _sim_files(SIM_EN)
    assert len(es) == 31, f"Expected 31 ES simulators, found {len(es)}"
    assert len(en) == 31, f"Expected 31 EN simulators, found {len(en)}"


def test_module_pairing_counts():
    for lang, folder in (("es", SIM_ES), ("en", SIM_EN)):
        counts = {m: 0 for m in EXPECTED_MODULE_COUNTS}
        for path in _sim_files(folder):
            m = re.match(r"Sim_(M\d+)_", path.name)
            assert m is not None, f"Unexpected filename without module prefix: {lang}/{path.name}"
            mod = m.group(1)
            assert mod in counts, f"Unknown module {mod} in {lang}/{path.name}"
            counts[mod] += 1
        assert counts == EXPECTED_MODULE_COUNTS, f"Module mismatch in {lang}: {counts}"


def test_html_structural_integrity_and_self_containment():
    for lang, folder in (("es", SIM_ES), ("en", SIM_EN)):
        for path in _sim_files(folder):
            text = path.read_text(encoding="utf-8", errors="replace")
            title_match = TITLE_RE.search(text)
            assert title_match and title_match.group(1).strip(), f"Missing <title> in {lang}/{path.name}"

            opens = len(SCRIPT_OPEN_RE.findall(text))
            closes = len(SCRIPT_CLOSE_RE.findall(text))
            assert opens == closes, f"Unbalanced <script> tags ({opens} vs {closes}) in {lang}/{path.name}"

            for ref in ATTR_RE.findall(text):
                low = ref.lower()
                if low.startswith(("http://", "https://", "#", "data:", "mailto:", "javascript:")):
                    continue
                target = (path.parent / ref).resolve()
                assert target.exists(), f"Broken local relative reference {ref!r} in {lang}/{path.name}"


def test_portal_and_validation_matrix_reference_all_simulators():
    portal = INDEX_HTML.read_text(encoding="utf-8")
    matrix = MATRIX_MD.read_text(encoding="utf-8")

    assert 'rel="icon"' in portal, "Portal index.html must include inline favicon"
    assert "CC BY-NC-SA 4.0" in portal, "Portal index.html must display CC BY-NC-SA 4.0 attribution"

    for lang, folder in (("es", SIM_ES), ("en", SIM_EN)):
        for path in _sim_files(folder):
            rel = f"simulators/{lang}/{path.name}"
            assert rel in portal, f"Missing simulator link {rel} in index.html"
            stem = path.stem
            assert stem in matrix, f"Missing simulator stem {stem} in VALIDATION_MATRIX.md"
