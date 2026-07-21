import random

def main() -> None:
    print("=== Game Data Alchemist ===\n")
    players: list[str] = ["Pablo", "jesus", "Laura", "cele", "Meriem", "Alvaro", "Lucy", "juan", "jorge"]
    print(f"Initial list of players: {players}")
    all_caps: list[str] = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_caps}")
    only_caps: list[str] = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {only_caps}")
    score_dict: dict = {name: random.randint(90,700) for name in only_caps}
    print(f"Score dict: {score_dict}")
    size: int = len(only_caps)
    total_scores: int = sum(score_dict.values())
    average: float = (total_scores / size)
    print(f"Score average is: {average:.2f}")
    high_scores: dict = {name: score_dict[name] for name in score_dict if score_dict[name] > average}
    print(f"High scores: {high_scores}")

if __name__ == "__main__":
    main()