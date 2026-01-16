def main() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter',
               'boss_slayer', 'speed_demon', 'perfectionist'}
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print("\n=== Achievement Analytics ===")
    unique = alice.union(bob, charlie)
    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)
    alice_intersection = alice.intersection(bob)
    bob_intersection = bob.intersection(charlie)
    charlie_intersection = charlie.intersection(alice)
    overlap = alice_intersection.union(bob_intersection, charlie_intersection)
    rare = unique.difference(overlap)
    alice_common = alice.intersection(bob)
    intersection = charlie.intersection(bob, alice)
    print(f"All unique achievements: {unique}")
    print(f"Total unique achievements: {len(unique)}\n")

    print(f"Common to all players: {intersection}")
    print(f"Rare achievements (1 player): {rare}")
    print(f"\nAlice vs Bob common: {alice_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


if __name__ == "__main__":
    main()
