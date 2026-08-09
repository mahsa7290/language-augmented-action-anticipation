from pathlib import Path
import csv
import json
import sys
from collections import Counter

root = Path(__file__).resolve().parent

expected = [
    'included_works.csv',
    'focal_selection_matrix.csv',
    'component_assignments.csv',
    'protocol_evidence_matrix.csv',
    'evidence_audit.csv',
    'source_locations.csv',
    'deployment_methods.csv',
    'bcap_checklist.csv',
    'bcap_worked_example.csv',
    'artifact_registry.csv',
    'search_templates.txt',
    'verification_search_log.csv',
    'table13_reporting_metadata.csv',
    'claim_evidence_map.csv',
    'coding_manual.md',
    'README.md',
    'corpus_counts.json',
]

report = {
    'missing_files': [name for name in expected if not (root / name).exists()],
    'checks': {},
}


def read_csv(name: str):
    with (root / name).open(newline='', encoding='utf-8') as handle:
        return list(csv.DictReader(handle))


included = read_csv('included_works.csv')
focal = read_csv('focal_selection_matrix.csv')
components = read_csv('component_assignments.csv')
evidence = read_csv('evidence_audit.csv')
claims = read_csv('claim_evidence_map.csv')
protocol = read_csv('protocol_evidence_matrix.csv')
table13 = read_csv('table13_reporting_metadata.csv')
deployment = read_csv('deployment_methods.csv')
bcap_checklist = read_csv('bcap_checklist.csv')
bcap_example = read_csv('bcap_worked_example.csv')
source_locations = read_csv('source_locations.csv')
artifact_registry = read_csv('artifact_registry.csv')
verification_log = read_csv('verification_search_log.csv')

focal_methods = {row['method'].strip() for row in focal}
component_methods = {row['method'].strip() for row in components}
evidence_methods = {row['method'].strip() for row in evidence}
source_methods = {row['method'].strip() for row in source_locations}

required_source_fields = ('method', 'source_location', 'locator_precision')
source_provenance_nonempty = all(
    all(row.get(field, '').strip() for field in required_source_fields)
    for row in source_locations
)
claim_fields = ('claim', 'supporting_studies', 'confidence')
claim_rows_nonempty = all(
    all(row.get(field, '').strip() for field in claim_fields)
    for row in claims
)
expected_claims = {
    'Goal/intention conditioning can improve long-horizon anticipation',
    'Semantic/action-history context can replace part of dense video in selected procedural settings',
    'A geometric intent signal can outperform textual conditioning in the studied regime',
    'Anti-repetition or structured decoding can improve sequence stability',
    'Published EK-100 numbers are difficult to reconcile',
    'Grounding/verification may improve feasibility',
    'Calibration/selective prediction require explicit measurement',
}
claim_set_matches_main_table = {row.get('claim', '').strip() for row in claims} == expected_claims
protocol_provenance_nonempty = all(
    row.get('method', '').strip()
    and row.get('source_location', '').strip()
    and row.get('verification', '').strip()
    for row in protocol
)

row_counts = {
    'claim_evidence_map.csv': len(claims),
    'protocol_evidence_matrix.csv': len(protocol),
    'table13_reporting_metadata.csv': len(table13),
    'deployment_methods.csv': len(deployment),
    'bcap_checklist.csv': len(bcap_checklist),
    'bcap_worked_example.csv': len(bcap_example),
    'source_locations.csv': len(source_locations),
    'artifact_registry.csv': len(artifact_registry),
    'verification_search_log.csv': len(verification_log),
}
expected_row_counts = {
    'claim_evidence_map.csv': 7,
    'protocol_evidence_matrix.csv': 10,
    'table13_reporting_metadata.csv': 5,
    'deployment_methods.csv': 10,
    'bcap_checklist.csv': 9,
    'bcap_worked_example.csv': 9,
    'source_locations.csv': 25,
}
row_count_checks = {
    name: row_counts.get(name) == expected
    for name, expected in expected_row_counts.items()
}

report['checks'].update(
    inventory_record_sum=sum(int(row.get('record_count', '1') or 1) for row in included),
    focal_rows=len(focal),
    component_rows=len(components),
    evidence_rows=len(evidence),
    row_counts=row_counts,
    expected_row_count_checks=row_count_checks,
    all_focal_have_component=focal_methods == component_methods,
    all_focal_have_evidence=focal_methods == evidence_methods,
    all_focal_have_source_location=focal_methods == source_methods,
    source_provenance_nonempty=source_provenance_nonempty,
    protocol_provenance_nonempty=protocol_provenance_nonempty,
    claim_rows_nonempty=claim_rows_nonempty,
    claim_set_matches_main_table=claim_set_matches_main_table,
    focal_groups=dict(Counter(row['focal_group'] for row in focal)),
    components=dict(Counter(row['primary_component'] for row in components)),
)

report['passed'] = (
    not report['missing_files']
    and report['checks']['inventory_record_sum'] == 79
    and len(focal) == 25
    and len(components) == 25
    and len(evidence) == 25
    and all(row_count_checks.values())
    and report['checks']['all_focal_have_component']
    and report['checks']['all_focal_have_evidence']
    and report['checks']['all_focal_have_source_location']
    and source_provenance_nonempty
    and protocol_provenance_nonempty
    and claim_rows_nonempty
    and claim_set_matches_main_table
    and report['checks']['focal_groups'] == {
        'core_language': 16,
        'non_llm_diagnostic': 6,
        'boundary': 3,
    }
    and report['checks']['components'] == {
        'C1': 8,
        'C2': 7,
        'C3': 4,
        'C4': 6,
    }
)

(root / 'audit_report.json').write_text(
    json.dumps(report, indent=2, ensure_ascii=False),
    encoding='utf-8',
)
print(json.dumps(report, indent=2, ensure_ascii=False))
sys.exit(0 if report['passed'] else 1)
