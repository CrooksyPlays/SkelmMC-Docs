Skelmsentials is intended to support **Minecraft/Paper 26.1 and newer**. That is the target baseline for development, with actual compatibility depending on the binary and API checks performed against each release.

## Support policy

| Environment | Position |
| --- | --- |
| Paper 26.1+ | Target platform; each release requires verification |
| Spigot | Not promised without dedicated testing |
| Purpur | Not promised without dedicated testing |
| Folia | Not supported by default; scheduler behavior must be adapted and tested |
| Older Minecraft server versions | Outside the stated target baseline |

## Runtime and build requirements

Build Java plugins with an explicit target and the Paper API version you intend to support. Use the Java runtime required by the respective Paper build; avoid documenting one universal Java version for all future Minecraft releases.

## Why version compatibility is important

- Plugin classes and methods may move or change between APIs.
- Scheduler calls can fail at runtime if a binary was compiled against an incompatible signature.
- GUI events can behave differently under changed server implementations.
- Serialization formats and registries may shift across versions.

## Minimum verification matrix

For every new Paper release under consideration, run startup/shutdown tests, basic command tests, menu inventory clicks, teleport scenarios and configuration loading. Record exact server versions and jar builds alongside the results.

## Test failures

If you see `NoSuchMethodError`, first compare the Paper API used to compile the plugin with the server on which you are executing it. See [Troubleshooting](../troubleshooting/) for a practical checklist.
