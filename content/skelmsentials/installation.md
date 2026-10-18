Follow this checklist to prepare a Paper server for a Skelmsentials build. This page covers the standard Java-plugin installation flow; exact release artifacts will be linked when the project has a public release process.

## Before you install

- Use **Paper 26.1 or newer**, subject to version-specific testing.
- Install the Java runtime required by your target Paper release.
- Back up your server files before changing plugins.
- Use a build explicitly released for your Minecraft version.

<div class="callout warning"><strong>Version support is a target</strong><p>Paper 26.1+ is the development baseline, not proof that every later Paper release works unchanged. Always check the release notes and test after a major server upgrade.</p></div>

## Install the plugin

1. Stop the server completely.
2. Place the built Skelmsentials `.jar` inside the server's `plugins/` folder.
3. Start the server and inspect the console for startup errors.
4. Check whether a `plugins/Skelmsentials/` directory was created and review any generated default files.
5. Join the server and verify the commands that are actually present in that build.

A typical server directory looks like:

```text
paper-server/
├── plugins/
│   └── Skelmsentials.jar
├── server.properties
└── paper.yml
```

## Confirm the plugin loaded

In the server console, look for a successful enable message and check `/plugins` in game if you have permission to use it. Do not assume that a green entry alone confirms all GUI and command handlers work; open the menus and exercise the relevant features as part of testing.

## After the first startup

Review the [Configuration](../configuration/) and [Messages & branding](../messages/) designs. Some examples in those pages are proposed rather than guaranteed configuration keys; only modify keys your installed release actually supports.

## Updating an existing installation

Make a copy of the jar and generated configuration. Replace the jar while the server is stopped, review any documented changes, and restart. Do not use `/reload` as a substitute for a clean restart when testing plugin behavior.
