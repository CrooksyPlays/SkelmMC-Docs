<div class="callout warning"><strong>1.2 / 1.3 beta branches only</strong><p>These commands were verified in the player-utilities feature source, but they are not in `develop` or `main`. They are not documented as a stable public release.</p></div>

## Open the utilities menu

Use `/utilities` (aliases `/utility` and `/utilgui`) to open the player utilities GUI. The menu shortcut also appears in `/menu` in the 1.2 beta code. Access to the GUI defaults to everyone via `skelmsentials.utilities.utilities`, although individual actions remain permission-restricted.

## Utility commands

| Command | What it does | Important note |
| --- | --- | --- |
| `/heal [player]` | Restore health. | Default cooldown 60 seconds. |
| `/feed [player]` | Restore hunger/saturation. | Default cooldown 60 seconds. |
| `/god [player]` | Toggle invulnerability. | Session-only by default; void protection off by default. |
| `/fly [player]` | Toggle flight. | Does not replace Creative/Spectator flight. |
| `/speed <1-10> [player]` | Set walk speed or flight speed when flying. | Accepts levels from 1 to 10. |
| `/repair` | Repair a damageable item in your hand. | Default cooldown 180 seconds. |
| `/hat` | Equip one held item as a hat. | Returns/drops an existing helmet safely. |
| `/workbench` | Open virtual crafting. | Alias `/craft`. |
| `/enderchest` | Open your ender chest. | Alias `/ec`. |
| `/trash` | Open a disposal inventory. | **Items inside are permanently destroyed when closed.** |
| `/anvil` | Open virtual anvil. | Permission controlled. |

The command-specific permissions follow `skelmsentials.utilities.<command>` and default to **operators**. Permission `skelmsentials.utilities.others` allows administering other players; `skelmsentials.utilities.bypasscooldown` skips command cooldowns. `skelmsentials.utilities.*` grants them together.

## Configure each action

~~~yaml
features:
  utilities: true
utilities:
  god-persistent: false
  god-protect-void: false
  commands:
    heal: {enabled: true, cooldown-seconds: 60, cost: 0.0}
    feed: {enabled: true, cooldown-seconds: 60, cost: 0.0}
    repair: {enabled: true, cooldown-seconds: 180, cost: 0.0}
~~~

These entries exist in the 1.2 branch's `config.yml`. Other utility commands use the same `enabled` / `cooldown-seconds` / `cost` structure. Costs use the internal economy; paid actions cannot work while economy is disabled.

## GUI appearance

Customize `utilities.gui-title` and `utilities.gui-items.<action>` to change icons, names, lore and slots. The **1.3 beta** additionally changes the Repair menu icon from an anvil to a **Mace**, including a migration for an older default icon.

For installations upgrading between beta versions, keep the `plugins/Skelmsentials` folder and back it up before changing JARs.
