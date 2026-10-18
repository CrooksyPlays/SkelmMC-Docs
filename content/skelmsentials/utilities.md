Player utilities are the planned lightweight command set administrators reach for every day: healing, feeding, temporary protection and other convenience actions.

<div class="callout warning"><strong>Not yet verified against a release</strong><p>The names and behavior on this page are feature designs, not promises that the commands are already available.</p></div>

## Heal and feed

`/heal [player]` would restore health without bypassing server restrictions, while `/feed [player]` would restore food level and saturation. If the target player argument is omitted, the command would normally affect the sender.

```text
/heal
/feed
/heal ExamplePlayer
```

Administrators may want separate permissions for self-targeting and targeting someone else.

## God mode

`/god [player]` is a proposed toggle for incoming damage immunity. Implementation should decide whether environmental damage, the void and custom plugin damage are affected, and whether the toggle persists across logout or restart.

## Flight and movement

Optional `/fly` and `/speed` commands could make player administration easier. They need careful permission checks, sane numeric ranges and predictable handling of game-mode changes.

## Data and lifecycle

Any persistent toggle should have a defined save strategy. Temporary player state must be cleaned up when the feature is disabled or when a player disconnects.

## Permissions

Permission design should separate normal self-use from actions targeting other players. The [Commands & permissions](../commands/) page contains candidate namespace conventions; final values require source verification.
