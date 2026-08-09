from pathlib import Path
import argparse, csv, json, re, sys

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('--release-mode', action='store_true')
args = parser.parse_args()
rows = list(csv.DictReader((root/'papers.csv').open()))
meta = json.loads((root/'release_metadata.json').read_text())
errors=[]
required=['method','primary_component','focal_group','year','venue_or_identifier','dataset_or_benchmark','paper_url']
for i,row in enumerate(rows,2):
    for key in required:
        if not row.get(key,'').strip(): errors.append(f'row {i}: missing {key}')
    if row.get('primary_component') not in {'C1','C2','C3','C4'}: errors.append(f'row {i}: invalid primary_component')
    if row.get('focal_group') not in {'core_language','non_llm_diagnostic','boundary'}: errors.append(f'row {i}: invalid focal_group')
    if not re.fullmatch(r'20(1[8-9]|2[0-6])', row.get('year','')): errors.append(f'row {i}: invalid year {row.get("year")}')
    for key in ('paper_url','code_url'):
        value=row.get(key,'').strip()
        if value and not value.startswith(('https://','http://')): errors.append(f'row {i}: invalid {key}')
if len(rows)!=25: errors.append(f'expected 25 focal records, got {len(rows)}')
if meta.get('version')!='1.0.0' or meta.get('release_tag')!='v1.0.0': errors.append('release version/tag mismatch')
if meta.get('license')!='CC-BY-4.0': errors.append('licence mismatch')
if args.release_mode:
    if not meta.get('repository_url'): errors.append('release mode: repository_url is unset')
    # An archival DOI is recommended but optional; never fabricate one.
print(f'records: {len(rows)}')
print(f'version: {meta.get("version")} ({meta.get("release_tag")})')
print(f'mode: {"release" if args.release_mode else "submission"}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('catalogue validation passed')
