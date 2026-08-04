# Legal translation

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Shared tasks and multilingual corpora with automatic and legal-expert translation scoring.

Snapshot: **2026-08-03** · 3 entries

[Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)

## On this page

- [JUST-NLP 2025 Legal MT Shared Task](#just-nlp-2025-legal-mt)
- [SwiLTra-Bench](#swiltra-bench)
- [Multilingual Indian Legal Parallel Corpus](#milpac)

<a id="just-nlp-2025-legal-mt"></a>
## JUST-NLP 2025 Legal MT Shared Task

`just-nlp-2025-legal-mt` · **shared-task** · **specialist** · completed

Translate legal text from English to Hindi.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Reference-based machine-translation metrics reward n-gram or character overlap; the shared task complements them with semantic metrics but still cannot alone establish legal fidelity. |
| Jurisdiction | India |
| Languages | English, Hindi |
| Size | InLMT: 50,000 train, 5,000 validation, 5,000 hidden test sentences |
| Splits | Train/validation plus hidden Codabench test references |
| Source | Indian legal parallel text released for the shared task |
| Input | XLSX rows containing English legal sentences and IDs |
| Output | CSV with ID and Hindi translation |
| Baselines / leaderboard context | The findings paper's Table 2 ranks Team-SVNIT first at AutoRank 61.62; the abstract instead says the highest AutoRank was 72.1, an unresolved internal conflict. |
| Dataset access | Competition bundle via Codabench |
| License | Not clearly stated in the durable public materials |
| Gating | Codabench account may be required for files/submission |
| Maintenance | Completed 2025 shared task; not a continuously maintained benchmark. |
| Reproducibility | Hidden references support clean competition scoring, but long-term artifact access and exact dependency versions are uncertain. |

### Metrics

- **AutoRank:** Arithmetic mean of six 0–100 normalized metrics: BLEU, METEOR, inverted TER, chrF++, BERTScore, and COMET; each receives equal weight. **Primary.**
- **BLEU / METEOR / TER / chrF++ / BERTScore / COMET:** Report all six component metrics; higher is better except raw TER, where lower is better. ROUGE scores appear in additional model analysis but are not part of AutoRank.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | None |
| Hugging Face | None |
| Paper / arXiv | [https://aclanthology.org/2025.justnlp-main.3/](https://aclanthology.org/2025.justnlp-main.3/) |
| Leaderboard / competition | [https://www.codabench.org/competitions/10351/](https://www.codabench.org/competitions/10351/)<br>[https://exploration-lab.github.io/JUST-NLP/JustNLP25_L-MT_Result.pdf](https://exploration-lab.github.io/JUST-NLP/JustNLP25_L-MT_Result.pdf) |
| Project | [https://exploration-lab.github.io/JUST-NLP/](https://exploration-lab.github.io/JUST-NLP/) |

### Validity and evidence

**Risks / caveats**
- Automatic overlap metrics can reward fluent mistranslations or penalize legally equivalent wording.
- The original README linked stale Codabench competition 3682; 10351 is the verified competition.

**Verified facts**
- The official findings paper and competition materials define the 50k/5k/5k splits, six AutoRank components, normalization direction, and equal-weight aggregation.

**Inference**
- None recorded.

**Unresolved ambiguity**
- A clear dataset license was not located.
- The findings abstract reports a top AutoRank of 72.1 while Table 2 and the official result sheet report 61.62.

Original source bullet(s): #8

[Back to page index](#on-this-page)

<a id="swiltra-bench"></a>
## SwiLTra-Bench

`swiltra-bench` · **benchmark-suite** · **recommended** · fixed-release

Translate Swiss laws, court headnotes, and press releases among official Swiss languages and English.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Reference-based and learned semantic metrics compare translation fidelity; SwiLTra-Judge is calibrated against legal experts to better capture specialized legal adequacy than lexical overlap alone. |
| Jurisdiction | Switzerland |
| Languages | German, French, Italian, Romansh, English |
| Size | More than 180,000 aligned translation pairs across three document families |
| Splits | Dataset-specific train/test evaluation sets |
| Source | Swiss laws, decision summaries/headnotes, and Supreme Court press releases |
| Input | Legal text in one source language |
| Output | Translation in a target language |
| Baselines / leaderboard context | Paper evaluates frontier LLMs, specialized MT systems, and fine-tuned smaller models. |
| Dataset access | Public HF datasets |
| License | Dataset/source-specific |
| Gating | None observed |
| Maintenance | Stable 2025 release. |
| Reproducibility | Good for public data; learned judges and frontier API baselines require pinned checkpoints/endpoints. |

### Metrics

- **XCOMET / BLEURT / GEMBA-MQM:** Learned/reference and LLM translation-quality scores reported by document/language pair; preserve model versions. Judge: GEMBA-MQM uses an LLM evaluator. **Primary.**
- **SwiLTra-Judge / expert rating:** Specialized judge compared with human legal-expert assessments. Judge: SwiLTra-Judge. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/JoelNiklaus/SwissLegalTranslations](https://github.com/JoelNiklaus/SwissLegalTranslations) |
| Hugging Face | [https://huggingface.co/collections/joelniklaus/swiltra-bench](https://huggingface.co/collections/joelniklaus/swiltra-bench)<br>[https://huggingface.co/datasets/joelniklaus/SwissLawTranslations](https://huggingface.co/datasets/joelniklaus/SwissLawTranslations)<br>[https://huggingface.co/datasets/joelniklaus/SwissDecisionSummaryTranslations](https://huggingface.co/datasets/joelniklaus/SwissDecisionSummaryTranslations)<br>[https://huggingface.co/datasets/joelniklaus/SwissSupremeCourtPressReleaseTranslations](https://huggingface.co/datasets/joelniklaus/SwissSupremeCourtPressReleaseTranslations) |
| Paper / arXiv | [https://arxiv.org/abs/2503.01372](https://arxiv.org/abs/2503.01372)<br>[https://aclanthology.org/2025.acl-long.725/](https://aclanthology.org/2025.acl-long.725/) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Machine metrics correlate imperfectly with legal-expert judgments.
- Document families and language pairs differ sharply in size and difficulty.

**Verified facts**
- Official paper/GitHub/HF collection define the corpus families and evaluator set.

**Inference**
- None recorded.

**Unresolved ambiguity**
- There is no single HF dataset; the canonical resource is a three-dataset collection.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="milpac"></a>
## Multilingual Indian Legal Parallel Corpus

`milpac` · **benchmark-suite** · **recommended** · fixed-release

Translate verified Indian legal text from English into nine Indian languages.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | BLEU/GLEU/chrF++ measure reference overlap at word/character levels, while law-practitioner ratings test preservation of meaning, suitability for legal use, and fluency—the intended high-stakes construct. |
| Jurisdiction | India |
| Languages | English, Hindi, Bengali, Marathi, Tamil, Gujarati, Telugu, Malayalam, Punjabi, Odia |
| Size | 17,853 aligned pairs across three datasets |
| Splits | Corpus/dataset-specific evaluation files |
| Source | Verified IP primers, Indian statutes/acts, and legal FAQ materials ratified by legal experts |
| Input | English legal text unit |
| Output | Translation in one of nine Indian languages |
| Baselines / leaderboard context | Paper compares commercial MT, academic systems, open models, and LLMs. |
| Dataset access | Public GitHub |
| License | Non-commercial license |
| Gating | None observed |
| Maintenance | Stable benchmark/corpus release; also included as IL-TUR's translation task. |
| Reproducibility | Strong for automatic metrics with recorded tokenizer/SacreBLEU signature; human survey replication requires the same protocol. |

### Metrics

- **BLEU / GLEU / chrF++:** Corpus/reference overlap scaled 0–100; IndicNLP tokenization and SacreBLEU signature are recorded for BLEU/chrF++. **Primary.**
- **POM / SLU / FLY human ratings:** Law practitioners rate Preservation of Meaning, Suitability for Legal Use, and Fluency on the study scale. Judge: Human law practitioners/students. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/Law-AI/MILPaC](https://github.com/Law-AI/MILPaC) |
| Hugging Face | None |
| Paper / arXiv | [https://arxiv.org/abs/2310.09765](https://arxiv.org/abs/2310.09765)<br>[https://doi.org/10.1145/3748313](https://doi.org/10.1145/3748313) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Automatic metrics show low correlation with legal-human scores for several languages/datasets.
- Reusing MILPaC through IL-TUR is duplicate evidence, not a second independent translation benchmark.

**Verified facts**
- Official GitHub, arXiv, and ACM article define 17,853 pairs, nine target languages, and exact automatic/human metrics.

**Inference**
- None recorded.

**Unresolved ambiguity**
- None recorded.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)
