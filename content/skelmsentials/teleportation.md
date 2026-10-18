<div class="callout warning"><strong>Development behaviour</strong><p>The commands on this page are implemented in the `develop` branch, but the repository's `main` branch has no installable release. Use a test server when a build becomes available.</p></div>

## Teleport delay and cancellation

The `develop` source has a configurable warm-up. Default:

~~~yaml
settings:
  teleport-delay-seconds: 3
  cancel-teleport-on-move: true
  cancel-teleport-on-damage: true
~~~

The plugin sends a teleport-start message and schedules the actual move after the configured delay (three seconds by default). **This is one initial message, not an automatic 3, 2, 1 countdown each second.** A pending teleport can be cancelled by movement or damage when those settings are enabled; another teleport cannot start while one is pending.

Change the visible text in `messages.yml` using the `teleport-start`, `teleport-done` and `teleport-cancelled` message keys.

## Homes

Use `/sethome` to save the default home or `/sethome <name>` to save a named home. `/home <name>` travels to it. `/home` can open the homes GUI or directly use the only saved home. Use `/delhome <name>` to remove one.

The default home limit is **3**, with configured optional permission increases (`settings.home-limit-permission-values`, initially 5, 10, 20 and 50).

## Spawn and warps

An operator can `/setspawn` at the desired location. Everyone with `skelmsentials.use` can `/spawn`. If `spawn.fallback-to-world-spawn` is enabled, the Minecraft world spawn acts as a fallback.

Operators set and delete public warps using `/setwarp <name>` and `/delwarp <name>`. Players use `/warp <name>`, `/warp` or `/warps`.

## Player requests

- `/tpa <player>` asks to travel to someone.
- `/tpahere <player>` asks them to travel to you.
- `/tpaccept` and `/tpdeny` respond; `/tprequests` opens the GUI.

Requests expire after **90 seconds** by default (`settings.teleport-request-expiry-seconds`). The current development code stores one pending incoming request per receiving player.

## Safe random teleport

`/rtp` chooses a random spot in the current Overworld; `/rtp [world]` can target a configured world. `/rtp gui` opens the world selector.

~~~yaml
rtp:
  enabled: true
  radius-min: 500
  radius-max: 4500
  attempts: 16
  cooldown-seconds: 300
  worlds: []
~~~

Candidates are checked against the world border, terrain and avoid-materials list. The module rejects Nether/End environments in this implementation. `skelmsentials.rtp.bypasscooldown` skips cooldowns.

## Previous position

`/back` returns to a tracked previous position when available; the foundation code keeps these previous-position entries in memory, so **do not expect them to survive a full server restart**.
