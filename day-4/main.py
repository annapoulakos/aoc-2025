import pathlib

import lib


def main():
    args = lib.parse_args()

    file_location = pathlib.Path(__file__).with_name(
        "actual.txt" if args.action_run else "example.txt"
    )
    data = lib.load_file(file_location)

    # Day 4 - Part 1
    locations = [list(line) for line in data]
    rows, cols = len(locations), len(locations[0])
    rolls = [[-1 for _ in range(cols)] for _ in range(rows)]

    def get_neighbor_count(x, y):
        deltas = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dx, dy in deltas:
            nx, ny = x + dx, y + dy
            valid_row = 0 <= nx < rows
            valid_col = 0 <= ny < cols

            if valid_row and valid_col and locations[nx][ny] == "@":
                count += 1
        return count

    for i, row in enumerate(locations):
        for j, col in enumerate(row):
            if col == "@":
                rolls[i][j] = get_neighbor_count(i, j)

    filtered = [cell for row in rolls for cell in row if 0 <= cell < 4]

    print(f"Day 4, Part 1 -- Movable Rolls: {len(filtered)}")

    # Day 4 - Part 2
    locations = [list(line) for line in data]
    rows, cols = len(locations), len(locations[0])
    removed = 0
    count = rows * cols
    while True:
        rolls = [[-1 for _ in range(cols)] for _ in range(rows)]
        for i, row in enumerate(locations):
            for j, col in enumerate(row):
                if col == "@":
                    rolls[i][j] = get_neighbor_count(i, j)
        filtered = [cell for row in rolls for cell in row if 0 <= cell < 4]
        if len(filtered) == 0:
            break

        removed += len(filtered)

        for i, row in enumerate(rolls):
            for j, col in enumerate(row):
                if col < 4 and locations[i][j] == "@":
                    locations[i][j] = "."

        count -= 1
        if count < 0:
            raise Exception("OH GOD NO")

    print(f"Day 4, Part 2 -- Removed: {removed}")


if __name__ == "__main__":
    main()
