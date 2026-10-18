Teleportation is a planned core module covering homes, warps, spawn points, teleport requests and safe cancellation. The following describes the proposed behavior, not a released contract.

## Warmups and cancellation

A common server rule is to delay certain teleports for a few seconds, then cancel if the player moves or takes damage.

```text
SkelmMC » Teleporting in 3...
SkelmMC » Teleporting in 2...
SkelmMC » Teleporting in 1...
SkelmMC » Teleported successfully!
```

Possible configuration controls include per-command delays, combat restrictions, movement tolerance and permission-based delay exemptions.

## Homes

The planned home system would allow saving and removing named locations. Questions to settle include whether limits are global or permission-based, whether worlds can be excluded and how unloaded chunks are handled.

## Teleport requests

A robust request flow should have an expiry time, clearly identify the requester, and clean up pending requests on logout. Repeated requests should not flood another player with messages.

## Safe destinations

- Validate loaded worlds and accessible destination blocks.
- Prevent suffocation, unsafe lava placement and falling into the void.
- Avoid sending players to coordinates in deleted worlds.
- Store world identifiers and positions in a format that survives restarts.

## Cross-version behavior

Paper versions can change event APIs and scheduler behavior. Teleport mechanics need runtime tests on each supported release, particularly when chunk loading or player state transitions are involved.
