<div class="callout warning"><strong>Development branch reference</strong><p>Branding and editable message formatting are present in development source, but no stable release is published from `main` yet.</p></div>

## Make chat show SkelmMC

Keep the internal plugin ID `Skelmsentials` so plugin folders and data stay compatible. In `plugins/Skelmsentials/config.yml`, configure:

~~~yaml
branding:
  name: 'SkelmMC'
  prefix: '<gradient:#00BFFF:#8A2BE2><bold>{server}</bold></gradient> <dark_gray>»</dark_gray> '
~~~

The token `{server}` becomes `SkelmMC`. MiniMessage supports normal colours, HEX values and gradients.

## Change player-facing messages

Player command messages belong in `plugins/Skelmsentials/messages.yml`. Example:

~~~yaml
messages:
  teleport-start: '<yellow>Teleporting in {seconds} seconds. Please stand still.</yellow>'
  teleport-cancelled: '<red>Teleport cancelled.</red>'
  reload: '<green>{server} configuration reloaded.</green>'
~~~

This lets you change text without recompiling the plugin. The source also defines player-facing feedback for homes, warps, requests, RTP cooldowns, currency and game-mode actions.

Some message templates use placeholders such as `{seconds}`, `<player>` and `<home>`. Preserve each template's required placeholders when changing it.

## Reload and upgrading

Use `/skelmsentials reload` or `/bc reload` for supported configuration and message changes. The beta READMEs state that customized `messages.yml` is retained on upgrades and missing message keys can fall back to bundled defaults. Back up your existing files before an upgrade.

The **1.3 beta** also migrates older default branding and changes the Utilities Repair icon to a Mace while retaining other custom icon settings.
