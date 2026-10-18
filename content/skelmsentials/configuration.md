The long-term goal is one predictable configuration system, with feature-specific settings and clearly separated player-facing messages. This page shows a **proposed schema** rather than a guaranteed currently supported `config.yml`.

<div class="callout warning"><strong>Design example, not a drop-in configuration</strong><p>Do not paste this sample into a production server until the plugin has implemented the same keys and validation. The installed jar's generated defaults take precedence.</p></div>

## Proposed config.yml

```yaml
# Illustrative future schema only
plugin:
  enabled: true
  debug: false

teleportation:
  warmup-seconds: 3
  cancel-on-move: true
  cancel-on-damage: true

homes:
  enabled: true
  default-limit: 3

utilities:
  heal-enabled: true
  feed-enabled: true
  god-enabled: true

menu:
  enabled: true
  title: "&8SkelmMC Menu"
  rows: 3

shop:
  enabled: false
```

## Configuration principles

- Use descriptive keys that are stable across updates.
- Keep GUI layout separate from its command handlers.
- Provide a complete default file with comments and valid types.
- Validate material names, numbers, durations and missing values at startup.
- Keep user-facing strings in a dedicated messages file.
- Log the exact file and key when parsing fails.

## Reloading settings

Some settings can be safely reloaded; others may require rebuilding inventories, unregistering listeners, or restarting the server. Any reload command should document what it refreshes, and the plugin should warn when a restart is required.

## Migrating between versions

A migration strategy should keep unknown keys intact when possible, supply newly introduced defaults, and provide a changelog explaining renamed or deleted settings. A backup is always recommended before upgrades.
