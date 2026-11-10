from typing import Dict


def merge_inventory(*stores: Dict[str, int]) -> Dict[str, int]:
    inventory: Dict[str, int] = {}
    for store in stores:
        for product, quantity in store.items():
            inventory[product] = inventory.get(product, 0) + quantity
    return inventory


def get_stock(inventory: Dict[str, int], product: str) -> int:
    return inventory.get(product, 0)


def low_stock(inventory: Dict[str, int], limit: int = 15) -> Dict[str, int]:
    return {p: q for p, q in inventory.items() if q < limit}


def add_inventory(inventory: Dict[str, int], updates: Dict[str, int]) -> Dict[str, int]:
    for product, qty in updates.items():
        inventory[product] = inventory.get(product, 0) + qty
    return inventory


def main():
    store1 = {"Laptop": 10, "Mouse": 25, "Keyboard": 15, "Monitor": 8}
    store2 = {"Laptop": 5, "Mouse": 20, "Headphones": 12, "Monitor": 7}
    store3 = {"Laptop": 3, "Keyboard": 10, "Headphones": 8}

    inventory = merge_inventory(store1, store2, store3)
    print("Combined Inventory:")
    for item, count in sorted(inventory.items()):
        print(f"  {item:<12}: {count}")

    print(f"\nLaptop stock : {get_stock(inventory, 'Laptop')}")
    print(f"Tablet stock : {get_stock(inventory, 'Tablet')}")

    print("\nLow Stock Items (< 16 units):")
    print(low_stock(inventory, 16))

    new_shipment = {"Laptop": 5, "Tablet": 10}
    add_inventory(inventory, new_shipment)
    print("\nUpdated Inventory (After Shipment):")
    for item, count in sorted(inventory.items()):
        print(f"  {item:<12}: {count}")


if __name__ == "__main__":
    main()
