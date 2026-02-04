# LBD Categorization Quick Reference

A concise reference for quickly categorizing literature-based discovery papers.

---

## Tier 1: Overall Paper Types (9 Categories)

### Method Papers (10.5% of corpus)

**1. New Method (LBD)** - 10.5%, avg 8.9 citations
- Novel algorithm/technique for LBD
- Uses KGs, networks, text mining, symbolic reasoning (NOT LLMs)
- Keywords: "propose method", "novel algorithm", "new approach"
- → **Fill Tier 2 fields**

**2. New Method (LLM-based)** - ~23.5% of recent papers
- Uses LLMs (GPT, BERT) as PRIMARY discovery mechanism
- Keywords: "GPT-4", "language model", "BERT", "prompt engineering"
- → **Flag for filtering** (belongs to "LLM ideation" taxonomy)
- → **Fill Tier 2 fields**

### Non-Method Papers (89.5% of corpus)

**3. Review/Survey** - 13.2%, avg 38.1 citations (highest)
- Comprehensive systematic review comparing multiple methods
- Keywords: "survey", "systematic review", "state of the art"
- High citation counts (reference works)

**4. Perspective/Position** - 6.4%, avg 27.4 citations
- Conceptual frameworks, paradigm discussions
- Keywords: "we argue", "perspective", "conceptual framework"
- Opinion/vision-oriented, not systematic review

**5. Methodological Critique** - 3.2%, avg 13.1 citations
- Critical analysis of limitations, evaluation practices
- Keywords: "limitations of", "challenges", "evaluation biases"
- Identifies gaps without full implementation

**6. Tutorial/Educational** - 2.9%, avg 12.8 citations
- Teaching practitioners how to use methods
- Keywords: "tutorial", "step-by-step", "guide to", "how to"
- Includes code examples, workflows

**7. Framework/Architecture** - 24.5%, avg 15.6 citations
- System designs integrating existing methods
- Keywords: "platform", "system architecture", "integration of"
- No algorithmic novelty (uses existing ML/NLP)

**8. Application/Case Study** - 1.5%, avg 4.8 citations (lowest)
- Applies existing methods to specific domains
- Keywords: "application of", "using [tool] for", "case study"
- Domain insights are primary contribution

**9. Other** - 33.6%, avg 28.8 citations
- Foundational works, datasets, hybrids
- Swanson's original papers, knowledge bases
- Use sparingly (try specific categories first)

---

## Decision Flowchart

```
New method proposed?
├─ YES: Uses LLMs as core mechanism?
│   ├─ YES → New Method (LLM-based) [FILTER OUT]
│   └─ NO: Algorithmic novelty?
│       ├─ YES → New Method (LBD)
│       └─ NO → Framework/Architecture
└─ NO: Systematically reviews methods?
    ├─ YES: Comprehensive & structured?
    │   ├─ YES → Review/Survey
    │   └─ NO → Perspective (conceptual) or Critique (critical)
    └─ NO: Applies existing method to domain?
        ├─ YES → Application/Case Study
        └─ NO: Educational/instructional?
            ├─ YES → Tutorial/Educational
            └─ NO: Examines limitations?
                ├─ YES → Methodological Critique
                └─ NO: Conceptual framework?
                    ├─ YES → Perspective/Position
                    └─ NO → Other
```

---

## Tier 2: Method Paper Fields (Required)

**Only for "New Method (LBD)" and "New Method (LLM-based)"**

### 1. datasets (array)
Common values:
- Biomedical: `PubMed/MEDLINE`, `Semantic MEDLINE`, `MeSH`
- Knowledge Graphs: `HetioNet`, `DrugBank`, `KEGG`, `Chem2BioRDF`, `UniProt`
- Materials: `Materials Project`, `OQMD`
- Special: `Custom corpus`, `Proprietary dataset`, `Not specified`

### 2. dataRepresentation (string)
- `Knowledge Graph` - entity-relation triples, typed edges
- `Heterogeneous Network` - multi-entity types with typed edges
- `Text/Document-based` - raw/processed text, abstracts
- `MeSH Terms` - Medical Subject Headings hierarchy
- `Embeddings/Vectors` - word2vec, BERT embeddings
- `Ontology-based` - formal ontological structures
- `Symbolic/Logic-based` - logical predicates, rules
- `Other` or `Not specified`

### 3. primaryEvaluationMetric (string)
Common metrics:
- Classification: `AUC-ROC`, `AUC-PR`, `Precision`, `Recall`, `F1-score`, `Accuracy`
- Ranking: `MRR`, `Hits@K`, `NDCG`, `MAP`
- Discovery-specific: `Success Rate`, `Enrichment`, `Novelty Score`
- Special: `Qualitative assessment`, `Case study validation`, `Not specified`

### 4. secondaryEvaluationMetrics (array)
- Additional metrics beyond primary (can be empty `[]`)
- Don't duplicate primary metric

### 5. dataSplitMethod (string)
- `Random split` - random train/test division
- `Temporal split` - earlier for train, later for test
- `By disease/category` - split by domain/type
- `Leave-one-out cross-validation`
- `K-fold cross-validation`
- `No split` - full dataset, no held-out test
- `Not specified`

---

## Tier 2: Optional Fields

### 6. discoveryMechanism (optional)
- `Link Prediction` - graph ML predicting missing edges
- `Transitive Inference` - A-B-C paths, co-occurrence chains
- `LLM Generation` - language model hypothesis generation
- `Semantic Similarity` - distance/relatedness metrics
- `Topic Modeling` - LDA, probabilistic topics
- `Rule-based Inference` - logical rules, symbolic reasoning
- `Ensemble/Hybrid` - combines multiple mechanisms

### 7. domain (optional)
- `Biomedicine` (general)
- `Drug Discovery/Repurposing` (47.8% of recent methods)
- `Genetics/Genomics`
- `Cancer/Oncology`
- `Materials Science` (10.4% of recent methods)
- `Chemistry`
- `General-purpose`

### 8. validationType (optional)
- `Retrospective` - recover known past discoveries
- `Prospective` - lab/clinical validation (46.1% of recent methods)
- `Prediction Task` - benchmark with standard metrics (13.5%)
- `Expert Review` - domain expert judgment
- `Citation Analysis` - check subsequent literature
- `No validation` - method description only

---

## Common Patterns & Indicators

### Method vs. Framework
- **Method:** "propose algorithm", "novel technique", "we develop a method"
- **Framework:** "integrate", "combine existing", "platform", "system architecture"

### LLM-Based (Flag for Filtering)
- **Indicators:** GPT-3/4, Claude, BERT for generation, prompt engineering, fine-tuning LLM
- **NOT LLM-based:** Using embeddings from BERT (that's just representation)

### Review vs. Perspective
- **Review:** Systematic, comprehensive, structured methodology, high citation count
- **Perspective:** Conceptual, argumentative, "we argue", research agenda

### Missing Information
- Use `"Not specified"` for required string fields
- Use `[]` for optional array fields
- Use `null` for optional single-value fields
- Don't guess - mark confidence as "low"

---

## Confidence Levels

- **high:** Clearly fits category, all required info available
- **medium:** Some ambiguity or missing optional fields
- **low:** Significant ambiguity or missing required info

---

## Common Mistakes to Avoid

1. ❌ Confusing Framework with Method → Look for algorithmic novelty
2. ❌ Missing LLM papers → Check for GPT, BERT, language models
3. ❌ Overusing "Other" → Try specific categories first
4. ❌ Guessing missing info → Use "Not specified"
5. ❌ Duplicating primary metric → Don't list in secondary
6. ❌ Wrong representation → "Embeddings" means algorithm operates on vectors
7. ❌ Mixing validation & split → validationType ≠ dataSplitMethod

---

## Output Format (JSON)

```json
{
  "paperId": "string",
  "overallType": "One of 9 categories",
  "isLLMBased": true/false,
  "shouldFilterOut": true/false,
  "methodDetails": {
    // null for non-method papers
    // OR object with 5 required + 3 optional fields
  },
  "confidence": "high|medium|low",
  "reasoning": "2-3 sentences explaining decision",
  "notes": "Additional observations"
}
```

---

## Expected Statistics (408-paper corpus)

**Tier 1 Distribution:**
- New Method (LBD): 10.5% (43 papers)
- Review/Survey: 13.2% (54 papers) - highest citations
- Framework/Architecture: 24.5% (100 papers)
- Other: 33.6% (137 papers) - includes foundational works
- Rest: <7% each

**Method Papers:**
- 89.5% are NOT new methods
- LLM-based should be filtered (LLM ideation taxonomy)
- Recent methods: 47.8% drug discovery, 46.1% prospective validation

---

## Quick Category Selection

**See "novel algorithm/method/approach"?**
→ Method (check if LLM-based)

**See "survey/review/comprehensive"?**
→ Review/Survey

**See "we argue/conceptual framework"?**
→ Perspective/Position

**See "platform/system/integrate existing"?**
→ Framework/Architecture

**See "limitations/challenges/evaluation biases"?**
→ Methodological Critique

**See "tutorial/guide/how-to"?**
→ Tutorial/Educational

**See "application of [tool] to [domain]"?**
→ Application/Case Study

**Swanson's original work or datasets?**
→ Other

---

## Resources

- **Full Guide:** `LBD_categorization_guide.md` (comprehensive definitions & examples)
- **LLM Prompt:** `LBD_categorization_prompt.md` (prompt template for automated categorization)
- **JSON Schema:** `categorization_schema.json` (output format specification)
- **Samples:** `sample_categorizations.json` (12 hand-categorized examples)
