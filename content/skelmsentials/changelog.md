<div class="callout warning"><strong>Development history</strong><p>This is a source-branch tracker, not a public release changelog. No installable release has been confirmed on `main`.</p></div>

## Source snapshot — 18 October 2026

| Branch | Commit | Milestone |
| --- | --- | --- |
| `main` | `e3cd59c` | Initial README and licence only |
| `develop` | `e2c1064` | 1.1.0 foundation source |
| `feature/player-utilities-1.2` | `c5cdd85` | 1.2.0-beta utilities |
| `feature/shop-1.3` | `b1b45aa` | 1.3.0-beta GUI shop and branding polish |
| `feature/modular-core-1.4` | `82cdb18` | 1.4.0-alpha reversible profiles and modular admin GUI |

## 1.1.0-foundation — `develop`

- Command handlers for homes, public warps, spawn, RTP, teleport requests, back, internal economy, chat preset/emoji shortcuts and GUI menus.
- Game-mode commands and selector GUI with separate permissions.
- Branding and MiniMessage-backed messages, feature switches and configurable menus.
- Paper 26.1.2 baseline with Java 25 target; further versions still need verification.

## 1.2.0-beta — `feature/player-utilities-1.2`

- Player utility commands: heal, feed, god, fly, speed, repair, hat, workbench, ender chest, trash, anvil.
- `/utilities` GUI and shortcut in `/menu`.
- Per-command enablement, cooldowns, optional costs and permission checks.
- Guardrails including explicit trash inventory warning and configurable god-mode behaviour.

## 1.3.0-beta — `feature/shop-1.3`

- `/shop` with 10 starter categories and 200+ items, buy/sell quantity selector and paged inventory menus.
- `/sell`, `/sellall`, `/worth` and administrative price/reload commands.
- Configurable `shop.yml` and transaction protections; trades currently use internal economy rather than Vault.
- Player-visible branding defaults to `SkelmMC`, Repair icon switched to **Mace**, and menu migration fixes.

## 1.4.0-alpha — `feature/modular-core-1.4`

- Adds YAML-editable Survival, Prison, Factions, Minigames and Creative server profiles.
- Implements `/setserver` listing, preview, explicit confirmation, checksummed config backups and rollback; `/skelmadmin` exposes profiles and switches for existing modules.
- Profile changes are restricted to allowlisted Skelmsentials configuration, not worlds, gamerules, inventories, player records or third-party data.
- Future profession, event, crate and NPC editors are **visibly unavailable** pending their runtime implementations. The [1.4–1.9 roadmap](../../platform/roadmap/) records the approved direction.

## Release policy

Features will only be marked **released** once they appear in a published build and the relevant server/gameplay checks are confirmed. An unmerged feature branch is never proof of a stable release. This page will be updated when source branches or releases change.
