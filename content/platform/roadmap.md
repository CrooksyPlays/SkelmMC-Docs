<div class="callout warning"><strong>Development roadmap, not a release list.</strong><p>This plan reflects decisions from the SkelmMC project conversations and the Skelmsentials source checked on 18 October 2026. Planned systems are not available just because they are listed. In particular, the 1.4 alpha does not ship the later gameplay engines.</p></div>

## Milestone overview

| Milestone | Focus | Status |
| --- | --- | --- |
| 1.1 | Essentials foundation: homes, teleportation, economy, chat, gamemodes, GUI | Source on `develop` |
| 1.2 | Player utilities | Beta feature branch |
| 1.3 | Configurable server shop and selling | Beta feature branch |
| **1.4** | **Reversible server profiles, module controls, administration framework** | **`feature/modular-core-1.4`, alpha source** |
| **1.5** | **Survival skills, unlockable money-making professions and achievement tiers** | **Planned** |
| **1.6** | **Auction house, virtual double chests and block/container locks** | **Planned** |
| **1.7** | **Mob spawners, kill rewards, crates and keys** | **Planned** |
| **1.8** | **Staff-built events and zones** | **Planned** |
| **1.9** | **NPC dialogue and quests** | **Planned** |

The `main` branch is not yet an installable plugin release. A beta or alpha branch is evidence of development, **not** a stable version running on a production server.

## 1.4 — Modular core and safe server profiles

The first requirement is a dependable core for configuration and later content modules:

- Five profiles: **Survival**, **Prison**, **Factions**, **Minigames**, **Creative**. Presets are editable YAML, not hard-coded worlds.
- `/setserver list`, `status`, `preview <profile>`, `apply <profile>`, `confirm`, `backups` and `rollback <id>` manage these presets. `/skelmadmin` opens the in-game profiles/modules GUI.
- Show a full preview of the allowlisted Skelmsentials configuration values to be changed. Confirm changes **in-game within two minutes**.
- Before applying a profile, keep timestamped, checksummed configuration backups, an audit trail and recovery/rollback support. Invalid backups or disk errors must fail safely.
- Only **implemented** modules can be toggled now. Later systems, their subfeatures and individual content (for example, the Woodsman profession) will become individually toggleable as those systems are implemented.
- Both GUI actions and directly edited YAML must ultimately manage the **same validated definitions**. New-content editors will arrive with their respective gameplay engines; they are not functional in the present alpha.

**Non-negotiable:** switching profiles must not alter worlds, terrain, gamerules, inventories, player data or third-party plugin files. The current implementation only changes explicitly allowlisted Skelmsentials configuration keys; profiles are not world reset tools or multi-server synchronization.

The `1.4.0-alpha` branch already contains profile backup and rollback code and an administration GUI. Future professions, crates, events and NPCs are labelled *unavailable* in that menu rather than shown as functional. Read [Commands & permissions](../skelmsentials/commands/) for currently implemented alpha commands.

## 1.5 — Survival skills and professions

Build an integrated **mcMMO-style skills system plus money-earning jobs**:

- **All skills always progress**, even when their corresponding profession hasn't been unlocked.
- **Unlimited active jobs/professions**: discovery and achievement requirements control unlocking, not job slot limits.
- Examples: catch a fish to unlock **Fisherman**, mine a naturally occurring diamond to unlock **Miner**, harvest **64 logs** to unlock **Woodsman**.
- Progress through **achievement-based profession tiers**, with meaningful requirements and rewards.
- Give administrators both global jobs/skills toggles and finer switches for a particular profession, unlock, skill or reward.
- Permit staff to **create entirely new professions, achievements and tiers in-game and via YAML**, using one schema and validation system.
- Protect progression and payouts against placed-block loops, invalid activity, farming abuses and transaction failures.

**Status:** approved design, not a working module in 1.4.

## 1.6 — Auctions, vaults and locks

- Player-to-player **auction house**, including listings, bidding/buying behavior as designed, expiry and transaction safety.
- Persistent **54-slot virtual double chests/player vaults**, with permissions and safe storage operations.
- **Block and container locking** with clear ownership and configurable access rules.
- SQLite-backed storage where appropriate, atomic economy/item transfers, logs and duplication safeguards.

**Status:** planned. The existing 1.3 GUI shop is **not** an auction house.

## 1.7 — Spawners, crates and keys

- Configurable spawners for common peaceful mobs and hostile variants, including spawn limits and permissions.
- Eligible **spawner-spawned mob kills generate money**, with sensible anti-exploit limits and eligibility checks.
- Staff-managed **crates, keys and reward tables**, including independent enable/disable switches.
- Create and edit spawner settings, crates and rewards from **in-game administration tools and YAML** where supported by each implemented module.

**Status:** planned; money-generating mob spawners and crate engines are not implemented in 1.4.

## 1.8 — Events and zoning

- Staff can **create, operate and manage events** with detailed controls, including entry rules, time windows, rewards and lifecycle.
- **Zones/regions** to define where events take place and apply event-specific rules.
- Reusable event presets, in-game creation/editing, YAML definitions and individual event toggles.
- Auditable rewards and abuse prevention, without using server-profile switching to change world data.

**Status:** planned; the admin event/zoning system is not available in 1.4.

## 1.9 — NPCs, dialogues and quests

- Configurable NPCs, interaction rules, conversations and quest/progression hooks.
- In-game and YAML creation/editing of NPC definitions and dialogue trees.
- Optional integration with professions, achievements, events and economy rewards.

**Status:** planned; no complete NPC/quest engine exists in the current alpha.

## Cross-cutting design requirements

1. **Maximum modularity:** if a part could reasonably be its own plugin, it must be independently controllable. Where appropriate, individual subfeatures and created content must also be toggleable.
2. **Admin GUI and YAML parity:** administrators can create **new** content, not just adjust hard-coded presets, when each runtime system arrives. YAML must remain human-editable.
3. **Data safety:** disablement and profile changes must preserve configuration, player progress, economies and world data. Use backups, checksums, confirmations and recoverable writes.
4. **Economy integrity:** atomic transfers, SQLite where suitable, auditing, permissions and anti-exploit controls are part of done—not optional polish.
5. **Truthful release states:** show unimplemented systems as unavailable; verify commands and configuration in source; only mark a feature *released* after a real published build and runtime testing.
6. **Compatibility:** Java/Paper support is verified per published build, not inferred from a roadmap.

## Roadmap versus release documentation

This roadmap is the **agreed product direction** from the SkelmMC ChatGPT planning conversation. GitHub source code establishes **implemented development features**; tested release artifacts establish **released features**. See [Skelmsentials overview](../skelmsentials/overview/) and [changelog](../skelmsentials/changelog/) for that distinction. The documentation hub will eventually cover other SkelmMC projects too.
