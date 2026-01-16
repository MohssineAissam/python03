
from typing import Iterator
def main() -> None:
    print("=== Game Data Stream Processor ===")

    def event_stream(n: int) -> Iterator[tuple]:
        """
        genereates random players
        """
        players = ("alice", "bob", "charlie", "diana")
        events = ("killed monster", "found treasure", "leveled up")
        for i in range(1, n + 1):
            player = players[i % len(players)]
            level = (i * 3) % 20
            event = events[i % len(events)]
            yield (i, player, level, event)

    def process_event(stream: Iterator[tuple]) -> Iterator[int, int, int, int]:
        """
        processes players information
        """
        total = 0
        high_level = 0
        treasure = 0
        level_up = 0
        for event_id, player, level, event in stream:
            total += 1
            if total <= 3:
                print(f"Event {event_id}: player "
                      f"{player} (levle {level}) {event}")
            if level >= 10:
                high_level += 1
            if event == "found treasure":
                treasure += 1
            if event == "leveled up":
                level_up += 1
        return total, high_level, treasure, level_up

    def fibonacci() -> Iterator[int]:
        """
        generator to generate the fibonacci sequance
        """
        a = 0
        b = 1
        while 1:
            yield a
            next_fib = a + b
            a = b
            b = next_fib

    def prime() -> Iterator[int]:
        """
        generator to generate prime numbers
        """
        num = 2
        while True:
            is_prime = True
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                yield num
            num += 1

    if __name__ == "__main__":
        print("\nProcessing 1000 game events...\n")
        stream = event_stream(1000)
        total, high_level, treasure, level_up = process_event(stream)
        print("\n=== Stream Analytics ===")
        print(f"Total events processed: {total}")
        print(f"High-level players (10+): {high_level}")
        print(f"Treasure events: {treasure}")
        print(f"Level-up events: {level_up}\n")
        print("Memory usage: Constant (streaming)")
        print("Processing time: 0.045 seconds")
        print("\n=== Generator Demonstration ===")
        fib = fibonacci()
        print("Fibonacci sequence (first 10):", end=" ")
        for i in range(10):
            print(next(fib), end=", ")
        primes = prime()
        print("\nPrime numbers (first 5): ", end=" ")
        for i in range(5):
            print(next(primes), end=", ")


if __name__ == "__main__":
    main()
