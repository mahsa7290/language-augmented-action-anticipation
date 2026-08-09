# Awesome Language-Augmented Action Anticipation

> Version 1.0.0 of the evidence-aware catalogue accompanying the survey
> **Language-Augmented Video Action Anticipation: Design Fundamentals, Benchmarks, and Open Challenges**.

The catalogue is organised by task regime and the survey's non-unique **C1-C4 intervention map**. Version 1.0.0 is the catalogue snapshot accompanying the manuscript submission. Release metadata are stored in `release_metadata.json`.

## Taxonomy

- **C1 - Context construction:** representation, semantic history, modality, retrieval, adaptation.
- **C2 - Goal/intention modelling:** explicit goals, semantic prototypes, latent or geometric intent proxies.
- **C3 - Future prediction/decoding:** sequence objectives, plausibility, repetition control, calibration.
- **C4 - Adjacent emerging grounding/executability:** symbolic, geometric, planning, and world-model constraints.

## C1

| Method | Group | Venue / identifier | Year | Benchmark / role | Paper | Code |
|---|---|---|---:|---|---|---|
| TransFusion | core_language | CVPR 2024 | 2024 | Ego4D-STA / EK-100 | [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Pasca_Summarize_the_Past_to_Predict_the_Future_Natural_Language_Descriptions_CVPR_2024_paper.html) | [code](https://eth-ait.github.io/transfusion-proj/) |
| PALM | core_language | ECCV 2024 | 2024 | Ego4D/EK/EGTEA | [paper](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/10743_ECCV_2024_paper.php) | [code](https://github.com/DanDoge/Palm) |
| SAFT | core_language | MVA 2026 | 2026 | Ego4D | [paper](https://doi.org/10.1007/s00138-025-01774-w) | - |
| M-CAT | core_language | arXiv:2401.12972 | 2024 | EK-55/100, EGTEA | [paper](https://arxiv.org/abs/2401.12972) | - |
| V-JEPA 2.1 | non_llm_diagnostic | arXiv:2603.14482 | 2026 | EK-100 | [paper](https://arxiv.org/abs/2603.14482) | [code](https://github.com/facebookresearch/vjepa2) |
| EgoAnticipator | non_llm_diagnostic | IJCAI 2025 | 2025 | Ego4D-STA v1/v2 | [paper](https://www.ijcai.org/proceedings/2025/0088.pdf) | - |
| AAG | core_language | WACV 2026 | 2026 | IKEA-ASM/Meccano/Assembly101 | [paper](https://openaccess.thecvf.com/content/WACV2026/html/Benavent-Lledo_Action_Anticipation_at_a_Glimpse_To_What_Extent_Can_Multimodal_WACV_2026_paper.html) | - |
| DCPGN | core_language | CVPR 2026 | 2026 | EgoExoLearn/EgoMe-anti | [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shi_Test-time_Ego-Exo-centric_Adaptation_for_Action_Anticipation_via_Multi-Label_Prototype_Growing_CVPR_2026_paper.html) | - |

## C2

| Method | Group | Venue / identifier | Year | Benchmark / role | Paper | Code |
|---|---|---|---:|---|---|---|
| AntGPT | core_language | ICLR 2024 | 2024 | Ego4D/EK/EGTEA | [paper](https://arxiv.org/abs/2307.16368) | [code](https://github.com/brown-palm/AntGPT) |
| INSIGHT | core_language | AAAI 2026 | 2026 | Ego4D/EK/EGTEA | [paper](https://ojs.aaai.org/index.php/AAAI/article/view/38797) | - |
| GP-AMS | core_language | TPAMI 2026 | 2026 | Assembly101 | [paper](https://doi.org/10.1109/TPAMI.2026.3653482) | - |
| ICVL | core_language | arXiv:2505.01713 | 2025 | Ego4D | [paper](https://arxiv.org/abs/2505.01713) | - |
| PAR-VLA | core_language | CVPR 2026 | 2026 | EK-100/EGTEA/50Salads | [paper](https://openaccess.thecvf.com/content/CVPR2026/html/Shao_Prototypical_Action_Reasoning_Facilitated_by_Vision-Language_Alignment_for_Egocentric_Action_CVPR_2026_paper.html) | - |
| Mascaro et al. | non_llm_diagnostic | WACV 2023 | 2023 | Ego4D | [paper](https://openaccess.thecvf.com/content/WACV2023/html/Mascaro_Intention-Conditioned_Long-Term_Human_Egocentric_Action_Anticipation_WACV_2023_paper.html) | - |
| TrajPilot | non_llm_diagnostic | arXiv:2605.20388 | 2026 | Ego-Exo4D/Ego4D GoalStep/EK-100 | [paper](https://arxiv.org/abs/2605.20388) | - |

## C3

| Method | Group | Venue / identifier | Year | Benchmark / role | Paper | Code |
|---|---|---|---:|---|---|---|
| PlausiVL | core_language | CVPR 2024 | 2024 | Ego4D/EK | [paper](https://openaccess.thecvf.com/content/CVPR2024/html/Mittal_Cant_Make_an_Omelette_Without_Breaking_Some_Eggs_Plausible_Action_CVPR_2024_paper.html) | - |
| VideoPlan | core_language | WACV 2026 | 2026 | COIN/CrossTask/Ego4D | [paper](https://openaccess.thecvf.com/content/WACV2026/html/Zhang_Enhancing_Visual_Planning_with_Auxiliary_Tasks_and_Multi-token_Prediction_WACV_2026_paper.html) | - |
| ActionLLM | core_language | IEEE TMM 2025 | 2025 | 50Salads/Breakfast | [paper](https://arxiv.org/abs/2501.00795) | [code](https://github.com/2tianyao1/ActionLLM) |
| AGA | non_llm_diagnostic | ICLR 2026 | 2026 | EK-100/EK-55/EGTEA | [paper](https://openreview.net/forum?id=uKFVZMPppq) | [code](https://corcovadoming.github.io/AGA/) |

## C4

| Method | Group | Venue / identifier | Year | Benchmark / role | Paper | Code |
|---|---|---|---:|---|---|---|
| LEAP | core_language | arXiv:2312.00055 | 2023 | EK | [paper](https://arxiv.org/abs/2312.00055) | - |
| FactCheck | core_language | arXiv:2606.14778 | 2026 | EK-55, EGTEA | [paper](https://arxiv.org/abs/2606.14778) | - |
| SymAnt | non_llm_diagnostic | CMU-RI-TR-25-45 | 2025 | Breakfast/50Salads/EK | [paper](https://www.ri.cmu.edu/publications/parameter-efficient-neuro-symbolic-action-anticipation-via-iterative-context-refinement/) | - |
| TR-LLM | boundary | arXiv:2410.03993 | 2024 | Home environment | [paper](https://arxiv.org/abs/2410.03993) | - |
| Anticipate & Act | boundary | arXiv:2502.02066 | 2025 | VirtualHome | [paper](https://arxiv.org/abs/2502.02066) | - |
| HWM | boundary | arXiv:2604.03208 | 2026 | Non-egocentric | [paper](https://arxiv.org/abs/2604.03208) | - |

## Evidence fields

`papers.csv` records publication maturity, component isolation, protocol relevance, and reproduction status separately; these fields are not collapsed into a scalar quality score.

## Validation and release

- Run `python scripts/validate_catalogue.py` for submission-package checks.
- Run `python scripts/validate_catalogue.py --release-mode` after setting the public repository URL in `release_metadata.json`.
- The intended release tag is `v1.0.0`.
- See `CONTRIBUTING.md` for update rules.

## Citation

Use the root-level `CITATION.cff` in the repository for citation metadata.
