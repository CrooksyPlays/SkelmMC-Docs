<div class="callout warning"><strong>Development / beta source only</strong><p>GUI handlers exist on `develop`. Utilities and Shop shortcuts come from later feature branches. All inventory actions must still be tested on the exact target Paper build.</p></div>

## Open the main menu

Run `/menu` (aliases `/essgui` and `/essentials`). The development menu provides navigation to player services, depending on which features are enabled:

| Action | Function |
| --- | --- |
| Homes | Saved home locations |
| Spawn | Server spawn |
| RTP | Random teleport |
| Teleport Requests | Request a teleport or respond to invitations |
| Warps | Server-managed public locations |
| Economy | Balance and payment GUI |
| Chat colours | Choose unlocked chat format presets |

The 1.2 beta adds a **Player Utilities** shortcut, and the 1.3 beta adds a **Shop** shortcut. These do not exist on the earlier `develop` branch.

## Customize the actual GUI defaults

The settings use `gui`, **not** a separate `menu.buttons` section:

~~~yaml
gui:
  enabled: true
  titles:
    main: '<gradient:#54daf4:#545eb6>{server} Menu</gradient>'
  items:
    main:
      homes:
        slot: 10
        material: RED_BED
        name: '<aqua>Homes</aqua>'
        lore: ['<gray>Manage your home locations</gray>']
      spawn:
        slot: 12
        material: COMPASS
        name: '<aqua>Spawn</aqua>'
        lore: ['<gray>Travel to spawn</gray>']
~~~

Other default main-menu slots on `develop` are RTP **14**, teleport players **16**, warps **28**, economy **30**, chat colours **32**, and incoming requests **34**. The 1.2 branch adds utilities at **40**.

Navigation arrows and back icons are under `gui.navigation`. Separate GUI titles live in `gui.titles`. Custom menu item icon/name/lore settings use the MiniMessage format.

## Enable and permissions

Use `features.gui` and `gui.enabled` to control menu availability. Individual modules (homes, RTP, warps, etc.) are independently toggleable under `features`. Opening the main menu uses `skelmsentials.use`; the actions inside still observe individual permissions.

## Test menu clicks before a release

Earlier pre-foundation beta testing exposed an inventory-click `NoSuchMethodError` from scheduler API mismatch. The exact latest compiled JAR should be tested for opening, moving between, and clicking menus before classifying the GUI as production-ready.
