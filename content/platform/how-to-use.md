The documentation website is intentionally easy to maintain. It is made of Markdown files, a small site configuration file, and a static build step. You do not need to maintain a database or a content-management server.

## Finding documentation

- Use the **sidebar** to browse topics by plugin.
- Press **Ctrl+K** or **⌘ K** to search titles, headings and full article content.
- Use **On this page** to jump to an article heading on large screens.
- Use the light/dark button in the top-right corner to change the theme.

## Editing an article

Find the page's `.md` file in the `content/` folder, change the text, and rebuild the site. For example, the commands page is at:

```text
content/skelmsentials/commands.md
```

Use Markdown headings (`##` and `###`), tables and fenced code blocks. Do not put a top-level `#` heading in the Markdown file, because the page template generates its title automatically.

## Adding a new page

Create a Markdown file and add its slug, title and path to the appropriate section in `site.yml`:

```yaml
- slug: skelmsentials/example
  title: Example guide
  file: content/skelmsentials/example.md
```

Then regenerate the static site:

```bash
python -m pip install -r requirements.txt
python build.py
```

The search index and article navigation are generated from the same content and site configuration.

## Publishing changes

Upload the `dist/` folder to a static host. Cloudflare Pages, Netlify, and GitHub Pages can also rebuild it automatically from a connected repository.

<div class="callout"><strong>Recommended workflow</strong><p>Keep this website in its own GitHub repository, use a pull request for documentation changes, and publish automatically after a reviewed merge. That keeps experimental documentation separate from released plugin behavior.</p></div>
