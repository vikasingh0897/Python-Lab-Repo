from typing import List


def remove_negative(matrix: List[List[int]]) -> List[List[int]]:
    return list(map(lambda row: list(map(lambda x: max(x, 0), row)), matrix))


def filter_positive(matrix: List[List[int]]) -> List[List[int]]:
    return list(map(lambda row: list(filter(lambda x: x > 0, row)), matrix))


def sort_rows(matrix: List[List[int]]) -> List[List[int]]:
    return list(map(lambda row: sorted(row), matrix))


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    return [list(row) for row in zip(*matrix)]


def main():
    matrix = [
        [5, -2, 8],
        [-4, 3, 1],
        [7, -6, 2]
    ]

    print("Original Matrix:")
    print(matrix)

    print("\nNegative values clamped to 0:")
    print(remove_negative(matrix))

    print("\nOnly positive values preserved:")
    print(filter_positive(matrix))

    print("\nSorted rows:")
    print(sort_rows(matrix))

    print("\nTransposed Matrix:")
    print(transpose(matrix))


if __name__ == "__main__":
    main()
