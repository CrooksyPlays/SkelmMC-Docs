This page is an initial command catalog **for design and review**. Commands should be generated or checked against the actual `plugin.yml`/runtime command registrations before publishing an authoritative release reference.

<div class="callout warning"><strong>Draft command matrix</strong><p>Except for the previously prototyped `/menu`, the entries below are proposed functionality. Permission nodes are proposed names, not guaranteed existing permission registrations.</p></div>

## Player commands

| Command | Intended behavior | Status |
| --- | --- | --- |
| `/menu` | Open the main server GUI | Prototype; retest |
| `/spawn` | Teleport to the configured spawn | Planned |
| `/sethome [name]` | Save a home location | Planned |
| `/home [name]` | Teleport to a saved home | Planned |
| `/delhome [name]` | Remove a saved home | Planned |
| `/tpa <player>` | Request teleportation | Planned |
| `/tpaccept` | Accept an incoming request | Planned |
| `/tpdeny` | Deny an incoming request | Planned |
| `/back` | Return to a previous location | Planned |
| `/warp [name]` | Teleport to a named warp | Planned |

## Utility and admin commands

| Command | Intended behavior | Status |
| --- | --- | --- |
| `/heal [player]` | Restore player health | Planned |
| `/feed [player]` | Restore hunger and saturation | Planned |
| `/god [player]` | Toggle damage protection | Planned |
| `/fly [player]` | Toggle flight where permitted | Proposed |
| `/speed <value>` | Adjust movement speed | Proposed |
| `/repair` | Repair permitted items | Proposed |
| `/setspawn` | Set the default spawn point | Planned |
| `/skelmsentials reload` | Reload safe configuration sections | Proposed |

## Permissions design

A predictable namespace makes permissions easier for admins to audit. These examples are **unconfirmed design candidates**:

```text
skelmsentials.command.menu
skelmsentials.command.home
skelmsentials.command.sethome
skelmsentials.command.heal
skelmsentials.command.feed
skelmsentials.command.god
skelmsentials.admin.reload
```

Before documenting defaults, define whether each node is granted to everyone, operators only, or neither. Permission plugins such as LuckPerms can then use the finalized nodes.

## Documentation automation

A future build step should inspect the plugin's command registrations and permission definitions, emitting a verified table for the website. This reduces the risk of documentation diverging from the jar after command renames or feature changes.
