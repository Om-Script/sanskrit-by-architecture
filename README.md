# Sanskrit by Architecture: Decoding the Rāmāyaṇa
### *A Generative, Functional Blueprint for the Human Mind*
**By Timothy A. George (2026)**

[![Book Trim](https://img.shields.io/badge/Amazon%20KDP-7x10%20Print%20Ready-orange.svg)](#)
[![Scala 3](https://img.shields.io/badge/Language-Scala%203-red.svg)](https://www.scala-lang.org/)
[![Python 3](https://img.shields.io/badge/Reader-Python%203.9%2B-blue.svg)](https://www.python.org/)
[![Errata Status](https://img.shields.io/badge/Errata-Active%20Tracking-green.svg)](ERRATA.md)

---

## Overview

This repository is the official open-source companion codebase and errata tracker for the book **"Sanskrit by Architecture: Decoding the Rāmāyaṇa"**.

Instead of memorizing 800 pages of 19th-century philological tables, this book approaches Classical Sanskrit through the lens of modern software engineering:
- **Pāṇini's Grammar as a Compiler:** Proving that the 4th-century BCE *Aṣṭādhyāyī* is a pure functional term-rewriting engine equivalent to Backus-Naur Form (BNF).
- **The "Base + Badge" Paradigm:** Understanding the 7-case nominal routing network (*Kārakas*) and verbal state machines (*Dhātus*).
- **Physical Mouth Mechanics:** Explaining sound collisions (*Sandhi*) through literal vocal-tract physiology.
- **Epic Combat Deconstructions:** Word-by-word morphological parsing of the climactic battle scenes of Valmiki's *Rāmāyaṇa* (*Yuddha Kāṇḍa* Sargas 67 and 108) and the *Bhagavad Gītā*.

---

## Repository Structure

```
├── ERRATA.md                     # Live errata, typos, and technical updates
├── code/
│   ├── SanskritEngine.scala      # Scala 3 functional compiler models
│   ├── static_memory_loader.py   # Python dictionary & memory loader
│   └── requirements.txt          # Python dependencies
└── chapters/                     # Sample exercises & reading protocols
```

---

## Quickstart: Running the Code

### 1. Scala 3 Pāṇinian Engine
Run the interactive verification suite in 10 seconds using `scala-cli`:
```bash
# Install scala-cli if needed:
# macOS/Linux: brew install virtuslab/scala-cli/scala-cli
# Windows: winget install VirtusLab.scala-cli

scala-cli run code/SanskritEngine.scala
```

### 2. Python Transliteration & Lexicon Reader
```bash
pip install -r code/requirements.txt
python code/static_memory_loader.py
```

---

## Errata & Community Reporting

Found a typo, an unhandled Sandhi split, or an unclear derivation?  
Please check [ERRATA.md](ERRATA.md) or open an issue:
- [Submit Errata / Typo Report](https://github.com/om-script/sanskrit-by-architecture/issues)

---

## Book Availability

The print edition of *Sanskrit by Architecture* (7.0" x 10.0" Trim, 216 pages) is available worldwide on Amazon:
- **Paperback & Case-Laminate Hardcover** on Amazon KDP.
