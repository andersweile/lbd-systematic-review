# LBD Categorization Scheme

**Note:** This file has been replaced by a comprehensive categorization system.

## New Categorization System (2026-02-03)

A complete two-tier categorization system has been developed based on analysis of the full 408-paper corpus. Please refer to the following files:

### Quick Start
- **`README_categorization.md`** - Start here for overview and usage instructions
- **`LBD_categorization_quick_reference.md`** - 2-page quick reference for rapid categorization

### Full Documentation
- **`LBD_categorization_guide.md`** - Comprehensive guide (8,000+ words) with detailed definitions, examples, and decision rules

### LLM Automation
- **`LBD_categorization_prompt.md`** - Complete prompt template for automated categorization with GPT-4/Claude
- **`categorization_schema.json`** - JSON schema for output validation

### Reference Examples
- **`sample_categorizations.json`** - 12 hand-categorized example papers covering all 9 types

---

## System Overview

### Two-Tier Structure

**Tier 1: Overall Paper Type (9 categories, applies to ALL papers)**
1. New Method (LBD) - Traditional LBD methods (10.5% of corpus)
2. New Method (LLM-based) - LLM-based discovery [FILTER OUT] (~23% of recent papers)
3. Review/Survey - Comprehensive systematic reviews (13.2%)
4. Perspective/Position - Conceptual frameworks (6.4%)
5. Methodological Critique - Critical analysis of limitations (3.2%)
6. Tutorial/Educational - How-to guides (2.9%)
7. Framework/Architecture - System integration (24.5%)
8. Application/Case Study - Domain applications (1.5%)
9. Other - Foundational works, datasets (33.6%)

**Tier 2: Detailed Method Fields (only for "New Method" papers)**
- Required: datasets, dataRepresentation, primaryEvaluationMetric, secondaryEvaluationMetrics, dataSplitMethod
- Optional: discoveryMechanism, domain, validationType

### Key Finding
**89.5% of papers are NOT new method papers.** Only 10.5% (43 papers) propose novel computational methods.

---

## Migration from Old Scheme

The new system addresses limitations of the preliminary scheme:

**Old Issues:**
- Only 3 overall categories (too coarse)
- No guidance for non-method papers (89.5% of corpus)
- Missing definitions and decision rules
- No LLM detection (important for filtering)

**New Features:**
- 9 distinct categories with clear definitions
- Comprehensive coverage of all paper types
- Decision flowchart and ambiguous case resolution
- LLM-based paper detection and filtering
- Detailed examples and quality control procedures
- JSON schema for automated validation
- LLM prompt templates for automation

---

## Quick Reference

For immediate use, the new system distinguishes:

**Method Papers (fill detailed fields):**
- Traditional LBD methods using KGs, networks, text mining
- LLM-based methods (GPT, BERT) → flag for filtering

**Non-Method Papers (simple labels):**
- Reviews & surveys (comprehensive coverage)
- Perspectives & positions (conceptual frameworks)
- Critiques (limitations & evaluation)
- Tutorials (educational content)
- Frameworks (system integration without novelty)
- Applications (domain-specific use of existing methods)
- Other (foundational works, datasets)

---

## Getting Started

1. Read `README_categorization.md` for overview
2. Use `LBD_categorization_quick_reference.md` for quick lookups
3. Consult `LBD_categorization_guide.md` for detailed definitions
4. Review `sample_categorizations.json` for examples

For automated categorization, see `LLM_categorization_prompt.md`.

---

**Version:** 2.0 (replaces preliminary scheme)
**Date:** 2026-02-03
**Corpus:** 408 papers analyzed
**Documentation:** See files listed above
