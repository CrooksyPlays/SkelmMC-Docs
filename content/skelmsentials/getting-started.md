This first-run checklist will help you set up a stable baseline before enabling more complex features.

## First-run checklist

1. Confirm the Paper server and Java versions meet the requirements of your plugin build.
2. Install the jar and restart the server.
3. Read console output for errors or warnings.
4. Check the generated configuration files without assuming draft examples are implemented.
5. Test a documented, available command in game.
6. Verify permission behavior with a non-operator test account.

## Start with the menu

The project has been prototyped around a `/menu` GUI command. The menu's intended job is to serve as a clear starting point for common player actions and links to larger systems.

```text
/menu
```

<div class="callout warning"><strong>Implementation note</strong><p>An earlier Skelmsentials beta produced a scheduler API error when a player clicked the menu. That is a development issue to verify as resolved in the actual compiled release before presenting the menu as stable.</p></div>

## Configure the server identity

The project goal is to allow server owners to change messages such as:

```text
Skelmsentials - teleporting in 3
```

to an identity that fits their server:

```text
SkelmMC - teleporting in 3
```

See [Messages & branding](../messages/) for a proposed consistent approach to prefix and message variables.

## Next steps

- Review the [Commands & permissions](../commands/) page before assigning permissions.
- Learn the proposed [Configuration](../configuration/) layout.
- Explore the [Roadmap](../../platform/roadmap/) for upcoming utilities and the shop GUI.
