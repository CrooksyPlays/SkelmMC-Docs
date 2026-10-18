Most plugin troubleshooting becomes easier when you can identify the exact server build, plugin build and failing operation. Keep full exception logs, not just the first line of the error.

## Plugin does not load

1. Check the Java runtime against the Paper version's requirements.
2. Look for the first error during plugin initialization.
3. Confirm the jar is the right build and was copied intact.
4. Check required dependencies and configuration parsing messages.
5. Restart the server after replacing files.

## Menu clicks throw an exception

An earlier Skelmsentials beta produced a stack trace similar to this:

```text
Could not pass event InventoryClickEvent to Skelmsentials v1.0.3-beta
java.lang.NoSuchMethodError:
  org.bukkit.scheduler.BukkitScheduler.runTaskLater(...)
```

A `NoSuchMethodError` usually means the code expects a method signature absent from the API available at runtime. Compare compile-time and server dependencies; inspect the method overloads in the target API; rebuild, then verify the actual jar on a clean test server.

<div class="callout warning"><strong>Avoid assuming it is just a configuration issue</strong><p>A missing method is a binary compatibility problem, not something ordinarily fixed by changing a YAML value.</p></div>

## A command says "unknown command"

Check whether the command actually exists in that build and whether it was registered successfully. Commands marked as planned in this documentation are not expected to work until implemented.

## A command works only for operators

Check the permission registration and default value, then inspect permission-plugin overrides. Use a fresh non-operator test account when verifying a permission rule.

## What to include in a bug report

- Minecraft version and exact Paper build.
- Java runtime version.
- Skelmsentials build and any other relevant plugins.
- Steps to reproduce (including the command or GUI click).
- Full console exception and relevant configuration files, with secrets removed.

## Debugging future updates

Keep regression cases for startup, `InventoryClickEvent`, teleport warmups and reload behavior. Automated testing and a small test server matrix can catch many version-specific failures before a public jar is released.
