SkelmMC Docs brings every SkelmMC project into one knowledge base. Each plugin gets its own guides, reference pages, support topics and release notes, while site-wide search finds answers across the ecosystem.

<div class="callout info"><strong>Currently listed</strong><p>Skelmsentials is the first documented SkelmMC plugin. Other projects will appear when their documentation is ready; we will not list hypothetical products as released.</p></div>

## Browse SkelmMC projects

Visit the [project directory](../../../projects/) for a catalog of documented projects. Select a project to open its overview, then use the left navigation to find commands, installation steps and configuration examples.

## Shared across all projects

- **Global search:** press Ctrl+K (Windows/Linux) or ⌘ K (macOS) to find a page from any project.
- **Dedicated areas:** each project has a collapsible sidebar section, its own guides and release notes.
- **Consistent layout:** every plugin uses the same content conventions, code highlighting and article navigation.
- **Verified publication:** plans and examples are marked as drafts until checked against plugin source and releases.

## Adding a project

For maintainers, run `python scripts/add_project.py --slug sample-plugin --name "Sample Plugin"` from the site source folder. The helper creates six starter articles and registers the project in `site.yml`. Review the generated draft pages, then rebuild the site with `python build.py`.
