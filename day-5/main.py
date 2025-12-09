import functools
import pathlib

import lib


def main():
    args = lib.parse_args()

    file_location = pathlib.Path(__file__).with_name(
        "actual.txt" if args.action_run else "example.txt"
    )
    data = lib.load_file(file_location)
    in_db = True
    fresh_ranges = []
    ingredients = []

    for line in data:
        if line == "":
            in_db = False
            continue
        if in_db:
            min_r, max_r = line.split("-")
            fresh_ranges.append((int(min_r), int(max_r)))
        else:
            ingredients.append(int(line))

    # Day 5 - Part 1
    fresh = set()
    for min_r, max_r in fresh_ranges:
        fresh.update([x for x in ingredients if min_r <= x <= max_r])
    print(f"Day 5, Part 1 -- Fresh ingredients: {len(fresh)}")

    # Day 5 - Part 2
    def merge(list_to_merge):
        def combine(accumulator, xy):
            if accumulator:
                a, b = accumulator[0]
                etc = accumulator[1:]
                x, y = xy

                if y >= b:
                    return [xy] + etc
                elif y >= a:
                    return [(x, b)] + etc
                else:
                    return [xy] + accumulator
            else:
                return [xy]

        def tup_sort(ab):
            a, b = ab
            return ab if a <= b else (b, a)

        return functools.reduce(
            combine, sorted(map(tup_sort, list_to_merge), reverse=True), []
        )

    consolidated = merge(fresh_ranges)
    quantity = sum([max_r - min_r + 1 for max_r, min_r in consolidated])

    print(f"Day 5, Part 2 -- Quantity: {quantity}")


if __name__ == "__main__":
    main()
