from sys import argv

def main() -> None:
    inventory: dict = {}
    print("=== Inventory System Analysis ===")
    inventory = parse_args(argv, inventory)
    if inventory:
        print(f"Got inventory:", inventory)
        items = list(inventory.keys())
        values = list(inventory.values())
        total = sum(values)
        print(f"Item list:", items)
        print(f"Total quantity of {len(items)} items: {total}")
        for item in inventory:
            value = inventory[item]
            percentage = round(((value / total) * 100), 1)
            print(f"Item {item} represents: {percentage}%")
        max_item = find_max(inventory)
        print(f"Item most abundant: {max_item} with quantity {inventory[max_item]}")
        min_item = find_min(inventory, inventory[max_item])
        print(f"Item least abundant: {min_item} with quantity {inventory[min_item]}")
        inventory.update({"magic_item" : 1})
        print(f"Updated inventory:", inventory)


class DupError(Exception):
    def __init__ (self, message: str = "Duplicated element") -> None: 
        self.message = message

def find_max(inventory: dict) -> str:
    max_value = 0
    for item in inventory:
        value = inventory[item]
        if value > max_value:
            max_value = value
            max_item = item
    return(max_item)

def find_min(inventory: dict, max_value = int) -> str:
    min_value = max_value
    for item in inventory:
        value = inventory[item]
        if value < min_value:
            min_value = value
            min_item = item
    return min_item

def parse_args(args: list[str], inventory: dict) -> dict:
    if len(argv) == 1:
        print("No items provided")
    for arg in args[1:]:
        try:
            pair: list[str] = arg.split(":")
            if len(pair) > 2:
                raise SyntaxError("Invalid syntax")
            elif len(pair) == 1 or not pair[0].isalpha():
                raise SyntaxError(f"Error -invalid parameter '{pair[0]}'")
            elif not pair[1].isdigit():
                raise SyntaxError(f"Quantity error for 'key': invalid literal for int() with base 10: '{pair[1]}'")
            elif pair[0] in inventory.keys():
                raise DupError(f"Redundant item '{pair[0]}' - discarding")
            else:
                inventory[pair[0]] = int(pair[1])
        except Exception as e:
            print(e)
    return inventory

if __name__ == "__main__":
    main()