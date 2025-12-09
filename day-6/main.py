import math
import pathlib
import re

import lib


def main():
    args = lib.parse_args()

    file_location = pathlib.Path(__file__).with_name(
        "actual.txt" if args.action_run else "example.txt"
    )
    data = lib.load_file(file_location)
    raw_clean = []
    for line in data:
        if line == "":
            continue
        cleaned = re.sub(r"\s+", " ", line)
        items = cleaned.split(" ")
        try:
            raw_clean.append([int(x) for x in items])
        except:
            raw_clean.append(items)

    problems = list(zip(*raw_clean))

    # Day 6 - Part 1
    def calc(problem):
        match problem[-1]:
            case "+":
                return sum(problem[:-1])
            case "*":
                return math.prod(problem[:-1])

    values = [calc(x) for x in problems]
    print(f"Day 6, Part 1 -- Total: {sum(values)}")

    # Day 6 - Part 2
    data = lib.load_file(file_location, strip_chars=False)
    fixed_data = []
    max_len = max([len(x) for x in data])
    for line in data:
        missing = max_len - len(line)
        new_line = line + " " * missing
        fixed_data.append(new_line.replace("\n", " "))

    raw_cleaned = list(zip(*[list(str(x)) for x in fixed_data]))
    blocks = []
    current = []
    for item in raw_cleaned:
        if all([x == " " for x in item]):
            if current:
                blocks.append(current)
            current = []
        else:
            current.append(item)

    problems = []
    for block in blocks:
        operator = ""
        problem = []
        for row in block:
            num = int("".join(row[:-1]))
            if row[-1] != " ":
                operator = row[-1]
            problem.append(num)
        problem.append(operator)
        problems.append(problem)

    values = [calc(x) for x in problems]
    print(f"Day 6, Part 2 -- Total: {sum(values)}")


if __name__ == "__main__":
    main()
