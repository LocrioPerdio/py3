from sys import argv

class NoScoresError(Exception):
        def __init__(self, message: str = 
            "No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...") -> None:
            self.message = message

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    size = len(argv)
    counter = 1
    if size == 1
        raise NoScoresError
    