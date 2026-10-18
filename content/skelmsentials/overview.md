Skelmsentials is a modular essentials-plugin project for modern Minecraft Paper servers. The goal is to provide commonly requested commands, menus, teleportation features and server administration tools, while giving owners control over how they look and behave.

<div class="callout warning"><strong>Work in progress</strong><p>This documentation is based on the project design discussions. Features listed as planned are not claims that they currently exist in a released jar.</p></div>

## Core principles

- **Modular by design:** start with a reliable core before adding larger features.
- **Configurable branding:** replace default plugin prefixes and user-facing messages with your server's own name.
- **GUI-first where helpful:** menus for player actions and, later, optional shop features.
- **Modern compatibility:** develop against Paper 26.1 and newer, with supported versions verified in testing.
- **Predictable upgrades:** clear defaults, explicit configuration changes and documented migration steps.

## Feature areas

| Area | Purpose | Current docs status |
| --- | --- | --- |
| GUI menu | `/menu` and player navigation | Under development |
| Teleportation | Home, spawn, requests and delays | Planned / design |
| Player utilities | Heal, feed, god mode and similar commands | Planned / design |
| Messaging | Editable prefix, prompts and feedback | Foundation design |
| Shop | Inventory-based buying and selling | Planned |

## Choose a guide

<div class="doc-cards"><a href="../installation/"><strong>Installation →</strong><span>Prepare your server and load the plugin.</span></a><a href="../messages/"><strong>Messages & branding →</strong><span>Design the custom message system.</span></a><a href="../menus/"><strong>Menu GUI →</strong><span>Structure inventory-based menus.</span></a><a href="../compatibility/"><strong>Compatibility →</strong><span>Supported server builds and testing.</span></a></div>

## Release and compatibility policy

The target baseline is **Paper 26.1+**. Each version still needs its own compilation and runtime checks. Compatibility should only be marked "verified" after successful testing on that server release.

## Development status

Use the [Roadmap](../../platform/roadmap/) to distinguish active development from future work. The commands and configuration pages contain examples that must be validated against source code before launch.
