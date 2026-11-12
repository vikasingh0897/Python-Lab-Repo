from typing import List, Tuple


def rgb_to_gray(r: int, g: int, b: int) -> int:
    return int(0.299 * r + 0.587 * g + 0.114 * b)


def apply_grayscale(pixels: List[List[Tuple[int, int, int]]]) -> List[List[int]]:
    return [[rgb_to_gray(r, g, b) for r, g, b in row] for row in pixels]


def apply_threshold(gray_pixels: List[List[int]], limit: int = 128) -> List[List[int]]:
    return [[255 if val >= limit else 0 for val in row] for row in gray_pixels]


def apply_box_blur(gray: List[List[int]]) -> List[List[int]]:
    h = len(gray)
    w = len(gray[0])
    result = [[gray[y][x] for x in range(w)] for y in range(h)]

    for y in range(1, h - 1):
        for x in range(1, w - 1):
            neighborhood = [
                gray[y + dy][x + dx]
                for dy in (-1, 0, 1)
                for dx in (-1, 0, 1)
            ]
            result[y][x] = sum(neighborhood) // 9
    return result


def main():
    sample_image = [
        [(255, 0, 0), (0, 255, 0), (0, 0, 255)],
        [(100, 150, 200), (200, 200, 200), (50, 50, 50)],
        [(255, 255, 0), (0, 255, 255), (255, 0, 255)]
    ]

    print("Original RGB Pixels (3x3 Sample):")
    for row in sample_image:
        print(row)

    gray = apply_grayscale(sample_image)
    print("\nGrayscale Luminosity Matrix:")
    for row in gray:
        print(row)

    bw = apply_threshold(gray, limit=120)
    print("\nBinary Threshold Matrix (cutoff=120):")
    for row in bw:
        print(row)

    blurred = apply_box_blur(gray)
    print("\nBox Blurred Center Pixel:")
    print(f"Center before blur: {gray[1][1]} -> after blur: {blurred[1][1]}")


if __name__ == "__main__":
    main()
