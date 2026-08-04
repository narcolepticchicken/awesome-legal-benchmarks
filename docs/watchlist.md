# Watchlist

These are plausible legal-evaluation artifacts that were **not promoted into the canonical catalog** at the 2026-08-03 research snapshot. Being on this page is not a rejection; it means that recency, missing artifacts, unstable versions, internal inconsistencies, gating, or incomplete scoring instructions prevent a stronger reproducibility label today.

| Candidate | Why it matters | Why it remains on the watchlist | Primary artifacts |
|---|---|---|---|
| PLawBench | Polish legal reasoning and knowledge | Very recent; verify stable data revision, scorer, license, and independent reproductions before promotion. | [GitHub](https://github.com/SKYLENAGE-AI/PLawBench) · [paper](https://arxiv.org/abs/2601.16669) · [ACL](https://aclanthology.org/2026.acl-long.458/) |
| BenGER | German legal benchmark platform | A platform can change independently of the paper; a fixed, versioned task/data/scorer release and durable result protocol are needed. | [GitHub](https://github.com/SebastianNagl/benger-platform) · [paper](https://arxiv.org/abs/2605.28183) · [platform](https://what-a-benger.net/) |
| UA-Legal-Bench | Ukrainian legal evaluation | The HF card identifies v1 while the paper describes v2; the canonical version relationship must be resolved. | [HF](https://huggingface.co/datasets/overthelex/ua-legal-bench) · [paper](https://arxiv.org/abs/2605.29170) · [paper code collection](https://github.com/overthelex/secondlayer-papers) |
| Multi-Legal-Bench | Large multilingual legal benchmark collection | Public descriptions conflict at roughly 134M versus 122M records; task-unit, split, scorer, and practical reproducibility need clarification. | [HF](https://huggingface.co/datasets/overthelex/multi-legal-bench) · [paper](https://arxiv.org/abs/2605.29738) |
| LegalCiteBench | Legal citation understanding and generation | Very recent; hold until release version, scorer, license, and citation-validity protocol stabilize. | [GitHub](https://github.com/Sijia711/LegalCiteBench) · [HF](https://huggingface.co/datasets/legalcitebench/LegalCiteBench) · [paper](https://arxiv.org/abs/2605.10186) |
| Legal-DC | Legal document comprehension | Very recent; inspect final task files, split construction, official scorer, and leakage controls before promotion. | [GitHub](https://github.com/legal-dc/Legal-DC) · [paper](https://arxiv.org/abs/2603.11772) |
| TW-LegalBench | Traditional-Chinese/Taiwan legal evaluation | Very recent; a canonical source repository and stable evaluation code were not located in this snapshot. | [HF](https://huggingface.co/datasets/feiyuehchen/TW-LegalBench) · [paper](https://arxiv.org/abs/2606.18699) |
| Legal Rikai Open Benchmark | Japanese legal evaluation | The HF release is gated, marked with a nonstandard “other” license, and exposes only about 100 samples, limiting auditability. | [HF](https://huggingface.co/datasets/legalontech/Legal-Rikai-Open-Benchmark) · [paper](https://arxiv.org/abs/2512.11297) |

## Lower-evidence leads

The following discovery leads were not promoted because this audit did not locate a sufficiently complete primary paper/code/data/scorer chain: [Taiwan legal benchmark v1](https://huggingface.co/datasets/lianghsun/tw-legal-benchmark-v1), [LegalBench.br](https://huggingface.co/datasets/celsowm/legalbench.br), and [Echo9k's Mexico legal dataset](https://huggingface.co/datasets/Echo9k/legal-benchmarks). A future contribution should identify canonical ownership, task construction, exact scoring, license, and a fixed evaluation revision.
