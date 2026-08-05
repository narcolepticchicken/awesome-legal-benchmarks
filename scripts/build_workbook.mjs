import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const projectDir = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const catalog = JSON.parse(
  await fs.readFile(path.join(projectDir, "catalog", "benchmarks.json"), "utf8"),
);
const resourceSnapshot = JSON.parse(
  await fs.readFile(path.join(projectDir, "catalog", "resource-snapshot.json"), "utf8"),
);
const outputDir = path.join(projectDir, "outputs");
const previewDir = path.join(os.tmpdir(), "awesome-legal-benchmarks-previews");
const outputPath = path.join(outputDir, "awesome-legal-benchmarks.xlsx");

const join = (items, separator = " | ") => (items ?? []).join(separator);
const resource = (entry, key) => join(entry.resources[key], "\n");
const statusLabel = (entry) => `${entry.tier} / ${entry.status}`;
const datedSource = (date) => date
  ? `${date.date} (${date.precision})\n${date.basis}\n${date.source}`
  : "No verified date located";
const numbered = (items) => (items ?? []).map((item, index) => `${index + 1}. ${item}`).join("\n");
const evidence = (entry) => [
  `VERIFIED: ${join(entry.evidence.verified) || "None recorded"}`,
  `INFERENCE: ${join(entry.evidence.inference) || "None recorded"}`,
  `AMBIGUITY: ${join(entry.evidence.ambiguities) || "None recorded"}`,
].join("\n");

const catalogHeaders = [
  "ID",
  "Canonical Name",
  "Aliases",
  "Owner",
  "Owner Type",
  "Commercial Interest",
  "Artifact Type",
  "Tier",
  "Status",
  "First Documented",
  "Creation Basis / Source",
  "Latest Verified Update",
  "Update Basis / Source",
  "Access Level",
  "Test Labels / Runnable",
  "Possible Use Cases",
  "Task / Capability",
  "Construct / Theory",
  "Jurisdictions",
  "Languages",
  "Data Size / Splits",
  "Data Source",
  "Input",
  "Output",
  "Exact Metrics / Protocol",
  "Judge Model",
  "Baselines / Leaderboard",
  "GitHub",
  "Hugging Face",
  "Paper / arXiv",
  "Leaderboard / Project",
  "Access / License",
  "Maintenance / Reproducibility",
  "Leakage / Key Caveat",
  "Evidence Classification",
  "Related Identities",
  "Original README Bullet(s)",
];

const catalogRows = catalog.entries.map((entry) => [
  entry.id,
  entry.name,
  join(entry.aliases),
  entry.owner.name,
  entry.owner.type,
  entry.owner.commercial_interest,
  entry.kind,
  entry.tier,
  entry.status,
  entry.dates.created?.date ?? "No verified date located",
  datedSource(entry.dates.created),
  entry.dates.last_updated?.date ?? "No verified update located",
  datedSource(entry.dates.last_updated),
  entry.access_profile.level,
  `labels=${entry.access_profile.test_labels}; runnable=${entry.access_profile.runnable}`,
  numbered(entry.possible_uses),
  entry.capability,
  entry.construct,
  join(entry.jurisdictions),
  join(entry.languages),
  `${entry.data.size}\nSPLITS: ${entry.data.splits}`,
  entry.data.source,
  entry.data.input,
  entry.data.output,
  entry.metrics
    .map(
      (metric) =>
        `${metric.primary ? "PRIMARY" : "SECONDARY"}: ${metric.name} — ${metric.protocol}`,
    )
    .join("\n"),
  join(entry.metrics.map((metric) => metric.judge).filter(Boolean), "\n") || "None",
  entry.baselines,
  resource(entry, "github") || "None",
  resource(entry, "huggingface") || "None",
  resource(entry, "papers") || "None",
  [resource(entry, "leaderboards"), resource(entry, "project")]
    .filter(Boolean)
    .join("\n") || "None",
  `${entry.access.dataset}; ${entry.access.gating}\nLICENSE: ${entry.access.license}`,
  `${entry.maintenance}\nREPRODUCIBILITY: ${entry.reproducibility}`,
  join(entry.risks, "\n"),
  evidence(entry),
  join(entry.related) || "None",
  entry.source_readme_bullets.length
    ? join(entry.source_readme_bullets.map(String), ", ")
    : "Curated addition",
]);

const selectionHeaders = [
  "Legal Work",
  "Open Starting Point(s)",
  "Private / Partial Signal",
  "Lead Evidence",
  "Possible Decision",
  "Direct URL(s)",
];
const selectionRows = [
  ["Broad English legal reasoning", "LegalBench; LexGLUE; PRBench legal", "—", "Per-task scorers; PRBench weighted criteria", "Choose model families for a fresh matter-specific set.", "https://github.com/HazyResearch/legalbench\nhttps://github.com/coastalcph/lex-glue\nhttps://www.justicebench.org/dataset/prbench"],
  ["Chinese legal reasoning and drafting", "LawBench; LexEval; LexGenius; PLawBench", "—", "Accuracy/F1 by task; open-response rubric coverage", "Choose models for a time-held-out Chinese-law evaluation.", "https://github.com/open-compass/LawBench\nhttps://github.com/CSHaitao/LexEval\nhttps://github.com/QwenQKing/LexGenius\nhttps://github.com/SKYLENAGE-AI/PLawBench"],
  ["Arabic and Saudi legal work", "ArabLegalEval; ALARB", "—", "Accuracy/F1 split by natural, translated, and synthetic source", "Test whether Arabic results survive a locally authored Saudi-law holdout.", "https://github.com/Thiqah/ArabLegalEval\nhttps://huggingface.co/datasets/THIQAH-RD/ALARB"],
  ["Multilingual legal NLU", "LEXTREME; IL-TUR", "—", "Per-language/task metrics plus named aggregate", "Identify language-task cells needing targeted evaluation or data work.", "https://github.com/JoelNiklaus/LEXTREME\nhttps://github.com/Exploration-Lab/IL-TUR"],
  ["Patent and intellectual-property work", "PILOT-Bench; MoZIP", "—", "PTAB classification; multilingual IPQuiz accuracy; IPQA human preference; PatentMatch accuracy", "Choose model families for a fresh, jurisdiction-specific patent drafting, prosecution, or validity-review holdout.", "https://github.com/TeamLab/pilot-bench\nhttps://github.com/AI-for-Science/MoZi"],
  ["Contract extraction and classification", "CUAD; ContractNLI; MAUD", "—", "AUPR/Jaccard; NLI/evidence F1; macro/micro-F1", "Choose a model and parser for document-family-held-out contracts.", "https://github.com/The-Atticus-Project/cuad\nhttps://github.com/stanfordnlp/contract-nli\nhttps://github.com/TheAtticusProject/maud"],
  ["Contract clause retrieval", "ACORD", "—", "nDCG@5/10 and graded precision@5", "Choose a retriever for a private clause-search pilot.", "https://github.com/TheAtticusProject/acord"],
  ["Redlining and contract review", "RedlineBench", "LegalOn 2026; Ivo study; legalbenchmarks.ai", "Weighted rubric; blind-lawyer dimensions; formatting retention; all-pass", "Choose systems for blind attorney review on unseen playbooks and native files.", "https://github.com/crosbylegal/redline-bench\nhttps://www.legalontech.com/post/the-contract-review-benchmark-2026\nhttps://www.ivo.ai/news/ivo-outperforms-claude-for-word-in-independent-contract-review-benchmark\nhttps://www.legalbenchmarks.ai/leaderboard"],
  ["Exact-support retrieval", "LegalBench-RAG", "—", "Character precision/recall plus document Recall@k", "Choose a retriever that supplies compact, sufficient evidence.", "https://github.com/zeroentropy-ai/legalbenchrag"],
  ["Statutory and case retrieval", "BSARD; RegLab retrieval; LeCaRDv2; COLIEE", "—", "Recall@k, MRR/MAP, nDCG, and expert rejudging", "Choose a stack for current, jurisdiction-matched authority.", "https://github.com/maastrichtlawtech/bsard\nhttps://reglab.github.io/legal-rag-benchmarks/\nhttps://github.com/THUIR/LeCaRDv2\nhttps://coliee.org/COLIEE2026/"],
  ["End-to-end legal RAG", "Legal RAG Bench; CanLegalRAGBench; LLeQA", "Vals Legal Research", "Retrieval, claim correctness, grounding, completeness, cost, latency", "Decide readiness for independent legal review on fresh questions.", "https://github.com/isaacus-dev/legal-rag-bench\nhttps://github.com/NLP-UBC/CanLegalRAGBench\nhttps://github.com/maastrichtlawtech/lleqa\nhttps://www.vals.ai/benchmarks/legal_research"],
  ["Citation verification and hallucination", "LegalCiteBench; Legal Phantom Citation; Large Legal Fictions; Hallucination-Free?", "—", "Citation retrieval/F1, span F1, groundedness, human-coded hallucination", "Set citation safety gates and human-review requirements.", "https://github.com/Sijia711/LegalCiteBench\nhttps://github.com/princeton-polaris-lab/legal-hallucination-agent\nhttps://github.com/reglab/legal_hallucinations\nhttps://reglab.stanford.edu/publications/hallucination-free-assessing-the-reliability-of-leading-ai-legal-research-tools/"],
  ["Long-horizon legal agents", "DLawBench; J1Bench; Mercor APEX legal; Harvey LAB public tasks", "Legora BAR; Harvey LAB private holdout", "Process/outcome, all-pass, criterion pass, repeated runs, cost, latency", "Choose architectures for an unseen environment and human work-product review.", "https://github.com/SKYLENAGE-AI/DLawBench\nhttps://github.com/FudanDISC/J1Bench\nhttps://github.com/Mercor-Intelligence/archipelago\nhttps://github.com/harveyai/harvey-labs\nhttps://legora.com/bar"],
  ["In-house and BigLaw workflows", "—", "GC AI In-House Legal Bench; CoCoBench; Harvey BigLaw Bench", "Task taxonomy, atomic criteria, source score, attorney gold responses", "Scope an internal benchmark; do not use vendor ranks alone for procurement.", "https://gc.ai/blog/in-house-legal-bench-evaluating-ai-assistants-for-in-house-legal-work\nhttps://www.thomsonreuters.com/en-us/posts/innovation/why-legal-ai-needs-a-new-standard-inside-thomson-reuters-cocobench/\nhttps://www.harvey.ai/blog/introducing-biglaw-bench"],
  ["Deontic and statutory robustness", "DeonticBench; OpenExempt", "—", "Accuracy, abstention, bootstrap intervals, perturbation-suite scores", "Test whether explicit rules are applied consistently under controlled changes.", "https://github.com/guangyaodou/DeonticBench\nhttps://github.com/servantez/OpenExempt"],
  ["Fairness and subgroup robustness", "FairLex", "—", "Overall, per-group, worst-group, gap, support, confidence interval", "Identify where targeted error analysis is needed; parity is not a legal rule.", "https://github.com/coastalcph/fairlex"],
  ["Legal translation", "SwiLTra-Bench; MILPaC; JUST-NLP 2025", "—", "Named automatic metrics plus legal-expert ratings", "Choose systems for terminology, omission, and legal-effect review.", "https://github.com/JoelNiklaus/SwissLegalTranslations\nhttps://github.com/Law-AI/MILPaC\nhttps://www.codabench.org/competitions/10351/"],
];

const metricHeaders = ["Family", "Metric / Formula", "What It Measures", "Theory / Interpretation", "Legal-Evaluation Caveat"];
const metricRows = [
  ["Classification", "Accuracy = exactly correct / N", "Single-label or MCQ correctness", "A Bernoulli mean under the benchmark item distribution.", "Class imbalance and item artifacts can hide legally important failures."],
  ["Classification", "Precision = TP/(TP+FP)", "Share of predicted positives that are correct", "Controls false-positive burden.", "A high precision system can omit many required issues."],
  ["Classification", "Recall = TP/(TP+FN)", "Share of known positives recovered", "Controls false-negative burden.", "Depends on exhaustive gold annotations."],
  ["Classification", "F1 = 2PR/(P+R)", "Harmonic balance of precision and recall", "Penalizes a near-zero component more than an arithmetic mean.", "Does not encode whether false positives or false negatives cost more."],
  ["Classification", "Fβ = (1+β²)PR/(β²P+R)", "Weighted precision/recall balance", "F2 gives recall four times precision's weight in the harmonic denominator.", "The chosen β is a value judgment; ContractEval uses F2 for missed-clause cost."],
  ["Aggregation", "Micro-F1 vs macro-F1", "Pooled decisions vs equal class weight", "Micro favors frequent classes; macro makes rare classes visible.", "Always report label supports and both views when imbalance is material."],
  ["Extraction", "Jaccard/IoU = |A∩B|/|A∪B|", "Token/character span overlap", "Partial credit for overlap with a gold clause/span.", "Cannot tell whether omitted qualifiers change the legal meaning."],
  ["Classification", "AUPR = area under precision–recall curve", "Threshold-free ranking quality for rare positives", "Integrates precision as the decision threshold changes.", "Implementation/interpolation and calibration must be pinned."],
  ["Retrieval", "P@k = relevant retrieved / k", "Top-k concentration", "Useful when context slots are scarce.", "Incomplete qrels penalize unseen valid authorities."],
  ["Retrieval", "R@k = relevant retrieved / known relevant", "Gold authority coverage within k", "Directly tests whether needed evidence enters the context window.", "Does not reward order inside k and assumes complete gold."],
  ["Retrieval", "MRR = mean(1 / first relevant rank)", "How early the first relevant result appears", "Fits find-one-authority tasks.", "Ignores every relevant result after the first."],
  ["Retrieval", "MAP = mean average precision", "Ranking of all known relevant documents", "Rewards repeated early precision across relevant items.", "Sensitive to incomplete pools and query relevance counts."],
  ["Retrieval", "DCG@k = Σ(2^relᵢ−1)/log₂(i+1); nDCG = DCG/IDCG", "Graded relevance with rank discount", "High relevance grades gain exponentially; later ranks are discounted.", "Gain mapping and cutoff are part of the protocol; ACORD uses attorney stars."],
  ["Generation / MT", "BLEU = brevity penalty × exp(weighted log n-gram precision)", "Reference n-gram precision", "Corpus overlap proxy with a brevity penalty.", "Tokenizer, smoothing, and references matter; overlap is not legal fidelity."],
  ["JUST-NLP 2025", "AutoRank = (1/6) × Σ six normalized metrics", "Equal-weight aggregate of BLEU, METEOR, inverted TER, chrF++, BERTScore, and COMET", "All components are mapped to a 0–100 higher-is-better scale before averaging.", "The findings abstract says 72.1 while Table 2 and the official result sheet report a winning 61.62."],
  ["Generation", "ROUGE-L = F-measure over longest common subsequence", "Reference sequence overlap", "Rewards retained ordering and phrasing.", "Does not establish entailment, authority, or completeness."],
  ["Generation", "BERTScore = contextual-token alignment P/R/F1", "Semantic embedding similarity", "Soft alignment captures more paraphrase than n-gram overlap.", "Encoder training overlap and domain mismatch affect scores."],
  ["Rubric judge", "WeightedPass = Σwᵢvᵢ / Σwᵢ", "Weighted rubric satisfaction", "Weights encode the benchmark author's loss function.", "Judge model, prompt, repeats, parser, and human agreement must be disclosed."],
  ["RedlineBench", "clamp((earned positive weight − penalties)/total positive weight, 0, 1)", "Scenario-specific drafting quality", "Variants average within input groups, then 12 scenario×turn cells are equally averaged.", "Do not recreate the headline with a simple mean of raw rubric rows."],
  ["Agent", "AllPass(task) = product of required criterion passes", "Conjunctive matter reliability", "One failed required criterion fails the task; Harvey LAB also reports rubric pass rate.", "Highly sensitive to rubric count and judge false negatives."],
  ["Agent", "Pass@1 = tasks passed on one evaluated trajectory / N", "One-shot task reliability", "Meaningful only with fixed run policy, environment, and grader.", "Repeated stochastic runs are needed to estimate variance."],
  ["RAG generation", "Claim score = supported generated claims / generated claims", "Claim correctness or evidence grounding precision", "Can separate answer agreement from retrieved-context support.", "Does not measure omitted necessary claims without a recall/completeness term."],
  ["Composite", "H(x₁…xₙ) = n / Σ(1/xᵢ)", "Harmonic robustness aggregation", "LEXTREME applies hierarchical harmonic means by dataset and language.", "One near-zero cell can collapse the score by design."],
  ["LawBench", "NLD = 1 − mean(|ln(g+1)−ln(p+1)|) / ln(216)", "Multiplicative distance between gold and predicted prison-term months", "The first parsed month, or first year × 12, is scored; an unparsed answer contributes zero after normalization.", "Death/life rows are skipped, scores are not clamped, and abstention handling is inconsistent across tasks."],
  ["KCL", "passed official rubric points / 2,905", "Weighted Korean bar-essay performance", "Official question points are divided over 2,739 rubrics and then summed.", "Gemini 2.5 Flash judge and rubric-generation dependence must be pinned."],
  ["DeonticBench", "Mean accuracy + 2.5/97.5 percentiles over 1,000 bootstrap resamples", "Accuracy uncertainty with sampled generations", "Numeric answers allow ±1; categorical answers require exact match; abstentions are separate.", "Pin the corrected Prolog/data revision and report parse/tool failures."],
  ["Ready Jurist One", "Scenario-specific exact, judge, charge, citation, process, and log-distance scores", "Outcome plus workflow adherence", "Table 2 maps ten metrics across three difficulty levels.", "Paper says 508 total tasks but its 160+186+192 level counts sum to 538."],
  ["PRBench", "Weighted rubric score over 10–30 binary criteria with weights from −10 to +10", "Professional requirement satisfaction", "Positive weights encode importance; negative criteria encode prohibited failures; law must be reported separately from finance.", "Official sources disagree on 19,356 versus 18,692 criteria, so pin the dataset and scorer revision."],
  ["DLawBench", "Mean of Fact Coverage, Inquiry, Elicitation, Fact Resolution, Issue Resolution, Resolution, and Fidelity", "Consultation process and final legal resolution", "Session-level dimensions are equally averaged across available jurisdictions.", "The configurable evaluator model is part of the instrument and must be named."],
  ["Harvey LAB", "AllPass(task)=∏ criterion passes; macro and pooled criterion-pass rates", "Conjunctive matter reliability plus partial completion", "Default judge is Claude Sonnet 4.6 at temperature 0; optional dual judging adds GPT-5.5 and strict agreement.", "All-pass falls mechanically with rubric count; current official files disagree at 1,671 versus 1,660 tasks."],
  ["Harvey BigLaw Bench", "Answer Score=(positive points earned + negative penalties)/positive points available; separate Source Score", "Substantive answer quality and source support", "Keeping answer and source scores separate prevents unsupported fluency from reading as sourced analysis.", "The full task set is private, so published scores are not independently reproducible."],
  ["Legora BAR", "Binary high/medium/low-weight expert criteria; three runs per case", "Facts, analysis, citations, and recommendations in legal work product", "Repeated runs expose trajectory variance; weighted criteria encode expert loss judgments.", "Exact judge model, prompt, calibration, weight formula, and aggregation are not public."],
  ["MoZIP IPQuiz / PatentMatch", "Exact answer accuracy, reported by task and language", "Closed-form IP knowledge and patent-semantic matching", "IPQuiz parses one or more option letters; PatentMatch selects one of four abstracts.", "Public labels, web-sourced quiz questions, and retrieved distractors create contamination and shortcut risk."],
  ["MoZIP IPQA", "Pairwise win/tie/loss; judge agreement gives 1 for agreement, 0.5 for one tie, 0 for opposite winners", "Human preference over open IP answers", "The reported 81% is inter-evaluator agreement, not a model score; outcomes remain pairwise.", "No released scalar aggregate or executable human-judging harness; language samples are small and uneven."],
  ["LegalOn 2026", "Reversed-order pairwise preference; only consistent preferences count as wins; Elo with 95% CI", "Relative contract-review preference within a fixed system pool", "Order reversal turns inconsistent judgments into ties before Elo aggregation.", "Exact K-factor, pairing schedule, private items, and judge details are not all public."],
  ["legalbenchmarks.ai / Vals", "All-pass reliability plus separate usefulness or weighted partial credit", "Complete rubric satisfaction versus diagnostic partial completion", "A task passes only when every required criterion passes; partial scores reveal near misses.", "Private tasks and owner-controlled judges prevent a fully independent audit; rubric length changes all-pass difficulty."],
  ["LegalCiteBench", "Mean average recall, citation precision/recall/F1, and correct-response rate", "Citation retrieval, production, verification, and abstention", "Task-specific 0–100 scores keep different citation failure modes separate.", "Citation form and retrieval do not establish that authority is controlling, current, or supports the proposition."],
];

const entryByBullet = new Map();
for (const entry of catalog.entries) {
  for (const bullet of entry.source_readme_bullets) entryByBullet.set(bullet, entry);
}
const sourceAuditHeaders = [
  "README #", "Canonical Name", "Identity / Type", "Task / Capability",
  "Data / Jurisdiction / Format", "Metrics", "GitHub", "Paper / arXiv",
  "Hugging Face", "Reproducibility / Status", "Correction / Key Caveat", "Other Official URL",
];
const sourceAuditRows = Array.from({ length: 22 }, (_, index) => {
  const bullet = index + 1;
  const entry = entryByBullet.get(bullet);
  const duplicate = bullet === 20;
  return [
    bullet,
    entry.name,
    duplicate ? "Duplicate of #3 (same MLEB identity)" : entry.kind,
    entry.capability,
    `${entry.data.size}; ${join(entry.jurisdictions)}; ${join(entry.languages)}; INPUT: ${entry.data.input}; OUTPUT: ${entry.data.output}`,
    join(entry.metrics.map((metric) => metric.name), "; "),
    resource(entry, "github") || "None",
    resource(entry, "papers") || "None",
    resource(entry, "huggingface") || "None",
    `${statusLabel(entry)}; ${entry.reproducibility}`,
    duplicate
      ? "Merge with bullet #3. Same artifacts, task, metrics, and public-label/vendor risks."
      : `${join(entry.risks, " ")} ${join(entry.evidence.ambiguities, " ")}`.trim(),
    [resource(entry, "leaderboards"), resource(entry, "project")].filter(Boolean).join("\n") || "None",
  ];
});

const resourceHeaders = [
  "Status", "Resource Role(s)", "URL", "Canonical URL", "Used By", "HTTP",
  "Private / Gated", "Archived / Disabled", "License", "Last Updated", "Downloads / Likes",
];
const resourceRows = resourceSnapshot.resources.map((item) => {
  const metadata = item.metadata ?? {};
  return [
    item.verification_status === "available" ? "OK" : item.ok ? "LIMITED" : "FAIL",
    join(item.families),
    item.url,
    item.canonical_url ?? "",
    join(item.benchmark_ids),
    item.http_status ?? "",
    `private=${metadata.private ?? "n/a"}; gated=${metadata.gated ?? "n/a"}`,
    `archived=${metadata.archived ?? "n/a"}; disabled=${metadata.disabled ?? "n/a"}`,
    (metadata.license_spdx ?? join(metadata.licenses)) || "Not declared in API metadata",
    metadata.pushed_at ?? metadata.last_modified ?? "",
    `downloads=${metadata.downloads ?? "n/a"}; likes=${metadata.likes ?? "n/a"}`,
  ];
});

const watchlistHeaders = ["Candidate", "Why It Matters", "Why Not Yet Promoted", "Primary URLs"];
const watchlistRows = [
  ["BenGER", "German legal benchmark platform", "Need a fixed, versioned task/data/scorer release separate from the mutable platform.", "https://github.com/SebastianNagl/benger-platform\nhttps://arxiv.org/abs/2605.28183\nhttps://what-a-benger.net/"],
  ["UA-Legal-Bench", "Ukrainian legal evaluation", "HF identifies v1 while the paper describes v2; canonical version relationship unresolved.", "https://huggingface.co/datasets/overthelex/ua-legal-bench\nhttps://arxiv.org/abs/2605.29170\nhttps://github.com/overthelex/secondlayer-papers"],
  ["Multi-Legal-Bench", "Large multilingual legal collection", "Public descriptions conflict at roughly 134M vs 122M records; scoring/reproducibility unclear.", "https://huggingface.co/datasets/overthelex/multi-legal-bench\nhttps://arxiv.org/abs/2605.29738"],
  ["Legal-DC", "Chinese legal document RAG", "Very recent; inspect final splits, official scorer, and leakage controls before promotion.", "https://github.com/legal-dc/Legal-DC\nhttps://arxiv.org/abs/2603.11772"],
  ["TW-LegalBench", "Taiwan/Traditional-Chinese legal evaluation", "Very recent; canonical source repository and stable evaluation code not located.", "https://huggingface.co/datasets/feiyuehchen/TW-LegalBench\nhttps://arxiv.org/abs/2606.18699"],
  ["Legal Rikai Open Benchmark", "Japanese legal evaluation", "Gated, nonstandard license metadata, and only about 100 exposed samples.", "https://huggingface.co/datasets/legalontech/Legal-Rikai-Open-Benchmark\nhttps://arxiv.org/abs/2512.11297"],
  ["LegalBench-BR", "Brazilian appellate classification and reasoning", "No canonical dataset or GitHub release located; an unrelated HF dataset has a confusingly similar name.", "https://arxiv.org/abs/2604.18878\nhttps://huggingface.co/pedronettotrue/bertimbau-legal-tjsc"],
  ["CaseFacts", "US Supreme Court fact checking and precedent retrieval", "Paper defines 6,294 claims, but no public dataset, scorer repository, or leaderboard was found.", "https://aclanthology.org/2026.acl-long.785/"],
  ["Better Call CLAUSE", "Adversarial contract review and legal citation", "Project describes 7,500+ perturbed contracts, but no public canonical dataset/scorer release was located.", "https://clause-legal.github.io/\nhttps://aclanthology.org/2026.findings-eacl.305/"],
  ["LeCoDe", "Multi-turn Chinese legal consultation", "Data/access boundary, license, exact judge, and conflicting clarification-recall values remain unresolved.", "https://github.com/PiLab-ZJU/LeCoDe\nhttps://arxiv.org/abs/2505.19667\nhttps://aclanthology.org/2026.acl-long.1667/"],
  ["Pro-Judice", "Procedural fairness and criminal-law reasoning", "Exact case count, language scope, data license, and scorer implementation are not yet pinned.", "https://github.com/CrexCheng/Pro-Judice\nhttps://journals.sagepub.com/doi/10.3233/FAIA251616"],
  ["JudiFair / LLMs on Trial", "Counterfactual robustness and judicial-decision fairness", "Repository may be a demonstration toolkit rather than the complete 177,100-case benchmark.", "https://github.com/KYSpring/ai_fairness_demo\nhttps://arxiv.org/abs/2507.10852\nhttps://iclr.cc/virtual/2026/poster/10010888"],
  ["DefGen-Bench", "Chinese criminal-defense opinion generation", "Only a sample is public; full data require contact and no clear license was verified.", "https://github.com/Statistical-NLP-Lab/DefGen-Bench\nhttps://aclanthology.org/2026.acl-long.1635/"],
  ["JurisBench", "Chinese civil-litigation breadth and workflow depth", "The ACL paper is detailed, but the official GitHub repository was empty at the cutoff.", "https://github.com/cza0927/JurisBench\nhttps://aclanthology.org/2026.acl-long.1666/"],
  ["LegDiff / SLeDoC", "Span-aware semantic comparison of legal text", "Dataset size, languages, label contract, metrics, and license remain incomplete.", "https://github.com/s-nlp/SLeDoC\nhttps://aclanthology.org/2026.acl-srw.86/"],
  ["LBOX OPEN", "Korean legal classification, prediction, and summarization", "Task identities, current maintenance, and license terms need a complete pass before merging with or separating from KCL.", "https://github.com/lbox-kr/lbox-open\nhttps://arxiv.org/abs/2206.05224\nhttps://proceedings.neurips.cc/paper_files/paper/2022/hash/d15abd14d5894eebd185b756541d420e-Abstract-Datasets_and_Benchmarks.html"],
  ["SCALE — One Law, Many Languages", "Multilingual Swiss legal reasoning", "Canonical code/data and the relationship among seven task datasets were not pinned; SCALE also collides with unrelated names.", "https://arxiv.org/abs/2306.09237"],
  ["AgentCourt / CourtBench", "Simulated Chinese civil litigation and agents", "Fixed benchmark boundary, released case set, scorer, and human-rating protocol need separation from simulation results.", "https://github.com/relic-yuexi/AgentCourt\nhttps://arxiv.org/abs/2408.08089\nhttps://aclanthology.org/2025.findings-acl.304/"],
  ["Australian legal QA and citation", "Australian QA, RAG, and citation prediction", "Identity relationship, synthetic-answer provenance, exact evaluator, and license/access need one canonical treatment.", "https://huggingface.co/datasets/isaacus/open-australian-legal-qa\nhttps://huggingface.co/datasets/isaacus/open-australian-legal-corpus\nhttps://arxiv.org/abs/2404.04302\nhttps://arxiv.org/abs/2412.06272"],
];

const notSeparateHeaders = ["Resource", "Decision", "Direct URLs"];
const notSeparateRows = [
  ["ILDC / CJPE", "Covered as an IL-TUR constituent task; a separate row would double-count the same Indian judgment-prediction evidence without a constituent hierarchy.", "https://github.com/Exploration-Lab/CJPE\nhttps://arxiv.org/abs/2105.13562"],
  ["CAIL2018 and later CAIL releases", "Source datasets and shared tasks already feed LawBench and FairLex; any future row must pin an edition, access, scorer, and license.", "https://github.com/china-ai-law-challenge\nhttps://arxiv.org/abs/1807.02478"],
  ["SCOTUS, EUR-LEX, and UNFAIR-ToS", "Kept inside LexGLUE instead of turning every constituent dataset into a top-level benchmark.", "https://github.com/coastalcph/lex-glue"],
  ["BillSum, Multi-LexSum, and CaseSumm", "Useful summarization datasets without one pinned evaluation contract for legal fidelity beyond reference-overlap baselines.", "https://huggingface.co/datasets/FiscalNote/billsum\nhttps://huggingface.co/datasets/allenai/multi_lexsum\nhttps://arxiv.org/abs/2501.00097"],
  ["legal-eval and MLEB bridge", "Mirrors or aggregations of existing benchmark identities, not new constructs.", "https://huggingface.co/datasets/nguha/legal-eval\nhttps://huggingface.co/datasets/isaacus/mleb-legal-rag-bench"],
  ["QwenClawBench, FormatBench, and HalluHard", "General agent, document-format, or hallucination benchmarks with legal examples or slices, not legal-specific evaluation populations.", "https://huggingface.co/datasets/skylenage-ai/QwenClawBench\nhttps://typeos.com/research/formatbench\nhttps://arxiv.org/abs/2602.01031"],
  ["PatentGPT and HUPD", "PatentGPT reports results on MoZIP rather than defining a separate PatentBench. HUPD is a large source dataset with benchmark tasks, but it is not the same multilingual IP instrument.", "https://arxiv.org/abs/2404.18255\nhttps://arxiv.org/abs/2207.04043\nhttps://arxiv.org/abs/2402.16389"],
];

const catalogEndRow = 4 + catalogRows.length;
const resourceEndRow = 4 + resourceRows.length;

const workbook = Workbook.create();
const summary = workbook.worksheets.add("Summary");
const catalogSheet = workbook.worksheets.add("Catalog");
const selectionSheet = workbook.worksheets.add("Selection Guide");
const metricSheet = workbook.worksheets.add("Metric Theory");
const sourceSheet = workbook.worksheets.add("Source Audit");
const resourceSheet = workbook.worksheets.add("Resource Check");
const watchlistSheet = workbook.worksheets.add("Watchlist");
const notSeparateSheet = workbook.worksheets.add("Not Separate");

const colors = {
  navy: "#17324D",
  teal: "#0F6B6D",
  tealLight: "#E8F6F5",
  blueLight: "#E8F0F5",
  grayLight: "#F5F7F9",
  amber: "#D97706",
  amberLight: "#FFF8EB",
  white: "#FFFFFF",
  text: "#1F2933",
  border: "#C7D2DA",
  link: "#0B5B8A",
};

function titleBlock(sheet, title, subtitle, lastColumn) {
  sheet.showGridLines = false;
  sheet.mergeCells(`A1:${lastColumn}1`);
  sheet.getRange("A1").values = [[title]];
  sheet.getRange(`A1:${lastColumn}1`).format = {
    fill: colors.navy,
    font: { bold: true, color: colors.white, size: 17 },
    verticalAlignment: "center",
  };
  sheet.getRange(`A1:${lastColumn}1`).format.rowHeight = 34;
  sheet.mergeCells(`A2:${lastColumn}2`);
  sheet.getRange("A2").values = [[subtitle]];
  sheet.getRange(`A2:${lastColumn}2`).format = {
    fill: colors.blueLight,
    font: { italic: true, color: "#3B5266", size: 10 },
    wrapText: true,
    verticalAlignment: "center",
  };
  sheet.getRange(`A2:${lastColumn}2`).format.rowHeight = 28;
}

function addTableSheet({ sheet, title, subtitle, headers, rows, lastColumn, tableName, widths, rowHeight = 72 }) {
  titleBlock(sheet, title, subtitle, lastColumn);
  sheet.getRange(`A4:${lastColumn}4`).values = [headers];
  sheet.getRangeByIndexes(4, 0, rows.length, headers.length).values = rows;
  const endRow = 4 + rows.length;
  const table = sheet.tables.add(`A4:${lastColumn}${endRow}`, true, tableName);
  table.style = "TableStyleMedium2";
  table.showHeaders = true;
  table.showFilterButton = true;
  table.showBandedRows = true;
  sheet.getRange(`A4:${lastColumn}4`).format = {
    fill: colors.teal,
    font: { bold: true, color: colors.white, size: 9 },
    wrapText: true,
    horizontalAlignment: "center",
    verticalAlignment: "center",
    borders: { preset: "outside", style: "thin", color: "#07494B" },
  };
  sheet.getRange(`A4:${lastColumn}4`).format.rowHeight = 38;
  sheet.getRange(`A5:${lastColumn}${endRow}`).format = {
    font: { color: colors.text, size: 8 },
    wrapText: true,
    verticalAlignment: "top",
    borders: {
      insideHorizontal: { style: "thin", color: "#DCE4E8" },
      bottom: { style: "thin", color: colors.border },
    },
  };
  sheet.getRange(`A5:${lastColumn}${endRow}`).format.rowHeight = rowHeight;
  widths.forEach((width, index) => {
    sheet.getRangeByIndexes(0, index, endRow, 1).format.columnWidth = width;
  });
  sheet.freezePanes.freezeRows(4);
  sheet.freezePanes.freezeColumns(2);
}

titleBlock(
  summary,
  "Awesome Legal Benchmarks — Curated Research Workbook",
  `Research snapshot ${catalog.as_of} · ${catalog.entries.length} canonical identities · all 22 original bullets mapped · all canonical URLs checked ${resourceSnapshot.checked_at}`,
  "H",
);
summary.getRange("A4:A11").values = [
  ["Canonical entries"], ["Original README bullets"], ["Canonical identities from original"],
  ["Curated additions"], ["Recommended"], ["Open access profiles"],
  ["Commercial-owner entries"], ["Verified canonical resource URLs"],
];
summary.getRange("B4").formulas = [[`=COUNTA(Catalog!$A$5:$A$${catalogEndRow})`]];
summary.getRange("B5").values = [[22]];
summary.getRange("B6").values = [[21]];
summary.getRange("B7").formulas = [[`=COUNTIF(Catalog!$AK$5:$AK$${catalogEndRow},\"Curated addition\")`]];
summary.getRange("B8").formulas = [[`=COUNTIF(Catalog!$H$5:$H$${catalogEndRow},\"recommended\")`]];
summary.getRange("B9").formulas = [[`=COUNTIF(Catalog!$N$5:$N$${catalogEndRow},\"open\")`]];
summary.getRange("B10").formulas = [[`=COUNTIF(Catalog!$F$5:$F$${catalogEndRow},\"yes\")`]];
summary.getRange("B11").formulas = [[`=COUNTIF('Resource Check'!$A$5:$A$${resourceEndRow},\"OK\")`]];
summary.getRange("A4:B11").format = {
  fill: colors.grayLight,
  font: { color: colors.navy },
  borders: { preset: "outside", style: "thin", color: colors.border },
  verticalAlignment: "center",
};
summary.getRange("A4:A11").format.font = { bold: true, color: colors.navy };
summary.getRange("B4:B11").format = { font: { bold: true, color: colors.teal, size: 13 }, horizontalAlignment: "right" };
summary.getRange("A4:A11").format.columnWidth = 34;
summary.getRange("B4:B11").format.columnWidth = 14;

summary.mergeCells("D4:H4");
summary.getRange("D4").values = [["How to use this workbook"]];
summary.getRange("D4:H4").format = { fill: colors.teal, font: { bold: true, color: colors.white } };
summary.mergeCells("D5:H8");
summary.getRange("D5").values = [["Start with the legal job, jurisdiction, source material, interface, and failure cost. Pair one public comparison set with a task-matched benchmark, a fresh private holdout, and human review of legally material failures. Resource Check verifies identity and availability—not scientific validity."]];
summary.getRange("D5:H8").format = { fill: colors.tealLight, font: { color: "#194B4D", size: 11 }, wrapText: true, verticalAlignment: "center", borders: { preset: "outside", style: "thin", color: "#8EC1BE" } };
summary.mergeCells("D9:H9");
summary.getRange("D9").values = [["Identity and reproducibility warnings"]];
summary.getRange("D9:H9").format = { fill: colors.amber, font: { bold: true, color: colors.white } };
summary.mergeCells("D10:H12");
summary.getRange("D10").values = [["MLEB bullets #3 and #20 are one identity. Harvey's current public files disagree at 1,671 versus 1,660 tasks. J1's paper says 508 tasks while its level counts total 538. Harvey, Legora, CoCoBench, GC AI, LegalOn, Ivo, legalbenchmarks.ai, and Vals use different private instruments and should not be merged into one vendor ranking."]];
summary.getRange("D10:H12").format = { fill: colors.amberLight, font: { color: "#5B3A05", size: 10 }, wrapText: true, verticalAlignment: "center", borders: { preset: "outside", style: "thin", color: "#E8C98F" } };
summary.getRange("D1:H12").format.columnWidth = 18;
summary.getRange("D5:H8").format.rowHeight = 25;
summary.getRange("D10:H12").format.rowHeight = 28;
summary.freezePanes.freezeRows(2);

addTableSheet({
  sheet: catalogSheet,
  title: "Canonical Catalog — Benchmarks, Datasets, Frameworks, and Related Resources",
  subtitle: "One row per canonical identity. Verified facts, inference, and unresolved ambiguity are kept separate; URLs are primary/official where located.",
  headers: catalogHeaders,
  rows: catalogRows,
  lastColumn: "AK",
  tableName: "CanonicalCatalogTable",
  widths: [20, 30, 28, 28, 16, 16, 22, 18, 18, 14, 48, 14, 48, 16, 24, 58, 44, 50, 28, 18, 42, 40, 38, 38, 60, 30, 40, 46, 46, 46, 48, 52, 52, 52, 58, 26, 18],
  rowHeight: 116,
});
catalogSheet.getRange(`B5:B${catalogEndRow}`).format.font = { bold: true, color: colors.navy, size: 9 };
catalogSheet.getRange(`J5:J${catalogEndRow}`).format.font = { bold: true, color: colors.teal, size: 8 };
catalogSheet.getRange(`L5:L${catalogEndRow}`).format.font = { bold: true, color: colors.teal, size: 8 };
catalogSheet.getRange(`K5:M${catalogEndRow}`).format.font = { color: colors.link, size: 8 };
catalogSheet.getRange(`AB5:AE${catalogEndRow}`).format.font = { color: colors.link, size: 8 };
catalogSheet.getRange(`H5:H${catalogEndRow}`).conditionalFormats.add("containsText", { text: "recommended", format: { fill: "#DDF3E5", font: { bold: true, color: "#17643A" } } });
catalogSheet.getRange(`H5:H${catalogEndRow}`).conditionalFormats.add("containsText", { text: "evaluate-carefully", format: { fill: "#FFF0D5", font: { bold: true, color: "#8A4E00" } } });
catalogSheet.getRange(`H5:H${catalogEndRow}`).conditionalFormats.add("containsText", { text: "related", format: { fill: "#EFE7F8", font: { bold: true, color: "#68418A" } } });
catalogSheet.getRange(`N5:N${catalogEndRow}`).conditionalFormats.add("containsText", { text: "private", format: { fill: "#FDE2E2", font: { bold: true, color: "#9B1C1C" } } });

addTableSheet({
  sheet: selectionSheet,
  title: "Possible Use Cases — Comparative Recommendation Matrix",
  subtitle: "Each row names the legal work, evidence to inspect, and decision the benchmark can inform. Open and owner-controlled signals remain separate.",
  headers: selectionHeaders,
  rows: selectionRows,
  lastColumn: "F",
  tableName: "SelectionGuideTable",
  widths: [30, 38, 42, 42, 52, 52],
  rowHeight: 76,
});
selectionSheet.getRange(`B5:B${4 + selectionRows.length}`).format.font = { bold: true, color: colors.navy, size: 9 };
selectionSheet.getRange(`F5:F${4 + selectionRows.length}`).format.font = { color: colors.link, size: 8 };

addTableSheet({
  sheet: metricSheet,
  title: "Metric Theory and Exact Scoring",
  subtitle: "Formulas are only the scoring layer; construct, sampling frame, interface, judge, aggregation, and uncertainty define the instrument.",
  headers: metricHeaders,
  rows: metricRows,
  lastColumn: "E",
  tableName: "MetricTheoryTable",
  widths: [22, 54, 42, 54, 56],
  rowHeight: 62,
});
metricSheet.getRange(`B5:B${4 + metricRows.length}`).format.font = { bold: true, color: colors.navy, size: 9 };

addTableSheet({
  sheet: sourceSheet,
  title: "Audit of Every Original README Bullet",
  subtitle: "22 rows, 21 identities. MLEB #3 and #20 are the same benchmark; blank artifacts are written as None rather than guessed.",
  headers: sourceAuditHeaders,
  rows: sourceAuditRows,
  lastColumn: "L",
  tableName: "SourceAuditTable",
  widths: [9, 30, 25, 42, 58, 38, 42, 42, 42, 44, 56, 44],
  rowHeight: 88,
});
sourceSheet.getRange("A5:A26").format.horizontalAlignment = "center";
sourceSheet.getRange("B5:B26").format.font = { bold: true, color: colors.navy, size: 9 };
sourceSheet.getRange("G5:I26").format.font = { color: colors.link, size: 8 };
sourceSheet.getRange("C5:C26").conditionalFormats.add("containsText", { text: "Duplicate", format: { fill: "#FDE2E2", font: { bold: true, color: "#9B1C1C" } } });

addTableSheet({
  sheet: resourceSheet,
  title: "Canonical Repository, Dataset, Paper, Leaderboard, and Project Check",
  subtitle: `${resourceSnapshot.summary.ok}/${resourceSnapshot.summary.total} unique URLs verified at ${resourceSnapshot.checked_at}; ${resourceSnapshot.summary.access_limited} were access-limited. API/HTTP availability verifies identity/access status, not scientific validity.`,
  headers: resourceHeaders,
  rows: resourceRows,
  lastColumn: "K",
  tableName: "ResourceCheckTable",
  widths: [10, 24, 54, 54, 30, 10, 28, 30, 28, 28, 28],
  rowHeight: 46,
});
resourceSheet.getRange(`A5:A${4 + resourceRows.length}`).conditionalFormats.add("containsText", { text: "OK", format: { fill: "#DDF3E5", font: { bold: true, color: "#17643A" } } });
resourceSheet.getRange(`C5:D${4 + resourceRows.length}`).format.font = { color: colors.link, size: 8 };
resourceSheet.getRange(`J5:J${4 + resourceRows.length}`).format.numberFormat = "yyyy-mm-dd hh:mm";

addTableSheet({
  sheet: watchlistSheet,
  title: "Watchlist — Promising but Not Yet Promoted",
  subtitle: "PLawBench and LegalCiteBench were promoted after primary artifacts were verified. These remaining candidates still lack a stable identity, release, scorer, license, or access boundary.",
  headers: watchlistHeaders,
  rows: watchlistRows,
  lastColumn: "D",
  tableName: "WatchlistTable",
  widths: [30, 42, 62, 58],
  rowHeight: 76,
});
watchlistSheet.getRange(`A5:A${4 + watchlistRows.length}`).format.font = { bold: true, color: colors.navy, size: 9 };
watchlistSheet.getRange(`D5:D${4 + watchlistRows.length}`).format.font = { color: colors.link, size: 8 };

addTableSheet({
  sheet: notSeparateSheet,
  title: "Known Resources Not Counted as Separate Benchmark Identities",
  subtitle: "Suite constituents, mirrors, dataset-only releases, and general benchmarks with a legal slice are recorded here to prevent silent omission and double counting.",
  headers: notSeparateHeaders,
  rows: notSeparateRows,
  lastColumn: "C",
  tableName: "NotSeparateTable",
  widths: [34, 74, 62],
  rowHeight: 82,
});
notSeparateSheet.getRange(`A5:A${4 + notSeparateRows.length}`).format.font = { bold: true, color: colors.navy, size: 9 };
notSeparateSheet.getRange(`C5:C${4 + notSeparateRows.length}`).format.font = { color: colors.link, size: 8 };

await fs.mkdir(outputDir, { recursive: true });
await fs.mkdir(previewDir, { recursive: true });

for (const sheetName of ["Summary", "Catalog", "Selection Guide", "Metric Theory", "Source Audit", "Resource Check", "Watchlist", "Not Separate"]) {
  const check = await workbook.inspect({
    kind: "table",
    range: `${sheetName}!A1:H12`,
    include: "values,formulas",
    tableMaxRows: 14,
    tableMaxCols: 8,
    maxChars: 3500,
  });
  console.log(`INSPECT ${sheetName}`);
  console.log(check.ndjson);
}

const errors = await workbook.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A",
  options: { useRegex: true, maxResults: 100 },
  summary: "final formula error scan",
});
console.log("ERROR_SCAN");
console.log(errors.ndjson);

const renderSpecs = [
  ["Summary", "A1:H12", "summary.png", 1.15],
  ["Catalog", "A1:O14", "catalog-identity-dates-access.png", 0.46],
  ["Catalog", "P1:AK12", "catalog-task-metrics-sources.png", 0.34],
  ["Selection Guide", `A1:F${4 + selectionRows.length}`, "selection-guide.png", 0.58],
  ["Metric Theory", "A1:E31", "metric-theory-core.png", 0.72],
  ["Metric Theory", `A28:E${4 + metricRows.length}`, "metric-theory-legal-benchmarks.png", 0.72],
  ["Source Audit", "A1:L16", "source-audit.png", 0.48],
  ["Resource Check", "A1:K18", "resource-check.png", 0.58],
  ["Resource Check", `A${Math.max(5, resourceEndRow - 20)}:K${resourceEndRow}`, "resource-check-tail.png", 0.58],
  ["Watchlist", `A1:D${4 + watchlistRows.length}`, "watchlist.png", 0.76],
  ["Not Separate", `A1:C${4 + notSeparateRows.length}`, "not-separate.png", 0.86],
];
for (const [sheetName, range, fileName, scale] of renderSpecs) {
  const preview = await workbook.render({ sheetName, range, scale, format: "png" });
  await fs.writeFile(path.join(previewDir, fileName), new Uint8Array(await preview.arrayBuffer()));
}

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);
console.log(`OUTPUT_PATH=${outputPath}`);
console.log(`PREVIEW_DIR=${previewDir}`);
