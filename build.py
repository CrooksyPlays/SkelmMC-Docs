#!/usr/bin/env python3
"""Build the zero-JavaScript-framework, Markdown-driven SkelmMC documentation hub."""
from pathlib import Path
from urllib.parse import quote
import html, json, os, posixpath, re, shutil
import yaml
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown_it import MarkdownIt
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, TextLexer

ROOT = Path(__file__).resolve().parent
DIST = ROOT / 'dist'
config = yaml.safe_load((ROOT / 'site.yml').read_text(encoding='utf-8'))
sections = config['sections']
projects = config.get('projects', [])
project_by_id = {p['id']: p for p in projects}
for s in sections:
    for entry in s['pages']:
        entry['project'] = s.get('project')
pages = [p for s in sections for p in s['pages']]
page_by_slug = {p['slug']: p for p in pages}
md = MarkdownIt('commonmark', {'html': True, 'linkify': True}).enable('table')


def highlight_code(code, lang, attrs):
    try:
        lexer = get_lexer_by_name(lang or 'text')
    except Exception:
        lexer = TextLexer()
    return highlight(code, lexer, HtmlFormatter(nowrap=False, cssclass='highlight'))

md.options['highlight'] = highlight_code

def slugify(x):
    return re.sub(r'[^a-z0-9-]+', '', re.sub(r'\s+', '-', x.lower())).strip('-') or 'section'

def headingize(markdown):
    soup = BeautifulSoup(md.render(markdown), 'html.parser')
    toc, used = [], set()
    for h in soup.select('h2, h3'):
        base = slugify(h.get_text(' ', strip=True))
        anchor, num = base, 2
        while anchor in used:
            anchor = f'{base}-{num}'
            num += 1
        used.add(anchor)
        h['id'] = anchor
        toc.append({'id': anchor, 'title': h.get_text(' ', strip=True), 'level': h.name})
        anchorEl = soup.new_tag('a', href=f'#{anchor}')
        anchorEl['class'] = 'heading-anchor'
        anchorEl['aria-label'] = f"Link to {h.get_text(' ', strip=True)}"
        anchorEl.string = '#'
        h.append(anchorEl)
    for code in soup.select('div.highlight'):
        wrapper = soup.new_tag('div')
        wrapper['class'] = 'code-frame'
        code.wrap(wrapper)
        btn = soup.new_tag('button', type='button')
        btn['class'] = 'copy-code'
        btn['aria-label'] = 'Copy code'
        btn.string = 'Copy'
        wrapper.insert(0, btn)
    return str(soup), toc


def page_dir(slug):
    return DIST / 'wiki' / slug


def relroot(slug=None):
    if slug is None:
        return './'
    return '../' * (len(slug.split('/')) + 1)


def url_for(slug, current=None):
    # Clean directory URLs, relative to current page, work on any sub-path.
    source = '' if current is None else 'wiki/' + current + '/'
    destination = '' if slug is None else 'wiki/' + slug + '/'
    result = posixpath.relpath(destination or '.', start=source or '.')
    return (result if result.startswith('.') else './' + result) + ('' if result.endswith('/') else '/')


def validate_config():
    if len(project_by_id) != len(projects):
        raise ValueError('Duplicate project IDs in site.yml')
    if len(page_by_slug) != len(pages):
        raise ValueError('Duplicate article paths in site.yml')
    for s in sections:
        if s.get('project') and s['project'] not in project_by_id:
            raise ValueError(f"Unknown project {s['project']} in section {s['title']}")
    for project in projects:
        if project.get('overview') not in page_by_slug:
            raise ValueError(f"Missing overview page for {project['id']}")
        if project.get('support') and project['support'] not in page_by_slug:
            raise ValueError(f"Missing support page for {project['id']}")
    for page in pages:
        if not (ROOT / page['file']).is_file():
            raise FileNotFoundError(f"Article not found: {page['file']}")


def render_page(env, slug, **extra):
    p = page_by_slug[slug]
    raw = (ROOT / p['file']).read_text(encoding='utf-8')
    body, toc = headingize(raw)
    title = p['title']
    # Page heading comes from the template (the authored MD starts with ##).
    all_pages = pages
    # Keep article pagination within the active section, not across unrelated plugins.
    section = next(s for s in sections if p in s['pages'])
    section_pages = section['pages']
    index = section_pages.index(p)
    previous = section_pages[index - 1] if index > 0 else None
    next_page = section_pages[index + 1] if index + 1 < len(section_pages) else None
    page = env.get_template('page.html').render(
        site=config['site'], sections=sections, projects=projects, current=p,
        section=section, toc=toc, body=body, title=title,
        root=relroot(slug), url_for=lambda dest: url_for(dest, slug),
        previous=previous, next_page=next_page, help_slug=project_by_id.get(p.get('project'), {}).get('support', 'platform/how-to-use'), **extra,
    )
    target = page_dir(slug)
    target.mkdir(parents=True, exist_ok=True)
    (target / 'index.html').write_text(page, encoding='utf-8')
    soup = BeautifulSoup(body, 'html.parser')
    text = soup.get_text(' ', strip=True)
    return {'slug': slug, 'path': 'wiki/' + slug + '/', 'title': title, 'section': section['title'], 'description': text[:230], 'text': text[:13000], 'headings': [t['title'] for t in toc]}


def main():
    validate_config()
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    shutil.copytree(ROOT / 'assets', DIST / 'assets')
    env = Environment(loader=FileSystemLoader(ROOT / 'templates'), autoescape=select_autoescape(['html']))
    search_data = [render_page(env, p['slug']) for p in pages]
    (DIST / 'search-index.json').write_text(json.dumps(search_data, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
    home = env.get_template('home.html').render(site=config['site'], projects=projects, sections=sections, root='./', url_for=lambda dest: url_for(dest, None), title='Home')
    (DIST / 'index.html').write_text(home, encoding='utf-8')
    catalog_dir = DIST / 'projects'
    catalog_dir.mkdir(parents=True, exist_ok=True)
    catalog = env.get_template('projects.html').render(site=config['site'], projects=projects, sections=sections, root='../', title='Projects')
    (catalog_dir / 'index.html').write_text(catalog, encoding='utf-8')
    (DIST / 'projects.json').write_text(json.dumps(projects, ensure_ascii=False, indent=2), encoding='utf-8')
    not_found = env.get_template('404.html').render(site=config['site'], root='./', title='Not found')
    (DIST / '404.html').write_text(not_found, encoding='utf-8')
    sitemap = ['<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">', '<url><loc>REPLACE_WITH_SITE_URL/projects/</loc></url>']
    sitemap += [f'<url><loc>REPLACE_WITH_SITE_URL/wiki/{html.escape(p["slug"])}/</loc></url>' for p in pages]
    sitemap.append('</urlset>')
    (DIST / 'sitemap-template.xml').write_text('\n'.join(sitemap), encoding='utf-8')
    # The deployment workflow supplies the final public URL, including the GitHub
    # Pages project prefix. Relative page URLs also work at custom domains.
    public_url = os.environ.get('SKELMMC_DOCS_URL', '').strip().rstrip('/')
    if public_url:
        if not re.fullmatch(r'https://[^\s]+', public_url):
            raise ValueError('SKELMMC_DOCS_URL must be an HTTPS website URL')
        final_sitemap = '\n'.join(sitemap).replace('REPLACE_WITH_SITE_URL', html.escape(public_url))
        (DIST / 'sitemap.xml').write_text(final_sitemap, encoding='utf-8')
    # GitHub Pages should serve the generated HTML as-is (not process via Jekyll).
    (DIST / '.nojekyll').write_text('', encoding='utf-8')
    print(f'Built {len(pages)} documentation pages + homepage + directory for {len(projects)} project(s) into {DIST}')

if __name__ == '__main__':
    main()
