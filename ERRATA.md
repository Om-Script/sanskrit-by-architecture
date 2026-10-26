# Errata & Technical Addenda
## Sanskrit by Architecture: Decoding the Rāmāyaṇa
**Author:** Timothy A. George  
**Publication Year:** 2026 | **Trim Size:** Amazon KDP 7" x 10"  
**Repository:** [https://github.com/om-script/sanskrit-by-architecture](https://github.com/om-script/sanskrit-by-architecture)

---

### How to Report Errata
If you discover a typographical error, an incorrect Sandhi split, an unclear grammatical derivation, or an issue running the Scala/Python companion code:
1. **GitHub Issues (Recommended):** [Open an issue on GitHub](https://github.com/om-script/sanskrit-by-architecture/issues) with the tag `errata`.
2. **Pull Requests:** Submit a direct PR to this `ERRATA.md` file.

Please include:
- **Chapter & Page Number** (or section heading)
- **Printed Text** (exact quote)
- **Suggested Correction**
- **Reason / Derivation**

All verified contributions will be listed below with public credit and incorporated into the next printing revision.

---

### Verified Errata Table

| Item # | Chapter | Page | Printed Text | Correction | Type | Status / Notes |
| :---: | :---: | :---: | :--- | :--- | :---: | :--- |
| *001* | Ch 7 | — | *Synonym callout note* | Replaced with architectural Alias System & Bridge Table | Clarification | Updated in v1.1 master |
| *002* | Ch 11 | — | *Continuous 12-verse combat* | Inserted Halftime Combat Checkpoint after v. 144 | Pacing | Updated in v1.1 master |

*(Table will be continuously updated as community reports are verified.)*

---

### Software & Environment Compatibility Updates

#### 1. Scala 3 Compiler Engine (`generative_cpu_engine.scala` / `SanskritEngine.scala`)
- **Verified Environment:** Scala 3.3.0+ LTS via `scala-cli` / Coursier (`cs`).
- **Command:** `scala-cli run SanskritEngine.scala`

#### 2. Python 3 Sanskrit Reader Stack (`static_memory_loader.py`)
- **Verified Environment:** Python 3.9 through Python 3.12.
- **Dependencies (`requirements.txt`):**
  - `indic-transliteration>=2.3.0`
- **Command:** `python static_memory_loader.py`

---

*Last Updated: October 2026*
