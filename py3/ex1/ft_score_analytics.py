from sys import argv


class NoScoresError(Exception):
    def __init__(self, message: str = "No scores provided. Usage: python3"
                                      "ft_score_analytics.py"
                                      " <score1> <score2> ...") -> None:
        self.message = message
        super().__init__(message)


def parse_args(args: list[str]) -> list[int]:
    valid_input: bool = False
    scores: list[int] = []
    try:
        for arg in args:
            if arg == args[0]:
                continue
            else:
                try:
                    score: int = int(arg)
                    scores.append(score)
                    valid_input = True
                except ValueError:
                    print(f"Invalid parameter: '{arg}'")
        if not valid_input:
            raise NoScoresError()
    except NoScoresError as e:
        print(e)
    return scores


def print_stats(scores: list[int]) -> None:
    average: float = float((sum(scores))/(len(scores)))
    print(f"👀 Total players: {len(scores)}")
    print(f"🙌 Total score: {sum(scores)}")
    print(f"😐 Average score: {average:.1f}")
    print(f"💯 High score: {max(scores)}")
    print(f"😶 Low score: {min(scores)}")
    print(f"🧐 Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    print("=== 🥳 Player Score Analytics 🥳 ===")
    size = len(argv)
    scores: list[int] = parse_args(argv)
    print(f"Scores processed: {scores}")
    print_stats(scores)
