The SkelmMC Docs source can be maintained by the same team that develops Skelmsentials, with review steps to prevent the published site from promising unfinished features.

## Update a guide

Open its corresponding Markdown file in `content/`, make the edit and preview the static site locally.

```bash
python -m pip install -r requirements.txt
python build.py
cd dist
python -m http.server 8080
```

Then open `http://localhost:8080` in your browser and verify both mobile and desktop behavior.

## Documentation conventions

- Write specific, testable instructions.
- Label planned features and proposed config formats explicitly.
- Include copyable commands and minimal examples.
- Keep supported version claims tied to tested releases.
- Update permissions and configuration examples when code changes.
- Add a changelog entry for public feature changes.

## Add a new plugin

1. Create `content/new-plugin/`.
2. Add an overview and a getting-started guide.
3. Register the pages in `site.yml` under a new section.
4. Add a plugin card on the homepage when the documentation is ready.
5. Run `python build.py` and test the search results.

## Before publishing

A reviewer should compare the documentation against the compiled jar, command registrations, actual generated configuration and supported Paper versions. Preview content should not silently become official release documentation.
