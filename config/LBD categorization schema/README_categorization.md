# LBD Paper Categorization System

## Overview

This directory contains a complete categorization system for classifying 408 literature-based discovery (LBD) papers. The system uses a two-tier approach:

1. **Tier 1:** Overall paper type (9 categories, applies to ALL papers)
2. **Tier 2:** Detailed method characteristics (only for "New Method" papers)

**Key Finding:** 89.5% of papers are NOT new method papers. Only 10.5% propose novel computational methods.

---

## Files in This System

### Core Documentation

1. **`LBD_categorization_guide.md`** (PRIMARY RESOURCE)
   - Comprehensive 8,000+ word categorization guide
   - Detailed definitions for all 9 paper types
   - Complete field specifications for method papers
   - Decision flowchart and examples
   - Ambiguous case resolution
   - Quality control checklist
   - **Use this for:** Understanding the full categorization scheme, training annotators, resolving ambiguous cases

2. **`LBD_categorization_quick_reference.md`**
   - Concise 2-page quick reference
   - All 9 categories with key indicators
   - Decision flowchart
   - Common patterns and mistakes
   - **Use this for:** Quick lookups during categorization, refreshers, onboarding

### LLM Automation

3. **`LBD_categorization_prompt.md`**
   - Complete prompt template for LLM-based categorization
   - Step-by-step instructions for LLMs
   - Input/output format specifications
   - 6 detailed worked examples
   - Error handling and edge cases
   - **Use this for:** Automating categorization with GPT-4, Claude, or other LLMs

4. **`categorization_schema.json`**
   - Formal JSON schema for output validation
   - All allowed values for each field
   - Required vs. optional field specifications
   - Example outputs
   - **Use this for:** Validating LLM outputs, building automated pipelines, ensuring consistency

### Reference Examples

5. **`sample_categorizations.json`**
   - 12 hand-categorized example papers
   - Covers all 9 paper types
   - Includes reasoning and notes
   - Mix of straightforward and ambiguous cases
   - **Use this for:** Training data, validation, few-shot prompting, quality checks

---

## Categorization Scheme Summary

### Tier 1: Nine Paper Types

| Category | % of Corpus | Avg Citations | Key Indicators |
|----------|-------------|---------------|----------------|
| **New Method (LBD)** | 10.5% | 8.9 | Novel algorithm, KG/text mining/symbolic (NOT LLM) |
| **New Method (LLM-based)** | ~23% (recent) | — | Uses GPT/BERT as PRIMARY mechanism [FILTER OUT] |
| **Review/Survey** | 13.2% | 38.1 | Comprehensive systematic review, high citations |
| **Perspective/Position** | 6.4% | 27.4 | Conceptual frameworks, "we argue" |
| **Methodological Critique** | 3.2% | 13.1 | Critical analysis of limitations |
| **Tutorial/Educational** | 2.9% | 12.8 | Step-by-step instructions, how-to guides |
| **Framework/Architecture** | 24.5% | 15.6 | System integration, no algorithmic novelty |
| **Application/Case Study** | 1.5% | 4.8 | Applies existing method to domain |
| **Other** | 33.6% | 28.8 | Foundational works, datasets, hybrids |

### Tier 2: Method Paper Fields (Required)

Only for "New Method (LBD)" and "New Method (LLM-based)" papers:

1. **datasets** - Data sources used (PubMed, HetioNet, DrugBank, etc.)
2. **dataRepresentation** - How data is structured (KG, text, embeddings, etc.)
3. **primaryEvaluationMetric** - Main performance metric (AUC-ROC, Precision, etc.)
4. **secondaryEvaluationMetrics** - Additional metrics reported
5. **dataSplitMethod** - How data is divided (random, temporal, k-fold, etc.)

**Optional fields:** discoveryMechanism, domain, validationType

---

## How to Use This System

### For Human Annotators

**Quick Start:**
1. Read `LBD_categorization_guide.md` sections 1-2 (Tier 1 categories)
2. Keep `LBD_categorization_quick_reference.md` open for lookups
3. Review `sample_categorizations.json` for examples
4. Use the decision flowchart for systematic categorization

**Workflow:**
1. Read paper title and abstract
2. Apply decision flowchart to determine Tier 1 category
3. If "New Method" type, extract Tier 2 fields from methods/results sections
4. Assign confidence level (high/medium/low)
5. Document reasoning and any ambiguities in notes

**Quality Checks:**
- Cross-reference ambiguous cases with guide examples
- Use "Not specified" rather than guessing
- Mark LLM-based papers for filtering
- Document alternative categories considered

---

### For LLM-Based Automation

**Setup:**

```python
# Example: Using OpenAI API
import openai
import json

# Load the prompt template
with open('LBD_categorization_prompt.md', 'r') as f:
    system_prompt = f.read()

# Load schema for validation
with open('categorization_schema.json', 'r') as f:
    schema = json.load(f)

# Load examples for few-shot prompting (optional)
with open('sample_categorizations.json', 'r') as f:
    examples = json.load(f)
```

**Basic Categorization:**

```python
def categorize_paper(paper_metadata):
    """
    Categorize a single paper using LLM.

    Args:
        paper_metadata: dict with keys 'paperId', 'title', 'abstract',
                       'year', 'venue', 'fieldsOfStudy' (optional)

    Returns:
        dict with categorization results matching schema
    """
    user_message = f"""
Categorize the following paper:

{json.dumps(paper_metadata, indent=2)}

Return a JSON object matching the categorization schema.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        response_format={"type": "json_object"},
        temperature=0.1  # Low temperature for consistency
    )

    result = json.loads(response.choices[0].message.content)

    # Validate against schema (recommended)
    # validate(result, schema)

    return result
```

**Batch Processing:**

```python
def categorize_papers_batch(papers, batch_size=10):
    """
    Categorize multiple papers with progress tracking.
    """
    results = []

    for i in range(0, len(papers), batch_size):
        batch = papers[i:i+batch_size]

        for paper in batch:
            try:
                result = categorize_paper(paper)
                results.append(result)

                # Log LLM-based papers flagged for filtering
                if result.get('shouldFilterOut'):
                    print(f"[FILTER] {paper['paperId']}: {result['overallType']}")

            except Exception as e:
                print(f"Error categorizing {paper['paperId']}: {e}")
                results.append({
                    "paperId": paper['paperId'],
                    "error": str(e)
                })

        # Save incremental results
        with open(f'categorization_results_batch_{i//batch_size}.json', 'w') as f:
            json.dump(results, f, indent=2)

    return results
```

**Few-Shot Prompting (Recommended):**

For better results, include 2-3 relevant examples in the prompt:

```python
def categorize_paper_with_examples(paper_metadata):
    """
    Use few-shot prompting with relevant examples.
    """
    # Select relevant examples based on paper characteristics
    # (e.g., if abstract mentions "survey", include a survey example)
    relevant_examples = select_relevant_examples(paper_metadata, examples)

    examples_text = "\n\n".join([
        f"Example {i+1}:\nInput: {ex['inputPaper']}\nOutput: {ex['categorization']}"
        for i, ex in enumerate(relevant_examples)
    ])

    user_message = f"""
Here are some example categorizations:

{examples_text}

Now categorize this paper:

{json.dumps(paper_metadata, indent=2)}
"""

    # ... rest of API call
```

**Quality Control:**

```python
def validate_categorization(result):
    """
    Perform quality checks on categorization results.
    """
    issues = []

    # Check required fields
    if not result.get('overallType'):
        issues.append("Missing overallType")

    # Check consistency
    if result.get('isLLMBased') and not result.get('shouldFilterOut'):
        issues.append("LLM-based papers should be filtered")

    # Check method details
    is_method = result.get('overallType', '').startswith('New Method')
    if is_method and result.get('methodDetails') is None:
        issues.append("Method paper missing methodDetails")

    if not is_method and result.get('methodDetails') is not None:
        issues.append("Non-method paper has methodDetails")

    # Check confidence matches completeness
    if result.get('confidence') == 'high':
        method_details = result.get('methodDetails', {}) or {}
        if is_method and 'Not specified' in str(method_details):
            issues.append("High confidence but has 'Not specified' fields")

    return issues
```

---

### For Reviewing and Analysis

**Extract Statistics:**

```python
def analyze_categorization_results(results):
    """
    Generate statistics from categorization results.
    """
    from collections import Counter

    # Overall type distribution
    type_counts = Counter(r['overallType'] for r in results)

    # Method paper statistics
    method_papers = [r for r in results
                     if r['overallType'].startswith('New Method')]

    llm_based = [r for r in results if r.get('isLLMBased')]
    to_filter = [r for r in results if r.get('shouldFilterOut')]

    # Confidence distribution
    confidence_counts = Counter(r['confidence'] for r in results)

    # Method characteristics (for method papers only)
    if method_papers:
        representations = Counter(
            r['methodDetails']['dataRepresentation']
            for r in method_papers
            if r.get('methodDetails')
        )

        metrics = Counter(
            r['methodDetails']['primaryEvaluationMetric']
            for r in method_papers
            if r.get('methodDetails')
        )

    return {
        'total_papers': len(results),
        'type_distribution': dict(type_counts),
        'method_papers': len(method_papers),
        'llm_based_papers': len(llm_based),
        'papers_to_filter': len(to_filter),
        'confidence_distribution': dict(confidence_counts),
        'top_representations': representations.most_common(5),
        'top_metrics': metrics.most_common(5)
    }
```

**Identify Papers Needing Review:**

```python
def find_papers_for_review(results):
    """
    Identify papers that need human review.
    """
    needs_review = []

    for r in results:
        if r['confidence'] == 'low':
            needs_review.append({
                'paperId': r['paperId'],
                'reason': 'Low confidence',
                'notes': r.get('notes', '')
            })

        # Check for ambiguous method papers
        if r['overallType'].startswith('New Method'):
            details = r.get('methodDetails', {}) or {}
            not_specified_count = str(details).count('Not specified')
            if not_specified_count >= 3:
                needs_review.append({
                    'paperId': r['paperId'],
                    'reason': f'Missing {not_specified_count} method fields',
                    'notes': r.get('notes', '')
                })

        # Check for potential miscategorizations
        if r['overallType'] == 'Other' and r['confidence'] != 'low':
            needs_review.append({
                'paperId': r['paperId'],
                'reason': 'Categorized as Other - verify specificity',
                'notes': r.get('notes', '')
            })

    return needs_review
```

---

## Expected Outcomes

### Primary Deliverable
A categorized dataset of all 408 papers with:
- Consistent tier 1 categorization (9 types)
- Detailed tier 2 fields for method papers (~43 papers)
- LLM-based papers flagged for filtering
- Confidence scores and reasoning documented

### Secondary Outcomes
- **Filtered corpus:** Traditional LBD papers only (LLM-based removed)
- **Method paper analysis:** Datasets, representations, metrics, validation approaches
- **Citation patterns:** By paper type and characteristics
- **Research gaps:** Identified through systematic categorization

### Success Criteria
✅ All 408 papers categorized with tier 1 labels
✅ Method papers have complete tier 2 fields (or "Not specified")
✅ LLM-based papers identified and flagged
✅ Consistency checks pass (>90% agreement for subset)
✅ Low-confidence papers (<10%) flagged for human review

---

## Quality Assurance

### Validation Steps

1. **Schema Validation:** All outputs match JSON schema
2. **Consistency Checks:**
   - isLLMBased ↔ shouldFilterOut alignment
   - overallType ↔ methodDetails presence
   - Confidence ↔ completeness alignment
3. **Sample Review:** Human review of 20 random papers (5% sample)
4. **Edge Case Review:** All low-confidence papers reviewed
5. **Inter-Rater Reliability:** 50-paper overlap with second annotator (>80% agreement)

### Common Issues to Watch

- **Framework vs. Method confusion:** Look for explicit algorithmic novelty
- **Missing LLM papers:** Check abstracts for GPT, BERT, language model mentions
- **"Other" overuse:** Should be <10% of corpus after filtering foundational papers
- **Guessed fields:** Use "Not specified" rather than inferring
- **Inconsistent naming:** Standardize dataset names (e.g., always "PubMed/MEDLINE")

---

## Next Steps

### After Initial Categorization

1. **Filter LLM-based papers** to create clean LBD corpus
2. **Analyze method papers** for evaluation patterns
3. **Generate statistics** on representation, metrics, domains
4. **Identify clusters** of similar methodological approaches
5. **Create visualizations** of categorization results

### Potential Extensions

- **Fine-grained method taxonomy:** Sub-categorize link prediction methods
- **Temporal analysis:** How methods evolved 1986-2024
- **Venue analysis:** Categorization by publication venue
- **Citation network analysis:** How categories cite each other
- **Dataset usage patterns:** Which datasets are most common

---

## Troubleshooting

### Issue: LLM produces invalid JSON
**Solution:** Use `response_format={"type": "json_object"}` (OpenAI) or explicitly request valid JSON

### Issue: LLM marks too many papers as "Other"
**Solution:** Add explicit instruction to minimize "Other" usage; provide more examples

### Issue: Missing method fields
**Solution:** If abstract lacks details, mark "Not specified" and flag for full-text review

### Issue: Inconsistent categorization across batches
**Solution:** Use low temperature (0.1), include examples in prompt, validate against earlier batches

### Issue: Ambiguous Framework vs. Method
**Solution:** Look for: "novel algorithm", "we propose", "new technique" → Method; "integrate", "platform", "existing methods" → Framework

---

## Contact & Contributions

For questions, issues, or suggestions:
- Review the full guide (`LBD_categorization_guide.md`)
- Check sample categorizations (`sample_categorizations.json`)
- Consult quick reference (`LBD_categorization_quick_reference.md`)

**Version:** 1.0
**Last Updated:** 2026-02-03
**Corpus Size:** 408 papers
**Categorization System:** Two-tier (9 overall types + method details)
