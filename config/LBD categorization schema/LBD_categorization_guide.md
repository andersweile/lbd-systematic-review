# LBD Paper Categorization Guide

## Overview

This guide provides a two-tier categorization system for 408 papers from a literature search on literature-based discovery (LBD). The system is designed to be used by both human annotators and large language models (LLMs) for consistent, automated categorization.

**Key Statistics:**
- 89.5% of papers (365/408) are NOT new method papers
- 10.5% (43 papers) propose novel computational methods
- Papers span from foundational works to recent LLM-based approaches

**Two-Tier Structure:**
1. **Tier 1**: Overall paper type (applies to ALL papers)
2. **Tier 2**: Detailed method characteristics (ONLY for "New Method" papers)

---

## Tier 1: Overall Paper Type

All papers receive exactly ONE of these nine categories:

### 1. New Method (LBD)

**Definition:** Papers proposing novel computational methods for literature-based discovery using traditional approaches (knowledge graphs, transitive inference, text mining, symbolic reasoning).

**Distinguishing Features:**
- Presents a NEW algorithm, technique, or computational approach
- Uses knowledge graphs, networks, text mining, symbolic logic, or semantic analysis
- Does NOT primarily rely on large language models (LLMs) for hypothesis generation
- Includes evaluation of the proposed method
- Focus is on the methodological contribution

**Common Keywords/Phrases:**
- "We propose a new method/algorithm/approach"
- "Novel framework for discovering"
- "Computational pipeline for"
- "Link prediction", "transitive inference", "knowledge graph"
- "Text mining approach", "semantic similarity"

**What to Look For:**
- Methods section describing algorithmic innovation
- Evaluation section with metrics and datasets
- Comparison to baseline methods
- Novel combination of existing techniques applied to LBD

**Examples:**
- A paper introducing a new link prediction algorithm for drug repurposing
- A system using transitive A-B-C paths with novel filtering criteria
- A knowledge graph embedding method for hypothesis generation

**NOT This Category:**
- Papers that only apply existing methods to new domains → **Application/Case Study**
- Papers describing system architecture without algorithmic novelty → **Framework/Architecture**
- Papers using LLMs for hypothesis generation → **New Method (LLM-based)**

**Statistics:** 10.5% of corpus (43 papers), average 8.9 citations

---

### 2. New Method (LLM-based)

**Definition:** Papers proposing methods that use large language models (GPT, BERT, etc.) as the PRIMARY mechanism for hypothesis generation or scientific discovery.

**Distinguishing Features:**
- Uses LLMs (GPT-3/4, Claude, BERT, etc.) for generating hypotheses
- LLM is central to the discovery mechanism, not just for preprocessing
- May involve prompting strategies, fine-tuning, or retrieval-augmented generation
- **IMPORTANT:** These papers should be filtered out - they belong to "LLM ideation" taxonomy, not traditional LBD

**Common Keywords/Phrases:**
- "Large language model", "LLM", "GPT-3/4", "ChatGPT"
- "Prompt engineering for hypothesis generation"
- "Language model for scientific discovery"
- "LLM-based ideation"

**What to Look For:**
- Methods section describing LLM usage as core mechanism
- Discussion of prompt design or model fine-tuning
- Evaluation of LLM-generated hypotheses
- Published primarily in 2020 or later (23.5% of recent papers)

**Examples:**
- Using GPT-4 to generate novel research hypotheses from literature
- Fine-tuning BERT for predicting gene-disease associations
- Prompt-based systems for drug repurposing hypothesis generation

**Statistics:** ~23.5% of papers from 2020+ may fall in this category

---

### 3. Review/Survey

**Definition:** Comprehensive surveys that systematically review existing LBD methods, compare approaches, or synthesize the state of the field.

**Distinguishing Features:**
- Broad coverage of multiple methods/systems
- Systematic comparison or taxonomy
- No new method proposed (or new method is minor compared to survey contribution)
- Structured review methodology
- Comprehensive reference list

**Common Keywords/Phrases:**
- "Survey of", "systematic review", "literature review"
- "State of the art", "comprehensive overview"
- "Taxonomy of approaches", "comparison of methods"
- "We reviewed X papers/systems"

**What to Look For:**
- Tables comparing multiple methods
- Historical progression of the field
- Classification schemes for existing work
- Gap analysis and future directions
- High citation counts (these are reference works)

**Examples:**
- Survey comparing knowledge graph approaches to LBD
- Systematic review of evaluation practices in hypothesis generation
- Historical overview of Swanson's ABC model and extensions

**NOT This Category:**
- Opinion pieces without systematic review → **Perspective/Position**
- Papers focusing on limitations rather than comprehensive coverage → **Methodological Critique**

**Statistics:** 13.2% of corpus (54 papers), average 38.1 citations (highest)

---

### 4. Perspective/Position

**Definition:** Papers presenting conceptual frameworks, paradigm discussions, or positions on how LBD should be conducted, without comprehensive systematic review.

**Distinguishing Features:**
- Proposes conceptual framework or theoretical model
- Discusses paradigms, philosophies, or approaches to LBD
- Opinion-oriented or vision-oriented
- May extend Swanson's framework conceptually
- Less systematic than reviews (more argumentative)

**Common Keywords/Phrases:**
- "We argue that", "perspective on", "position paper"
- "Conceptual framework", "theoretical model"
- "Paradigm shift", "new way of thinking"
- "Framework for understanding"

**What to Look For:**
- Focus on concepts and ideas rather than implementation
- Argumentation for a particular approach
- Discussion of what LBD should be or could be
- Philosophical or methodological positioning
- May propose terminology or classifications

**Examples:**
- Paper arguing for semantic integration in LBD systems
- Conceptual extension of Swanson's ABC model
- Position on the role of domain knowledge in discovery

**NOT This Category:**
- Systematic comparison of methods → **Review/Survey**
- Implementation of the proposed framework → **Framework/Architecture** or **New Method**

**Statistics:** 6.4% of corpus (26 papers), average 27.4 citations

---

### 5. Methodological Critique

**Definition:** Papers critically examining limitations, evaluation practices, or methodological issues in LBD research, with focus on identifying gaps and future directions.

**Distinguishing Features:**
- Critical analysis of existing methods
- Focus on limitations, challenges, or problems
- Evaluation of evaluation practices (meta-analysis)
- Identifies gaps in current research
- Proposes improvements without full implementation

**Common Keywords/Phrases:**
- "Limitations of", "challenges in", "problems with"
- "Evaluation practices", "methodological issues"
- "We identify gaps", "future directions"
- "Critical examination", "pitfalls of"

**What to Look For:**
- Critique of specific methods or the field as a whole
- Analysis of evaluation biases or shortcomings
- Discussion of reproducibility or validity issues
- Recommendations for better practices
- Lower implementation focus, higher analytical focus

**Examples:**
- Paper examining why LBD systems fail to generalize
- Analysis of evaluation biases in retrospective validation
- Critique of knowledge graph incompleteness issues

**NOT This Category:**
- Papers that include critique but focus on comprehensive survey → **Review/Survey**
- Papers proposing solutions to identified problems → **New Method**

**Statistics:** 3.2% of corpus (13 papers), average 13.1 citations

---

### 6. Tutorial/Educational

**Definition:** Papers designed to teach practitioners how to use LBD methods, with focus on practical guidance, how-to instructions, or educational content.

**Distinguishing Features:**
- Pedagogical purpose (teaching, not research contribution)
- Step-by-step instructions or guidelines
- Practical examples and demonstrations
- Aimed at practitioners or newcomers
- May include code, workflows, or recipes

**Common Keywords/Phrases:**
- "Tutorial on", "guide to", "how to"
- "Step-by-step", "practical guide", "workflow"
- "For practitioners", "introduction to"
- "Getting started with"

**What to Look For:**
- Instructional tone and structure
- Practical examples with detailed explanations
- Code snippets, command-line examples, or tool demonstrations
- Focus on reproducibility and usability
- Educational objectives stated explicitly

**Examples:**
- Tutorial on using semantic MEDLINE for hypothesis discovery
- Guide to building knowledge graphs for LBD
- Workshop paper teaching text mining for biomedical discovery

**NOT This Category:**
- Papers that include examples but focus on research contribution → **New Method**
- Conceptual teaching without practical steps → **Perspective/Position**

**Statistics:** 2.9% of corpus (12 papers), average 12.8 citations

---

### 7. Framework/Architecture

**Definition:** Papers describing system designs, architectures, or software frameworks for LBD without proposing novel algorithms or computational methods.

**Distinguishing Features:**
- Describes system architecture or software design
- Integrates existing methods/tools rather than creating new algorithms
- Focus on engineering, integration, or implementation
- May describe APIs, interfaces, or software components
- No significant algorithmic novelty (uses existing ML/NLP methods)

**Common Keywords/Phrases:**
- "System architecture", "framework for", "platform"
- "Integration of", "pipeline combining"
- "Software framework", "tool for"
- "Implementation of", "we developed a system"

**What to Look For:**
- Architecture diagrams, system components
- Description of data flows and integration
- Software engineering contributions
- User interfaces or APIs
- Uses existing algorithms/methods in new combination

**Examples:**
- Web platform integrating multiple LBD databases
- Pipeline system combining PubMed search with existing link prediction
- Software framework for biomedical hypothesis generation using off-the-shelf NLP

**NOT This Category:**
- Papers with novel algorithmic contributions → **New Method**
- Papers focused on conceptual design without implementation → **Perspective/Position**

**Statistics:** 24.5% of corpus (100 papers), average 15.6 citations

---

### 8. Application/Case Study

**Definition:** Papers applying existing LBD methods to specific domains or case studies, without proposing new methods or significant system development.

**Distinguishing Features:**
- Applies existing method to new domain or problem
- Focus is on the application domain, not the method
- Case study demonstrating use of LBD in practice
- No algorithmic innovation
- Domain-specific insights are the primary contribution

**Common Keywords/Phrases:**
- "Application of X to Y", "case study"
- "Using [existing method] for [domain problem]"
- "Discovery of [domain-specific finding]"
- "We applied", "we used [existing tool]"

**What to Look For:**
- Domain focus (drug discovery, materials science, etc.)
- Uses existing tools/methods with minimal modification
- Results focus on domain findings, not method performance
- Validation in specific domain context
- May demonstrate value of LBD but doesn't advance methodology

**Examples:**
- Using existing knowledge graph methods to discover drug candidates for COVID-19
- Applying Semantic MEDLINE to neurodegenerative disease research
- Case study of hypothesis generation in materials science

**NOT This Category:**
- Papers modifying methods for domain → **New Method**
- Papers building domain-specific systems → **Framework/Architecture**

**Statistics:** 1.5% of corpus (6 papers), average 4.8 citations (lowest)

---

### 9. Other

**Definition:** Papers that don't fit cleanly into above categories, including foundational works, dataset/resource papers, hybrids, or papers with multiple contributions of equal weight.

**Distinguishing Features:**
- Foundational papers establishing the field (Swanson's original work)
- Dataset or resource contributions
- Papers with mixed contributions (e.g., equal parts method + survey)
- Historical or philosophical works
- Papers that genuinely span multiple categories

**Common Keywords/Phrases:**
- (Varies widely - no consistent pattern)
- Foundational: Swanson's ABC model, early discovery systems
- Resources: "We present a dataset", "knowledge base", "corpus"

**What to Look For:**
- Papers cited as foundational work
- Dataset/resource papers describing new corpora
- Papers that are 50/50 method + survey
- Historical analyses of discovery process
- Papers defying simple categorization

**Examples:**
- Swanson's original 1986 papers on fish oil and Raynaud's disease
- Papers introducing major knowledge bases (e.g., Semantic MEDLINE)
- Hybrid papers proposing both method and comprehensive survey

**Use Sparingly:** Try to fit papers into specific categories first; only use "Other" when truly ambiguous or foundational.

**Statistics:** 33.6% of corpus (137 papers), average 28.8 citations (includes seminal foundational papers)

---

## Tier 2: Detailed Method Paper Fields

**IMPORTANT:** The following fields are ONLY filled out for papers categorized as **"New Method (LBD)"** or **"New Method (LLM-based)"** in Tier 1. All other paper types skip this section.

### Required Fields

These fields MUST be completed for all method papers:

#### 1. Dataset(s)

**Description:** The data sources or corpora used to evaluate the method.

**Format:** Comma-separated list of dataset names

**Allowed Values:**
- **Biomedical Databases:**
  - PubMed/MEDLINE (most common)
  - Semantic MEDLINE (structured extractions from MEDLINE)
  - PubMed Central (full-text articles)
  - MeSH (Medical Subject Headings)

- **Knowledge Graphs/Databases:**
  - Chem2BioRDF
  - HetioNet
  - DrugBank
  - KEGG (Kyoto Encyclopedia of Genes and Genomes)
  - UniProt
  - STRING (protein interactions)
  - DisGeNET (gene-disease associations)

- **Materials Science:**
  - Materials Project
  - OQMD (Open Quantum Materials Database)
  - MatWeb

- **Citation Networks:**
  - Microsoft Academic Graph
  - Semantic Scholar corpus
  - Web of Science

- **Special Values:**
  - "Custom corpus" (authors created their own dataset)
  - "Proprietary dataset" (non-public data)
  - "Not specified" (paper doesn't clearly state)

**How to Identify:**
- Look in "Data", "Materials", "Methods", or "Experimental Setup" sections
- Check for mentions of database versions (e.g., "PubMed articles up to 2015")
- Look for dataset URLs or access statements
- Check acknowledgments for data sources

**Examples:**
- "PubMed/MEDLINE, DrugBank, UniProt"
- "HetioNet"
- "Custom corpus (materials science abstracts)"
- "Not specified"

**Edge Cases:**
- If multiple versions of same dataset used, list once: "PubMed/MEDLINE" (not "PubMed 2015, PubMed 2020")
- If dataset is subset of larger database, use the larger name: "PubMed/MEDLINE" (not "PubMed cancer subset")
- If paper uses proprietary pharmaceutical data, use: "Proprietary dataset"

---

#### 2. Data Representation

**Description:** How the literature data is structured and represented for computational processing.

**Format:** Single selection from allowed values

**Allowed Values:**

- **Knowledge Graph:** Entities (drugs, diseases, genes) and relations (treats, causes, interacts) in graph structure with typed edges
  - Indicators: "knowledge graph", "KG", "entity-relation triples", "RDF graph"

- **Heterogeneous Network:** Multiple entity types with typed edges, but less formal than KG
  - Indicators: "heterogeneous network", "multi-relational network", "typed edges"

- **Text/Document-based:** Raw or processed text documents, abstracts, sentences
  - Indicators: "text mining", "document corpus", "abstracts", "NLP on text"

- **MeSH Terms:** Medical Subject Headings hierarchy and term co-occurrences
  - Indicators: "MeSH terms", "Medical Subject Headings", "MeSH co-occurrence"

- **Embeddings/Vectors:** Word embeddings, document embeddings, or learned representations
  - Indicators: "word2vec", "embeddings", "vector space", "neural embeddings", "BERT embeddings"

- **Ontology-based:** Formal ontological structures with defined semantics
  - Indicators: "ontology", "OWL", "semantic web", "formal semantics"

- **Symbolic/Logic-based:** Logical predicates, rules, first-order logic
  - Indicators: "logical rules", "predicates", "first-order logic", "symbolic reasoning"

- **Other (specify):** For representations not covered above, specify in notes

**How to Identify:**
- Look in "Methods", "Approach", or "Data Representation" sections
- Check for diagrams showing data structure
- Look for preprocessing steps that create specific representations
- Check what the algorithm operates on

**Examples:**
- "Knowledge Graph"
- "Text/Document-based"
- "Embeddings/Vectors"
- "Other (co-occurrence matrices)"

**Edge Cases:**
- If multiple representations used sequentially (text → graph), choose the PRIMARY representation the method operates on
- If hybrid (text + KG), choose the dominant one or note in "Other"
- Embeddings derived from KG → choose "Embeddings/Vectors" (it's what the algorithm uses)

---

#### 3. Primary Evaluation Metric

**Description:** The MAIN metric used to evaluate method performance - the one featured most prominently in results.

**Format:** Single metric name

**Allowed Values:**

**Classification/Ranking Metrics:**
- AUC-ROC (Area Under ROC Curve)
- AUC-PR (Area Under Precision-Recall Curve)
- Precision (at K or overall)
- Recall (at K or overall)
- F1-score / F-measure
- Accuracy
- Specificity
- Sensitivity

**Ranking Metrics:**
- MRR (Mean Reciprocal Rank)
- Hits@K (e.g., Hits@10)
- NDCG (Normalized Discounted Cumulative Gain)
- MAP (Mean Average Precision)

**Discovery-Specific:**
- Success Rate (% of hypotheses validated)
- Enrichment (fold enrichment over baseline)
- Novelty Score (measures unexpectedness)

**Special Values:**
- "Qualitative assessment" (expert evaluation without numerical metrics)
- "Case study validation" (validation through specific examples)
- "Not specified" (no clear evaluation metric)

**How to Identify:**
- Look in "Results" section for the first/main table or figure
- Check "Evaluation" section for primary metric definition
- Look for bolded or emphasized numbers in results
- If multiple metrics reported, choose the one discussed most in conclusions

**Examples:**
- "AUC-ROC"
- "Hits@10"
- "Precision"
- "Success Rate"
- "Qualitative assessment"

**Edge Cases:**
- If paper reports "Precision@10" and regular "Precision", use "Precision"
- If AUC-ROC and AUC-PR both featured equally, choose "AUC-ROC" (more common convention)
- If no quantitative metric exists, use "Qualitative assessment"

---

#### 4. Secondary Evaluation Metrics

**Description:** Additional metrics reported beyond the primary metric.

**Format:** Comma-separated list (can be empty if only one metric used)

**Allowed Values:** Same as Primary Evaluation Metric options

**How to Identify:**
- Look in results tables for all metrics reported
- Exclude the primary metric (don't duplicate)
- Include metrics from ablation studies if reported

**Examples:**
- "Recall, F1-score, Accuracy"
- "Hits@5, Hits@20, MRR"
- "" (empty - only one metric used)

**Edge Cases:**
- Don't include metrics from baseline methods unless also computed for proposed method
- Don't include metrics mentioned but not actually reported with numbers

---

#### 5. Data Split Method

**Description:** How the dataset is divided into training and test sets, or how evaluation is structured.

**Format:** Single selection from allowed values

**Allowed Values:**

- **Random split:** Random division of data into train/test (e.g., 80/20 split)
  - Indicators: "randomly split", "80/20 split", "random division"

- **Temporal split:** Earlier time period for training, later for testing
  - Indicators: "temporal split", "time-based split", "papers before 2010 for training, after for test"

- **By disease/category:** Split by domain, disease type, or category
  - Indicators: "split by disease", "category-based split", "some diseases for training, others for test"

- **Leave-one-out cross-validation:** Each instance used as test set once
  - Indicators: "leave-one-out", "LOO", "LOOCV"

- **K-fold cross-validation:** Dataset divided into K folds
  - Indicators: "5-fold cross-validation", "10-fold CV", "k-fold"

- **No split:** Full dataset used without held-out test set
  - Indicators: "all data used", "no test set", "evaluated on full dataset"

- **Not specified:** Paper doesn't clearly describe split method

**How to Identify:**
- Look in "Evaluation", "Experimental Setup", or "Methods" sections
- Check for train/test descriptions
- Look for temporal mentions (dates, years)
- Check for cross-validation descriptions

**Examples:**
- "Temporal split"
- "5-fold cross-validation"
- "Random split"
- "Not specified"

**Edge Cases:**
- If nested cross-validation used, note the outer loop type: "5-fold cross-validation"
- If multiple splits reported (e.g., random and temporal), choose the primary/main one
- If paper does case studies without formal split, use "No split"

---

### Optional Fields

These fields provide additional useful information but are not required:

#### 6. Discovery Mechanism (Optional)

**Description:** The core computational approach used to generate hypotheses or discover connections.

**Allowed Values:**

- **Link Prediction:** Graph-based machine learning predicting missing edges
  - Indicators: "link prediction", "predict missing edges", "graph neural network"

- **Transitive Inference:** A-B-C path-based reasoning, co-occurrence chains
  - Indicators: "ABC model", "transitive closure", "A-B-C paths", "bridging concepts"

- **LLM Generation:** Using language models for hypothesis generation
  - Indicators: "GPT-3", "language model generation", "LLM-based"

- **Semantic Similarity:** Distance or relatedness metrics in semantic space
  - Indicators: "semantic similarity", "cosine distance", "vector similarity"

- **Topic Modeling:** LDA, probabilistic topic models
  - Indicators: "LDA", "topic modeling", "latent topics"

- **Rule-based Inference:** Logical rules, symbolic reasoning, pattern matching
  - Indicators: "logical rules", "if-then rules", "symbolic inference"

- **Ensemble/Hybrid:** Combines multiple mechanisms
  - Indicators: "ensemble", "hybrid approach", "combines X and Y"

- **Other (specify):** For mechanisms not covered above

**How to Identify:**
- Look in "Methods" or "Approach" sections
- Check the algorithm description
- Look for the core innovation in method papers

---

#### 7. Domain (Optional)

**Description:** The application domain or scientific field targeted by the method.

**Allowed Values:**

- **Biomedicine:** General biomedical discovery (broad)
- **Drug Discovery/Repurposing:** Pharmaceutical applications, drug-disease
- **Genetics/Genomics:** Gene function, gene-disease associations
- **Cancer/Oncology:** Cancer-specific applications
- **Materials Science:** Material property discovery
- **Chemistry:** Chemical compound discovery
- **General-purpose:** Domain-agnostic, applicable to any field
- **Other (specify):** Other specific domains

**How to Identify:**
- Look at evaluation datasets (PubMed → biomedicine)
- Check use cases or examples
- Look at author affiliations and venue
- Check conclusion claims about applicability

**Statistics:**
- 47.8% of recent method papers: Drug Discovery/Repurposing
- 10.4% of recent method papers: Materials Science

---

#### 8. Validation Type (Optional)

**Description:** How the discovered hypotheses or predictions are validated.

**Allowed Values:**

- **Retrospective:** Recover known discoveries from past literature
  - Indicators: "retrospective validation", "recover known findings", "historical validation"

- **Prospective:** Validate predictions through lab experiments or clinical studies
  - Indicators: "experimental validation", "lab validation", "clinical validation", "wet-lab"

- **Prediction Task:** Benchmark evaluation with standard metrics (test set performance)
  - Indicators: "test set evaluation", "benchmark", "held-out data"

- **Expert Review:** Domain expert judgment of generated hypotheses
  - Indicators: "expert evaluation", "domain expert assessment"

- **Citation Analysis:** Check if subsequent literature confirms predictions
  - Indicators: "citation-based validation", "check future publications"

- **No validation:** Method description only, no validation
  - Indicators: No results section, or only synthetic data

**How to Identify:**
- Look in "Results", "Validation", or "Evaluation" sections
- Check if paper reports experimental confirmation
- Look for collaboration with domain experts or labs

**Statistics:**
- 46.1% of recent method papers use Prospective Validation
- 13.5% use Prediction Tasks
- 11.8% use Retrospective Case Studies

---

## Decision Flowchart

Use this flowchart to categorize papers systematically:

```
1. Does the paper propose a NEW computational method/algorithm?
   YES → Go to 2
   NO → Go to 4

2. Is the method LLM-based (uses GPT/BERT as core mechanism)?
   YES → Category: "New Method (LLM-based)" + Fill Tier 2 fields
   NO → Go to 3

3. Is there algorithmic novelty (not just system integration)?
   YES → Category: "New Method (LBD)" + Fill Tier 2 fields
   NO → Category: "Framework/Architecture"

4. Does the paper systematically review/compare multiple methods?
   YES → Go to 5
   NO → Go to 6

5. Is it comprehensive with structured methodology?
   YES → Category: "Review/Survey"
   NO → Category: "Perspective/Position" (if conceptual) or "Methodological Critique" (if critical)

6. Does it apply existing methods to a specific domain/case?
   YES → Category: "Application/Case Study"
   NO → Go to 7

7. Is it primarily educational/instructional?
   YES → Category: "Tutorial/Educational"
   NO → Go to 8

8. Does it critically examine limitations or evaluation practices?
   YES → Category: "Methodological Critique"
   NO → Go to 9

9. Does it propose conceptual frameworks or positions?
   YES → Category: "Perspective/Position"
   NO → Category: "Other" (foundational work, resource, hybrid)
```

---

## Example Categorizations

### Example 1: Link Prediction Method Paper

**Paper Title:** "Drug Repurposing Using Deep Graph Neural Networks on Heterogeneous Biological Networks"

**Tier 1 Categorization:**
- **Overall Type:** New Method (LBD)
- **Reasoning:** Proposes novel GNN architecture for link prediction; algorithmic contribution

**Tier 2 Method Details:**
- **Datasets:** HetioNet, DrugBank
- **Data Representation:** Heterogeneous Network
- **Primary Evaluation Metric:** AUC-ROC
- **Secondary Evaluation Metrics:** AUC-PR, Precision@50, Recall@50
- **Data Split Method:** Random split
- **Discovery Mechanism:** Link Prediction
- **Domain:** Drug Discovery/Repurposing
- **Validation Type:** Retrospective (recovers known drug-disease associations)

---

### Example 2: Survey Paper

**Paper Title:** "Literature-Based Discovery in Biomedicine: A Survey of Methods and Applications"

**Tier 1 Categorization:**
- **Overall Type:** Review/Survey
- **Reasoning:** Comprehensive systematic review comparing 30+ methods; no new method proposed

**Tier 2 Method Details:**
- (None - not a method paper)

---

### Example 3: LLM-Based Method (Should Filter)

**Paper Title:** "GPT-4 for Automated Hypothesis Generation in Materials Science"

**Tier 1 Categorization:**
- **Overall Type:** New Method (LLM-based)
- **Reasoning:** Uses GPT-4 as core mechanism for hypothesis generation
- **Action:** Flag for filtering (belongs to "LLM ideation" taxonomy)

**Tier 2 Method Details:**
- **Datasets:** Materials Project abstracts
- **Data Representation:** Text/Document-based
- **Primary Evaluation Metric:** Expert Review (domain scientists rate hypotheses)
- **Secondary Evaluation Metrics:** Novelty Score
- **Data Split Method:** Not specified
- **Discovery Mechanism:** LLM Generation
- **Domain:** Materials Science
- **Validation Type:** Expert Review

---

### Example 4: Framework Paper

**Paper Title:** "BioDiscovery: An Integrated Platform for Literature-Based Hypothesis Generation"

**Tier 1 Categorization:**
- **Overall Type:** Framework/Architecture
- **Reasoning:** Describes system integrating existing NLP tools and databases; no algorithmic novelty

**Tier 2 Method Details:**
- (None - not a method paper)

---

### Example 5: Application Paper

**Paper Title:** "Discovering Novel Targets for Alzheimer's Disease Using Semantic MEDLINE"

**Tier 1 Categorization:**
- **Overall Type:** Application/Case Study
- **Reasoning:** Applies existing Semantic MEDLINE tool to Alzheimer's research; domain-specific findings

**Tier 2 Method Details:**
- (None - not a method paper)

---

### Example 6: Perspective Paper

**Paper Title:** "Towards a New Paradigm for Knowledge-Based Discovery in Biomedicine"

**Tier 1 Categorization:**
- **Overall Type:** Perspective/Position
- **Reasoning:** Proposes conceptual framework for thinking about LBD; no implementation

**Tier 2 Method Details:**
- (None - not a method paper)

---

## Ambiguous Cases and How to Resolve

### Case 1: Method + Application Hybrid
**Scenario:** Paper proposes a new method AND applies it to a specific domain extensively

**Resolution:** If the method is novel and generalizable → **New Method (LBD)**. The application is just the evaluation context.

---

### Case 2: Framework with Minor Algorithmic Contribution
**Scenario:** Paper describes system architecture with one small novel algorithm component

**Resolution:** Judge based on emphasis. If paper focuses on system integration and the algorithm is minor → **Framework/Architecture**. If algorithm is featured prominently → **New Method (LBD)**.

---

### Case 3: Review with New Categorization Scheme
**Scenario:** Survey paper that proposes a new way to categorize existing methods

**Resolution:** If the categorization is the main contribution and comprehensive → **Review/Survey**. If categorization is conceptual without systematic coverage → **Perspective/Position**.

---

### Case 4: Tutorial with Small Method Contribution
**Scenario:** Educational paper that introduces a small methodological improvement

**Resolution:** If primary purpose is teaching → **Tutorial/Educational**. If method is significant → **New Method (LBD)**.

---

### Case 5: Missing Information in Paper
**Scenario:** Paper doesn't clearly specify datasets or evaluation metrics

**Resolution:** Use "Not specified" for missing required fields. Use your best judgment from context (e.g., if biomedical and no dataset mentioned, likely "PubMed/MEDLINE"). Note low confidence.

---

### Case 6: Multiple Datasets Used
**Scenario:** Paper evaluates on 5 different datasets

**Resolution:** List all datasets in comma-separated format. If too many (>5), list primary ones and note "and others" in notes field.

---

### Case 7: Hybrid Representation
**Scenario:** Method uses both text and knowledge graph

**Resolution:** Choose the PRIMARY representation the algorithm operates on. If truly hybrid with equal weight, note in "Other (hybrid: text + KG)".

---

## Quality Control Checklist

Before finalizing categorization, verify:

**For All Papers:**
- [ ] Exactly one Tier 1 category assigned
- [ ] Category matches paper's primary contribution
- [ ] Checked title, abstract, introduction, and conclusion
- [ ] Confidence level noted if ambiguous

**For Method Papers Only:**
- [ ] All 5 required Tier 2 fields completed
- [ ] Dataset names match standard names (not abbreviated)
- [ ] Primary evaluation metric is the main one from results
- [ ] Data split method matches what's described in methods
- [ ] Optional fields filled where information available

**Common Errors to Avoid:**
- ❌ Confusing "Framework/Architecture" with "New Method" (check for algorithmic novelty)
- ❌ Marking LLM-based papers as regular LBD (check for GPT/BERT usage)
- ❌ Using "Other" too frequently (try to fit into specific categories)
- ❌ Listing datasets used in paper but not for evaluation
- ❌ Confusing validation type with data split method

---

## Confidence Levels

Assign confidence to each categorization:

- **High:** Paper clearly fits category, all required information available
- **Medium:** Some ambiguity in categorization or missing optional fields
- **Low:** Significant ambiguity, missing required information, or genuinely hybrid

**When to mark Low confidence:**
- Paper fits multiple categories equally well
- Required method fields have "Not specified"
- Paper is foundational/historical and doesn't fit modern categories
- Abstract-only information (no full text available)

---

## Notes Field Usage

Use the notes field to document:
- Ambiguous cases and reasoning for choice
- Missing information that would help categorization
- Unusual characteristics worth noting
- Alternative category considerations
- Specific details about "Other" category papers

**Example notes:**
- "Borderline between New Method and Framework; chose Method due to novel ranking algorithm"
- "Missing dataset information; inferred PubMed from context"
- "Hybrid paper with equal parts method + survey; chose Review due to comprehensive coverage"
- "Foundational Swanson paper; doesn't fit modern categories cleanly"

---

## Summary Statistics to Expect

Based on 408-paper corpus analysis:

**Tier 1 Distribution:**
- New Method (LBD): ~10.5% (43 papers)
- New Method (LLM-based): ~23.5% of recent papers (estimate to filter)
- Review/Survey: 13.2% (54 papers)
- Perspective/Position: 6.4% (26 papers)
- Methodological Critique: 3.2% (13 papers)
- Tutorial/Educational: 2.9% (12 papers)
- Framework/Architecture: 24.5% (100 papers)
- Application/Case Study: 1.5% (6 papers)
- Other: 33.6% (137 papers)

**Method Papers (Tier 2):**
- Primary Data Representation: Knowledge Graphs (19.1% in 2020+), Text-based (18.4%)
- Primary Discovery Mechanism: LLM Generation (23.5% in 2020+), Transitive Paths (5.6%)
- Primary Validation: Prospective (46.1% in 2020+), Prediction Tasks (13.5%)
- Primary Domain: Drug Discovery (47.8% recent), Materials Science (10.4% recent)

**Citation Impact by Type:**
- Review/Survey: 38.1 avg citations (highest)
- Perspective/Position: 27.4 avg citations
- Other: 28.8 avg citations (includes foundational papers)
- Framework/Architecture: 15.6 avg citations
- New Method (LBD): 8.9 avg citations (lowest)

---

## Version History

- **v1.0 (2026-02-03):** Initial guide created based on 408-paper corpus analysis
