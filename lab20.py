import math
from typing import Dict, List, Tuple


def calculate_descriptive_stats(data: List[float]) -> Dict[str, float]:
    n = len(data)
    if n == 0:
        return {}

    sorted_data = sorted(data)
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - 1) if n > 1 else 0.0
    std_dev = math.sqrt(variance)

    # Median
    mid = n // 2
    median = (sorted_data[mid] if n % 2 != 0 else (sorted_data[mid - 1] + sorted_data[mid]) / 2)

    # Quartiles
    q1 = sorted_data[n // 4]
    q3 = sorted_data[(3 * n) // 4]
    iqr = q3 - q1

    return {
        "count": n,
        "mean": round(mean, 2),
        "median": round(median, 2),
        "variance": round(variance, 2),
        "std_dev": round(std_dev, 2),
        "min": min(data),
        "max": max(data),
        "q1": q1,
        "q3": q3,
        "iqr": iqr
    }


def pearson_correlation(x: List[float], y: List[float]) -> float:
    n = len(x)
    mean_x = sum(x) / n
    mean_y = sum(y) / n
    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denom = math.sqrt(sum((val - mean_x) ** 2 for val in x) * sum((val - mean_y) ** 2 for val in y))
    return round(numerator / denom, 4) if denom != 0 else 0.0


def print_ascii_histogram(data: List[float], bins: int = 5) -> None:
    min_val, max_val = min(data), max(data)
    bin_width = (max_val - min_val) / bins
    counts = [0] * bins

    for val in data:
        idx = min(int((val - min_val) / bin_width), bins - 1)
        counts[idx] += 1

    print("\nFrequency Distribution Histogram:")
    for i in range(bins):
        low = min_val + i * bin_width
        high = low + bin_width
        bar = "█" * (counts[i] * 3)
        print(f"  [{low:>5.1f} - {high:>5.1f}] : {bar:<20} ({counts[i]})")


def main():
    scores = [65.0, 72.0, 88.0, 95.0, 78.0, 82.0, 91.0, 85.0, 90.0, 76.0, 84.0, 99.0]
    study_hours = [10.0, 12.0, 20.0, 25.0, 15.0, 16.0, 22.0, 18.0, 21.0, 14.0, 17.0, 28.0]

    stats = calculate_descriptive_stats(scores)
    print("--- Descriptive Statistical Analysis ---")
    for key, val in stats.items():
        print(f"  {key:<10}: {val}")

    r = pearson_correlation(study_hours, scores)
    print(f"\nPearson Correlation (Hours vs Scores): r = {r}")

    print_ascii_histogram(scores, bins=5)


if __name__ == "__main__":
    main()
