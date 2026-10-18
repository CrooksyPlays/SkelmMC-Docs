#!/usr/bin/env python3
"""Add an independent SkelmMC documentation project and starter pages."""
from pathlib import Path
import argparse
import re
import sys
try:
    import yaml
except ModuleNotFoundError:
    sys.exit("Missing dependency: PyYAML. From the website folder run "
             "'python manage.py add' for automatic setup, or "
             "'python -m pip install -r requirements.txt' first.")

ROOT = Path(__file__).resolve().parent.parent

ARTICLES = [
    ('overview', 'Overview', 'layers'),
    ('installation', 'Installation', 'download'),
    ('getting-started', 'Getting started', 'play'),
    ('commands', 'Commands & permissions', 'terminal'),
    ('configuration', 'Configuration', 'sliders'),
    ('troubleshooting', 'Troubleshooting', 'wrench'),
    ('changelog', 'Changelog', 'clock'),
]

def main():
    ap = argparse.ArgumentParser(description='Scaffold a new project in SkelmMC Docs')
    ap.add_argument('--slug', required=True, help='URL path and directory name, e.g. skelm-shop')
    ap.add_argument('--name', required=True, help='Display title, e.g. SkelmShop')
    ap.add_argument('--description', default='Documentation for a SkelmMC project.')
    ap.add_argument('--category', default='SkelmMC project')
    args = ap.parse_args()
    slug = args.slug.strip().lower()
    name = args.name.strip()
    if not re.fullmatch(r'[a-z][a-z0-9]*(?:-[a-z0-9]+)*', slug):
        ap.error('--slug must use lowercase letters, digits and single hyphens')
    if not name or any(ch in name for ch in '<>\r\n'):
        ap.error('--name must be a single nonempty plain-text line')
    site_path = ROOT / 'site.yml'
    config = yaml.safe_load(site_path.read_text(encoding='utf-8'))
    if any(p['id'] == slug for p in config.get('projects', [])):
        ap.error('that project slug is already registered')
    if any(page['slug'].split('/')[0] == slug for sec in config['sections'] for page in sec['pages']):
        ap.error('the path is already used by another section')
    target = ROOT / 'content' / slug
    if target.exists():
        ap.error(f'folder already exists: {target}')
    project = {'id':slug, 'name':name,'category':args.category,'status':'Draft',
               'description':args.description,'overview':f'{slug}/overview','support':f'{slug}/troubleshooting'}
    section = {'title':name,'description':args.category,'project':slug,'pages':[
        {'slug': f'{slug}/{file}','title':title,'file':f'content/{slug}/{file}.md','icon':icon}
        for file,title,icon in ARTICLES]}
    target.mkdir(parents=True)
    for file,title,icon in ARTICLES:
        if file == 'overview':
            content = f'{args.description}\n\n<div class="callout warning"><strong>Draft</strong><p>This is an unverified documentation scaffold, not a published release reference.</p></div>\n\n## About {name}\n\nDescribe the project, its purpose, release status and key links here.\n'
        elif file == 'changelog':
            content = 'Release notes will be added when a version is verified.\n\n## Unreleased\n\n- Documentation scaffold created. No feature release implied.\n'
        else:
            content = f'This page is a draft for {name}. Replace with details verified against your project source and release.\n\n<div class="callout warning"><strong>Draft</strong><p>This is a placeholder; do not treat examples here as available features.</p></div>\n\n## {title}\n\nTo be documented.\n'
        (target / (file + '.md')).write_text(content, encoding='utf-8')
    config.setdefault('projects', []).append(project)
    sections = config['sections']
    insert_at = next((i for i,s in enumerate(sections) if s.get('title') == 'SkelmMC platform'),len(sections))
    sections.insert(insert_at, section)
    site_path.write_text(yaml.safe_dump(config, sort_keys=False, allow_unicode=True, width=120), encoding='utf-8')
    print(f'Created draft docs for {name} ({slug}). Run python build.py to refresh the website.')

if __name__=='__main__':
    main()
