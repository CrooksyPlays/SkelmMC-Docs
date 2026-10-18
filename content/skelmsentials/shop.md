<div class="callout warning"><strong>1.3.0-beta feature branch only</strong><p>The shop is implemented on `feature/shop-1.3`, not on the repository's current `main` or `develop` branch. This is a test implementation that still needs real player trade/GUI testing.</p></div>

## How players use the shop

1. Use `/shop` to open the shop GUI (requires `skelmsentials.shop.use`, granted by default).
2. Select one of the default **10 item categories**.
3. Choose an item and select a buy or sell quantity: **1, 16, 32, 64 or 128**.
4. Confirm the trade in the GUI; use the menu's option to sell all matching eligible items where appropriate.

The beta catalog includes **200+ items**. Prices use the symbol configured under `economy.currency-symbol`.

## Quick commands

| Command | Effect |
| --- | --- |
| `/shop` | Open the shop GUI. |
| `/sell` | Sell eligible items held in your hand. |
| `/sell all` or `/sellall` | Sell eligible **plain** items from main inventory storage. |
| `/worth` | Show the unit sell price of your held item. |
| `/shopadmin list` | List catalog entries (operator by default). |
| `/shopadmin reload` | Reload shop catalog changes. |
| `/shopadmin price <category> <item-id> buy|sell <amount>` | Change an item price. |

For example: `/shopadmin price ores diamond buy 1200` changes the diamond buy price in the `ores` category to 1200 currency units (subject to the implementation's price parser).

## Configuration

The beta includes `plugins/Skelmsentials/shop.yml` with category IDs, names, materials, permissions, enabled status, per-item `buy` / `sell` prices, GUI titles and world/transaction limits. Setting `buy: 0` or `sell: 0` disables that transaction direction.

`config.yml` also includes `features.shop`, `shop.enabled` and `shop.max-wallet-balance`. Existing `shop.yml` files are preserved during upgrades; you can edit prices in YAML then run `/shopadmin reload`.

## Permissions

- `skelmsentials.shop.use` — open/trade in the shop, **everyone by default**.
- `skelmsentials.shop.admin` — price changes/reload, **operators by default**.
- Individual catalog products may have additional permission restrictions.

## Important limitations

- Trades use the **Skelmsentials internal economy**. Shop balances are not currently integrated with Vault.
- Purchases check inventory capacity before charging; transactions use checked integer-cents arithmetic.
- Bulk selling accepts only eligible plain vanilla items, reducing accidental sale of customized/enchanted equipment.
- There is **no multi-server shared wallet, dynamic stock, auction house, or drag-and-drop catalog editor** in this beta.
- Shop prices are starter examples. Review them on a backup server before allowing production trading.

See [commands](../commands/) for foundation economy commands and [configuration](../configuration/) for more settings.
