# Benchmark theory and exact metrics

This page explains what a legal benchmark score counts, which assumptions turn that count into a capability claim, and where the claim breaks.

[Catalog index](catalog.md) · [Selection guide](selection-guide.md) · [Methodology](methodology.md) · [Back to README](../README.md)

## Contents

- [The benchmark is not the dataset](#the-benchmark-is-not-the-dataset)
- [Four validity questions](#four-validity-questions)
- [Classification and extraction](#classification-and-extraction)
- [Ranking and retrieval](#ranking-and-retrieval)
- [Generation and translation](#generation-and-translation)
- [LLM judges and rubric scoring](#llm-judges-and-rubric-scoring)
- [Benchmark-specific composite scores](#benchmark-specific-composite-scores)
- [Contamination and leakage](#contamination-and-leakage)
- [Reliability and uncertainty](#reliability-and-uncertainty)
- [Minimum honest result card](#minimum-honest-result-card)

## The benchmark is not the dataset

A benchmark is at least five coupled objects:

1. **Construct** — the capability the authors intend to measure, such as statutory retrieval, clause issue spotting, deontic rule application, or end-to-end legal work.
2. **Items and sampling frame** — the questions, documents, environments, jurisdictions, dates, and populations from which items were selected.
3. **Interface** — the information and tools the system receives and the exact output contract.
4. **Scorer** — deterministic code, human rubric, model judge, or some composition of them.
5. **Aggregation and uncertainty** — how item scores become task, language, jurisdiction, or headline scores, and whether variation is quantified.

Changing any one of these changes the instrument. For example, LegalBench is explicitly a collection of 162 tasks mapped to six kinds of legal reasoning, not a single psychometric scale ([paper](https://arxiv.org/abs/2308.11462)). LEXTREME deliberately uses harmonic aggregation so weak language/task performance cannot be hidden by a high arithmetic average ([paper](https://arxiv.org/abs/2301.13126)).

## Four validity questions

Before interpreting a score, ask:

- **Construct validity:** Does success require the intended legal capability, or can formatting, boilerplate, citation frequency, source identity, or distractor artifacts solve it?
- **Content validity:** Does the item set cover the legal tasks, jurisdictions, difficulty, and failure costs relevant to the use case?
- **Criterion validity:** Does the automatic score agree with competent legal reviewers or downstream outcomes? MILPaC found that automatic translation metrics often had low correlation with law-practitioner ratings outside English–Hindi settings ([ACM article](https://doi.org/10.1145/3748313)).
- **Ecological validity:** Does the interface resemble actual work? Agent benchmarks improve realism with files and tools, but add harness, simulator, and judge variance. Harvey LAB's all-pass standard is a deliberate conjunctive reliability claim, not ordinary partial-credit grading ([methodology repository](https://github.com/harveyai/harvey-labs)).

No metric can repair a sample that does not represent the target use case.

## Classification and extraction

Let `TP`, `FP`, `FN`, and `TN` be true positives, false positives, false negatives, and true negatives.

### Accuracy and exact match

\[
\text{Accuracy} = \frac{\text{number of exactly correct items}}{N}
\]

Accuracy is appropriate for balanced single-label or multiple-choice tasks. It hides class imbalance and gives no partial credit. Exact match is stricter still: a structurally or semantically correct output can score zero after a formatting mismatch unless normalization is part of the scorer.

### Precision, recall, and F-score

\[
P = \frac{TP}{TP+FP}, \qquad
R = \frac{TP}{TP+FN}
\]

\[
F_1 = \frac{2PR}{P+R}, \qquad
F_\beta = (1+\beta^2)\frac{PR}{\beta^2P+R}
\]

`F2` uses `β=2`, making recall four times as influential as precision in the weighted harmonic mean. ContractEval uses F2 because missing a relevant clause is treated as more costly than returning some extra text ([paper](https://arxiv.org/abs/2508.03080)).

### Micro, macro, and worst-group aggregation

- **Micro-F1** pools all label decisions before computing F1. Frequent labels and large groups dominate.
- **Macro-F1** computes F1 per class and takes the arithmetic mean. Every class receives equal weight, so rare labels matter more.
- **Worst-group score** is the minimum score across named groups. It asks whether a system's floor is acceptable, but small groups can have high variance.
- **Group gap** is usually a difference between best/overall and worst group. It measures disparity in performance, not whether legal outcomes satisfy a normative fairness rule.

FairLex reports overall and group-robustness views across four jurisdictions; subgroup definition and support size are part of the result ([paper](https://aclanthology.org/2022.acl-long.301/), [repository](https://github.com/coastalcph/fairlex)).

### Span overlap / Jaccard (IoU)

For predicted token or character set `A` and gold set `B`:

\[
J(A,B) = \frac{|A \cap B|}{|A \cup B|}
\]

CUAD uses token-overlap/Jaccard-style evaluation alongside precision, recall, and AUPR ([paper](https://arxiv.org/abs/2103.06268)). It gives partial credit for overlapping the right clause but cannot determine whether the returned fragment preserves all legal qualifiers.

### Area under the precision–recall curve (AUPR)

AUPR integrates precision as the confidence threshold moves across the recall range. It is more informative than ROC-AUC when relevant clauses are rare. The exact value depends on score calibration, interpolation, and implementation; cite the official scorer.

## Ranking and retrieval

For query `q`, cutoff `k`, retrieved list `R_k`, and known relevant set `G`:

### Precision@k and Recall@k

\[
P@k = \frac{|R_k \cap G|}{k}, \qquad
R@k = \frac{|R_k \cap G|}{|G|}
\]

`Recall@k` answers “did the context window contain the needed authorities?” It does not reward ranking within the top `k` and assumes `G` is complete. CanLegalRAGBench's expert rejudging found relevant Canadian cases outside the initial gold set, demonstrating pooling bias directly ([paper](https://arxiv.org/abs/2605.30497), [repository](https://github.com/NLP-UBC/CanLegalRAGBench)).

### Reciprocal rank and MRR

If the first relevant result is at rank `r_q`:

\[
RR_q = \frac{1}{r_q}, \qquad
MRR = \frac{1}{|Q|}\sum_{q \in Q} RR_q
\]

MRR strongly rewards the first relevant result and ignores every relevant result after it. It fits “find one authority” tasks better than “collect all controlling authorities” tasks.

### Average precision and MAP

\[
AP_q = \frac{1}{|G_q|}\sum_{i=1}^{n} P@i \cdot \mathbf{1}[d_i \in G_q]
\]

\[
MAP = \frac{1}{|Q|}\sum_{q \in Q} AP_q
\]

MAP rewards ranking all known relevant documents early. Again, an incomplete `G_q` makes valid unseen authorities look wrong.

### DCG and nDCG

For graded relevance `rel_i` at rank `i`:

\[
DCG@k = \sum_{i=1}^{k}\frac{2^{rel_i}-1}{\log_2(i+1)}
\]

\[
nDCG@k = \frac{DCG@k}{IDCG@k}
\]

`IDCG` is the score of the ideal ranking for that query. The exponential gain makes high-grade items disproportionately valuable; the logarithmic discount penalizes placing them late. ACORD's attorney ratings (1–5 stars, encoded 0–4) make nDCG a natural primary metric ([official repository](https://github.com/TheAtticusProject/acord)). MLEB principally uses nDCG@10 through MTEB-compatible task definitions ([repository](https://github.com/isaacus-dev/mleb)).

### Exact-span retrieval

LegalBench-RAG represents support as character intervals and computes precision/recall over the covered character sets ([paper](https://arxiv.org/abs/2408.10343), [repository](https://github.com/zeroentropy-ai/legalbenchrag)). This directly exposes context bloat, unlike document-level Recall@k. It can still penalize a different, equally sufficient span unless the gold annotations are exhaustive.

## Generation and translation

### BLEU

For modified n-gram precisions `p_n`, weights `w_n`, candidate length `c`, and reference length `r`:

\[
BP = \begin{cases}
1 & c > r \\
e^{1-r/c} & c \le r
\end{cases}
\]

\[
BLEU = BP \cdot \exp\left(\sum_{n=1}^{N} w_n \log p_n\right)
\]

BLEU rewards reference n-gram precision with a brevity penalty ([original paper](https://aclanthology.org/P02-1040/)). Tokenizer, smoothing, case, and corpus versus sentence aggregation materially change it; record a SacreBLEU signature when available. MILPaC does this explicitly ([article](https://doi.org/10.1145/3748313)).

### GLEU and chrF++

- **GLEU** balances n-gram precision and recall for individual segments, using the lower of the two under the common implementation.
- **chrF++** computes an F-score over character n-grams and augments it with word n-grams. It is often more tolerant of morphology and tokenization differences.

Both remain reference-overlap metrics: a legally wrong translation can share vocabulary, and a legally equivalent translation can use different wording.

### ROUGE-L

Given longest common subsequence length `LCS`:

\[
P_{LCS}=\frac{LCS}{|candidate|}, \qquad
R_{LCS}=\frac{LCS}{|reference|}
\]

ROUGE-L combines these with an F-measure. It rewards retained sequence structure, not legal entailment or authority.

### BERTScore and learned MT metrics

BERTScore greedily aligns contextual token embeddings and aggregates cosine similarity into precision, recall, and F1 ([paper](https://arxiv.org/abs/1904.09675)). XCOMET and BLEURT learn quality estimators; GEMBA-MQM and SwiLTra-Judge use model judgment. SwiLTra-Bench compares these with legal experts ([paper](https://aclanthology.org/2025.acl-long.725/)). Their checkpoints, prompts, language coverage, and training overlap are part of the metric.

## LLM judges and rubric scoring

An LLM judge is not “the ground truth.” It is a measurement model. A reproducible judge protocol records:

- exact model/version and provider;
- full system/user prompt and rubric;
- reference answer and evidence visibility;
- sampling parameters, number of repeats, and aggregation;
- treatment of abstentions, parser failures, ties, and judge disagreement;
- validation against independent legal reviewers, ideally stratified by difficulty and subgroup.

### Weighted rubric pass rate

For criterion verdict `v_i ∈ {0,1}` and positive weight `w_i`:

\[
\text{WeightedPass} = \frac{\sum_i w_i v_i}{\sum_i w_i}
\]

Some benchmarks add negative penalties. RedlineBench's exact task reward is:

\[
\text{task reward}=\operatorname{clamp}_{[0,1]}\left(
\frac{\text{earned positive weight}-\text{penalty weight}}
{\text{total positive weight}}
\right)
\]

It averages identical-input rubric variants within input groups, then equally averages the 12 scenario × turn cells; the released headline is 0–100 ([HF card](https://huggingface.co/datasets/crosbylegal/RedlineBench), [code](https://github.com/crosbylegal/redline-bench)).

### All-pass

For `m` required criteria:

\[
\text{AllPass(task)} = \prod_{i=1}^{m}\mathbf{1}[criterion_i\ passes]
\]

The benchmark score is the mean across tasks. This models conjunctive reliability: one missed required issue fails the entire matter. It is strict, useful for high-stakes autonomy claims, and highly sensitive to rubric count and judge false-negative rate. Harvey LAB publishes both all-pass and rubric pass rate ([repository](https://github.com/harveyai/harvey-labs), [results](https://www.harvey.ai/blog/legal-agent-benchmark-initial-results)).

### Pass@1

\[
Pass@1 = \frac{\text{tasks passed on one evaluated trajectory}}{N}
\]

APEX-Agents uses Pass@1 for long-horizon professional tasks ([paper](https://arxiv.org/abs/2601.14242)). It reflects one-shot reliability only when the run policy, environment, and grader are fixed.

### Claim correctness and groundedness

CanLegalRAGBench decomposes a generated answer into atomic claims. A generated claim is counted correct when at least one gold-answer claim entails it; groundedness instead checks support from the retrieved evidence set. If `A(ŷ_q)` is the generated claim set and `E` the relevant evidence set:

\[
Score(\hat y_q,E)=\frac{1}{|A(\hat y_q)|}\sum_{a\in A(\hat y_q)}
\mathbf{1}\left[\max_{e\in E} Support(a,e)=1\right]
\]

The difference between answer-claim evidence and retrieved-document evidence separates reference agreement from context grounding ([paper](https://arxiv.org/abs/2605.30497)). It measures precision of generated claims, not omitted necessary claims, unless a complementary recall/completeness check is added.

Legal RAG Bench uses binary `correct` and `grounded` verdicts per question under a released GPT-5.2 high-reasoning judge; it also records whether the relevant passage was retrieved, enabling factorial error attribution ([code](https://github.com/isaacus-dev/legal-rag-bench)).

## Benchmark-specific composite scores

### LawBench task scoring and normalized log-distance

LawBench does **not** use one common scoring rule. Its official task map is ([README task table](https://github.com/open-compass/LawBench/blob/main/README_EN.md#task-list), [evaluator directory](https://github.com/open-compass/LawBench/tree/main/evaluation/evaluation_functions)):

| Cognitive level | Task IDs and official metrics |
|---|---|
| Memorization | 1-1 Article Recitation — ROUGE-L; 1-2 Knowledge QA — accuracy |
| Understanding | 2-1 Document Proofread — F0.5; 2-2 Dispute Focus — F1; 2-3 Marital Disputes — F1; 2-4 Issue Topic — accuracy; 2-5 Reading Comprehension — rc-F1; 2-6 Named Entity Recognition — soft-F1; 2-7 Opinion Summarization — ROUGE-L; 2-8 Argument Mining — accuracy; 2-9 Event Detection — F1; 2-10 Trigger Extraction — soft-F1 |
| Application | 3-1 Fact-based Article Prediction — F1; 3-2 Scene-based Article Prediction — ROUGE-L; 3-3 Charge Prediction — F1; 3-4/3-5 Prison Term Prediction without/with article — normalized log-distance; 3-6 Case Analysis — accuracy; 3-7 Criminal Damages — accuracy; 3-8 Consultation — ROUGE-L |

For prison-term prediction, let `g` and `p` be gold and parsed predicted months. The released evaluator computes:

\[
\text{NLD}=1-\frac{\frac{1}{N}\sum_i |\ln(g_i+1)-\ln(p_i+1)|}{\ln(216)}
\]

The parser takes the first number followed by “month,” otherwise the first number followed by “year” times 12. An unparsed prediction receives distance `ln(216)`, which contributes zero after normalization; gold death-penalty and life-imprisonment rows are skipped. This is a multiplicative-error-oriented score: equal ratios produce similar log distances, so an error from 1 to 2 months matters more than the same one-month absolute error at a long sentence. The code does not clamp the result, so sufficiently extreme predictions can make it negative ([official implementation](https://github.com/open-compass/LawBench/blob/main/evaluation/evaluation_functions/ljp_imprison.py)).

LawBench also reports a parser-defined abstention rate per task ([evaluation README](https://github.com/open-compass/LawBench/blob/main/evaluation/README.md)). That field needs audit before comparison: the named-entity scorer returns `anstention_rate` (misspelled), while the top-level evaluator only reads `abstention_rate`, silently producing zero for task 2-6 ([named-entity utility](https://github.com/open-compass/LawBench/blob/main/evaluation/utils/comprehension_scores.py), [top-level evaluator](https://github.com/open-compass/LawBench/blob/main/evaluation/main.py)). Its `rc-F1` is character-level after lowercasing and deleting punctuation; “soft-F1” uses that character overlap inside extracted entities/triggers ([official rc-F1 code](https://github.com/open-compass/LawBench/blob/main/evaluation/utils/rc_f1.py)). The published `AVG` is therefore an arithmetic combination of unlike constructs and scales, not a psychometrically calibrated general legal-ability score.

### LEXTREME hierarchical harmonic mean

For positive component scores `x_1…x_n`:

\[
H(x_1,\ldots,x_n)=\frac{n}{\sum_i 1/x_i}
\]

LEXTREME computes a dataset-oriented aggregate and a language-oriented aggregate using hierarchical harmonic means, then takes the harmonic mean of those two views ([paper, §4](https://arxiv.org/abs/2301.13126)). A single near-zero component can collapse the total; that is intentional robustness pressure.

### JUST-NLP 2025 AutoRank

The English-to-Hindi legal-MT shared task normalizes six metrics to a 0–100 higher-is-better scale, inverting TER, and then applies equal arithmetic weight:

\[
\text{AutoRank}=\frac{1}{6}\sum_{i=1}^{6}M_{i,\mathrm{norm}}
\]

The six components are BLEU, METEOR, TER, chrF++, BERTScore, and COMET ([official findings paper, §3.1](https://aclanthology.org/2025.justnlp-main.3/)). Equal weighting is transparent but does not make the components independent or turn their average into legal-fidelity evidence. The paper also contains an unresolved reporting conflict: its abstract says the top AutoRank was 72.1, while Table 2 and the [official result sheet](https://exploration-lab.github.io/JUST-NLP/JustNLP25_L-MT_Result.pdf) report Team-SVNIT first at 61.62.

### KCL essay score

KCL preserves each Korean Bar Exam question's official point value and divides it evenly across its instance rubrics. Model points are summed and divided by **2,905 total benchmark points**; Gemini 2.5 Flash judges rubric satisfaction ([paper](https://arxiv.org/abs/2512.24572), [code](https://github.com/lbox-kr/kcl)). This is a weighted percentage, not an average of questions.

### DeonticBench bootstrap

DeonticBench resamples cases with replacement for 1,000 replicates and samples one generation per case, then reports mean accuracy with 2.5/97.5 percentile bounds. Numeric SARA/Airline answers allow ±1 rounding tolerance; categorical answers require exact match. Empty, errored, timed-out, or unparsable outputs are reported as abstentions ([official evaluation instructions](https://github.com/guangyaodou/DeonticBench#evaluating-results-bootstrap-ci)).

### Ready Jurist One dual scoring

J1-EVAL combines outcome metrics (binary/open answer, document, judgment, charge, and penalty scores) with process metrics (format order, procedural stage completion, reasoning, and cited-law precision). Exact match, normalized log-distance, and model-based scoring are selected per scenario; the public paper's Table 2 is the authoritative map ([paper](https://aclanthology.org/2026.acl-long.471/), [code](https://github.com/FudanDISC/J1Bench)). Do not compare its overall score to a static QA accuracy.

## Contamination and leakage

Treat contamination as a family of failure modes:

- **Pretraining contamination:** test questions, answers, opinions, or contracts occur in the model's training corpus.
- **Development leakage:** public test labels influence prompts, routing, post-training, model selection, or repeated benchmark iteration.
- **Document-family leakage:** provisions or near-duplicate documents from one transaction/court template cross train and test.
- **Gold-in-context leakage:** the reference answer, decisive later procedural text, headnote, or outcome-bearing section remains in the model input.
- **Temporal leakage:** later law, later judgment sections, or current annotations are used to predict an earlier state.
- **Judge leakage:** the evaluated model family created the rubric, synthetic items, references, or evaluator labels.
- **Tool leakage:** filenames, metadata, hidden tests, or accessible grader files reveal the solution.

Public benchmarks remain useful for diagnosis and regression testing, but public-label scores should not be the sole evidence for a frontier capability claim. Prefer document/entity/time-grouped splits, private or freshly sampled holdouts, canary strings where lawful, duplicate detection, and evaluation logs that disclose prior benchmark exposure.

## Reliability and uncertainty

At minimum, report the number of items and repeated runs. For a simple mean over independent items, bootstrap confidence intervals are often practical. For agent evaluations, variance arises at several nested levels—task, environment, model sampling, tool execution, and judge repetition—so a single run per task understates uncertainty.

When humans or judges rate outputs, report agreement as well as mean score. Cohen's kappa adjusts two-rater categorical agreement for chance:

\[
\kappa = \frac{p_o-p_e}{1-p_e}
\]

For continuous multi-rater scores, choose and name the exact intraclass-correlation form; different ICC models answer different reliability questions.

## Minimum honest result card

Every published legal benchmark result should identify:

1. benchmark name, version/commit, dataset revision, and evaluation date;
2. exact task subset, jurisdiction, language, and item count;
3. input context, retrieval corpus, tools, and maximum budgets;
4. model endpoint/checkpoint, prompt, decoding, harness, dependencies, and number of runs;
5. scorer implementation, normalization, judge model/prompt/repeats, and aggregation formula;
6. per-task and subgroup scores plus uncertainty—not only a headline average;
7. abstentions, parser/tool failures, cost, latency, and human interventions;
8. known training/development exposure and contamination controls;
9. license/access constraints and any items excluded from reproduction;
10. concrete examples of legally material failures.

Without those fields, another reader cannot reproduce the run or judge whether the number supports the claimed capability.
