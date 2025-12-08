import pathlib

import lib


def main():
    args = lib.parse_args()

    file_location = pathlib.Path(__file__).with_name(
        "actual.txt" if args.action_run else "example.txt"
    )
    data = lib.load_file(file_location)

    # Day 1 - Part 1
    current = 50
    count = 0
    for line in data:
        value = int(line[1:])
        if line[0] == "L":
            value = value * -1

        current = (current + value) % 100
        if current == 0:
            count += 1

    print(f"Day 1, Part 1 -- Count: {count}")

    # Day 1 - Part 2
    current = 50
    count = 0
    for line in data:
        value = int(line[1:])
        direction = 1 if line[0] == "R" else -1
        for _ in range(value):
            current = (current + direction) % 100
            if current == 0:
                count += 1

    print(f"Day 1, Part 2 -- Count: {count}")


if __name__ == "__main__":
    main()
