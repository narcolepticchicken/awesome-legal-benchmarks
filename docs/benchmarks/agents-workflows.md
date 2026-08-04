# Agents and legal workflows

<!-- Generated from catalog/benchmarks.json. Edit the source record or scripts/generate_catalog.py. -->

Tool use, process compliance, simulated legal work, and long-horizon professional tasks.

Snapshot: **2026-08-03** · 4 entries

[Catalog index](../catalog.md) · [Selection guide](../selection-guide.md) · [Metric field guide](../metric-theory.md) · [Methodology](../methodology.md)

## On this page

- [LegalAgentBench](#legalagentbench)
- [Ready Jurist One](#ready-jurist-one)
- [Legal Agent Benchmark](#harvey-lab)
- [APEX-Agents — Corporate Lawyer](#apex-agents-corporate-law)

<a id="legalagentbench"></a>
## LegalAgentBench

`legalagentbench` · **benchmark** · **specialist** · fixed-release

Chinese legal tool use, multi-hop information gathering, and legal writing.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Success and progress scores estimate whether an agent selects and sequences tools toward a task; BERTScore assesses writing similarity, but neither alone proves legal correctness. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | 17 corpora, 37 tools, 300 tasks |
| Splits | Tasks span one-to-five-hop and writing categories |
| Source | Chinese legal corpora wrapped as tools and authored tasks |
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
| Hugging Face | None |
| Paper / arXiv | [https://arxiv.org/abs/2412.17259](https://arxiv.org/abs/2412.17259) |
| Leaderboard / competition | None |
| Project | None |

### Validity and evidence

**Risks / caveats**
- Keyword graders can be gamed without producing a legally adequate result.
- Public solutions and tool corpora permit benchmark-specific planning.

**Verified facts**
- Official repository specifies 17 corpora, 37 tools, and 300 tasks.

**Inference**
- Use as a tool-use benchmark with legal grounding checks, not as proof of deployable lawyering.

**Unresolved ambiguity**
- None recorded.

Original source bullet(s): #10

[Back to page index](#on-this-page)

<a id="ready-jurist-one"></a>
## Ready Jurist One

`ready-jurist-one` · **benchmark** · **specialist** · active

Operate interactively in Chinese legal consultation, drafting, civil-court, and criminal-court environments.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | J1-EVAL uses dual outcome- and process-oriented scoring so an agent must reach the right result and follow required procedural steps, formats, reasoning, and citation constraints. |
| Jurisdiction | China |
| Languages | Chinese |
| Size | Paper reports 508 environments across six scenarios and three levels |
| Splits | Scenario/level-specific interactive environments |
| Source | Chinese judgments and legal articles, structured into role-based environments |
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

**Inference**
- None recorded.

**Unresolved ambiguity**
- Reported total and per-level counts conflict; licensing is unclear.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="harvey-lab"></a>
## Legal Agent Benchmark

`harvey-lab` · **benchmark** · **check before use** · active

Complete long-horizon legal matters using files, research, analysis, drafting, and validation tools.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | All-pass treats legal work as conjunctive reliability: a task passes only if every required expert rubric criterion passes; rubric pass rate exposes partial completion but is not the headline autonomy threshold. |
| Jurisdiction | United States / commercial legal practice, mixed practice areas |
| Languages | English |
| Size | Evolving public release; launch materials describe 1,200+ tasks, 24 practice areas, and 75,000+ rubric criteria, with later contracting extensions |
| Splits | Public task set plus Harvey's separate holdout used for published model results |
| Source | Synthetic client matters and expert-curated instructions, files, outputs, and rubrics |
| Input | Matter instruction and sandboxed document/file environment |
| Output | Research, analysis, and professional work-product artifacts |
| Baselines / leaderboard context | Harvey publishes frontier-model holdout results; public tasks/harness allow community runs but are not identical to the holdout. |
| Dataset access | Public tasks and harness; published headline holdout is private |
| License | MIT |
| Gating | Running agents/judges requires model access and compute |
| Maintenance | Rapidly evolving vendor-maintained benchmark. |
| Reproducibility | Public harness is reproducible in principle; headline holdout scores cannot be independently reproduced and model/judge versions change. |

### Metrics

- **All-pass rate:** A task receives 1 only when every applicable rubric criterion passes; mean across tasks. Judge: Repeated cross-model LLM judging under repository rubric protocol. **Primary.**
- **Rubric pass rate:** Fraction of individual criteria passed; also report cost and latency for deployment trade-offs. Judge: LLM judge with expert-authored rubrics.

### Resources

| Resource | Direct URL |
|---|---|
| GitHub | [https://github.com/harveyai/harvey-labs](https://github.com/harveyai/harvey-labs) |
| Hugging Face | None |
| Paper / arXiv | None |
| Leaderboard / competition | None |
| Project | [https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark)<br>[https://www.harvey.ai/blog/legal-agent-benchmark-initial-results](https://www.harvey.ai/blog/legal-agent-benchmark-initial-results) |

### Validity and evidence

**Risks / caveats**
- Benchmark owner is a legal-AI vendor and publishes results on a private mirror holdout.
- All-pass is sensitive to rubric granularity and judge false negatives; a single criterion zeroes the task.

**Verified facts**
- Official GitHub and Harvey posts define the harness, expert rubrics, all-pass, and rubric-pass metrics.

**Inference**
- None recorded.

**Unresolved ambiguity**
- The evolving public task count should be read from a pinned release rather than a timeless number.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)

<a id="apex-agents-corporate-law"></a>
## APEX-Agents — Corporate Lawyer

`apex-agents-corporate-law` · **benchmark** · **check before use** · active

Complete realistic long-horizon corporate-law tasks across applications, files, and professional work environments.

### Evaluation contract

| Field | Detail |
|---|---|
| Construct / theory | Pass@1 measures single-run task completion against multiple criteria; the legal slice tests workflow execution, not legal knowledge in isolation. |
| Jurisdiction | Corporate-law practice / mixed |
| Languages | English |
| Size | 480 total APEX tasks, including 160 corporate-law tasks across 12 worlds |
| Splits | Role-specific public benchmark and leaderboard evaluations |
| Source | Tasks authored by corporate lawyers, consultants, and bankers with files, rubrics, and gold outputs |
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
| Project | None |

### Validity and evidence

**Risks / caveats**
- Only one third of APEX is legal; aggregate APEX scores are not legal scores.
- Public gold outputs/rubrics permit targeted agent tuning.

**Verified facts**
- Official paper/HF/leaderboard identify 480 total and a 160-task corporate-law slice.

**Inference**
- None recorded.

**Unresolved ambiguity**
- Jurisdiction varies by authored task and is not summarized as one national corpus.

Original source bullet(s): Curated addition.

[Back to page index](#on-this-page)
