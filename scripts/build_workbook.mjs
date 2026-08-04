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
const evidence = (entry) => [
  `VERIFIED: ${join(entry.evidence.verified) || "None recorded"}`,
  `INFERENCE: ${join(entry.evidence.inference) || "None recorded"}`,
  `AMBIGUITY: ${join(entry.evidence.ambiguities) || "None recorded"}`,
].join("\n");

const catalogHeaders = [
  "ID",
  "Canonical Name",
  "Type",
  "Tier / Status",
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
  "Other Official URLs",
  "Access / License",
  "Maintenance / Reproducibility",
  "Leakage / Key Caveat",
  "Evidence Classification",
  "Original README Bullet(s)",
];

const catalogRows = catalog.entries.map((entry) => [
  entry.id,
  entry.name,
  entry.kind,
  statusLabel(entry),
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
  entry.source_readme_bullets.length
    ? join(entry.source_readme_bullets.map(String), ", ")
    : "Curated addition",
]);

const selectionHeaders = [
  "Use Case",
  "Primary Pick(s)",
  "Lead Metric",
  "Pair With / Hold Out",
  "Main Limitation",
  "Direct URL(s)",
];
const selectionRows = [
  ["Broad English legal NLU", "LexGLUE + LegalBench", "Per-task macro/micro-F1 or official task scorer", "Fresh matter-specific private set", "Public labels and heavy reuse make contamination likely.", "https://github.com/coastalcph/lex-glue\nhttps://github.com/HazyResearch/legalbench"],
  ["Broad Chinese legal ability", "LawBench + LexEval", "Accuracy/F1 by task; task-specific ROUGE-L", "Time-held-out current-law questions", "Public examinations and CAIL-derived data are highly contamination-prone.", "https://github.com/open-compass/LawBench\nhttps://github.com/CSHaitao/LexEval"],
  ["Multilingual European legal NLU", "LEXTREME", "Per-language/task macro-F1 + hierarchical harmonic score", "FairLex subgroup analysis", "Missing language-task cells and unequal scales complicate one-number comparisons.", "https://github.com/JoelNiklaus/LEXTREME\nhttps://github.com/coastalcph/fairlex"],
  ["Multilingual Indian legal work", "IL-TUR", "Every official task metric, split by language", "MILPaC practitioner translation ratings", "Eight tasks have different sizes and language coverage.", "https://github.com/Exploration-Lab/IL-TUR\nhttps://github.com/Law-AI/MILPaC"],
  ["Korean professional exams", "KCL", "MCQ accuracy + 2,905-point essay percentage", "Fresh Korean-counsel-reviewed questions", "Gemini 2.5 Flash judges essays and helped generate rubric candidates.", "https://github.com/lbox-kr/kcl"],
  ["Arabic / Saudi legal tasks", "ArabLegalEval + ALARB", "Accuracy/F1 by natural vs synthetic subset", "Human-authored jurisdiction-specific holdout", "Translation, synthetic generation, and model judging weaken validity.", "https://github.com/Thiqah/ArabLegalEval\nhttps://huggingface.co/datasets/THIQAH-RD/ALARB"],
  ["Contract clause extraction", "CUAD + ContractNLI + MAUD", "AUPR/Jaccard; NLI/evidence F1; macro/micro-F1", "Document-family-held-out target-practice contracts", "Boilerplate and public SEC agreements create near-duplicate leakage.", "https://github.com/The-Atticus-Project/cuad\nhttps://github.com/stanfordnlp/contract-nli\nhttps://github.com/TheAtticusProject/maud"],
  ["Contract clause retrieval", "ACORD", "nDCG@5/10 + graded precision@5", "New attorney-authored requests", "Only 114 queries; individual queries can move category scores materially.", "https://github.com/TheAtticusProject/acord"],
  ["Redlining / negotiation", "RedlineBench", "Official 12-cell weighted rubric + dimension scores", "Blind attorney review on unseen playbooks", "Rubrics, judge, and public scenarios are part of the instrument.", "https://github.com/crosbylegal/redline-bench"],
  ["Exact-support retrieval", "LegalBench-RAG", "Character precision and recall", "Document Recall@k + latency/cost", "Gold spans may not exhaust legally sufficient support; labels are public.", "https://github.com/zeroentropy-ai/legalbenchrag"],
  ["Statutory retrieval", "BSARD + RegLab", "Recall@k, MRR/MAP, downstream QA accuracy", "Current-law time-stamped holdout", "Static statutes and public bar questions can be stale or memorized.", "https://github.com/maastrichtlawtech/bsard\nhttps://reglab.github.io/legal-rag-benchmarks/"],
  ["Case retrieval", "LeCaRDv2 + COLIEE + CanLegalRAGBench", "nDCG/Recall@k + pool-depth disclosure", "Expert rejudging of unjudged top results", "Incomplete qrels can mark valid authority irrelevant.", "https://github.com/THUIR/LeCaRDv2\nhttps://coliee.org/COLIEE2025/overview\nhttps://github.com/NLP-UBC/CanLegalRAGBench"],
  ["End-to-end legal RAG", "Legal RAG Bench + CanLegalRAGBench + LLeQA", "Retrieval success + claim correctness/groundedness", "Independent review for omitted/current/controlling authority", "Judges mostly score precision, not professional completeness.", "https://github.com/isaacus-dev/legal-rag-bench\nhttps://github.com/NLP-UBC/CanLegalRAGBench\nhttps://github.com/maastrichtlawtech/lleqa"],
  ["Judgment / outcome prediction", "ECtHR + CaseHOLD", "Macro/micro-F1 or MCQ accuracy", "Strict chronology + pre-outcome input audit", "Later judgment language, headnotes, and citations can leak outcomes.", "https://huggingface.co/datasets/coastalcph/lex_glue\nhttps://github.com/neelguha/legal-ml-datasets"],
  ["Fairness / subgroup robustness", "FairLex", "Overall + per-group + worst-group + gap + confidence interval", "Domain-specific harm review", "Parity metrics do not define legal or normative fairness.", "https://github.com/coastalcph/fairlex"],
  ["Deontic / rule reasoning", "DeonticBench", "Accuracy + 1,000-replicate bootstrap interval + abstention", "Adversarial rule variants + private split", "Pin the post-audit Prolog/test revision; cases are public.", "https://github.com/guangyaodou/DeonticBench"],
  ["Legal agents and tools", "J1Bench + LegalAgentBench + APEX-Agents", "Process/outcome metrics + Pass@1/all-pass + tool failure", "Repeated runs + human review + unseen environment", "Harness, tools, simulator, and judge add variance.", "https://github.com/FudanDISC/J1Bench\nhttps://github.com/CSHaitao/LegalAgentBench\nhttps://github.com/Mercor-Intelligence/archipelago"],
  ["Legal translation", "SwiLTra-Bench + MILPaC + JUST-NLP 2025", "Named automatic metrics + legal-expert ratings", "Terminology/omission/enforceability error analysis", "BLEU/chrF++ similarity does not establish legal fidelity.", "https://github.com/JoelNiklaus/SwissLegalTranslations\nhttps://github.com/Law-AI/MILPaC\nhttps://www.codabench.org/competitions/10351/"],
  ["Current US legal answers/citations", "Open Legal-Answer Benchmark", "Must-include + citation support/in-range + cleanliness + authority", "Independent time-stamped questions + blind grading", "Sponsor-maintained, self-run, public, and only 54 canonical questions.", "https://github.com/Vaquill-AI/open-legal-answer-benchmark"],
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
  ["PLawBench", "Polish legal reasoning and knowledge", "Very recent; stable data/scorer/license and independent reproductions need confirmation.", "https://github.com/SKYLENAGE-AI/PLawBench\nhttps://arxiv.org/abs/2601.16669\nhttps://aclanthology.org/2026.acl-long.458/"],
  ["BenGER", "German legal benchmark platform", "Need a fixed, versioned task/data/scorer release separate from the mutable platform.", "https://github.com/SebastianNagl/benger-platform\nhttps://arxiv.org/abs/2605.28183\nhttps://what-a-benger.net/"],
  ["UA-Legal-Bench", "Ukrainian legal evaluation", "HF identifies v1 while the paper describes v2; canonical version relationship unresolved.", "https://huggingface.co/datasets/overthelex/ua-legal-bench\nhttps://arxiv.org/abs/2605.29170\nhttps://github.com/overthelex/secondlayer-papers"],
  ["Multi-Legal-Bench", "Large multilingual legal collection", "Public descriptions conflict at roughly 134M vs 122M records; scoring/reproducibility unclear.", "https://huggingface.co/datasets/overthelex/multi-legal-bench\nhttps://arxiv.org/abs/2605.29738"],
  ["LegalCiteBench", "Legal citation understanding and generation", "Very recent; release version, scorer, license, and citation-validity protocol need to stabilize.", "https://github.com/Sijia711/LegalCiteBench\nhttps://huggingface.co/datasets/legalcitebench/LegalCiteBench\nhttps://arxiv.org/abs/2605.10186"],
  ["Legal-DC", "Chinese legal document RAG", "Very recent; inspect final splits, official scorer, and leakage controls before promotion.", "https://github.com/legal-dc/Legal-DC\nhttps://arxiv.org/abs/2603.11772"],
  ["TW-LegalBench", "Taiwan/Traditional-Chinese legal evaluation", "Very recent; canonical source repository and stable evaluation code not located.", "https://huggingface.co/datasets/feiyuehchen/TW-LegalBench\nhttps://arxiv.org/abs/2606.18699"],
  ["Legal Rikai Open Benchmark", "Japanese legal evaluation", "Gated, nonstandard license metadata, and only about 100 exposed samples.", "https://huggingface.co/datasets/legalontech/Legal-Rikai-Open-Benchmark\nhttps://arxiv.org/abs/2512.11297"],
];

const workbook = Workbook.create();
const summary = workbook.worksheets.add("Summary");
const catalogSheet = workbook.worksheets.add("Catalog");
const selectionSheet = workbook.worksheets.add("Selection Guide");
const metricSheet = workbook.worksheets.add("Metric Theory");
const sourceSheet = workbook.worksheets.add("Source Audit");
const resourceSheet = workbook.worksheets.add("Resource Check");
const watchlistSheet = workbook.worksheets.add("Watchlist");

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
  `Research snapshot ${catalog.as_of} · 45 canonical entries · all 22 original bullets mapped · all canonical URLs checked ${resourceSnapshot.checked_at}`,
  "H",
);
summary.getRange("A4:A11").values = [
  ["Canonical entries"], ["Original README bullets"], ["Canonical identities from original"],
  ["Curated additions"], ["Recommended"], ["Public benchmark/suite/shared-task"],
  ["Related/non-comparable"], ["Verified canonical resource URLs"],
];
summary.getRange("B4").formulas = [["=COUNTA(Catalog!$A$5:$A$49)"]];
summary.getRange("B5").values = [[22]];
summary.getRange("B6").values = [[21]];
summary.getRange("B7").formulas = [["=COUNTIF(Catalog!$X$5:$X$49,\"Curated addition\")"]];
summary.getRange("B8").formulas = [["=COUNTIF(Catalog!$D$5:$D$49,\"recommended / active\")+COUNTIF(Catalog!$D$5:$D$49,\"recommended / annual\")+COUNTIF(Catalog!$D$5:$D$49,\"recommended / fixed-release\")"]];
summary.getRange("B9").formulas = [["=COUNTIF(Catalog!$C$5:$C$49,\"benchmark\")+COUNTIF(Catalog!$C$5:$C$49,\"benchmark-suite\")+COUNTIF(Catalog!$C$5:$C$49,\"shared-task\")"]];
summary.getRange("B10").formulas = [["=COUNTIF(Catalog!$D$5:$D$49,\"related / active\")+COUNTIF(Catalog!$D$5:$D$49,\"related / fixed-release\")+COUNTIF(Catalog!$D$5:$D$49,\"related / private\")"]];
summary.getRange("B11").formulas = [[`=COUNTIF('Resource Check'!$A$5:$A$${4 + resourceRows.length},\"OK\")`]];
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
summary.getRange("D5").values = [["Choose benchmarks by the deployment task and jurisdiction, then pair a public benchmark with a task-specific set and a fresh private holdout. Read Metric Theory before interpreting a score. Resource Check proves that a canonical URL responded on the audit date; it does not prove scientific validity."]];
summary.getRange("D5:H8").format = { fill: colors.tealLight, font: { color: "#194B4D", size: 11 }, wrapText: true, verticalAlignment: "center", borders: { preset: "outside", style: "thin", color: "#8EC1BE" } };
summary.mergeCells("D9:H9");
summary.getRange("D9").values = [["Identity and reproducibility warnings"]];
summary.getRange("D9:H9").format = { fill: colors.amber, font: { bold: true, color: colors.white } };
summary.mergeCells("D10:H12");
summary.getRange("D10").values = [["MLEB bullets #3 and #20 are one identity. J1's paper says 508 tasks but 160+186+192=538. LegalBench-RAG reports 6,858 vs 6,889 queries. ContractEval reports 4,128 vs 4,182 rows. Gated HF resources are valid links but are not frictionless public access."]];
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
  lastColumn: "X",
  tableName: "CanonicalCatalogTable",
  widths: [20, 28, 20, 22, 42, 48, 28, 22, 40, 38, 38, 38, 54, 28, 40, 42, 42, 42, 42, 44, 48, 48, 56, 18],
  rowHeight: 100,
});
catalogSheet.getRange("B5:B49").format.font = { bold: true, color: colors.navy, size: 9 };
catalogSheet.getRange("P5:S49").format.font = { color: colors.link, size: 8 };
catalogSheet.getRange("D5:D49").conditionalFormats.add("containsText", { text: "recommended", format: { fill: "#DDF3E5", font: { bold: true, color: "#17643A" } } });
catalogSheet.getRange("D5:D49").conditionalFormats.add("containsText", { text: "evaluate-carefully", format: { fill: "#FFF0D5", font: { bold: true, color: "#8A4E00" } } });
catalogSheet.getRange("D5:D49").conditionalFormats.add("containsText", { text: "related", format: { fill: "#EFE7F8", font: { bold: true, color: "#68418A" } } });

addTableSheet({
  sheet: selectionSheet,
  title: "Comparative Recommendation Matrix",
  subtitle: "Use a portfolio, not a single score: public comparability + construct fit + a fresh private holdout.",
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
  subtitle: "Recency, version ambiguity, gating, missing code/scorer, or internal inconsistency prevents a stronger reproducibility label in this snapshot.",
  headers: watchlistHeaders,
  rows: watchlistRows,
  lastColumn: "D",
  tableName: "WatchlistTable",
  widths: [30, 42, 62, 58],
  rowHeight: 76,
});
watchlistSheet.getRange(`A5:A${4 + watchlistRows.length}`).format.font = { bold: true, color: colors.navy, size: 9 };
watchlistSheet.getRange(`D5:D${4 + watchlistRows.length}`).format.font = { color: colors.link, size: 8 };

await fs.mkdir(outputDir, { recursive: true });
await fs.mkdir(previewDir, { recursive: true });

for (const sheetName of ["Summary", "Catalog", "Selection Guide", "Metric Theory", "Source Audit", "Resource Check", "Watchlist"]) {
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
  ["Catalog", "A1:X14", "catalog.png", 0.42],
  ["Selection Guide", "A1:F23", "selection-guide.png", 0.62],
  ["Metric Theory", "A1:E31", "metric-theory.png", 0.72],
  ["Source Audit", "A1:L16", "source-audit.png", 0.48],
  ["Resource Check", "A1:K18", "resource-check.png", 0.58],
  ["Resource Check", "A73:K95", "resource-check-leaderboards-papers.png", 0.58],
  ["Resource Check", "A132:K151", "resource-check-papers-projects.png", 0.58],
  ["Watchlist", "A1:D12", "watchlist.png", 0.82],
];
for (const [sheetName, range, fileName, scale] of renderSpecs) {
  const preview = await workbook.render({ sheetName, range, scale, format: "png" });
  await fs.writeFile(path.join(previewDir, fileName), new Uint8Array(await preview.arrayBuffer()));
}

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);
console.log(`OUTPUT_PATH=${outputPath}`);
console.log(`PREVIEW_DIR=${previewDir}`);
