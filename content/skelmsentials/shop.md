An inventory-based shop has been proposed as a possible Skelmsentials module. The intention is to give server owners a familiar purchasing interface, without making an economy integration mandatory for the rest of the essentials plugin.

<div class="callout info"><strong>Planned feature</strong><p>The shop is a design direction. No shop inventory, item prices or currency integration is claimed to exist yet.</p></div>

## Goals

- Open a category-based GUI through a command such as `/shop`.
- Support configurable item groups and prices.
- Handle buying and, optionally, selling.
- Integrate with an external economy provider when available.
- Restrict access by permission or world if desired.

## Example shop entry

A future shop could use entries along these lines:

```yaml
# Concept example; not an implemented file format
categories:
  blocks:
    title: "Building Blocks"
    entries:
      stone:
        material: STONE
        buy: 4.0
        sell: 1.0
```

## Economy design

A shop should use a narrow economy abstraction instead of coupling every menu handler to a particular provider. For Paper servers, an integration layer compatible with common economy plugins can be investigated, but it should not be presented as supported until tested.

## Transaction safety

- Check inventory capacity before charging for a purchase.
- Avoid duplicate transactions from repeated clicks.
- Validate prices and prevent zero/negative-price exploits.
- Keep payment and item delivery consistent when a transaction fails.
- Log meaningful errors for admins without exposing sensitive internal state to players.

## One plugin or separate jar?

A modular core can provide the shared GUI, messages and permission infrastructure. The shop can remain an optional module initially; if its dependencies and release cadence become substantially different, it can later move into a companion jar without rewriting the shared platform.
