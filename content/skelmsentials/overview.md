<div class="callout warning"><strong>Development documentation — not a stable release</strong><p>The plugin repository currently has no installable release on its <strong>main</strong> branch. This reference describes code found on <strong>develop</strong> and separate beta feature branches. Do not assume all documented features are available in one published JAR.</p></div>

## Project at a glance

Skelmsentials is an Essentials-style plugin for modern Paper Minecraft servers, with configurable SkelmMC branding, player teleportation, homes, menus, economy, chat, and game modes. More features are being developed in separate branches.

| Git branch | Source version | What is included | Availability |
| --- | --- | --- | --- |
| `main` | Initial README and licence | No plugin source or release JAR | Not installable |
| `develop` | `1.1.0-foundation` | Homes, spawn, RTP, teleport requests, warps, `/back`, internal economy, chat colours/emojis, game modes, GUIs | Development source only |
| `feature/player-utilities-1.2` | `1.2.0-beta` | Foundation plus utility commands and a utilities GUI | Unmerged beta branch |
| `feature/shop-1.3` | `1.3.0-beta` | Utilities plus configurable shop and pricing tools | Unmerged beta branch |

Branch feature information is based on the actual `plugin.yml`, Java handlers and YAML defaults, not just a roadmap. It does **not** constitute a verified live release.

## Where to begin

- [Commands and permissions](../commands/) — see what exists in each source branch and how to use it.
- [Configuration](../configuration/) — feature switches, teleport delays, homes, economy and branding.
- [Player utilities](../utilities/) — the 1.2 beta commands, access, costs and warnings.
- [Shop and economy](../shop/) — the 1.3 beta shop, buying, selling and administration.
- [Messages and branding](../messages/) — choose the visible server name and edit MiniMessage text.
- [Changelog and branch status](../changelog/) — identify which milestone introduced each feature.

## Compatibility target

The Java 25 plugin targets **Paper 26.1.2, 26.2 and 26.3**. It is not advertised as Folia-compatible. Passing CI or source review is not equivalent to successful testing on your own server.

## Documentation status

This documentation was initially synchronized with the source on **18 October 2026**. It will be revised as the source changes and as features are merged or released. See the changelog for branch-specific status.
