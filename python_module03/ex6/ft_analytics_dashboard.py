def main() -> None:
    print("=== Game Analytics Dashboard ===\n")

    print("=== List Comprehension Examples ===")

    players = [("Alice", 2300, "north", "Active", 5),
               ("Bob", 1800, "east", "Active", 3),
               ("Charlie", 2150, "central", "Active", 7),
               ("Diana", 2050, "west", "Unactive", 2)
               ]
    achievment = ["First Kill", "Boss Slayer",
                  "First Kill", "Level 10", "Level 10", "First Kill"]
#     achievments = [5, 3, 7]
    difficulty_count = [3, 2, 1]
    difficulty = ["high", "medium", "low"]
    high_scores = [player[0] for player in players if player[1] > 2000]
    double_scores = [player[1] * 2 for player in players]
    active_players = [player[0] for player in players if player[3] == "Active"]
    print("High scorers (>2000): ", high_scores)
    print("Scores doubled: ", double_scores)
    print("Active players: ", active_players)
    print("\n=== Dict Comprehension Examples ===")
    d = {key: value for (key, value, _, s, _) in players if s == "Active"}
    print("Player scores:", d)
    score_categorie = {difficulty[i]:difficulty_count[i]  for i
                       in range(len(difficulty))}
    print("Score categories:", score_categorie)
    achievement_count = {key: c for (key, _, _, s, c)
                         in players if s == "Active"}
    print("Achievement counts", achievement_count)
    print("\n=== Set Comprehension Examples ===")
    unique_names = {name[0] for name in players}
    unique_achievments = {achievment for achievment in achievment}
    active_regions = {p[2] for p in players if p[3] == "Active"}
    print(unique_names)
    print(unique_achievments)
    print("Active regions:", active_regions)
    print("\n=== Combined Analysis ===")
    total_player = len(players)
    avg_score = sum([p[1] for p in players]) / total_player
    top_player = max([(p[1], p) for p in players])[1]
    print("Total players:", total_player)
    print("Total unique achievements:", len(unique_achievments) )
    print("Average score:", avg_score)
    print(f"Top performer: {top_player[0]}"
          f" ({top_player[1]} points {top_player[4]} achievements)")


if __name__ == "__main__":
    main()
