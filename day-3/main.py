import pathlib

import lib


def main():
    args = lib.parse_args()

    file_location = pathlib.Path(__file__).with_name(
        "actual.txt" if args.action_run else "example.txt"
    )
    data = lib.load_file(file_location)

    # Day 3 - Part 1
    joltage = 0
    for line in data:
        highest = 0
        for x in range(len(line) - 1):
            first, second = line[x], sorted(line[x + 1 :])[-1]
            value = int(first + second)
            highest = max(highest, value)
        joltage += highest
    print(f"Day 3, Part 1 -- Joltage: {joltage}")

    # Day 3 - Part 2
    joltage = 0
    for line in data:
        n = len(line)
        results = []
        current = 0

        for i in range(12):
            remaining = 12 - i
            end = n - remaining
            max_d = "-1"
            max_idx = -1

            for j in range(current, end + 1):
                digit = line[j]
                if digit > max_d:
                    max_d = digit
                    max_idx = j
                if max_d == "9":
                    break

            results.append(max_d)
            current = max_idx + 1
        highest = int("".join(results))
        joltage += highest

    print(f"Day 3, Part 2 -- Joltage: {joltage}")


if __name__ == "__main__":
    main()
