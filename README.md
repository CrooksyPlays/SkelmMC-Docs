# SkelmMC Documentation Hub

A responsive, searchable documentation hub for **all** SkelmMC projects. It follows the multi-plugin *use case* of [EcoHub](https://hub.auxilor.io/wiki/eco/home) with its own design.

## Start here — Windows

1. Extract the **whole ZIP** into a folder. Don't run scripts from inside the ZIP or copy only the script.
2. Install Python 3 from [python.org](https://www.python.org/downloads/) if you don't already have it. Ensure `py` or `python` works in your terminal.
3. **Double-click `START-HERE.bat`** in the extracted `SkelmMC-Docs-Hub` folder.
4. Choose **1** to preview the included website, **2** to add a project, or **3** to rebuild the site.

Option 1 only uses the Python standard library. Adding or rebuilding a project automatically creates an isolated `.venv` and installs the packages required for the build. An internet connection may be needed for first-time dependency installation.

## macOS / Linux

From the extracted directory:

```bash
./START-HERE.sh
```

Or use the same direct CLI commands as below, replacing `py` with `python3`.

## Commands — Windows PowerShell or Command Prompt

**Run these from the extracted `SkelmMC-Docs-Hub` directory** (the folder that contains `manage.py` and `site.yml`):

```powershell
# Preview the already-built website (requires no extra Python libraries)
py manage.py preview

# Add a new project, then automatically rebuild the site
py manage.py add --slug skelm-shop --name "SkelmShop"

# Rebuild after editing Markdown or site.yml
py manage.py build
```

Opening `http://localhost:8080/` shows the preview. Leave the terminal open while previewing, and press `Ctrl+C` to stop. If port 8080 is busy, run `py manage.py preview --port 8081`.

If `py` is not recognized, use `python` in place of `py`. If Python itself is not installed, install it first. The preview server is needed for search; opening `dist/index.html` with a `file://` URL doesn't allow local JSON requests in many browsers.

**Note:** The `skelm-shop` name above is only an example. Use a unique slug for each new project. Running the same add command again will correctly report that the project already exists.

## Original commands (manual setup)

If you prefer calling scripts directly, install the build dependencies **first**:

```powershell
py -m pip install -r requirements.txt
py scripts/add_project.py --slug skelm-shop --name "SkelmShop"
py build.py
```

The original add and build scripts need `PyYAML` and other dependencies; the `manage.py` launcher automates this setup instead.

## Edit documentation

- `site.yml`: global site identity, projects, navigation, and page registration.
- `content/<project>/`: Markdown articles for each independent SkelmMC project.
- `assets/`: JavaScript, CSS, favicon.
- `templates/`: templates for the homepage, project directory, and articles.
- `dist/`: generated static output, ready to upload to a hosting provider.

New projects automatically appear in the projects directory, sidebar and site-wide search index after building. The generated article templates are intentionally labelled as drafts, not working-plugin feature specifications.

## Free GitHub Pages hosting

This package is **ready for free GitHub Pages deployment** using `.github/workflows/deploy.yml`. Follow [GITHUB-PAGES.md](GITHUB-PAGES.md) to create the public `CrooksyPlays/SkelmMC-Docs` repository, publish it at `https://docs.skelm.xyz/`, and automatically rebuild the website whenever documentation changes. You do **not** have to keep Python running locally after publishing.

## Deploy

**Primary website domain:** `docs.skelm.xyz` (requires a DNS CNAME and GitHub Pages custom-domain setting). `mc.skelm.xyz` stays assigned to the Minecraft server.


- **Cloudflare Pages:** build command `python -m pip install -r requirements.txt && python build.py`, output folder `dist`.
- **Netlify:** same build command, publish folder `dist`.
- **GitHub Pages:** build with GitHub Actions and publish the contents of `dist/`.
- **Any static hosting service:** upload the contents of `dist/` to the web root.

Before production publishing, set the real site URL in `dist/sitemap-template.xml` and verify plugin commands, permissions and configuration against shipped versions. The current Skelmsentials documentation is a **preview**.

## Troubleshooting

| Error | What to do |
| --- | --- |
| `'py' is not recognized` | Try `python` or install Python 3. |
| `No module named 'yaml'` | Use `py manage.py build` or `py manage.py add`, which installs requirements automatically. |
| `can't open file 'scripts/add_project.py'` | Change directory into the extracted `SkelmMC-Docs-Hub` folder, not `dist`. |
| `Project slug already registered` | Pick a new slug, or edit the existing project under `content/<slug>/`. |
| `Address already in use` | Run `py manage.py preview --port 8081`. |
| `pip install` fails | Verify Internet access and check the error message; rerun `py manage.py setup`. |
| `python` opens Microsoft Store | Install Python from python.org, or use the Windows `py` launcher. |

This site is designed as a centralized SkelmMC docs hub. A future improvement is to generate the commands, permissions and config docs from verified GitHub plugin releases.
