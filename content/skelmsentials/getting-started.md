<div class="callout warning"><strong>Development branch only</strong><p>The plugin's `main` branch does not yet publish a verified installable build. This guide is for configuring and testing a future build or a beta test JAR, not for claiming production readiness.</p></div>

## Set up a safe test server

1. Prepare a **Paper 26.1.2, 26.2 or 26.3** test server with **Java 25**.
2. Back up the complete server and existing `plugins/Skelmsentials/` folder before replacing any beta JAR.
3. Install only one Skelmsentials JAR in `plugins/` and restart.
4. Watch the console for an enable message, errors and version warnings.
5. Check the `plugins/Skelmsentials/config.yml` and `messages.yml` files.
6. Use a non-operator account to check normal permissions and an operator to check admin actions.

For the current development/release state, read [Installation](../installation/) before downloading or using a build.

## First useful commands

| Try | Expected purpose in the `develop` source |
| --- | --- |
| `/skelmsentials version` | Display plugin version and Paper version. |
| `/menu` | Open the main player GUI. |
| `/sethome base` | Save a home named `base`. |
| `/home base` | Travel back to `base` after the configured warmup. |
| `/tpa <player>` | Request to teleport to another online player. |
| `/balance` | Inspect the standalone economy balance. |

Game-mode shortcuts have separate permissions and default to operators. More details are in [Commands](../commands/).

## Use your SkelmMC brand

In `config.yml`:

~~~yaml
branding:
  name: 'SkelmMC'
  prefix: '<gradient:#00BFFF:#8A2BE2><bold>{server}</bold></gradient> <dark_gray>»</dark_gray> '
~~~

This changes what players see without renaming the internal plugin, its JAR metadata or its data folder. Customize the individual replies in `messages.yml`.

## What to test

Create and delete homes; verify teleport cancellation by walking; test RTP safety; open and click each enabled menu; check economy balances; restart and verify stored locations. For a **1.2/1.3 beta**, additionally test the utilities GUI, permissions, costs, and any shop trades with disposable test accounts.

Review [Configuration](../configuration/), [Player utilities](../utilities/) and [Shop](../shop/) for details specific to each branch.
