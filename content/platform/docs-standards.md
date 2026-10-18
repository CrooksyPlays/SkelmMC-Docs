This hub is a common documentation home for SkelmMC projects. These standards keep instructions understandable and, once a release is verified, dependable.

## Each project has its own documentation

A plugin section normally includes an overview, installation, getting started, commands and permissions, configuration, troubleshooting, compatibility and a changelog. Project-specific topics can be added at any time.

## Accuracy and release status

<div class="callout warning"><strong>Starter documentation</strong><p>Several Skelmsentials pages in this preview describe proposed commands and configuration structures. They are not an authoritative description of shipped plugin features.</p></div>

- Keep example commands and permission nodes aligned with the release they apply to.
- Clearly mark a **draft** or **planned** command until it actually ships.
- Include tested Paper/Minecraft compatibility per release rather than silently applying one version range to every project.
- Update a project's changelog and migration notes when behavior changes.

## Suggested source of truth

For future automation, generate known commands, permissions and default configuration keys from release artifacts or the plugin source repository. Human-written tutorials remain Markdown and can be reviewed separately. Automatic extraction is a roadmap item, **not** a feature included in this starter.

## Shared design and search

All projects use one responsive theme, site-wide search, copyable code examples, and consistent URL paths: `/wiki/<project>/<article>/`. Projects are registered in `site.yml`; docs are in `content/<project>/`.
