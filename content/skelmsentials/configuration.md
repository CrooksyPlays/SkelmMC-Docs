<div class="callout warning"><strong>Development defaults</strong><p>These keys are from the <strong>develop</strong> branch unless marked beta. Always back up your existing configuration and check the file bundled with your installed JAR.</p></div>

## Configuration files

| File | Purpose |
| --- | --- |
| `plugins/Skelmsentials/config.yml` | Server branding, feature switches, teleportation, homes, economy, menus, chat and game-mode settings. |
| `plugins/Skelmsentials/messages.yml` | Customizable player-facing messages. |
| `plugins/Skelmsentials/players.yml` | Player-related stored data; back this up before upgrades. |
| `plugins/Skelmsentials/locations.yml` | Stored spawn and warp locations; back this up. |
| `plugins/Skelmsentials/shop.yml` | Shop categories, item prices and settings, **1.3 beta branch only**. |

## Change the displayed name

The internal plugin name remains `Skelmsentials`. Change the visible name and prefix in `config.yml`:

~~~yaml
branding:
  name: 'SkelmMC'
  prefix: '<gradient:#00BFFF:#8A2BE2><bold>{server}</bold></gradient> <dark_gray>»</dark_gray> '
~~~

`{server}` expands to `branding.name`. MiniMessage tags support colours and gradients. Change message bodies in `messages.yml` rather than editing code.

## Enable or disable modules

~~~yaml
features:
  gui: true
  homes: true
  spawn: true
  rtp: true
  tpa: true
  warps: true
  back: true
  economy: true
  chat: true
  gamemodes: true
~~~

These are the foundation modules. `features.utilities` was added in the **1.2 beta** branch and `features.shop` in the **1.3 beta** branch. Disabled modules also block their corresponding GUI actions.

## Home and teleport settings

~~~yaml
settings:
  teleport-delay-seconds: 3
  cancel-teleport-on-move: true
  cancel-teleport-on-damage: true
  home-limit: 3
  home-limit-permission-values: [5, 10, 20, 50]
  teleport-request-expiry-seconds: 90
  back-enabled: true
rtp:
  enabled: true
  radius-min: 500
  radius-max: 4500
  attempts: 16
  cooldown-seconds: 300
  worlds: []
~~~

The delay controls countdown time before teleportation; movement and damage can cancel it. Empty `rtp.worlds` uses the player's current world. The RTP safety list is under `rtp.avoid-materials`. `spawn.fallback-to-world-spawn` defaults to `true`.

## Economy and chat

~~~yaml
economy:
  enabled: true
  currency-name: 'Coins'
  currency-symbol: '⛃'
  starting-balance: 100.00
  max-transfer: 100000000.00
chat:
  enabled: true
  default-preset: normal
  allow-player-minimessage: true
  emoji-enabled: true
~~~

Chat presets have a `name`, `style`, `material` and `permission` under `chat.presets.<id>`. Defaults include `normal`, `aqua`, `sunset`, `birdflop` and `rainbow`. Chat emoji aliases are under `chat.emoji`.

## Menus and game modes

`gui.titles` sets GUI titles; `gui.items.main` controls icons, names, lore and slots on the main menu. `gui.navigation` controls paging and back buttons. Game modes use `gamemode.enabled`, `gamemode.allow-other-players`, `gamemode.gui-enabled`, `gamemode.gui-title` and `gamemode.gui-items`.

## Beta-only configuration

- **1.2 utilities:** `utilities.commands.<action>.enabled`, `cooldown-seconds` and `cost`; `utilities.gui-items`; `utilities.god-persistent` and `utilities.god-protect-void`.
- **1.3 shop:** `features.shop`, `shop.enabled` and `shop.max-wallet-balance` in `config.yml`; item categories and buy/sell prices in `shop.yml`.

Use [utilities](../utilities/) and [shop](../shop/) for the commands and side effects.

## 1.4 modular profiles (unreleased alpha)

The `feature/modular-core-1.4` source introduces editable `profiles/survival.yml`, `prison.yml`, `factions.yml`, `minigames.yml` and `creative.yml` under `plugins/Skelmsentials/`. Each profile may change only the explicitly allowlisted plugin configuration keys.

- `/setserver preview <profile>` prints the changes; `/setserver apply <profile>` asks for **in-game confirmation within two minutes**.
- `/setserver backups` lists checksummed configuration backups saved under `backups/profile-config/`; `/setserver rollback <id>` requests a separately confirmed restore.
- `/skelmadmin` controls profiles and **implemented** modules. Planned professions, events, crates and NPCs appear as unavailable.
- Profiles must never touch world files, terrain, gamerules, inventories, player records or third-party plugin data.
- In-game **new-content creation**, paired with editable YAML, is planned for later modules (jobs, tiers, spawners, crates, events and NPCs); it does not work in 1.4 alpha.

See the [1.4–1.9 roadmap](../../platform/roadmap/) for the agreed requirements.

## Apply changes

Use `/skelmsentials reload` (or `/bc reload`) for supported configuration/message changes. **Restart the server for command or permission changes and after installing/upgrading a JAR.** Keep backups of your original YAML and player/location data.
