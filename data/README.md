# Machine-readable evidence package

This directory accompanies **Language-Augmented Video Action Anticipation: Design Fundamentals, Benchmarks, and Open Challenges**.

- Included works were required to be publicly available by **31 July 2026**.
- Verification passes were completed on **2 and 3 August 2026** and were restricted to pre-cutoff records.
- Initial Windows 1-2 set: **61 works**.
- Added by verification passes: **3 + 5 eligible pre-cutoff records**.
- Final retained synthesis set: **69 works**.
- Separately flagged evidence records: **10**.
- Total inventory: **79 records**.
- Focal methods: **25** (16 core language/VLM, 6 non-LLM diagnostic, 3 boundary).

The package documents the final coded evidence inventory. It does not reconstruct missing historical query logs or attrition counts and does not claim blind independent recoding.

The verification-search log records the query families actually executed on 2 and 3 August 2026. Search templates for the earlier retrieval windows are reconstructed from authors' notes and are labelled accordingly.

## CSV inventory

| File | Rows | Schema |
|---|---:|---|
| `artifact_registry.csv` | 3 | `method, artifact_url, artifact_version_or_commit, access_date, evaluation_script, configuration_file, verification_status` |
| `bcap_checklist.csv` | 9 | `step, name, requirement` |
| `bcap_worked_example.csv` | 9 | `step, dimension, AntGPT, PlausiVL, V-JEPA_2.1` |
| `claim_evidence_map.csv` | 7 | `claim, supporting_studies, independent_groups, shared_evaluator, controlled_ablation, confidence, scope_note` |
| `component_assignments.csv` | 25 | `method, primary_component, focal_group, publication_maturity, component_isolation, protocol_relevance, reproduction_status` |
| `deployment_methods.csv` | 10 | `method, E2, E3, relation_to_anticipation` |
| `evidence_audit.csv` | 25 | `method, publication_maturity, component_isolation, protocol_relevance, reproduction_status, source_location` |
| `focal_selection_matrix.csv` | 25 | `method, condition_i_design_novelty, condition_ii_protocol, condition_iii_ablation, condition_iv_lineage, condition_v_boundary, focal_group` |
| `included_works.csv` | 79 | `work, venue_or_identifier, publication_maturity, benchmark_or_role, inventory_group, record_count` |
| `protocol_evidence_matrix.csv` | 10 | `benchmark, method, version_or_label_space, setting, subset, reported_value, source_location, verification` |
| `source_locations.csv` | 25 | `method, source_location, locator_precision, artifact_url, artifact_version_or_commit, access_date, evaluation_script, configuration_file, verification_status` |
| `table13_reporting_metadata.csv` | 5 | `method, provenance, clip_length_fps, encoder_predictor_usage, probe_depth, training_loss, pretraining_volume, anticipation_time_sampling, evaluator_implementation, baseline_rerun_status, verification` |
| `verification_search_log.csv` | 11 | `publication_eligibility_cutoff, search_date, sources, query_family, candidate, disposition, reason` |

## Key relations to the PDF

- `component_assignments.csv`, `focal_selection_matrix.csv`, and `evidence_audit.csv`: Main Table 3, Figure 4, Supplementary S1/S4/S6.
- `protocol_evidence_matrix.csv`: Main Tables 12-13 and Supplementary S2/S2A.
- `table13_reporting_metadata.csv`: configuration/provenance audit for the EK-100 reporting-incompatibility case study.
- `claim_evidence_map.csv`: claim-evidence table in the main synthesis.
- `verification_search_log.csv`: candidate dispositions from the dated prospective passes.
- `source_locations.csv`: source and public-artifact locators where verified.

## Comparability levels

- Level (i): source-described alignment only.
- Level (ii): same released evaluation code.
- Level (iii): independent reproduction under identical data and code.

## Coding reliability

The 25-row final matrix was not blindly recoded in full by an independent second coder, so no agreement statistic is reported. Auditability is supported by the row-level assignments, coding manual, source locators, and alternate-assignment sensitivity analysis.

## Artefact inspection

Public artefacts recorded in the registry/source index were last inspected on 3 August 2026. Repository availability does not imply that a result was rerun.

## Versioned catalogue

`awesome_catalogue/` is included as version 1.0.0 under CC BY 4.0. Its public repository URL and archival DOI are deliberately unset until actual release. `release_metadata.json` is the single source of truth for those fields.
