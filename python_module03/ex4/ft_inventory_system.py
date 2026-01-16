def analyze_inventory(inventory: dict) -> None:
    """
    Manage and track inventory using dictionary

    Args:
        inventory:(dict)
    """
    print("=== Inventory System Analysis ===")
    total_items = 0
    for i in inventory.values():
        total_items += i.get("quantity")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print("\n=== Current Inventory ===")
    for key, value in inventory.items():
        qt = value.get("quantity")
        percentage = (qt / total_items * 100)
        print(f"{key}: {qt} units ({percentage:.1f})%")

    print("\n=== Inventory Statistics ===")

    highest_qt, most_abundat_item = max((v["quantity"], k)
                                        for k, v in inventory.items())
    least_abundat_item, highest_qt = min((k, v["quantity"])
                                         for k, v in inventory.items())
    print(f"Most abundant: {most_abundat_item} ({highest_qt} units)")
    print(f"Least abundant: {least_abundat_item}, ({highest_qt} units)")

    print("\n=== Item Categories ===")

    moderate = {k: v["quantity"] for k, v
                in inventory.items() if v["quantity"] >= 5}
    scarce = {k: v["quantity"] for k, v
              in inventory.items() if v["quantity"] < 5}
    print(f"Moderate: {moderate}")
    print(f"Scarce: ({scarce})")

    print("\n=== Management Suggestions ===")

    restock = [key for key, value
               in inventory.items() if value.get("quantity") <= 1]
    print(f"Restock needed: {restock}")

    print("\n=== Dictionary Properties Demo ===")

    keys = [key for key in inventory.keys()]
    values = [key["quantity"] for key in inventory.values()]
    print(f"Dictionary keys: {keys}")
    print(f"Dictionary values : {values}")
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


def main() -> None:
    inventory = {
        "potion": {"quantity": 5},
        "armor": {"quantity": 3},
        "shield": {"quantity": 2},
        "sword": {"quantity": 1},
        "helmet": {"quantity": 1},
        }
    analyze_inventory(inventory)


if __name__ == "__main__":
    main()

# print("=== Player Inventory System ===\n")
# total_value = 0
# updated_total_value = 0
# updated_items = 0
# items = 0
# alice_inventory = {"sword": {"type": "weapon", "rarety": "rare",
#                              "quantity": "1", "price": "500"},
#                    "potion": {"type": "consumable", "rarety": "common",
#                               "quantity": "5", "price": "50"},
#                    "shield": {"type": "armor", "rarety": "uncommon",
#                               "quantity": "1", "price": "200"}}
# bob_inventory = {"magic ring": {
#     "type": "weapon", "rarety": "rare", "quantity": "1", "price": "500"}}
# to_bob = 2
# print("=== Alice's Inventory ===")
# for key, value in alice_inventory.items():
#     qt = int(value.get("quantity"))
#     pr = int(value.get("price"))
#     total_gold = qt * pr
#     total_value += total_gold
#     items += qt
#     print(f"{key} ({value.get("type")}, "
#           f"{value.get("rarety")}): "
#           f"{qt}x @ {pr} gold each = {total_gold} gold")

# print(f"\nInventory value: {total_value} gold")
# print(f"Item count: {items} items")
# print(
#     f"Categories: weapon({alice_inventory['sword']["quantity"]}), "
#     f"consumable({alice_inventory['potion']["quantity"]}), "
#     f"armor({alice_inventory['shield']["quantity"]})")
# print(f"\n=== Transaction: Alice gives Bob {to_bob} potions ===")
# alice_potion = alice_inventory.get("potion")
# alice_potion.update({"quantity": int(alice_potion.get("quantity")) - to_bob})
# bob_inventory.update({"potion": {
#     "type": "consumable", "rarety": "common",
#     "quantity": to_bob, "price": "50"}})
# print("Transaction successful!\n")

# print("=== Updated Inventories ===")
# print(f"Alice potions: {alice_inventory.get("potion").get("quantity")}")
# print(f"Bob potions: {bob_inventory.get("potion").get("quantity")}")
# print("\n=== Inventory Analytics ===")
# for key, value in alice_inventory.items():
#     qt = int(value.get("quantity"))
#     pr = int(value.get("price"))
#     updated_total_gold = (qt * pr)
#     updated_total_value += updated_total_gold
#     updated_items += qt
# bob_total_value = 0
# bob_items = 0
# for key, value in bob_inventory.items():
#     qt = int(value.get("quantity"))
#     pr = int(value.get("price"))
#     bob_total_gold = (qt * pr)
#     bob_total_value += bob_total_gold
#     bob_items += qt
# if updated_total_gold > bob_total_gold:
#     winner = "Alice"
# elif bob_total_gold > updated_total_gold:
#     winner = "Bob"
# else:
#     winner = "it's a tie"
# print(f"Most valuable player: {winner} {updated_total_value}")
# if updated_total_gold > bob_total_gold:
#     item_winner = "Alice"
# elif bob_total_gold > updated_total_gold:
#     item_winner = "Bob"
# else:
#     item_winner = "it's a tie"
# print(f"Most items: {item_winner}")
# all_players = [alice_inventory, bob_inventory]
# rarest = []
# for details in all_players:
#     for key, value in details.items():
#         if value.get("rarety") == "rare":
#             rarest.append(key)
# i = 0

# print("Rarest items:", *rarest, sep=", ")
