One of the key design requirements for Skelmsentials is **editable output branding**. Servers should not be forced to show a hard-coded Skelmsentials prefix when they want their own identity.

## The intended result

**Default-style output**

```text
Skelmsentials - teleporting in 3
```

**Customized output**

```text
SkelmMC - teleporting in 3
```

The goal is to configure the prefix once and reuse it consistently, rather than replacing text in dozens of different messages.

## Proposed messages.yml

<div class="callout info"><strong>Example configuration only</strong><p>These keys illustrate a design choice. Match them against the released plugin before using them.</p></div>

```yaml
# Illustrative future schema only
prefix: "&aSkelmMC &8» &r"

teleport:
  countdown: "&7Teleporting in &a{seconds}&7..."
  cancelled-moved: "&cTeleportation cancelled: you moved."
  successful: "&aTeleported successfully!"

utility:
  healed: "&aYour health has been restored."
  fed: "&aYour hunger has been restored."

errors:
  no-permission: "&cYou don't have permission to do that."
  player-not-found: "&cThat player isn't online."
```

## Variables and formatting

The proposed system uses named placeholders like `{seconds}` and `{player}` for clarity. Color handling should be chosen deliberately: either legacy `&` codes, MiniMessage, or both with clearly documented precedence and escaping.

## Consistent feedback

- Send helpful explanations when permissions block a command.
- Distinguish a cancelled teleport from an internal error.
- Provide sensible fallback text if a message key is missing.
- Avoid formatting codes leaking into console logs.

## Testing changes

Use a development server, vary each supported placeholder, and check messages with and without permissions. Do not let a malformed message entry prevent the entire plugin from enabling.
