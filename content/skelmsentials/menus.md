The main inventory GUI is intended to provide quick access to important features without expecting every player to memorize commands. This area covers design and implementation considerations for the `/menu` prototype.

## The menu command

```text
/menu
```

The menu should open a configurable inventory with clearly named actions such as homes, warps, utilities and, where installed, the shop. Specific layouts and clickable actions are **not final**.

## Proposed layout model

A simple slot-based configuration could look like this:

```yaml
# Illustrative design; not a confirmed config file
menu:
  title: "&8Server Menu"
  rows: 3
  buttons:
    homes:
      slot: 11
      material: RED_BED
      name: "&aHomes"
      action: "OPEN_HOMES"
    warps:
      slot: 13
      material: ENDER_PEARL
      name: "&bWarps"
      action: "OPEN_WARPS"
    shop:
      slot: 15
      material: EMERALD
      name: "&6Shop"
      action: "OPEN_SHOP"
```

## Inventory event safety

- Validate that the clicked inventory belongs to Skelmsentials.
- Guard against null items, shift-clicks, number-key swaps and closing inventories.
- Keep event handlers lightweight and move longer work into supported scheduler APIs.
- Avoid linking the code to unavailable or version-specific method signatures.
- Check GUI transitions after updating Paper and other plugins.

<div class="callout warning"><strong>Known development concern</strong><p>An earlier 1.0.3-beta log showed a <code>NoSuchMethodError</code> from an inventory-click handler calling a scheduler method. Ensure the plugin is compiled and tested against the intended API signature before considering the GUI ready for release.</p></div>

## Making menus extensible

Instead of hard-coding button behavior into a single command listener, define a small menu registry and action handlers. That lets more plugins add their own destinations later without forcing an entirely separate menu system.
