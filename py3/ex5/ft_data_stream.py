from typing import Generator
import random

def main() -> None:
    print("=== Game Data Stream Processor ===")
    print_1000()
    
def gen_event() -> Generator:
    players: list[str] = ["laura", "pablo", "jesus", "cele"]
    actions: list[str] = ["run", "eat", "sleep", "smash PC", "heal", "move", "climb", "catch Pokemon", "breed Chocobo", ]
    player: str = random.choice(players)
    yield player
    action: str = random.choice(actions)
    yield action

def print_1000() -> None:
    for number in range(1000):
        event = gen_event()
        print(f"Event {number}: Player {next(event)} did action {next(event)}")


if __name__ == "__main__":
    main()