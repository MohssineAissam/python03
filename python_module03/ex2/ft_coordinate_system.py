import math


def main() -> None:
    print("=== Game Coordinate System ===\n")
    cords_list = ["10", "20", "5"]
    try:
        cords = tuple(int(i)for i in cords_list)
        print(f"Position created: {cords}")
        distance = math.sqrt(
              cords[0]**2 +
              cords[1]**2 +
              cords[2]**2)
        print(f"Distance between (0, 0, 0) and {cords} {distance:.2f}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}\n"
              f"Error details - {type(e).__name__},Args (\"{e.args}\")")

    cords_str = "3", "4", "0"
    print("\nParsing coordinates: \"3,4,0\"")
    try:
        scords = tuple(int(i)for i in cords_str)
        print(f"Position created: {scords}")
        sdistance = math.sqrt(
              scords[0]**2 +
              scords[1]**2 +
              scords[2]**2)
        print(f"Distance between (0, 0, 0) and {scords} {sdistance:.2f}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}\n"
              f"Error details - {type(e).__name__},Args (\"{e}\")")

    invalid_cords = "abc", "def", "ghi"
    print("\nParsing coordinates: \"abc,def,ghi\"")
    try:
        invalid = tuple(int(i)for i in invalid_cords)
        print(f"Position created: {invalid}")
        invalid_distance = math.sqrt(
              invalid[0]**2 +
              invalid[1]**2 +
              invalid[2]**2)
        print(f"Distance between (0, 0, 0)"
              f" and {invalid_cords} {invalid_distance:.2f}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}\n"
              f"Error details - {type(e).__name__},Args (\"{e}\")")
    print("Unpacking demonstration:")
    x, y, z = scords
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
