from typing import Generator
import random


def main() -> None:
    print("=== Game Data Stream Processor ===")
    print_1000()
    event_list: list[tuple] = gen_list()
    print(f"Built list of 10 events: {event_list}")
    size = len(event_list)
    for event in range(size):
        gen = consume_event(event_list)
        event = next(gen)
        print(f"Got event from list: {event}")
        event_list = next(gen)
        print(f"Remains in list: {event_list}")


def gen_event() -> Generator:
    players: list[str] = ["laura", "pablo", "jesus", "cele"]
    actions: list[str] = ["run", "eat", "sleep", "smash PC", "heal", "move",
                          "climb", "catch Pokemon", "breed Chocobo"]
    player: str = random.choice(players)
    yield player
    action: str = random.choice(actions)
    yield action


def consume_event(events: list[tuple]):
    event = random.choice(events)
    events.remove(event)
    yield event
    yield events


def gen_list() -> list[tuple]:
    event_list: list[tuple] = []
    for _ in range(10):
        gen = gen_event()
        event: tuple = (next(gen), next(gen))
        event_list.append(event)
    return event_list


def print_1000() -> None:
    for number in range(1000):
        event = gen_event()
        print(f"Event {number}: Player {next(event)} did action {next(event)}")


if __name__ == "__main__":
    main()
