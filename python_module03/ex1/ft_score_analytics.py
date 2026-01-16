import sys


def main() -> None:
    scores = []
    print("=== Player Score Analytics ===")
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            try:
                scores.append(int(sys.argv[i]))
            except ValueError:
                print(f"incompatible value "
                      f"`{sys.argv[i]}` please enter a number")
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(sys.argv) - 1}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {sum(scores) / len(scores):.2f}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")
    else:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
