<div class="callout warning"><strong>Target vs verified support</strong><p>The source targets particular Paper versions, but a passing build or console smoke test does not establish complete compatibility. Check the exact JAR on a staging server.</p></div>

## Development baseline

| Environment | Source-code position |
| --- | --- |
| Paper **26.1.2** | Intended compile/minimum server baseline |
| Paper **26.2** and **26.3** | Target test versions in beta CI |
| Paper **26.1.1** or earlier | Rejected by the source's version guard |
| Later Paper versions | Can start with a warning; not automatically verified |
| Java | **25** for the current development/beta builds |
| Folia | **Not supported** |
| Spigot/Purpur | No verified support promise |

The `PaperCompatibility` class checks Minecraft version and rejects older or malformed values. `plugin.yml` declares `api-version: '26.1'`, which is not a guarantee that all patch versions of 26.1 are supported.

## Testing coverage

The beta branches describe GitHub Actions compiling against the Paper 26.1.2 API and booting server builds for 26.1.2, 26.2 and 26.3 to conduct **console smoke tests**. They explicitly call out the need for real-player GUI clicks, permissions and trades on a test server.

A successful compilation is not enough: also verify `/menu` inventory interactions, teleports/warmups, configuration reload, data persistence, utility actions, and shop transactions before production use.

## Troubleshooting binary mismatches

`NoSuchMethodError` can indicate the plugin was compiled against a different Paper scheduler/API signature than the server provides. Check the full stack trace, the JAR build and the exact Paper version instead of attempting to solve a binary error through config changes.

See [Troubleshooting](../troubleshooting/) for diagnostics.
