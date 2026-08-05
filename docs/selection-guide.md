# Selection guide

Start with the legal job, not the benchmark name. Match the jurisdiction, source material, interface, scorer, and failure cost to the system you plan to use. A multiple-choice score does not establish reliable research, drafting, citation, redlining, or tool use.

[Catalog index](catalog.md) · [Methodology](methodology.md) · [Metric field guide](metric-theory.md) · [Back to README](../README.md)

## Recommendation matrix

Open artifacts support independent runs. Private and partial artifacts are included because they shape legal-AI claims and can supply useful protocol ideas, but their headline scores are not interchangeable with public results.

| Legal work | Open starting point | Private or partial signal | Lead evidence | Possible decision |
|---|---|---|---|---|
| Broad English legal reasoning | [LegalBench](https://github.com/HazyResearch/legalbench), [LexGLUE](https://github.com/coastalcph/lex-glue), [PRBench legal](https://www.justicebench.org/dataset/prbench) | — | Per-task task scorers; PRBench weighted criteria | Which model families merit testing on a fresh matter-specific set. |
| Chinese legal reasoning and drafting | [LawBench](https://github.com/open-compass/LawBench), [LexEval](https://github.com/CSHaitao/LexEval), [LexGenius](https://github.com/QwenQKing/LexGenius), [PLawBench](https://github.com/SKYLENAGE-AI/PLawBench) | — | Accuracy/F1 by task; open-response rubric coverage | Which model to carry into a time-held-out Chinese-law evaluation. |
| Arabic and Saudi legal work | [ArabLegalEval](https://github.com/Thiqah/ArabLegalEval), [ALARB](https://huggingface.co/datasets/THIQAH-RD/ALARB) | — | Accuracy/F1 separated by natural, translated, and synthetic source | Whether a model's Arabic result survives a locally authored Saudi-law holdout. |
| Multilingual legal NLU | [LEXTREME](https://github.com/JoelNiklaus/LEXTREME), [IL-TUR](https://github.com/Exploration-Lab/IL-TUR) | — | Per-language/task metrics plus named aggregate | Which language-task cells need targeted evaluation or data work. |
| Patent and intellectual-property work | [PILOT-Bench](https://github.com/TeamLab/pilot-bench), [MoZIP](https://github.com/AI-for-Science/MoZi) | — | PTAB issue/authority/outcome classification; multilingual IPQuiz accuracy; IPQA human preference; PatentMatch accuracy | Which model families merit a fresh, jurisdiction-specific patent drafting, prosecution, or validity-review holdout. |
| Contract clause extraction and classification | [CUAD](https://github.com/The-Atticus-Project/cuad), [ContractNLI](https://github.com/stanfordnlp/contract-nli), [MAUD](https://github.com/TheAtticusProject/maud) | — | AUPR/Jaccard; NLI and evidence F1; macro/micro-F1 | Which model and parser to test on document-family-held-out target contracts. |
| Contract clause retrieval | [ACORD](https://github.com/TheAtticusProject/acord) | — | nDCG@5/10 and graded precision@5 | Which retriever should enter a private clause-search pilot. |
| Redlining and contract review | [RedlineBench](https://github.com/crosbylegal/redline-bench) | [LegalOn 2026](https://www.legalontech.com/post/the-contract-review-benchmark-2026), [Ivo study](https://www.ivo.ai/news/ivo-outperforms-claude-for-word-in-independent-contract-review-benchmark), [legalbenchmarks.ai](https://www.legalbenchmarks.ai/leaderboard) | Weighted rubric score; blind lawyer dimensions; formatting retention; all-pass reliability | Which systems deserve blind attorney review on unseen playbooks and native files. |
| Exact-support retrieval | [LegalBench-RAG](https://github.com/zeroentropy-ai/legalbenchrag) | — | Character precision and recall, paired with document Recall@k | Which retriever supplies compact, sufficient evidence to a downstream answerer. |
| Statutory and case retrieval | [BSARD](https://github.com/maastrichtlawtech/bsard), [RegLab retrieval](https://reglab.github.io/legal-rag-benchmarks/), [LeCaRDv2](https://github.com/THUIR/LeCaRDv2), [COLIEE](https://coliee.org/COLIEE2026/) | — | Recall@k, MRR/MAP, nDCG, and expert rejudging of unjudged results | Which retrieval stack to evaluate on current, jurisdiction-matched authority. |
| End-to-end legal RAG | [Legal RAG Bench](https://github.com/isaacus-dev/legal-rag-bench), [CanLegalRAGBench](https://github.com/NLP-UBC/CanLegalRAGBench), [LLeQA](https://github.com/maastrichtlawtech/lleqa) | [Vals Legal Research](https://www.vals.ai/benchmarks/legal_research) | Retrieval success plus claim correctness, grounding, completeness, cost, and latency | Whether a research system is ready for independent legal review on fresh questions. |
| Citation verification and hallucination | [LegalCiteBench](https://github.com/Sijia711/LegalCiteBench), [Legal Phantom Citation](https://github.com/princeton-polaris-lab/legal-hallucination-agent), [Large Legal Fictions](https://github.com/reglab/legal_hallucinations), [Hallucination-Free?](https://reglab.stanford.edu/publications/hallucination-free-assessing-the-reliability-of-leading-ai-legal-research-tools/) | — | Citation retrieval/F1, span F1, factual correctness, groundedness, and human-coded hallucination | Which citation and research failure modes require hard gates or human review. |
| Long-horizon legal agents | [DLawBench](https://github.com/SKYLENAGE-AI/DLawBench), [J1Bench](https://github.com/FudanDISC/J1Bench), [Mercor APEX legal](https://github.com/Mercor-Intelligence/archipelago), [Harvey LAB public tasks](https://github.com/harveyai/harvey-labs) | [Legora BAR](https://legora.com/bar), Harvey's private LAB holdout | Process/outcome scores, all-pass, criterion pass rate, repeated runs, cost, and latency | Which agent architecture to test in an unseen environment with human work-product review. |
| In-house and BigLaw workflows | — | [GC AI In-House Legal Bench](https://gc.ai/blog/in-house-legal-bench-evaluating-ai-assistants-for-in-house-legal-work), [Thomson Reuters CoCoBench](https://www.thomsonreuters.com/en-us/posts/innovation/why-legal-ai-needs-a-new-standard-inside-thomson-reuters-cocobench/), [Harvey BigLaw Bench](https://www.harvey.ai/blog/introducing-biglaw-bench) | Task taxonomy, atomic criteria, source score, and attorney gold responses | How to scope an internal benchmark; vendor ranks alone should not drive procurement. |
| Deontic and statutory robustness | [DeonticBench](https://github.com/guangyaodou/DeonticBench), [OpenExempt](https://github.com/servantez/OpenExempt) | — | Accuracy, abstention, bootstrap intervals, and per-perturbation suite scores | Whether a model applies explicit rules consistently under controlled changes. |
| Fairness and subgroup robustness | [FairLex](https://github.com/coastalcph/fairlex) | — | Overall, per-group, worst-group, gap, support, and confidence interval | Which groups or jurisdictions require targeted error analysis; parity is not itself a legal fairness rule. |
| Legal translation | [SwiLTra-Bench](https://github.com/JoelNiklaus/SwissLegalTranslations), [MILPaC](https://github.com/Law-AI/MILPaC), [JUST-NLP 2025](https://www.codabench.org/competitions/10351/) | — | Named automatic metrics plus legal-expert ratings | Which translation systems should undergo terminology, omission, and legal-effect review. |

## Build a useful evaluation portfolio

Use four layers:

1. One established public benchmark for comparison with published work.
2. One task-specific benchmark matching the legal job, jurisdiction, language, and interface.
3. One fresh private holdout sampled from the actual decision context.
4. Human review of legally material failures, including omissions, unsupported authority, process violations, and native-file damage.

Then freeze the run:

1. Pin benchmark, dataset, scorer, prompt, judge, model endpoint, and dependency revisions.
2. Report per-task, language, jurisdiction, and subgroup results with item counts and uncertainty.
3. Separate retrieval, generation, citation, process, cost, and latency rather than hiding them in one rank.
4. Record prior exposure to public tasks and use document-, entity-, and time-grouped splits where possible.
5. Keep vendor-reported results in their own instrument. Harvey LAB, Harvey BigLaw Bench, Legora BAR, CoCoBench, GC AI, LegalOn, Ivo, legalbenchmarks.ai, and Vals do not share a common test or scorer.

The exact formulas and interpretation limits are documented in [metric theory](metric-theory.md).
