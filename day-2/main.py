import pathlib

import lib


def is_invalid(number):
    value = str(number)
    mp = len(value) // 2
    return value[:mp] == value[mp:]


def is_extra_invalid(number):
    print(f"CHECKING {number}", "*" * 40)
    value = str(number)
    list_value = list(value)
    mp = len(value) // 2

    for x in range(1, mp):
        chunks = [i for i in lib.n_chunks(list_value, x)]
        print(chunks)

    return True


def main():
    args = lib.parse_args()

    file_location = pathlib.Path(__file__).with_name(
        "actual.txt" if args.action_run else "example.txt"
    )
    data = lib.load_file(file_location)
    lines = []
    for pair in data[0].split(","):
        x, y = pair.split("-")
        lines.append((int(x), int(y)))

    dataset = []
    for x, y in lines:
        for z in range(x, y + 1):
            dataset.append(z)

    # Day 2 - Part 1
    invalids = [x for x in dataset if is_invalid(x)]
    print(f"Day 2, Part 1 -- Sum: {sum(invalids)}")

    # Day 2 - Part 2
    invalids = set()
    for row in dataset:
        value = str(row)
        list_value = list(value)
        mp = len(value) // 2
        if mp < 2:
            chunks = set([x[0] for x in lib.chunk(list_value, 1)])
            if len(chunks) == 1:
                invalids.add(row)

        for x in range(1, mp + 1):
            chunks = set(["".join(x) for x in lib.chunk(list_value, x)])
            if len(chunks) == 1:
                invalids.add(row)

    print(f"Day 2, Part 2 -- Sum: {sum(invalids)}")


if __name__ == "__main__":
    main()
