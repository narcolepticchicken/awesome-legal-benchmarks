# Agents and legal workflows

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Tool use, process compliance, simulated legal work, and long-horizon professional tasks.

Snapshot: **2026-08-05** · 11 entries

[Back to README](../../README.md) · [Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)

## On this page

- [LegalAgentBench](#legalagentbench)
- [Ready Jurist One (J1Bench)](#ready-jurist-one)
- [Harvey Legal Agent Benchmark (LAB)](#harvey-lab)
- [Mercor APEX-Agents — Corporate Lawyer](#apex-agents-corporate-law)
- [DLawBench](#dlawbench)
- [Harvey BigLaw Bench](#harvey-biglaw-bench)
- [Legora Benchmark for Agentic Reasoning (BAR)](#legora-bar)
- [GC AI In-House Legal Bench](#gc-ai-in-house-legal-bench)
- [Thomson Reuters CoCoBench](#thomson-reuters-cocobench)
- [Realm Legal Reasoning](#realm-legal-reasoning)
- [CourtReasoner](#courtreasoner)

<a id="legalagentbench"></a>
## LegalAgentBench

`legalagentbench` · **benchmark** · **specialist** · fixed-release

Chinese legal tool use, multi-hop information gathering, and legal writing.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | LegalAgentBench authors (academic) |
| Catalog geography | China |
| First recorded public event | [2024-12-23](https://arxiv.org/abs/2412.17259) — arXiv v1 submission |
| Latest verified event | [2026-04-10](https://github.com/CSHaitao/LegalAgentBench) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Compare agent frameworks on Chinese legal multi-hop tool use across 17 corpora, 37 tools, and 300 tasks.
- Test tool selection and sequencing (progress rate) separately from final-answer keyword success.
- Research agent planning behavior in a legal tool environment.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Success and progress scores estimate whether an agent selects and sequences tools toward a task; BERTScore assesses writing similarity, but neither alone proves legal correctness. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 17 corpora, 37 tools, 300 tasks |
| Splits | Tasks span one-to-five-hop and writing categories |
| Source material | Chinese legal corpora wrapped as tools and authored tasks |
| Input | Natural-language task plus tool environment |
| Output | JSON tool calls and a final legal answer or document |
| Baselines / leaderboard context | Paper compares multiple LLM agents and prompting configurations. |
| Dataset access | Public code, data, prompts, and environment |
| License | MIT repository |
| Gating | Model/API credentials may be needed to run baselines |
| Maintenance | Fixed research release. |
| Reproducibility | Harness is public; API model drift and environment dependencies still affect trajectories. |

### Metrics

- **Keyword success rate / progress rate:** Rule-based matching of required milestones and final keywords across task trajectories. **Primary.**
- **BERTScore:** Contextual token similarity for generated legal writing; token use is also reported.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/CSHaitao/LegalAgentBench](https://github.com/CSHaitao/LegalAgentBench) |
| Hugging Face | None located |
| Paper / arXiv | [https://arxiv.org/abs/2412.17259](https://arxiv.org/abs/2412.17259) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Keyword graders can be gamed without producing a legally adequate result.
- Public solutions and tool corpora permit benchmark-specific planning.

**Verified facts**
- Official repository specifies 17 corpora, 37 tools, and 300 tasks.

**Inference**
- Use as a tool-use benchmark with legal grounding checks, not as proof of deployable lawyering.

Original source bullet(s): #10

[Back to page index](#on-this-page)

<a id="ready-jurist-one"></a>
## Ready Jurist One (J1Bench)

`ready-jurist-one` · **benchmark** · **specialist** · active

Operate interactively in Chinese legal consultation, drafting, civil-court, and criminal-court environments.

**Also known as:** Ready Jurist One, J1Bench, J1-ENVS, J1-EVAL

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | FudanDISC (academic) |
| Catalog geography | China |
| First recorded public event | [2025-07-05](https://arxiv.org/abs/2507.04037) — arXiv v1 submission |
| Latest verified event | [2026-04-07](https://github.com/FudanDISC/J1Bench) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test interactive performance in simulated Chinese consultation, drafting, civil-court, and criminal-court environments.
- Score outcomes and process separately — formats, procedural stages, reasoning, cited law — when evaluating Chinese legal agents.
- Research process-oriented evaluation design for multi-turn legal agents.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | J1-EVAL uses dual outcome- and process-oriented scoring so an agent must reach the right result and follow required procedural steps, formats, reasoning, and citation constraints. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | Paper reports 508 environments across six scenarios and three levels |
| Splits | Scenario/level-specific interactive environments |
| Source material | Chinese judgments and legal articles, structured into role-based environments |
| Input | Multi-turn role interactions, facts, and procedural state |
| Output | Answers, complaints/defences, courtroom actions, reasons, citations, and judgments |
| Baselines / leaderboard context | Official paper evaluates 17 general, open, and legal-specific agents; OpenCompass integration is linked. |
| Dataset access | Public code/data links |
| License | No clear repository license was visible in the primary GitHub page |
| Gating | API models and significant compute may be required |
| Maintenance | Active ACL 2026 release. |
| Reproducibility | Harness and data are public, but simulator/judge model drift and stochastic multi-agent interaction require repeated trials. |

### Metrics

- **Outcome-oriented scores:** Binary/non-binary answer score, component document score, judgment score, crime accuracy, and normalized-log penalty deviation. Judge: Rule-based plus task-specific LLM judges. **Primary.**
- **Process-oriented scores:** Format following, procedural stage completeness, reasoning quality, and cited-law precision; except procedural completeness, metrics use explicit references. Judge: Rule-based plus task-specific LLM judges. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/FudanDISC/J1Bench](https://github.com/FudanDISC/J1Bench) |
| Hugging Face | [https://huggingface.co/datasets/CimoInkPool/J1-Eval_Dataset](https://huggingface.co/datasets/CimoInkPool/J1-Eval_Dataset) |
| Paper / arXiv | [https://arxiv.org/abs/2507.04037](https://arxiv.org/abs/2507.04037)<br>[https://aclanthology.org/2026.acl-long.471/](https://aclanthology.org/2026.acl-long.471/) |
| Leaderboard / competition | [https://hub.opencompass.org.cn/dataset-detail/J1Bench](https://hub.opencompass.org.cn/dataset-detail/J1Bench) |
| Project | [https://j1bench.github.io/](https://j1bench.github.io/) |

### Validity and evidence

**Risks / caveats**
- LLM-driven roles and judges can create correlated simulator/evaluator bias.
- The paper states 508 total but lists 160 + 186 + 192 = 538 level instances; this arithmetic conflict is unresolved.

**Verified facts**
- Official GitHub/project/paper define six scenarios and the dual metric table.

**Unresolved ambiguity**
- Reported total and per-level counts conflict; licensing is unclear.

**Related entries**

- [JuDGE](reasoning-education.md#judge)

[Back to page index](#on-this-page)

<a id="harvey-lab"></a>
## Harvey Legal Agent Benchmark (LAB)

`harvey-lab` · **benchmark** · **check before use** · active

Complete long-horizon legal matters using files, research, analysis, drafting, and validation tools.

**Also known as:** Legal Agent Benchmark, LAB, Harvey LAB

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Harvey (company; commercial interest) |
| Catalog geography | United States |
| First recorded public event | [2026-05-06](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark) — Official launch post |
| Latest verified event | [2026-08-03](https://github.com/harveyai/harvey-labs) — GitHub repository push |
| Access level | partial |
| Test labels | mixed |
| Independently runnable | partial |

### Possible use cases

- Run Harvey's public task set and harness to test long-horizon matter completion under expert rubrics, reporting all-pass and rubric pass rates with cost and latency.
- Read Harvey's published holdout results as the vendor's own frontier-model comparison on its own instrument.
- Adapt the expert-rubric and all-pass protocol when designing an internal matter-level holdout.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | All-pass treats legal work as conjunctive reliability: a task passes only if every required expert rubric criterion passes; rubric pass rate exposes partial completion but is not the headline autonomy threshold. |
| Jurisdiction | United States / commercial legal practice, mixed practice areas |
| Languages | English |
| Size | Launch: 1,200+ tasks, 24 practice areas, and 75,000+ criteria; current main README badge reports 1,671 tasks while the evaluation-methodology page reports 1,660 tasks and about 101,000 criteria |
| Splits | Public task set plus Harvey's separate private holdout used for published model results |
| Source material | Synthetic client matters and expert-curated instructions, files, outputs, and rubrics |
| Input | Matter instruction and sandboxed document/file environment |
| Output | Research, analysis, and professional work-product artifacts |
| Baselines / leaderboard context | Harvey publishes frontier-model holdout results; public tasks/harness allow community runs but are not identical to the holdout. |
| Dataset access | Public tasks and harness; published headline holdout is private |
| License | MIT |
| Gating | Running agents/judges requires model access and compute |
| Maintenance | Rapidly evolving vendor-maintained benchmark. |
| Reproducibility | Public harness is reproducible in principle; headline holdout scores cannot be independently reproduced and model/judge versions change. |

### Metrics

- **All-pass rate:** A task receives 1 only when every applicable equally weighted binary criterion passes; mean across tasks. The optional dual profile averages per-judge task values and separately requires both judges for strict all-pass. Judge: Default Claude Sonnet 4.6 at temperature 0; optional dual Claude Sonnet 4.6 + GPT-5.5. **Primary.**
- **Criterion pass rate:** Report both macro average of task-level criterion-pass fractions and pooled passed criteria divided by total criteria; also report cost and latency. Judge: Default Claude Sonnet 4.6 at temperature 0; optional dual profile.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/harveyai/harvey-labs](https://github.com/harveyai/harvey-labs) |
| Hugging Face | None located |
| Paper / arXiv | None located |
| Leaderboard / competition | None located |
| Project | [https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)<br>[https://www.harvey.ai/blog/legal-agent-benchmark-initial-results](https://www.harvey.ai/blog/legal-agent-benchmark-initial-results)<br>[https://github.com/harveyai/harvey-labs/tree/v1.0](https://github.com/harveyai/harvey-labs/tree/v1.0)<br>[https://github.com/harveyai/harvey-labs/blob/main/docs/eval-strategies.md](https://github.com/harveyai/harvey-labs/blob/main/docs/eval-strategies.md) |

### Validity and evidence

**Risks / caveats**
- Benchmark owner is a legal-AI vendor and publishes results on a private mirror holdout.
- All-pass is sensitive to rubric granularity and judge false negatives; a single criterion zeroes the task.
- The rolling main branch is mutable; the README badge currently says 1,671 tasks while the methodology page says 1,660.

**Verified facts**
- Official GitHub and Harvey posts define the harness, expert rubrics, all-pass, criterion-pass, default judge, optional dual-judge profile, and public/private boundary.

**Unresolved ambiguity**
- The evolving public task count should be read from a pinned release rather than a timeless number; two official files on main disagree by 11 tasks.

**Related entries**

- [Realm Legal Reasoning](agents-workflows.md#realm-legal-reasoning)
- [OAB-Bench](reasoning-education.md#oab-bench)

[Back to page index](#on-this-page)

<a id="apex-agents-corporate-law"></a>
## Mercor APEX-Agents — Corporate Lawyer

`apex-agents-corporate-law` · **benchmark** · **check before use** · active

Complete realistic long-horizon corporate-law tasks across applications, files, and professional work environments.

**Also known as:** APEX-Agents — Corporate Lawyer, APEX Corporate Lawyer Agent

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Mercor (company; commercial interest) |
| Catalog geography | Evaluation population not published |
| First recorded public event | [2026-01-20](https://arxiv.org/abs/2601.14242) — arXiv v1 submission |
| Latest verified event | [2026-08-04](https://github.com/Mercor-Intelligence/archipelago) — GitHub repository push |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test cross-application corporate-law task completion on Mercor's 160-task slice across 12 simulated work environments.
- Compare agent stacks on pass@1 for realistic professional deliverables with files and rubrics.
- Protocol reference for file-and-application-grounded legal agent evaluation.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Pass@1 measures single-run task completion against multiple criteria; the legal slice tests workflow execution, not legal knowledge in isolation. |
| Jurisdiction | Corporate-law practice / mixed |
| Languages | English |
| Size | 480 total APEX tasks, including 160 corporate-law tasks across 12 worlds |
| Splits | Role-specific public benchmark and leaderboard evaluations |
| Source material | Tasks authored by corporate lawyers, consultants, and bankers with files, rubrics, and gold outputs |
| Input | Professional task plus realistic multi-file application world |
| Output | Cross-application actions and completed professional artifact |
| Baselines / leaderboard context | Official Mercor leaderboard compares agent/model configurations by professional role. |
| Dataset access | Public HF benchmark including prompts, rubrics, gold outputs, files, and metadata |
| License | See dataset/harness repositories |
| Gating | Substantial agent infrastructure/model access required |
| Maintenance | Active Mercor professional-agent benchmark. |
| Reproducibility | Public benchmark and harness support reruns, but desktop/application state and model endpoints must be pinned. |

### Metrics

- **Pass@1:** Fraction of tasks passed on one evaluated trajectory under task rubrics. Judge: Archipelago task graders / rubric evaluation. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/Mercor-Intelligence/archipelago](https://github.com/Mercor-Intelligence/archipelago) |
| Hugging Face | [https://huggingface.co/datasets/mercor/apex-agents](https://huggingface.co/datasets/mercor/apex-agents) |
| Paper / arXiv | [https://arxiv.org/abs/2601.14242](https://arxiv.org/abs/2601.14242) |
| Leaderboard / competition | [https://www.mercor.com/apex/apex-agents-leaderboard/corporate-lawyer-agent/](https://www.mercor.com/apex/apex-agents-leaderboard/corporate-lawyer-agent/) |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Only one third of APEX is legal; aggregate APEX scores are not legal scores.
- Public gold outputs/rubrics permit targeted agent tuning.

**Verified facts**
- Official paper/HF/leaderboard identify 480 total and a 160-task corporate-law slice.

**Unresolved ambiguity**
- Jurisdiction varies by authored task and is not summarized as one national corpus.

[Back to page index](#on-this-page)

<a id="dlawbench"></a>
## DLawBench

`dlawbench` · **benchmark** · **recommended** · active

Conduct multi-turn legal consultations and turn elicited facts into a reasoned legal memorandum.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | DLawBench authors / SKYLENAGE-AI (mixed; commercial interest unclear) |
| Catalog geography | Multi-jurisdiction and supranational |
| First recorded public event | [2026-06-09](https://github.com/SKYLENAGE-AI/DLawBench) — GitHub repository creation |
| Latest verified event | [2026-06-11](https://arxiv.org/abs/2606.13931) — arXiv v1 submission |
| Access level | open |
| Test labels | public |
| Independently runnable | yes |

### Possible use cases

- Test whether a legal agent elicits missing facts during multi-turn consultations before producing a final memorandum.
- Compare China and US consultation performance while keeping jurisdiction-level scores separate.
- Diagnose fact coverage, inquiry quality, issue resolution, and fidelity rather than relying on one answer score.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Separate fact, inquiry, resolution, and fidelity rubrics test whether an agent discovers legally material facts and resolves issues across a dialogue. |
| Jurisdiction | China, United States |
| Languages | Chinese, English |
| Size | 461 cases: 264 Chinese and 197 US; 5,532 paired facts, 3,411 inquiry rubrics, and 3,348 issue-resolution rubrics |
| Splits | Official case files and evaluator artifacts |
| Source material | Case-style legal consultations with client beliefs, court facts, and personas |
| Input | Client opening, persona, hidden/known facts, and multi-turn dialogue |
| Output | Consultation dialogue and final legal memorandum |
| Baselines / leaderboard context | Paper evaluates leading general and reasoning models on both jurisdictions. |
| Dataset access | Public repository |
| License | MIT code; CC BY 4.0 data |
| Gating | None observed |
| Maintenance | Active 2026 research release; pin repository commit and evaluator model. |
| Reproducibility | Public data and evaluation code are available; scores still depend on the selected judge and stochastic sessions. |

### Metrics

- **Fact, inquiry, resolution, and fidelity scores:** Session-level Fact Coverage, Inquiry, Elicitation, Fact Resolution, Issue Resolution, Resolution, and Fidelity scores; available jurisdictions are averaged equally. Judge: User-supplied evaluation model via --eval-model; no universal default is fixed. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/SKYLENAGE-AI/DLawBench](https://github.com/SKYLENAGE-AI/DLawBench) |
| Hugging Face | None located |
| Paper / arXiv | [https://arxiv.org/abs/2606.13931](https://arxiv.org/abs/2606.13931) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Public cases and rubrics permit direct optimization.
- Changing the evaluation model changes the instrument.
- Equal jurisdiction averaging can hide different case counts and difficulty.

**Verified facts**
- The official repository and arXiv paper report 461 bilingual cases and the named rubric families.

**Inference**
- This is one of the stronger public complements to private matter-level agent benchmarks.

**Unresolved ambiguity**
- The canonical judge model is not fixed across runs.

**Related entries**

- [Realm Legal Reasoning](agents-workflows.md#realm-legal-reasoning)

[Back to page index](#on-this-page)

<a id="harvey-biglaw-bench"></a>
## Harvey BigLaw Bench

`harvey-biglaw-bench` · **private-benchmark** · **check before use** · private

Complete transactional and litigation research, drafting, retrieval, and long-document tasks.

**Also known as:** BigLaw Bench, BLB

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Harvey (company; commercial interest) |
| Catalog geography | United States |
| First recorded public event | [2024-08-29](https://www.harvey.ai/blog/introducing-biglaw-bench) — Official launch post |
| Latest verified event | [2026-03-17](https://github.com/harveyai/biglaw-bench) — GitHub repository push |
| Access level | partial |
| Test labels | mixed |
| Independently runnable | partial |

### Possible use cases

- Inspect Harvey's earlier rubric framework for transactional, litigation, research, drafting, and long-document work.
- Use Answer Score and Source Score separately when designing evaluation for substantive quality and evidentiary support.
- Treat Harvey's published results as vendor evidence, not as a cross-benchmark rank against LAB or Legora BAR.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Positive and negative weighted rubric criteria measure expected answer content and prohibited failure modes; a separate source score measures evidentiary support. |
| Jurisdiction | Primarily United States; later extensions described broader coverage |
| Languages | English |
| Size | Full corpus size is not publicly released |
| Splits | Public samples and appendix; private full evaluation materials |
| Source material | Prompt/document pairs modeled on legal time entries and BigLaw workflows |
| Input | Legal task prompt plus source documents |
| Output | Research answer, analysis, draft, or long-document work product |
| Baselines / leaderboard context | Harvey published model comparisons and later research/global extensions; no independent official live leaderboard exists. |
| Dataset access | Public samples and methodology; full benchmark private |
| License | No SPDX license declared in the repository |
| Gating | Full dataset and resources are not openly downloadable |
| Maintenance | Earlier Harvey benchmark family still documented; LAB is a separate newer instrument, not a rename. |
| Reproducibility | Partial for published samples; low for full vendor scores because data and evaluator details are not fully public. |

### Metrics

- **Answer Score:** Sum earned positive points and negative-criterion penalties, divided by total available positive points; report the pinned rubric set. Judge: Rubric-based evaluator described by Harvey; exact current model configuration is not fully public. **Primary.**
- **Source Score:** Separately measures whether claims are supported by supplied or retrieved sources. Judge: Evaluator configuration not fully public.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/harveyai/biglaw-bench](https://github.com/harveyai/biglaw-bench) |
| Hugging Face | None located |
| Paper / arXiv | None located |
| Leaderboard / competition | None located |
| Project | [https://www.harvey.ai/blog/introducing-biglaw-bench](https://www.harvey.ai/blog/introducing-biglaw-bench)<br>[https://www.harvey.ai/blog/expanding-big-law-bench](https://www.harvey.ai/blog/expanding-big-law-bench)<br>[https://www.harvey.ai/blog/introducing-big-law-bench-global](https://www.harvey.ai/blog/introducing-big-law-bench-global)<br>[https://www.harvey.ai/blog/introducing-big-law-bench-research](https://www.harvey.ai/blog/introducing-big-law-bench-research) |

### Validity and evidence

**Risks / caveats**
- Harvey owns the benchmark and sells a product evaluated by it.
- The full task set is private and the repository has no clear license.
- BigLaw Bench, LAB, and BAR use different tasks, judges, and aggregation and cannot share one leaderboard.

**Verified facts**
- Harvey's official posts and GitHub repository establish BigLaw Bench as a distinct benchmark family predating LAB.

**Unresolved ambiguity**
- Current operating status alongside LAB and the exact full-corpus size are not publicly resolved.

[Back to page index](#on-this-page)

<a id="legora-bar"></a>
## Legora Benchmark for Agentic Reasoning (BAR)

`legora-bar` · **private-benchmark** · **check before use** · private

Complete multi-step legal matters using source documents and produce professional files or chat answers.

**Also known as:** Legora BAR, Benchmark for Agentic Reasoning

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Legora (company; commercial interest) |
| Catalog geography | Evaluation population not published |
| First recorded public event | [2025-09-09](https://legora.com/bar) — Official page's displayed original publication date |
| Latest verified event | [2026-07-28](https://legora.com/bar) — Official page's displayed updated date |
| Access level | private |
| Test labels | hidden |
| Independently runnable | no |

### Possible use cases

- Read Legora's results as vendor evidence about long-horizon legal work across research, drafting, redlining, and analysis.
- Inspect the synthetic public tax case to understand BAR's native-file and granular-rubric design.
- Borrow the matter-room, repeated-run, and weighted-criterion structure for a private law-firm evaluation.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Partner- and engineer-authored matter cases use weighted binary criteria for factual coverage, analysis, citations, and recommendations across repeated agent runs. |
| Jurisdiction | Multiple; exact distribution not publicly enumerated |
| Languages | English |
| Size | BAR subset described as hundreds of cases; broader Legora corpus reports 5,161 cases, 11,075 documents, and 28 practice areas |
| Splits | Private benchmark; one fully synthetic public tax example with 175 graded criteria |
| Source material | Partner and in-house engineer-authored matters and file rooms; client/IP-sensitive corpus |
| Input | Matter prompt plus PDFs, Word documents, spreadsheets, and other source files |
| Output | PDF, Word document, spreadsheet, redline, or chat answer |
| Baselines / leaderboard context | Official page reports vendor-run model and product comparisons; no independently runnable public leaderboard exists. |
| Dataset access | Private; one synthetic example is public |
| License | Apache-2.0 for the public sample repository; private corpus terms undisclosed |
| Gating | Full benchmark is not available for independent execution |
| Maintenance | Active private benchmark; official page displayed an update on 2026-07-28. |
| Reproducibility | Low for the full benchmark because data, judge, prompts, and calibration are private; the single sample is inspectable. |

### Metrics

- **Weighted quality-rubric score:** High-, medium-, and low-weight binary criteria are judged for three repeated runs; report criterion and task aggregation under Legora's private protocol. Judge: LLM-as-judge; exact model, prompt, and calibration are undisclosed. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/legora-oss/legora-bar-tax-case](https://github.com/legora-oss/legora-bar-tax-case) |
| Hugging Face | None located |
| Paper / arXiv | None located |
| Leaderboard / competition | None located |
| Project | [https://legora.com/bar](https://legora.com/bar) |

### Validity and evidence

**Risks / caveats**
- Legora owns the instrument and sells a system evaluated by it.
- The broader 5,161-case corpus must not be misreported as the BAR subset size.
- Private tasks and an undisclosed judge prevent independent score reproduction.
- Results are not directly comparable with Harvey LAB or other agent benchmarks.

**Verified facts**
- Legora's official page describes BAR, the broader corpus, repeated runs, weighted rubrics, and private access; the official GitHub organization publishes one synthetic example.

**Inference**
- The public example demonstrates the format, not benchmark representativeness.

**Unresolved ambiguity**
- Exact BAR case count, jurisdiction mix, judge model, prompt, calibration, and aggregation formula are not public.
- The page displays July 28, 2026 as updated, while its page-build metadata indicates a later August 4 publication event; the meaning of those dates differs.

[Back to page index](#on-this-page)

<a id="gc-ai-in-house-legal-bench"></a>
## GC AI In-House Legal Bench

`gc-ai-in-house-legal-bench` · **private-benchmark** · **check before use** · private

Complete common in-house legal drafting, analysis, research, strategy, extraction, regulatory, and checklist tasks.

**Also known as:** In-House Legal Bench

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | GC AI (company; commercial interest) |
| Catalog geography | United States |
| First recorded public event | [2026-05-15](https://gc.ai/blog/in-house-legal-bench-evaluating-ai-assistants-for-in-house-legal-work) — Official publication date |
| Latest verified event | [2026-06-05](https://gc.ai/blog/in-house-legal-bench-evaluating-ai-assistants-for-in-house-legal-work) — Official displayed update date |
| Access level | partial |
| Test labels | mixed |
| Independently runnable | partial |

### Possible use cases

- Inspect a 100-task taxonomy for in-house drafting, research, strategy, extraction, regulatory work, and checklists.
- Use the public examples to prototype atomic criteria for an internal legal-department holdout.
- Read published model results as GC AI's vendor-run evidence, with judge agreement and private-task limits disclosed.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Attorney-authored binary criteria measure whether each response includes required substantive and work-product elements across ten task categories. |
| Jurisdiction | Primarily United States; exact distribution not fully published |
| Languages | English |
| Size | 100 tasks in 10 categories with more than 1,200 criteria |
| Splits | Private full benchmark with public examples |
| Source material | In-house legal workflows authored by attorneys |
| Input | Single-turn prompt plus URLs, PDFs, or Word documents |
| Output | Draft, analysis, research answer, strategy, extraction, regulatory work, or checklist |
| Baselines / leaderboard context | Official post reports vendor-run comparisons across 100 tasks. |
| Dataset access | Public examples only |
| License | No explicit SPDX license located in the example repository |
| Gating | Full tasks, documents, criteria, and scoring harness are private |
| Maintenance | Active vendor benchmark, updated June 2026. |
| Reproducibility | Partial for examples and low for headline results because most data and the exact judge are private. |

### Metrics

- **Criteria pass rate:** A binary LLM judge scores each atomic criterion; GC AI reports manual checking of more than 300 criteria and 87% agreement. Judge: Single LLM judge; exact model not disclosed on the benchmark page. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/GC-AI-Inc/in-house-legal-bench](https://github.com/GC-AI-Inc/in-house-legal-bench) |
| Hugging Face | None located |
| Paper / arXiv | None located |
| Leaderboard / competition | None located |
| Project | [https://gc.ai/blog/in-house-legal-bench-evaluating-ai-assistants-for-in-house-legal-work](https://gc.ai/blog/in-house-legal-bench-evaluating-ai-assistants-for-in-house-legal-work) |

### Validity and evidence

**Risks / caveats**
- GC AI owns the instrument and sells an evaluated legal assistant.
- Private tasks and an unnamed judge prevent independent reproduction.
- An 87% judge-human agreement rate leaves material measurement error at criterion level.

**Verified facts**
- GC AI's official post reports 100 tasks, 10 categories, more than 1,200 criteria, manual review of 300+ criteria, and 87% agreement.

**Unresolved ambiguity**
- Exact judge model, full task distribution, and repository license are not public.

**Related entries**

- [Realm Legal Reasoning](agents-workflows.md#realm-legal-reasoning)

[Back to page index](#on-this-page)

<a id="thomson-reuters-cocobench"></a>
## Thomson Reuters CoCoBench

`thomson-reuters-cocobench` · **private-benchmark** · **check before use** · private

Complete attorney-authored legal research, drafting, review, and multi-step reasoning tasks using supplied materials.

**Also known as:** CoCoBench

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Thomson Reuters (company; commercial interest) |
| Catalog geography | Evaluation population not published |
| First recorded public event | [2026-05-04](https://www.thomsonreuters.com/en-us/posts/innovation/why-legal-ai-needs-a-new-standard-inside-thomson-reuters-cocobench/) — Official methodology post |
| Latest verified event | [2026-06-22](https://www.thomsonreuters.com/en-us/posts/innovation/the-next-phase-of-professional-ai-is-here/) — Official expansion post |
| Access level | private |
| Test labels | hidden |
| Independently runnable | no |

### Possible use cases

- Read Thomson Reuters' results as vendor evidence about research, drafting, review, and multi-step legal work.
- Use the query-plus-materials-plus-attorney-gold structure when designing an internal professional-work benchmark.
- Track CoCoBench as a moving private instrument; do not compare its scores directly with public task suites.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Attorney-authored tasks and gold responses aim to test complete professional outputs rather than isolated legal knowledge questions. |
| Jurisdiction | Not fully disclosed |
| Languages | English |
| Size | Initially hundreds of tasks; expanded to more than 1,000 attorney-authored tasks with 100+ legal subject-matter experts |
| Splits | Private fixed core with continuing expansion |
| Source material | Attorney-authored queries, supporting materials, and gold attorney responses |
| Input | Legal query plus supporting materials |
| Output | Research, draft, review, or multi-step legal response |
| Baselines / leaderboard context | Thomson Reuters reports internal product/model comparisons; no public leaderboard or result files exist. |
| Dataset access | Private |
| License | Not publicly stated |
| Gating | No public tasks, rubrics, scorer, GitHub, Hugging Face, paper, or leaderboard |
| Maintenance | Active private benchmark expanded between May and June 2026. |
| Reproducibility | Low outside Thomson Reuters because the full evaluation contract is private. |

### Metrics

- **Attorney-grounded task assessment:** Responses are evaluated against attorney-authored gold answers and task expectations; exact scoring dimensions, aggregation, and judge implementation are not public. Judge: Not fully disclosed. **Primary.**

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | None located |
| Hugging Face | None located |
| Paper / arXiv | None located |
| Leaderboard / competition | None located |
| Project | [https://www.thomsonreuters.com/en-us/posts/innovation/why-legal-ai-needs-a-new-standard-inside-thomson-reuters-cocobench/](https://www.thomsonreuters.com/en-us/posts/innovation/why-legal-ai-needs-a-new-standard-inside-thomson-reuters-cocobench/)<br>[https://www.thomsonreuters.com/en-us/posts/innovation/the-next-phase-of-professional-ai-is-here/](https://www.thomsonreuters.com/en-us/posts/innovation/the-next-phase-of-professional-ai-is-here/) |

### Validity and evidence

**Risks / caveats**
- Thomson Reuters owns the benchmark and sells products evaluated with it.
- Changing task counts make snapshots non-comparable unless versioned.
- Undisclosed scoring and private gold answers prevent independent audit.

**Verified facts**
- Two official Thomson Reuters posts document the expansion from hundreds to more than 1,000 tasks and participation by 100+ legal SMEs.

**Unresolved ambiguity**
- Exact task distribution, metrics, judge, splits, and benchmark license are not public.

[Back to page index](#on-this-page)

<a id="realm-legal-reasoning"></a>
## Realm Legal Reasoning

`realm-legal-reasoning` · **private-benchmark** · **check before use** · active

Produce and revise United States litigation, transactional, and compliance work products across evolving multi-stage matters.

**Also known as:** Realm: Legal reasoning benchmark, Warren

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | micro1 Realm (company; commercial interest) |
| Catalog geography | United States |
| First recorded public event | [2026-04-10](https://www.micro1.ai/benchmark/realm-legal) — Date of the original evaluations stated on the official benchmark page; public launch date is not separately exposed |
| Latest verified event | [2026-08-05](https://www.micro1.ai/benchmark/realm-legal) — Official page HTML last-published timestamp and expanded model-evaluation notice |
| Access level | private |
| Test labels | hidden |
| Independently runnable | no |

### Possible use cases

- Read as an owner-run comparison of long-horizon United States legal work products that must change when facts, authority, jurisdiction, or procedural posture changes.
- Reuse the disclosed IRAC criterion taxonomy and paired-bootstrap reporting design when building a private matter-level holdout.
- Inspect the three public trajectories to study tool use, image review, and reasoning continuity without treating them as representative of the hidden set.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Weighted atomic criteria decompose the final work product into issue, rule, application, conclusion, and task-specific requirements; later-stage criteria test whether earlier analysis is correctly revised as the record changes. |
| Jurisdiction | United States federal and state law |
| Languages | English |
| Size | Exact task count is not published; the page references numbered tasks through Task 26 and states that each task has 35–60 criteria |
| Splits | Hidden owner-controlled task set; three full model trajectories from one example task are public |
| Source material | Realistic litigation, transactional, and compliance scenarios with statutes, case law, client files, and optional image exhibits |
| Input | Multi-stage legal assignment inside a read-only sandbox with shell, file, image-viewing, and web-search tools |
| Output | Legal work product such as a motion, memorandum, or compliance analysis, revised across later stages where required |
| Baselines / leaderboard context | The original April 10 report compares Claude Opus 4.7, GPT-5.5, and Gemini 3.1 Pro; the current page says evaluations were later added for Kimi K3, Inkling, Muse Spark 1.1, GPT-5.6, Grok 4.5, Claude Sonnet 5, Claude Opus 4.8, Claude Opus 5, and Claude Fable 5. |
| Dataset access | Private; the page publishes methodology, aggregate results, examples, and three trajectories from one task |
| License | No benchmark data or scorer license published |
| Gating | No public path to the full tasks, labels, weights, judge prompt, or rerunnable harness |
| Maintenance | Active rolling company benchmark; the page was republished August 5, 2026 with additional model evaluations. |
| Reproducibility | Low for headline scores because the task set, exact count, criteria, weights, judge model/prompt, and harness are private; only the disclosed method and example trajectories can be inspected. |

### Metrics

- **Weighted criterion reward (0–1):** An LLM judge checks each criterion against the submitted work product; criterion weights are summed into a 0–1 reward. The public taxonomy is issue 4%, rule 33%, application 48%, conclusion 9%, and other 6%. Judge: Undisclosed LLM judge. **Primary.**
- **Paired bootstrap 95% confidence interval:** The official comparison resamples tasks with replacement 10,000 times, paired across models.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | None located |
| Hugging Face | None located |
| Paper / arXiv | None located |
| Leaderboard / competition | [https://www.micro1.ai/benchmark/realm-legal](https://www.micro1.ai/benchmark/realm-legal) |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- micro1 owns the hidden instrument and offers commercial evaluation/data services.
- The unnamed LLM judge and private rubrics prevent independent error analysis or score reproduction.
- The rolling model roster can change while the original narrative and charts still describe an older three-model run, so every result needs a page date.
- A task-number reference through 26 is not proof of the total task count; the catalog deliberately records that count as undisclosed.

**Verified facts**
- The official page defines the federal/state scope, long-horizon task design, sandbox tools, 35–60 criteria per task, IRAC distribution, weighted 0–1 score, and 10,000-resample paired bootstrap.
- The official page publishes three full trajectories from one task and explicitly identifies the original April 10 evaluations and the later expanded model list.

**Inference**
- The benchmark is useful as vendor evidence and protocol inspiration, not as an independently comparable public leaderboard.

**Unresolved ambiguity**
- Exact task count, task distribution, task dates, judge model, judge prompt, criterion weights, benchmark license, and public launch date are not disclosed.
- The old URL slug used Warren and now redirects to Realm Legal Reasoning; the official page does not explain whether this was only a rename or a broader version change.

**Related entries**

- [Harvey Legal Agent Benchmark (LAB)](agents-workflows.md#harvey-lab)
- [DLawBench](agents-workflows.md#dlawbench)
- [GC AI In-House Legal Bench](agents-workflows.md#gc-ai-in-house-legal-bench)

[Back to page index](#on-this-page)

<a id="courtreasoner"></a>
## CourtReasoner

`courtreasoner` · **benchmark** · **check before use** · fixed-release

Generate appellate-style judicial reasoning that identifies constraints, uses relevant authorities, and supports a valid argument under controlled factual changes.

### Identity, dates, and access

| Field | Detail |
|---|---|
| Owner | Yale NLP / CourtReasoner authors (academic) |
| Catalog geography | United States |
| First recorded public event | [2025-10-29](https://github.com/yale-nlp/CourtReasoner) — GitHub repository creation |
| Latest verified event | [2025-11](https://aclanthology.org/2025.emnlp-main.1787/) — EMNLP 2025 publication |
| Access level | open |
| Test labels | public |
| Independently runnable | partial |

### Possible use cases

- Evaluate generation of US appellate judicial reasoning for an assigned side from a case record.
- Test whether reasoning changes appropriately under opposite-side and fact-deletion perturbations.
- Audit candidate LLM graders against the released attorney/paralegal meta-evaluation labels before using one as a judge.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Three 0–4 expert dimensions score citation relevance, constraint extraction, and argument validity; a separate meta-evaluation measures how well LLM graders correlate with human judgments. |
| Jurisdiction | United States appellate law |
| Languages | English |
| Size | 50 seed appellate cases; 292 expert-annotated meta-evaluation examples across original, opposite-side, fact-deletion, and model-output variants |
| Splits | Fixed public case/question files and meta-evaluation examples; no conventional train/development/test split |
| Source material | US appellate opinions and case.law materials with attorney/paralegal annotations |
| Input | Issue, introduction/background, facts, and assigned side |
| Output | Full judicial reasoning with legal authorities and argument |
| Baselines / leaderboard context | The repository publishes outputs and scores for multiple generation models and compares several LLM graders with expert judgments. |
| Dataset access | Public repository with case questions, outputs, annotator scores, judge prompt, and meta-evaluation code |
| License | No repository or dataset license file was located |
| Gating | None observed |
| Maintenance | Fixed EMNLP 2025 research release; repository activity was concentrated around publication. |
| Reproducibility | Partial: data, prompt, outputs, and meta-evaluator are inspectable, but no license, no hidden test, and dependence on hosted judge snapshots limit clean reruns. |

### Metrics

- **Citation relevance / constraint extraction / argument validity:** Human experts assign 0–4 scores on each dimension; report dimensions separately and identify annotator aggregation. Judge: Attorneys and paralegals. **Primary.**
- **LLM-grader correlation with humans:** Use the released meta-evaluation script to compare candidate judge scores with human labels across perturbation types. Judge: Candidate graders include o3, Claude, Gemini, and Qwen variants.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/yale-nlp/CourtReasoner](https://github.com/yale-nlp/CourtReasoner) |
| Hugging Face | None located |
| Paper / arXiv | [https://aclanthology.org/2025.emnlp-main.1787/](https://aclanthology.org/2025.emnlp-main.1787/) |
| Leaderboard / competition | None located |
| Project | None located |

### Validity and evidence

**Risks / caveats**
- Only 50 seed cases make aggregate conclusions sensitive to case selection.
- Public opinions, questions, outputs, and annotations create contamination and direct optimization risk.
- LLM-grader agreement with experts is not proof that either captures substantive judicial quality.

**Verified facts**
- The official EMNLP paper and Yale repository establish 50 seed cases, 292 expert-annotated meta-evaluation examples, three 0–4 dimensions, public question/output files, and a released grader prompt/script.

**Inference**
- CourtReasoner fills a judge-side generation gap but remains a narrow research instrument rather than a professional-quality certification.

**Unresolved ambiguity**
- No license, canonical Hugging Face dataset, arXiv record, hidden test, or maintained leaderboard was located.

[Back to page index](#on-this-page)
