import random

def main() -> None:
    print("=== Game Data Alchemist ===\n")
    players: list[str] = ["Pablo", "jesus", "Laura", "cele", "Meriem", "Alvaro", "Lucy", "juan", "jorge"]
    print(f"Initial list of players: {players}")
    all_caps: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_caps}")
    only_caps: list[str] = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {only_caps}")

    
if __name__ == "__main__":
    main()