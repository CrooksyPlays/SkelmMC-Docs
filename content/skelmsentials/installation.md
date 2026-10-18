<div class="callout warning"><strong>No release on main yet</strong><p>The repository's `main` branch currently holds an initial README and licence, not an installable plugin JAR. Development and beta-branch code exists, but this documentation does not certify it as a production release.</p></div>

## Requirements

- A **Paper** server, with development targets **26.1.2**, **26.2** and **26.3**.
- **Java 25** for the development/beta JAR.
- A server backup and a staging environment for testing before production.
- No Folia support is claimed.

## Once a verified release is provided

1. Stop the Paper server.
2. Back up the whole server, especially `plugins/Skelmsentials/` and its `players.yml` and `locations.yml` files.
3. Remove the previous Skelmsentials JAR from `plugins/` to avoid loading multiple versions.
4. Place the new verified Skelmsentials JAR into `plugins/`. **Do not delete the existing data directory.**
5. Start the server and check the console for successful enablement and errors.
6. Edit `config.yml` and `messages.yml` for branding and messages; restart after version upgrades.
7. Test `/menu`, `/skelmsentials version`, a home teleport, permissions and menu clicks using a test account.

The 1.2 and 1.3 beta branch READMEs describe this replacement procedure for their test JARs, but they are **not production-ready release announcements**.

## Why the installation instructions are provisional

A real release needs a built JAR plus compatibility and behaviour testing. The repository's `main` branch does not currently have those deliverables. Check the [changelog](../changelog/) to see what belongs to which branch.
