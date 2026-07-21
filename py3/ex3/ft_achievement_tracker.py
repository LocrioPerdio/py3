import random


def main():
    players: list = []
    players = init_players(players)
    distinct = set.union(*(player.achievements for player in players))
    common = set.intersection(*(player.achievements for player in players))
    print("=== Achievement Tracker System ===\n")
    for player in players:
        player.show()
    print("\nAll distinct achievements:", distinct)
    print("\nCommon achievements:", common)
    for player in players:
        only = unique_achievements(player, players)
        print(f"Only {player.name} has: {only}")
    print()
    for player in players:
        missing = distinct.difference(player.achievements)
        print(f"{player.name} is missing:", missing)


class Player:
    def __init__(self, name: str):
        self.name: str = name.capitalize()
        self.achievements: set = set()

    def show(self):
        print(f"Player {self.name}:", self.achievements)

    def gen_player_achievements(self) -> set:
        achievements: list = ["Exorcist", "Floraphobe", "Natural Selector",
                              "Galuf's Grail", "Limit Breaker",
                              "Adamant Will", "Master's Seal",
                              "Treasure Hunter", "Loremaster", "Superstar",
                              "Instrument of Fate", "Instrument of Dissent",
                              "Instrument of Tragedy", "Instrument of Flight",
                              "Instrument of Survival", "Instrument of Heal",
                              "Instrument of Shame"]
        number: int = random.randint(4, 10)
        player_achievements: list = random.sample(achievements, number)
        player_set: set = set(player_achievements)
        return player_set


def unique_achievements(player: Player, players: list[Player]) -> set:
    others = set.union(*(p.achievements for p in players if p != player))
    return player.achievements - others


def init_players(players: list) -> list:
    lbiosca = Player("laura")
    players.append(lbiosca)
    lbiosca.achievements = lbiosca.gen_player_achievements()
    parenas = Player("Pablo")
    parenas.achievements = parenas.gen_player_achievements()
    players.append(parenas)
    jleiva = Player("Jesus")
    jleiva.achievements = jleiva.gen_player_achievements()
    players.append(jleiva)
    lodazzan = Player("Cele")
    lodazzan.achievements = lodazzan.gen_player_achievements()
    players.append(lodazzan)
    return players


if __name__ == "__main__":
    main()
