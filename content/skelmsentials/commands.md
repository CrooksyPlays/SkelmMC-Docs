<div class="callout warning"><strong>Source reference, not a released command list</strong><p>The foundation commands below exist in the <strong>develop</strong> branch (1.1.0-foundation). Utilities exist in the 1.2 beta branch, shop commands in the 1.3 beta branch, and profile commands in the 1.4 alpha branch. The <strong>main</strong> branch does not yet contain a runnable plugin.</p></div>

## General and player commands — `develop`

| Command | How to use it |
| --- | --- |
| `/menu` | Open the main server GUI (aliases: `/essgui`, `/essentials`). |
| `/sethome [name]` | Save your location; defaults to `home` when omitted. |
| `/home [name]` | Teleport to a saved home; with no name, teleports if there is one home or opens the homes GUI. |
| `/homes`, `/home gui` | Open the homes GUI. |
| `/delhome <name>` | Delete a saved home. |
| `/spawn` | Teleport to the configured spawn. `/spawn gui` opens its GUI. |
| `/rtp [world]` | Find a safe random location; `/rtp gui` opens world choices. Alias: `/wild`. |
| `/tpa [player]` | Ask to teleport to an online player. Without a player, opens a selector. |
| `/tpahere [player]` | Ask another player to teleport to you. |
| `/tpaccept [player]` | Accept a request (optionally naming sender); `/tpaccept gui` opens requests. |
| `/tpdeny [player]` | Deny a request; `/tpdeny gui` opens requests. |
| `/tprequests` | Open incoming teleport requests GUI. |
| `/back` | Return to a recent location if one is recorded and the feature is enabled. |
| `/warp [name]` | Teleport to a warp or show the warps GUI with no name. |
| `/warps` | Open the public warps GUI. |
| `/balance` | View your internal balance; aliases `/bal`, `/money`. `/balance gui` opens the economy GUI. |
| `/pay <player> <amount>` | Transfer money to an online player; missing arguments open the player/payment GUI. |
| `/economy gui` | Open the economy GUI; alias `/eco`. |
| `/chatcolor [preset]` | Choose a permitted preset or open the colour selector. Alias `/ccolor`. |
| `/emoji` | List configured chat emoji aliases. |
| `/gamemodes` | Open the game-mode selection GUI, if permitted; alias `/gmgui`. |
| `/gmc [player]`, `/gms [player]` | Set Creative or Survival. |
| `/gmsp [player]`, `/gma [player]` | Set Spectator or Adventure. |
| `/skelmsentials help` | Display plugin commands; aliases `/sk`, `/skelms`, `/bc`. |
| `/skelmsentials version` | Display the plugin version and running Paper version. |

### Admin commands — `develop`

| Command | Description |
| --- | --- |
| `/setspawn` | Save spawn at your location. |
| `/setwarp <name>` | Create a public warp at your location. |
| `/delwarp <name>` | Remove a warp. |
| `/eco set <online-player> <amount>` | Set an internal balance. |
| `/eco give <online-player> <amount>` | Add money to a player. |
| `/eco take <online-player> <amount>` | Remove money (minimum zero). |
| `/skelmsentials reload` | Reload configuration, presentation and cached emoji; alias `/bc reload`. |

Administrative commands above use `skelmsentials.admin` (operator by default). Most player commands use `skelmsentials.use` (granted by default), and can also be individually disabled via `features` in `config.yml`. The game-mode shortcuts additionally check their specific game-mode permissions.

## Additional beta-branch commands

The following are **not on develop or main as of this snapshot**:

| Branch | Commands |
| --- | --- |
| `feature/player-utilities-1.2` | `/utilities`, `/heal`, `/feed`, `/god`, `/fly`, `/speed`, `/repair`, `/hat`, `/workbench` (alias `/craft`), `/enderchest` (alias `/ec`), `/trash`, `/anvil` |
| `feature/shop-1.3` | `/shop`, `/sell`, `/sellall`, `/worth`, `/shopadmin` |

### Modular-core commands — `feature/modular-core-1.4` alpha

The following commands exist in the **unreleased alpha source**. They require `skelmsentials.profiles.admin` (operator by default) or `skelmsentials.admin`.

| Command | Purpose |
| --- | --- |
| `/setserver list` | List Survival, Prison, Factions, Minigames and Creative presets. |
| `/setserver status` | Display the active profile and any recovery lock. |
| `/setserver preview survival` | Show the changes to supported Skelmsentials configuration values, without applying. |
| `/setserver apply survival` | Preview and request an in-game confirmation within two minutes. |
| `/setserver confirm` | Confirm the pending profile/module change or rollback **in-game**; a checked config backup is created first for changes. |
| `/setserver backups` | List recent backup IDs. |
| `/setserver rollback <id>` | Prepare to restore a verified backup; needs separate in-game confirmation. |
| `/skelmadmin` | Open the GUI for profiles and already implemented modules. Planned systems are marked unavailable. |

Switching profiles never resets worlds, inventories or player data. The in-game editors for professions, crates, events and NPCs are future modules. See [the roadmap](../../platform/roadmap/).

See [utilities](../utilities/) and [shop](../shop/) for usage and important safety notes.

## Permission nodes — foundation

| Permission | Default | Purpose |
| --- | --- | --- |
| `skelmsentials.use` | Everyone | Foundation player commands. |
| `skelmsentials.admin` | Operators | Spawn/warp management, economy admin, reload. |
| `skelmsentials.homes.10` | Operators | One home-limit override. Additional `homes.<number>` values are configured in `settings.home-limit-permission-values`. |
| `skelmsentials.rtp.bypasscooldown` | Operators | Skip RTP cooldown. |
| `skelmsentials.chat.format` | Operators | Use limited MiniMessage tags in chat if enabled. |
| `skelmsentials.chat.allcolors` | Operators | Access any configured chat preset. |
| `skelmsentials.gamemode.creative` / `survival` / `spectator` / `adventure` | Operators | Individual game-mode access. |
| `skelmsentials.gamemode.others` | Operators | Set another player's mode. |
| `skelmsentials.gamemode.gui` | Operators | Access game-mode GUI. |
| `skelmsentials.gamemode.*` and `skelmsentials.*` | Operators | Group permissions defined in `plugin.yml`. |

Shop: `skelmsentials.shop.use` defaults to everyone; `skelmsentials.shop.admin` to operators. Utilities: `skelmsentials.utilities.utilities` (GUI) defaults to everyone; action permissions and `skelmsentials.utilities.others` default to operators.

**Important:** Server owners can change effective access using a permissions manager such as LuckPerms. Permissions mentioned here are from each branch's `plugin.yml`, not guesses.
